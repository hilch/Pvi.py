#
# Pvi.py
# Python connector for B&R Pvi (process visualization interface)
#
#  https://github.com/hilch/Pvi.py
# Permission is hereby granted, free of charge, 
# to any person obtaining a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#from collections import namedtuple
from .include import *
from .Error import PviError
from .Object import PviObject
from .VariableType import VariableType


class Variable(PviObject):

    def __init__( self, parent, name, **objectDescriptor ):
        if parent._type != T_POBJ_TYPE.POBJ_CPU and  parent._type != T_POBJ_TYPE.POBJ_TASK and  parent._type != T_POBJ_TYPE.POBJ_STATION:
            raise PviError(12009, self )        
        self._value = None 
        self._valueChanged = None 
        self._variableType = None
        objectDescriptor.update({'CD':name})
        if not('RF' in objectDescriptor):
            objectDescriptor.update({'RF':0}) # do not cyclic refrehs variables by default       
        super().__init__( parent, 'POBJ_PVAR', name, **objectDescriptor)

    def __repr__(self):
        return f"Variable( name={self._name}, linkID={self._linkID}, VT={self._objectDescriptor.get('VT')} )"


    @property
    def writable(self):
        '''
        Variable: signals if this variable can be written
        '''
        access = self._objectDescriptor.get('AT')    
        return self._variableType != None and 'w' in access # data type already read and write access ?

    @property
    def readable(self):
        '''
        Variable: signals if this variable can be read
        '''        
        access = self._objectDescriptor.get('AT')
        return self._variableType != None and 'r' in access # data type already read and read access ?


    def __readRawData(self, wParam, responseInfo):
        '''
        reads data (byte) from PVI_ACC_DATA or PVI_EVENT_DATA
        > wParam: points to response data
        > responseInfo: responseInfo or 'None' in case of synchronous read request
        '''
        _ = self.dataType # ensure variable data type is known
        
        buffer = create_string_buffer(self._variableType.vn * self._variableType.vl)

        if responseInfo: # data is answer of a request
            self._result = PviReadResponse( wParam, byref(buffer), sizeof(buffer) )
        else: # data shall be immediately read
            self._result = PviRead( self._linkID, POBJ_ACC_DATA, None, 0, byref(buffer), sizeof(buffer) )
        
        if self._result == 0:
            self._value = self._variableType.readFromBuffer(bytes(buffer))
        else:
            raise PviError(self._result, self)

        if self._errorChanged: # fire callback in case of response
            self._errorChanged(0)

 
    def _eventData( self, wParam, responseInfo ):
        self.__readRawData( wParam, responseInfo )
        if callable(self._valueChanged):
            self._valueChanged(self._value)


    def _eventDataType( self, wParam, responseInfo ):
        s = create_string_buffer(b'\000' * 64*1024)       
        self._result = PviReadResponse( wParam, s, sizeof(s) )
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            self._variableType = VariableType(s)
            self._objectDescriptor |= self._variableType.objectDescriptor
        else:
            raise PviError(self._result, self)

            
    @property
    def value(self):
        '''
        Variable : read value
        '''
        self.__readRawData( 0, None )
        return self._value

    @value.setter
    def value(self,v):
        '''
        Variable: set value
        '''
        vt = self._variableType.vt

        if vt == PvType.STRUCT:
            self._result = 0
        else:
            buffer = self._variableType.allocateBuffer(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(buffer), sizeof(buffer), None, 0 )  

        if self._result:
            raise PviError(self._result, self)

    @property
    def valueChanged(self):
        '''
        Variable: read callback for 'value changed'
        '''
        return self._valueChanged

    @valueChanged.setter
    def valueChanged(self, cb):
        '''
        Variable: set callback for 'value changed'
        '''
        if callable(cb):
            self._valueChanged = cb
        else:
            raise ValueError


    @property
    def dataType(self) -> str:
        '''
        Variable: returns datatype
        '''
        try:
            return self._variableType.vt.value \
            + f'[{self._variableType.vn}]' if self._variableType.vn > 1 else '' # variable data type 

        except AttributeError:
            s = create_string_buffer(b'\000' * 64*1024) 
            self._result = PviRead( self._linkID, POBJ_ACC_TYPE_INTERN, None, 0, s, sizeof(s) )
            if self._result == 0:
                s = str(s, 'ascii').rstrip('\x00')
                self._variableType = VariableType(s)
                self._objectDescriptor |= self._variableType.objectDescriptor
                return self._variableType.vt.value \
                + f'[{self._variableType.vn}]' if self._variableType.vn > 1 else '' # variable data type                      
            else:
                raise PviError(self._result, self)

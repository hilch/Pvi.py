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

from ctypes import *
import re
import datetime
import time
from .include import *
from .Error import PviError
from .Object import PviObject

class Variable(PviObject):
    __patternDataTypeInformation = re.compile(r"([A-Z]{2}=\w+)|(\{[^}]+\})")
    __patternStructureElementDefinition = re.compile(r"(\x2E\w+)|([A-Z]{2}=\w+)")

    def __init__( self, parent, name, **objectDescriptor ):
        if parent._type != T_POBJ_TYPE.POBJ_CPU and  parent._type != T_POBJ_TYPE.POBJ_TASK and  parent._type != T_POBJ_TYPE.POBJ_STATION:
            raise PviError(12009, self )        
        self._value = None 
        self._valueChanged = None 
        objectDescriptor.update({'CD':name})
        self._structureElements = None
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
        vt = self._objectDescriptor.get('VT') # variable data type
        access = self._objectDescriptor.get('AT')    
        return vt and 'w' in access # data type already read and write access ?

    @property
    def readable(self):
        '''
        Variable: signals if this variable can be read
        '''        
        vt = self._objectDescriptor.get('VT') # variable data type
        access = self._objectDescriptor.get('AT')
        return vt and 'r' in access # data type already read and read access ?


    def _updateElementDefinition(self, s):
        '''
        Variable: parses result of POBJ_ACC_TYPE_EXTERN 
            and updates list with element description
            > s: string with data type information
        '''
        matches = Variable.__patternStructureElementDefinition.finditer(s)
        element = dict()
        for m in matches:
            ex = m.group()
            if ex.startswith('.'):
                element.update({'name' : ex[1:]}) # element's name
            else:
                element.update({ex[0:2]: ex[3:]}) # element's parameter
        self._structureElements.append(element)


    def _updateDataTypeInformation(self, s ):
        '''
        Variable: parses result of POBJ_ACC_TYPE or POBJ_ACC_TYPE_EXTERN 
            and updates object descriptor
            > s: string with data type information
        '''
        self._structureElements = list()
        matches = Variable.__patternDataTypeInformation.finditer(s)
        for m in matches:
            ex = m.group()
            if ex.startswith('{'): # structure element definition
                self._updateElementDefinition(ex)
            else:
                self._objectDescriptor.update({ex[0:2]: ex[3:]}) 
        if self._objectDescriptor.get('VT') == 'struct':
            self._structureElements.sort( key = lambda e: int(e.get('VO')) ) # sort element list according to variable offset VO



    def __castRawData(self, vt, data ):
        '''
        cast result data returned by PVI_ACC_DATA or PVI_EVENT_DATA
        > vt: variable type
        > data: c_type data
        '''
        if vt == 'dt':
            return datetime.datetime.fromtimestamp(data)
        elif vt == 'date':
            return datetime.date.fromtimestamp(data)                    
        elif vt == 'time':
            return time.gmtime(data)
        else:
            return data        


    def __readRawData(self, wParam, responseInfo):
        '''
        reads data (byte) from PVI_ACC_DATA or PVI_EVENT_DATA
        > wParam: points to response data
        > responseInfo: responseInfo or 'None' in case of synchronous read request
        '''
        vt = self.dataType # variable data type
        vl = int(self._objectDescriptor.get('VL')) # sizeof(variable)
        vn = int(self._objectDescriptor.get('VN')) # number of array elements
        
        data = None

        if vt == 'boolean':
            data = (c_uint8*vn)()
        elif vt == 'u8':
            data = (c_uint8*vn)()
        elif vt == 'i8':
            data = (c_int8*vn)()
        elif vt == 'u16':
            data = (c_uint16*vn)()
        elif vt == 'i16':
            data = (c_int16*vn)()
        elif vt == 'u32':
            data = (c_uint32*vn)()
        elif vt == 'i32':
            data = (c_int32*vn)()
        elif vt == 'f32':
            data = (c_float*vn)()
        elif vt == 'f64':
            data = (c_double*vn)() 
        elif vt == 'string':
            data = create_string_buffer(b'\000' * vl*vn)
        elif vt == 'struct':
            data = create_string_buffer(b'\000' * vl*vn)
        elif vt == 'dt' or vt == 'time' or vt == 'date':
            data = (c_uint32*vn)()
        else: # not handled data type
            data = (c_uint8*vn)()    

        if responseInfo: # data is answer of a request
            self._result = PviReadResponse( wParam, byref(data), sizeof(data) )
        else: # data shall be immediately read
            self._result = PviRead( self._linkID, POBJ_ACC_DATA, None, 0, byref(data), sizeof(data) )

        if self._result == 0:
            if vn == 1: # single value
                self._value = self.__castRawData(vt, data[0])
            else: # array: send a tuple
                self._value = tuple([ self.__castRawData(vt, _) for _ in data])
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
            self._updateDataTypeInformation(s) 
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
        vt = self._objectDescriptor.get('VT') # variable data type
        if vt == 'boolean':
            data = c_uint8(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'u8':
            data = c_uint8(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'i8':
            data = c_int8(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'u16':
            data = c_uint16(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'i16':
            data = c_int16(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'u32':
            data = c_uint32(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'i32':
            data = c_int32(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'f32':
            data = c_float(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'f64':
            data = c_double(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )            
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
        vt = self._objectDescriptor.get('VT') # variable data type

        if vt == None:
            s = create_string_buffer(b'\000' * 64*1024) 
            self._result = PviRead( self._linkID, POBJ_ACC_TYPE_EXTERN, None, 0, s, sizeof(s) )
            if self._result == 0:
                s = str(s, 'ascii').rstrip('\x00')
                self._updateDataTypeInformation(s)                               
                vt = self._objectDescriptor.get('VT') # variable data type
            else:
                raise PviError(self._result, self)
        return vt
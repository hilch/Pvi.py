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

from typing import Type

from inspect import signature
from ctypes import create_string_buffer, sizeof, byref
from typing import Any
from .include import *
from .Error import PviError
from .Object import PviObject
from .VariableTypeDescription import VariableTypeDescription



class Variable(PviObject):
    '''representing a PVI Variable object

    Typical usage example:
    ```
    task1 = Task( cpu, 'mainlogic')  
    temperature = Variable( task1, 'gHeating.status.actTemp' )  
    ```        
    '''
    def __init__( self, parent : PviObject, name : str, **objectDescriptor  ):
        '''
        Args:
            parent : the task object (or the CPU object in case of a global variable)
            name : name of the variable in PVI hierarchy. Will be used for name of variable in plc if possible.
            objectDescriptor : e.g.  - see PVI documentation for details
                ANSL : e.g. CD="/RO=TempField[7] /ROI=1"

                INA2000 : e.g. AT=rwe CD="/RO=View::TempField[7]"

                SNMP : name of SNMP variable e.g. CD='serialNumber' or CD='ipAddress'
                
        '''
        if parent.type != T_POBJ_TYPE.POBJ_CPU and  parent.type != T_POBJ_TYPE.POBJ_TASK and  parent.type != T_POBJ_TYPE.POBJ_STATION:
            raise PviError(12009, self )        
        self._value = None 
        self._valueChanged = lambda _ : _
        self._valueChangedArgCount = 0      
        self._variableTypeDescription = VariableTypeDescription()
        if 'CD' not in objectDescriptor:
            objectDescriptor.update({'CD':name})
        if 'RF' not in objectDescriptor:
            objectDescriptor.update({'RF':0}) # do not cyclic refrehs variables by default       
        super().__init__( parent, T_POBJ_TYPE.POBJ_PVAR, name, **objectDescriptor)

    def __repr__(self):
        return f"Variable( name={self._name}, linkID={self._linkID}, VT={self._objectDescriptor.get('VT')} )"


    @property
    def writable(self) -> bool:
        '''
        signals if this variable can be written
        '''
        if self._variableTypeDescription.vt != PvType.UNKNOWN:
            access = self._objectDescriptor.get('AT', '')  
            return 'w' in access # data type already read and write access ?
        else:
            return False

    @property
    def readable(self) -> bool:
        '''
        signals if this variable can be read
        '''
        if self._variableTypeDescription.vt != PvType.UNKNOWN:
            access = self._objectDescriptor.get('AT', '')
            return 'r' in access # data type already read and read access ?
        else:
            return False

    def __readRawData(self, wParam, responseInfo):
        '''
        reads data (byte) from PVI_ACC_DATA or PVI_EVENT_DATA
        > wParam: points to response data
        > responseInfo: responseInfo or 'None' in case of synchronous read request
        '''
        if self._variableTypeDescription.vt == PvType.UNKNOWN:
            self._variableTypeDescription.readFrom(self)

        buffer = create_string_buffer(self._variableTypeDescription.vn * self._variableTypeDescription.vl)

        if responseInfo: # data is answer of a request
            self._result = PviReadResponse( wParam, byref(buffer), sizeof(buffer) )
        else: # data shall be immediately read
            self._result = PviRead( self._linkID, POBJ_ACC_DATA, None, 0, byref(buffer), sizeof(buffer) )
        
        if self._result == 0:
            self._value = self._variableTypeDescription.readFromBuffer(bytes(buffer))
        else:
            raise PviError(self._result, self)

        if self._errorChanged: # fire callback in case of response
            self._errorChanged(0)

 
    def _eventData( self, wParam, responseInfo ):
        self.__readRawData( wParam, responseInfo )
        if self._valueChangedArgCount == 1:
            self._valueChanged(self._value)
        elif self._valueChangedArgCount == 2:
            self._valueChanged(self._value, self) # type: ignore


    def _eventDataType( self, wParam, responseInfo ):
        s = create_string_buffer(b'\000' * 64*1024)       
        self._result = PviReadResponse( wParam, s, sizeof(s) )
        if self._result == 0:
            pass # TODO

            
    @property
    def value(self) -> Any:
        '''
        read value
        '''
        self.__readRawData( 0, None )
        return self._value


    @value.setter
    def value(self,v : Any):
        '''
        set value
        '''
        if self._variableTypeDescription.vt == PvType.UNKNOWN:
            self._variableTypeDescription.readFrom(self)

        if self._variableTypeDescription.vt == PvType.STRUCT: 
            raise ValueError(f'Writing of struct not implemented\n{repr(self)}')
        else:
            buffer = self._variableTypeDescription.writeToBuffer(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(buffer), sizeof(buffer), None, 0 )  
        if self._result:
            raise PviError(self._result, self)


    @property
    def valueChanged(self):
        '''
        callback for 'value changed'

        accepts:
        fn( value)
        or
        fn( value, vo ) where 'vo' is the Variable object itself

        '''
        return self._valueChanged

    @valueChanged.setter
    def valueChanged(self, cb):
        if callable(cb):
            self._valueChanged = cb
            self._valueChangedArgCount = len(signature(cb).parameters)
        else:
            raise ValueError


    @property
    def dataType(self) -> str:
        '''
        variable's type as string. e.g 'i8', 'i16', 'f32', 'boolean', 'string'
        in case of an array the string is surrouned by brackets, e.g. '[i32]'
        '''
        t = "?"
        if self._variableTypeDescription.vt == PvType.UNKNOWN:
            self._variableTypeDescription.readFrom(self)
            t = self._variableTypeDescription.vt.value
            if self._variableTypeDescription.vn > 1: # is variable an array ?
                t += f'[{self._variableTypeDescription._vn}]'
        else:
            t = self._variableTypeDescription.vt.value
        return t


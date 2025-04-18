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

from inspect import signature
from ctypes import create_string_buffer, sizeof, byref, c_int32
from typing import Union, Any
from .include import *
from .Error import PviError
from .Object import PviObject
from .VariableTypeDescription import VariableTypeDescription
from .Helpers import dictFromParameterPairString


class Variable(PviObject):
    '''representing a PVI Variable object

    Typical usage example:
    ```
    task1 = Task( cpu, 'mainlogic')  
    temperature = Variable( task1, 'gHeating.status.actTemp' )  
    ```        
    '''
    def __init__( self, parent : PviObject, name : str, **objectDescriptor: Union[str,int, float] ):
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

        if 'CD' not in objectDescriptor:
            objectDescriptor.update({'CD':name})
        if 'RF' not in objectDescriptor:
            objectDescriptor.update({'RF':0}) # do not cyclic refrehs variables by default       
        super().__init__( parent, T_POBJ_TYPE.POBJ_PVAR, name, **objectDescriptor)
        self._variableTypeDescription = VariableTypeDescription(self._hPvi)

    def __repr__(self):
        return f"Variable( name={self._name}, linkID={self._linkID}, VT={self._objectDescriptor.get('VT')} )"


    @property
    def writable(self) -> bool:
        '''
        signals if this variable can be written
        '''
        if self._variableTypeDescription.vt != PvType.UNKNOWN:
            access = str(self._objectDescriptor.get('AT', ''))
            return 'w' in access # data type already read and write access ?
        else:
            return False

    @property
    def readable(self) -> bool:
        '''
        signals if this variable can be read
        '''
        if self._variableTypeDescription.vt != PvType.UNKNOWN:
            access = str(self._objectDescriptor.get('AT', ''))
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
            try:
                self._objectDescriptor = self._variableTypeDescription.readFrom(self._linkID)
            except PviError as e:
                raise PviError( e.number, self._name )

        buffer = create_string_buffer(self._variableTypeDescription.vn * self._variableTypeDescription.vl)

        if responseInfo: # data is answer of a request
            self._result = PviXReadResponse( self._hPvi, wParam, byref(buffer), sizeof(buffer) )
        else: # data shall be immediately read
            self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_DATA, None, 0, byref(buffer), sizeof(buffer) )
        
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
            self._valueChanged(self, self._value) # type: ignore


    def _eventDataType( self, wParam, responseInfo ):
        s = create_string_buffer(b'\000' * 64*1024)       
        self._result = PviXReadResponse( self._hPvi, wParam, s, sizeof(s) )
        if self._result == 0:
            pass # TODO

            
    @property
    def value(self) ->Any:
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
            try:
                self._objectDescriptor = self._variableTypeDescription.readFrom(self._linkID)
            except PviError as e:
                raise PviError( e.number, self._name )                

        if self._variableTypeDescription.vt == PvType.STRUCT: 
            raise ValueError(f'Writing of struct not implemented\n{repr(self)}')
        else:
            buffer = self._variableTypeDescription.writeToBuffer(v)
            self._result = PviXWrite( self._hPvi, self._linkID, POBJ_ACC_DATA, byref(buffer), sizeof(buffer), None, 0 )  
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
        in case of an array the indices are given in a bracket, e.g. 'i32[0..2]'
        '''
        t = "?"
        if self._variableTypeDescription.vt == PvType.UNKNOWN:
            try:
                self._objectDescriptor = self._variableTypeDescription.readFrom(self._linkID)
            except PviError as e:
                raise PviError( e.number, self._name )                  

        if self._variableTypeDescription.vt == PvType.STRUCT:
            t = self._variableTypeDescription.sn
            if self.isArray: # is variable an array of structs ?
                t += f'[{self._variableTypeDescription.indices[0]}..{self._variableTypeDescription.indices[1]}]'
        else:
            t = self._variableTypeDescription.vt.value
            if self.isArray: # is variable an array ?
                t += f'[{self._variableTypeDescription.indices[0]}..{self._variableTypeDescription.indices[1]}]'            
        return t
    
    @property
    def isArray(self) -> bool:
        return( self._variableTypeDescription.vn > 1 or self._variableTypeDescription.sn.startswith('a'))

    @property
    def attributes(self) -> dict:
        '''
        object attributes

        Typical usage example:
        ```
        temperature = Variable( task1, name='gHeating.status.actTemp', AT = 'r' )        
        ```
 
        '''
        s = create_string_buffer(b'\000' * 256)   
        self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_TYPE , None, 0, byref(s), sizeof(s) )
        if self._result == 0:
            ret = dict()
            ret.update( dictFromParameterPairString(str(s, 'ascii').rstrip('\x00')))
            self._objectDescriptor.update(ret)
            return ret
        else:
            raise PviError(self._result, self)  

    @attributes.setter
    def attributes(self, a : str ):
        '''
        object attributes
        '''
        s = create_string_buffer(a.encode('ascii'))
        self._result = PviXWrite( self._hPvi, self._linkID, POBJ_ACC_TYPE, byref(s), sizeof(s), None, 0 ) 
        if self._result:
            raise PviError(self._result, self)  



    @property
    def refresh(self) -> int:
        '''
        refresh time [ms]

        Typical usage example:
        ```
        temperature = Variable( task1, name='gHeating.status.actTemp', RF = 2000 )      
        ```
        '''
        t = c_int32(0)
        self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_REFRESH , None, 0, byref(t), sizeof(t) )
        if self._result == 0:
            self._objectDescriptor.update({'RF' : t.value }) # type: ignore
            return t.value
        else:
            raise PviError(self._result, self)  

    @refresh.setter
    def refresh(self, time : int ):
        '''
        refresh time [ms]
        '''
        t = c_int32(time)
        self._result = PviXWrite( self._hPvi, self._linkID, POBJ_ACC_REFRESH, byref(t), sizeof(t), None, 0 ) 
        if self._result:
            raise PviError(self._result, self) 
        self._objectDescriptor.update({'RF' : time }) # type: ignore 


    @property
    def hysteresis(self) -> float:
        '''
        event hysteresis

        Typical usage example:
        ```
        temperature = Variable( task1, name='gHeating.status.actTemp', HY = 5.0, LinkDescriptor="LT=prc" )        
        ```
        '''
        s = create_string_buffer(b'\000' * 10)   
        self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_HYSTERESE , None, 0, byref(s), sizeof(s) )
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            self._objectDescriptor.update({'HY' : s }) # type: ignore  
            try:          
                return float(s)
            except ValueError:
                return 0.0
        else:
            raise PviError(self._result, self)  

    @hysteresis.setter
    def hysteresis(self, h : float ):
        '''
        event hysteresis
        '''
        s = create_string_buffer(str(h).encode('ascii'))
        self._result = PviXWrite( self._hPvi, self._linkID, POBJ_ACC_HYSTERESE, byref(s), sizeof(s), None, 0 ) 
        if self._result:
            raise PviError(self._result, self)  
        self._objectDescriptor.update({'HY' : h }) # type: ignore                    
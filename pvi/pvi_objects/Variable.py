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
from typing import Union, Any, List
from collections import OrderedDict
import re
from copy import deepcopy
from .include import *
from .Error import PviError
from .Object import PviObject
from .VariableTypeDescription import TypeDescription, MemberStack
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
        self._type_description = TypeDescription( name=name)
        self._struct_members : OrderedDict[ str, TypeDescription] = OrderedDict()        

    def __repr__(self):
        return f"Variable( name={self._name}, linkID={self._linkID}, VT={self._objectDescriptor.get('VT')} )"


    @property
    def writable(self) -> bool:
        '''
        signals if this variable can be written
        '''
        if self._type_description.vt != PvType.UNKNOWN:
            access = str(self._objectDescriptor.get('AT', ''))
            return 'w' in access # data type already read and write access ?
        else:
            return False

    @property
    def readable(self) -> bool:
        '''
        signals if this variable can be read
        '''
        if self._type_description.vt != PvType.UNKNOWN:
            access = str(self._objectDescriptor.get('AT', ''))
            return 'r' in access # data type already read and read access ?
        else:
            return False

    def _processRawData(self, wParam, responseInfo):
        '''
        reads data (byte) from PVI_ACC_DATA or PVI_EVENT_DATA
        > wParam: points to response data
        > responseInfo: responseInfo or 'None' in case of synchronous read request
        '''
        if self._type_description.vt == PvType.UNKNOWN:
            try:
                self._readTypeDescription()
            except PviError as e:
                raise PviError( e.number, self._name )

        buffer = create_string_buffer(self._type_description.get_buffer_size())

        if responseInfo: # data is answer of a request
            self._result = PviXReadResponse( self._hPvi, wParam, byref(buffer), sizeof(buffer) )
        else: # data shall be immediately read
            self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_DATA, None, 0, byref(buffer), sizeof(buffer) )
        
        if self._result == 0:
            self._value = self._readValueFromBuffer(bytes(buffer))
        else:
            raise PviError(self._result, self)

        if self._errorChanged: # fire callback in case of response
            self._errorChanged(0)

 
    def _eventData( self, wParam, responseInfo ):
        self._processRawData( wParam, responseInfo )
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
        self._processRawData( 0, None )
        return self._value


    @value.setter
    def value(self,v : Any):
        '''
        set value
        '''
        if self._type_description.vt == PvType.UNKNOWN:
            try:
                self._readTypeDescription()
            except PviError as e:
                raise PviError( e.number, self._name )                

        if self._type_description.vt == PvType.STRUCT: 
            raise ValueError(f'Writing of struct not implemented\n{repr(self)}')
        else:
            buffer = self._type_description.pack_value_to_buffer(v)
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
        if self._type_description.vt == PvType.UNKNOWN:
            try:
                self._readTypeDescription()
            except PviError as e:
                raise PviError( e.number, self._name )                  

        if self._type_description.vt == PvType.STRUCT:
            t = self._type_description.sn
            if self.isArray: # is variable an array of structs ?
                indices = self._type_description.get_array_indices()
                assert(indices)
                if indices and len(indices) == 2: # two dimensional array
                    dim1 = indices[0]
                    dim2 = indices[1]
                    t += f'[{dim1[0]}..{dim1[1]}][{dim2[0]}..{dim2[1]}]'
                else: # one dimension only
                    dim1 = indices[0]
                    t += f'[{dim1[0]}..{dim1[1]}]'
        else:
            t = self._type_description.vt.value
            if self._type_description.vt == PvType.I32 and 'e' in self._type_description.vs: # enum ?
                t = self._type_description.sn
            if 'v' in self._type_description.vs: # derived datatype
                subrange = self._type_description.get_subrange()
                if len(self._type_description.tn) > 0:
                    t = self._type_description.tn
                elif subrange:
                    t += f'({subrange[0]}..{subrange[1]})'
            
            indices = self._type_description.get_array_indices()
            if indices: # is variable an array ?
                t += f'[{indices[0][0]}..{indices[0][1]}'
                if len(indices) == 2:
                    t += f',{indices[1][0]}..{indices[1][1]}'
                t += ']'
        return t
    
    @property
    def isArray(self) -> bool:
        return( bool(self._type_description.get_array_indices()) )

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
        
        
    def _readTypeDescription(self):
        '''
        read type description from object
        object: Variable object
        ''' 

        s = create_string_buffer(b'\000' * 1024*1024) 
        
        result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_TYPE_EXTERN, None, 0, s, sizeof(s) )
        if result == 0:
            stripped = str(s, 'ascii').rstrip('\x00')
        else:
            raise PviError(result)        

        '''
        update object descriptor and find all members if this PV is a structure
        s : member definition returned by POBJ_ACC_TYPE_EXTERN
            e.g "{.ton.IN VT=boolean VL=1 VN=1 VO=16}"       
        '''
        self._struct_members.clear()
        descriptions = stripped.split('{')
        for d in descriptions:
            if d.rfind('}') >= 0: # structure member definition
                d = d.rstrip(' }')
                m = TypeDescription()
                m.parse(d)
                self._struct_members.update({ m.name: m })
            else: # definition of variable itself
                td = TypeDescription()
                td.parse(d)
                td.name = self._type_description.name
                self._type_description = td
                
        with open( 'C:/temp/members1.txt', 'w') as f:
            for i, m in self._struct_members.items():
                f.write( str(m) + '\n')
    

        result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_TYPE_INTERN, None, 0, s, sizeof(s) )
        if result == 0:
            stripped = str(s, 'ascii').rstrip('\x00')
        else:
            raise PviError(result)
        
        '''
        get the offsets and length of the variable and the members in case of a structure 
        given by information delivered by POBJ_ACC_TYPE_INTERN
        since information from POBJ_ACC_TYPE_EXTERN does not fit to POBJ_ACC_DATA
        '''
        descriptions = stripped.split('{')
        for d in descriptions:
            if d.rfind('}') >= 0: # structure member definition
                d = d.rstrip(' }')
                m = TypeDescription()
                m.parse(d)
                member = self._struct_members[m.name]
                # POBJ_ACC_TYPE_EXTERN did not return the offsets and lengths used by POBJ_ACC_DATA
                # so we take them from POBJ_ACC_TYPE_INTERN
                member.vo = m.vo
                member.vl = m.vl
            else: # definition of variable itself
                m = TypeDescription()
                m.parse(d)
                self._type_description.vl = m.vl # use length given by POBJ_ACC_TYPE_INTERN
                
        del s, stripped

        with open( 'C:/temp/members2.txt', 'w') as f:
            for i, m in self._struct_members.items():
                f.write( str(m) + '\n')
        
        if self._type_description.vn > 1 or self._type_description.vt == PvType.STRUCT:
            self._expand()             
            with open( 'C:/temp/members3.txt', 'w') as f:
                for i, m in self._struct_members.items():
                    f.write( str(m) + '\n')
  
                    
              
    def _expand_struct_array(self, struct_array : TypeDescription, members : OrderedDict[ str, TypeDescription] ) -> OrderedDict[ str, TypeDescription]:
        new_members : OrderedDict[ str, TypeDescription] = OrderedDict()
        indices = struct_array.get_array_indices()
        sname = struct_array.name
        assert(indices)
        re_child_of_struct = re.compile(rf'{struct_array.name}(\[\d*\])?')
        for idx, m in members.items():
            if re_child_of_struct.match(idx): # is member a part of this struct ?
                if len(indices) == 2:
                    offset = m.vo
                    for i in range(indices[0][0],indices[0][1]+1):
                        for j in range(indices[1][0],indices[1][1]+1):
                            new_member = deepcopy(m)
                            new_member.name = m.name.replace( sname, f'{sname}[{i},{j}]', 1)
                            new_member.vo = offset
                            offset += struct_array.vl
                            new_members.update( { new_member.name : new_member})
                else:
                    offset = m.vo
                    for i in range(indices[0][0], indices[0][1]+1):
                        new_member = deepcopy(m)
                        new_member.name = m.name.replace( sname, f'{sname}[{i}]', 1)
                        new_member.vo = offset
                        offset += struct_array.vl
                        new_members.update( { new_member.name : new_member})
            else: # member is not part of this struct
                new_members.update( { m.name : m})
        return new_members             
                    
                    
    def _expand(self):
        '''
        expand if variable is struct
        '''
        members : OrderedDict[ str, TypeDescription] = OrderedDict()
        structs = MemberStack()
        struct_arrays : OrderedDict[ str, TypeDescription] = OrderedDict()       
           
        # remove struct definitions and expand the members             
        for idx, m in self._struct_members.items():
            idx : str
            m : TypeDescription
                        
            order = m.get_order()
            if m.vt == PvType.STRUCT: # struct member is a struct itself
                if order == 1: # base level
                    structs.clear()
                    structs.push( m )
                elif order == (structs.level + 1): # nth level
                    m.vo = m.vo + structs.peek().vo
                    structs.push( m )               
                elif order == (structs.level - 1):
                    structs.pop()
                elif order == structs.level:
                    structs.pop()
                    m.vo = m.vo + structs.peek().vo
                    structs.push( m )
                if m.get_array_indices(): # struct is an array
                    struct_arrays.update( {m.name : m} )
                
            else: # all datatypes but structs go to here
                if order == 1:
                    structs.clear()
                member = m
                member.vo += structs.peek().vo
                members.update( {m.name :  m} )
                
        # order struct arrays according their deepest level coming first
        struct_arrays = OrderedDict(sorted( struct_arrays.items(), key = lambda x : x[1].get_order(), reverse=True))
        
        for idx, s in struct_arrays.items():
            members = self._expand_struct_array( s, members )
        
        # sort dict according variable offset
        self._struct_members = OrderedDict(sorted( members.items(), key = lambda x : x[1].vo ))
        pass
        
    def _readValueFromBuffer(self, buffer : bytes):
        '''
        gets the value from raw buffer data.
        returns a tuple in case of array.

        buffer : raw buffer data from POBJ_ACC_DATA
        '''

        arrayBuffers = [ buffer[_:_+self._type_description.vl] for _ in range(0,len(buffer), self._type_description.vl)] # split buffer into array elements
        result = list()

        for buffer in arrayBuffers:
            if self._type_description.vt == PvType.STRUCT:
                structResult = OrderedDict()
                for name, m in self._struct_members.items():
                    if m.get_array_indices() == None: # struct member is a single value
                        buf = buffer[m.vo : m.vo+m.vl]
                        value = m.unpack_data_from_buffer( buf )
                    else: # struct member is an array
                        indices = m.get_array_indices()
                        value = []
                        if indices and len(indices) == 2: # two dimensional array
                            el1dim = indices[0][1] - indices[0][0] + 1 # number of elements in first dimension
                            el2dim = indices[1][1] - indices[1][0] + 1 # number of elements in second dimension
                            offset = m.vo
                            for i in range(el1dim):
                                r = []
                                for _ in range(el2dim):
                                    v = m.unpack_data_from_buffer( buffer[offset:offset+m.vl] )
                                    r.append( v )
                                    offset += m.vl
                                value.append( r )
                        else: # one dimension only                      
                            memberBuffers = ( buffer[_:_+m.vl] for _ in range( m.vo, m.vo + m.vl*m.vn, m.vl)) # split buffer
                            value = [ m.unpack_data_from_buffer( buf ) for buf in memberBuffers ]
                    structResult.update( { m.name : value } )
                result.append( structResult )
            else:
                result.append( self._type_description.unpack_data_from_buffer( buffer ) )

        if len(result) == 1: # single value
            return result[0]
        else: # array
            indices = self._type_description.get_array_indices()
            if indices and len(indices) == 2: # two dimensional array
                r = []
                el1dim = indices[0][1] - indices[0][0] + 1 # number of elements in first dimension
                el2dim = indices[1][1] - indices[1][0] + 1 # number of elements in second dimension
                for i in range(el1dim):
                    r.append( [result[i*el2dim:(i+1)*el2dim]] )
                return r
            else: # one dimension only
                return result
            
            
   
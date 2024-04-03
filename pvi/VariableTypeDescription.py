
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

from typing import List, NamedTuple, Tuple
import datetime
from ctypes import sizeof, create_string_buffer
from ctypes import c_bool, c_uint8, c_int8, c_uint16, c_int16, c_uint32, c_int32, c_uint64, c_int64, c_float, c_double
from ctypes import c_char, c_wchar
import re
import struct
from collections import OrderedDict
from .Error import PviError
from .Object import PviObject
from .include import *


patternDataTypeInformation = re.compile(r"([A-Z]{2}=[\w\x2C]+)|(\{[^}]+\})") # pattern for variable definition
patternStructureMemberDefinition = re.compile(r"(\x2E[\w\x2E]+)|([A-Z]{2}=[\w\x2C]+)") # pattern for structure member definition
patternVSa = re.compile(r"a,(\d+),(\d+)") # pattern for parameter VS=a

StructMember = NamedTuple( 'StructMember', [('name', str), ('vt', PvType), ('sn', str), ('vn', int), ('vo', int), ('vl', int), ('vs', str)])
'''
helper class for structure member 
'''


class VariableTypeDescription():
    '''
    helper class for class Variable to parse data type information
    '''
    def __init__(self):
        self._vn = -1
        self._vl = -1
        self._vt = PvType.UNKNOWN
        self._sn = ''
        self._sc = ''
        self._vs = ''
        self._lowerIndex = -1
        self._higherIndex = -1
        self._parentObject = None
        self._memberOffsets : List[StructMember] = list()
        self._members : List[StructMember] = list()
        self._innerStructures : List[StructMember] = list()
        '''
        list of all data type (structure) members if this variable is a struct
        '''

    def readFrom(self, object : PviObject ):
        '''
        read type description from object
        object: Variable object
        '''        
        self._parentObject = object
        self._parentObject._objectDescriptor.update({'VN' : '1', 'VL' : '1' })        

        s = create_string_buffer(b'\000' * 64*1024) 
        object._result = PviRead( self._parentObject._linkID, POBJ_ACC_TYPE_INTERN, None, 0, s, sizeof(s) )
        if self._parentObject._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
        else:
            raise PviError(self._parentObject._result, self._parentObject)
        
        self._getByteOffsetsAndLength(s)

        s = create_string_buffer(b'\000' * 64*1024) 
        object._result = PviRead( self._parentObject._linkID, POBJ_ACC_TYPE_EXTERN, None, 0, s, sizeof(s) )
        if self._parentObject._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
        else:
            raise PviError(self._parentObject._result, self._parentObject)        

        self._updateObjectDescriptor(s) # udpate object descriptor

        self._vt = PvType( self._parentObject._objectDescriptor.get('VT')) 

        self._vn = int( self._parentObject.descriptor.get('VN', 0) )
        assert self._vn > 0

        self._vl = int( self._parentObject.descriptor.get('VL', 0) )
        assert self._vl > 0

        self._sn = str( self._parentObject.descriptor.get('SN', '') )
        self._sc = str( self._parentObject.descriptor.get('SC', '') )
        self._vs = str( self._parentObject.descriptor.get('VS', '') )  
        
        if self._vn > 1 or self._vs.startswith('a'): # is variable an array ?
            self._lowerIndex = 0
            m = patternVSa.findall(self._vs)
            if m:
                self._lowerIndex = int(m[0][0])
            self._higherIndex = self._lowerIndex + self._vn -1
        pass     

    @property
    def vn(self) -> int:
        '''
        number of array elements : int
        '''
        return self._vn
    
    @property
    def vl(self) -> int:
        '''
        variable byte length : int
        '''
        return self._vl
    
    @property
    def indices(self) -> Tuple[int,int]:
        '''
        array indices (int, int)
        '''
        return self._lowerIndex, self._higherIndex


    @property
    def vt(self) -> PvType:
        '''
        PVI Variable Type : PvType
        '''        
        return self._vt
    
    @property
    def sn(self) -> str:
        '''
        structure name : str
        '''        
        return self._sn if self._vt == PvType.STRUCT else ''
    

    def _getByteOffsetsAndLength(self, s):
        '''
        get the offsets and length of the variable and the members in case of a structure 
        given by information delivered by POBJ_ACC_TYPE_INTERN
        since information from POBJ_ACC_TYPE_EXTERN does not fit to POBJ_ACC_DATA
        '''
        for m in patternDataTypeInformation.finditer(s) : # update object descriptor
            ex = m.group()
            if ex.startswith('{'): # structure member definition
                self._updateMemberOffsetsAndLength(ex)
            else: # definition of variable itself
                assert isinstance(self._parentObject, PviObject)
                parameter = ex[0:2]
                value = ex[3:]
                if parameter == 'VL':
                    self._parentObject._objectDescriptor.update({parameter: value })

    def _updateMemberOffsetsAndLength(self, s):
        '''
        extract data type member's information
        s : member definition returned by POBJ_ACC_TYPE_INTERN
            e.g "{.ton.IN VT=boolean VL=1 VN=1 VO=16}"
        '''
        desc: dict[str, str] = {} # member's object descriptor
        for m in patternStructureMemberDefinition.finditer(s): # find matches
            ex = m.group()
            if ex.startswith('.'):
                desc.update({'name' : ex}) # member's name
            else:
                desc.update({ex[0:2]: ex[3:]}) # member's object descriptor

        vt = PvType(desc.get('VT'))
        vo = int(desc.get('VO',0)) # variable offset in PVI
        vn = int(desc.get('VN',0))
        vl = int(desc.get('VL',0))
        name = desc.get('name','')
        self._memberOffsets.append(  StructMember( name, vt, '', vn, vo, vl, '' ) )


    def _updateObjectDescriptor(self, s):
        '''
        update object descriptor and find all members if this PV is a structure
        s : member definition returned by POBJ_ACC_TYPE_EXTERN
            e.g "{.ton.IN VT=boolean VL=1 VN=1 VO=16}"       
        '''
        for m in patternDataTypeInformation.finditer(s) : # update object descriptor
            ex = m.group()
            if ex.startswith('{'): # structure member definition
                self._updateMemberList(ex)
            else: # definition of variable itself
                assert isinstance(self._parentObject, PviObject)
                parameter = ex[0:2]
                value = ex[3:]
                if parameter != 'VL': # VL is length of variable in PLC not in PVI !
                    self._parentObject._objectDescriptor.update({parameter: value })
        del ex

        # correct the members' VO and VL since PVI_ACC_TYPE_EXTERN delivers PLC variable information 
        # not PVI tag information !

        for li in (self._innerStructures, self._members):
            for n, extern in enumerate(li):
                for intern in self._memberOffsets:
                    if extern.name == intern.name and extern.vt == intern.vt and extern.vo != intern.vo:
                        li[n] = StructMember( extern.name, extern.vt, extern.sn, extern.vn, intern.vo, intern.vl, extern.vs)
        self._memberOffsets.clear() # the offsets are not needed anymore

        # sort inner structures with highest nesting depth first
        self._innerStructures.sort( key = lambda s : s.name.count('.'), reverse=True)

        # correct names and offsets of structure members
        for structure in self._innerStructures:
            newMembers : List[StructMember] = list()
            oldMembers = self._members.copy()
            for mb in self._members:
                if mb.name.startswith( structure.name ):
                    if structure.vn > 1 or structure.vs.startswith('a'): # struct is an array
                        lowerIndex = 0
                        if len(structure.vs) != 0:
                            m = patternVSa.findall(structure.vs)
                            if m:
                                lowerIndex = int(m[0][0])
                        elementName = mb.name[len(structure.name):]
                        oldMembers.remove(mb)
                        for index in range(0, structure.vn ):
                            # correct name + offset
                            newMembers.append( StructMember( f"{structure.name}[{index+lowerIndex}]{elementName}", mb.vt, mb.sn, mb.vn, mb.vo + structure.vo + structure.vl*index, mb.vl, mb.vs))
                        del index, elementName
                    else: # structure is not an array
                        oldMembers.remove(mb)
                        # correct offset only
                        newMembers.append( StructMember( mb.name, mb.vt, mb.sn, mb.vn, mb.vo + structure.vo, mb.vl, mb.vs ) )
            self._members = oldMembers                            
            self._members.extend(newMembers)
            del oldMembers, newMembers, mb
        # sort structure members according variable offsets
        self._members.sort(key = lambda m: m.vo)
        pass


    def _updateMemberList(self, s ):
        '''
        extract data type member's information
        s : member definition returned by POBJ_ACC_TYPE_EXTERN
            e.g "{.ton.IN VT=boolean VL=1 VN=1 VO=16}"
        '''
        desc: dict[str, str] = {} # member's object descriptor
        for m in patternStructureMemberDefinition.finditer(s): # find matches
            ex = m.group()
            if ex.startswith('.'):
                desc.update({'name' : ex}) # member's name
            else:
                desc.update({ex[0:2]: ex[3:]}) # member's object descriptor

        vt = PvType(desc.get('VT'))
        sn = str(desc.get('SN', ''))        
        vo = int(desc.get('VO',0)) # variable offset in PLC but not in PVI !
        vn = int(desc.get('VN',0))
        vl = int(desc.get('VL',0))
        vs = str(desc.get('VS',''))
        name = desc.get('name','')
        if vt == PvType.STRUCT:
            self._innerStructures.append(  StructMember( name, vt, sn, vn, vo, vl, vs ) )
        elif vt != PvType.UNKNOWN:
            self._members.append(  StructMember( name, vt, sn, vn, vo, vl, vs ) )

        


    def _unpackRawData(self, data : bytes, vt : PvType, vl :int):
        '''
        unpacks data returned by PVI_ACC_DATA or PVI_EVENT_DATA to the appropriate Python data type
        data: ctype raw data        
        vt: PVI variable type
        vl: variable byte length 
        '''        
        if vt == PvType.BOOLEAN:
            return bool(struct.unpack('<?', data )[0])
        elif vt == PvType.U8:
            return struct.unpack('<B', data )[0] 
        elif vt == PvType.I8:
            return struct.unpack('<b', data)[0] 
        elif vt == PvType.U16:
            return struct.unpack('<H', data)[0] 
        elif vt == PvType.I16:
            return struct.unpack('<h', data)[0] 
        elif vt == PvType.U32 or vt == PvType.DT  or vt == PvType.DATE or vt == PvType.TOD:
            value = struct.unpack('<L', data)[0]
            if vt == PvType.DT:
                return datetime.datetime.fromtimestamp(value)
            elif vt == PvType.DATE:
                return datetime.date.fromtimestamp(value)                    
            elif vt == PvType.TOD:
                hour = int(value / 3600000)
                value %= 3600000
                minute = int(value / 60000)
                value %= 60000
                second = int(value/1000)
                millisecond = value % 1000
                return datetime.time( hour = hour, minute = minute, second = second, microsecond=millisecond*1000 ) 
            else:
                return value           
        elif vt == PvType.I32 or vt == PvType.TIME:
            value = struct.unpack('<l', data)[0]
            if vt == PvType.TIME:
                absValue = abs(value)
                sgn = 1 if value >= 0 else -1
                days = int(absValue / 86400000 )
                absValue %= 86400000
                seconds = int(absValue/1000)
                milliseconds = absValue % 1000
                return sgn * datetime.timedelta( days = days, seconds = seconds, microseconds=milliseconds*1000 )           
            else:
                return value
        elif vt == PvType.U64:
            return struct.unpack('<Q', data)[0] 
        elif vt == PvType.I64:
            return struct.unpack('<q', data)[0] 
        elif vt == PvType.F32:
            return struct.unpack('<f', data)[0] 
        elif vt == PvType.F64:
            return struct.unpack('<d', data)[0] 
        elif vt == PvType.STRING:
            return bytes(''.join( chr(_) for _ in data if _ != 0 ), 'ascii')
        elif vt == PvType.WSTRING:
            return ''.join( chr(int(data[_]) + int(data[_+1])) for _ in range(0,len(data),2) if int(data[_]))
        else:
            raise BaseException("not implemented")


    def readFromBuffer(self, buffer : bytes):
        '''
        gets the value from raw buffer data.
        returns a tuple in case of array.

        buffer : raw buffer data from POBJ_ACC_DATA
        '''
        assert type(self._vl) is int
        arrayBuffers = ( buffer[_:_+self._vl] for _ in range(0,len(buffer), self._vl)) # split buffer into array elements
        result = list()

        for elementBuffer in arrayBuffers:
            if self._vt == PvType.STRUCT:
                structResult = OrderedDict()
                assert isinstance( self._members, list)
                for m in self._members:
                    if m.vn == 1: # struct member is a single value
                        buf = elementBuffer[m.vo : m.vo+m.vl]
                        value = self._unpackRawData( buf, m.vt, m.vl )
                    else: # struct member is an array
                        memberBuffers = ( elementBuffer[_:_+m.vl] for _ in range( m.vo, m.vo + m.vl*m.vn, m.vl)) # split buffer
                        value = tuple( self._unpackRawData( _, m.vt, m.vl ) for _ in memberBuffers )
                    structResult.update( { m.name : value } )
                result.append( structResult )
            else:
                result.append( self._unpackRawData( elementBuffer, self._vt, self._vl ) )

        if len(result) == 1: # single value
            return result[0]
        else:
            return tuple(result)


    def writeToBuffer(self, value):
        '''
        packs Python data type to byte buffer
        value: value
        '''     
        buffer = None

        if self._vn > 1 and not isinstance(value, list) and not isinstance(value, tuple): # variable is an array
            value = [value for _ in range(0, self._vn)] # create a list with identical values

        try:
            if self._vt == PvType.BOOLEAN:
                if self._vn == 1: # single value
                    buffer = c_bool(value != 0)
                else: # array of BOOLEAN
                    buffer = (c_bool*self._vn)(*value)

            elif self._vt == PvType.U8:           
                if self._vn == 1: # single value
                    assert type(value) is int
                    buffer = c_uint8(value)
                else: # array of U8
                    buffer = (c_uint8*self._vn)(*value)

            elif self._vt == PvType.I8:              
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_int8(value)
                else: # array of I8
                    buffer = (c_int8*self._vn)(*value)

            elif self._vt == PvType.U16:             
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_uint16(value)
                else: # array of U16
                    buffer = (c_uint16*self._vn)(*value)

            elif self._vt == PvType.I16:              
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_int16(value)
                else: # array of I16
                    buffer = (c_int16*self._vn)(*value)

            elif self._vt == PvType.U32:              
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_uint32(value)
                else: # array of U32
                    buffer = (c_uint32*self._vn)(*value)

            elif self._vt == PvType.DT:
                if self._vn == 1: # single value
                    if type(value) == datetime.datetime:
                        buffer = c_uint32( int(value.timestamp()) )
                    elif type(value) == int:
                        buffer = c_uint32(value)
                else: # array of DT
                    if type(value[0]) == datetime.datetime:
                        v = (int(v.timestamp()) for v in value)
                        buffer = (c_uint32*self._vn)( *v )
                    elif type(value[0]) == int:
                        buffer = (c_uint32*self._vn)(*value)

            elif self._vt == PvType.DATE:
                if self._vn == 1: # single value
                    if type(value) == datetime.date:
                        value = datetime.datetime.combine(value, datetime.time())
                        buffer = c_uint32( int(value.timestamp()) )
                    elif type(value) == int:
                        buffer = c_uint32(value)
                else: # array of DATE
                    if type(value[0]) == datetime.date:
                        v = (int(datetime.datetime.combine(v, datetime.time()).timestamp()) for v in value)
                        buffer = (c_uint32*self._vn)( *v )
                    elif type(value[0]) == int:
                        buffer = (c_uint32*self._vn)(*value)            

            elif self._vt == PvType.TOD:
                if self._vn == 1: # single value
                    if type(value) == datetime.time:
                        buffer = c_uint32( value.hour * 3600000 + value.minute * 60000 + value.second * 1000 + int(value.microsecond / 1000) )
                    elif type(value) == int:
                        buffer = c_uint32(value)
                else: # array of TOD
                    if type(value[0]) == datetime.time:
                        v = (v.hour * 3600000 + v.minute * 60000 + v.second * 1000 + int(v.microsecond / 1000) for v in value)
                        buffer = (c_uint32*self._vn)( *v )
                    elif type(value[0]) == int:
                        buffer = (c_uint32*self._vn)(*value)

            elif self._vt == PvType.TIME:
                if self._vn == 1: # single value
                    if type(value) == datetime.timedelta: 
                        buffer = c_int32( int( value / datetime.timedelta(milliseconds=1)) )
                    elif type(value) == int:
                        buffer = c_int32(value)
                else: # array of TIME
                    if type(value[0]) == datetime.timedelta: 
                        v = (int( v / datetime.timedelta(milliseconds=1)) for v in value)
                        buffer = (c_int32*self._vn)( *v)
                    elif type(value[0]) == int:
                        buffer = (c_int32*self._vn)(value)

            elif self._vt == PvType.I32:
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_int32(value)
                else: # array of I32
                    buffer = (c_int32*self._vn)(*value)                

            elif self._vt == PvType.U64:              
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_uint64(value)
                else: # array of U64
                    buffer = (c_uint64*self._vn)(*value)                

            elif self._vt == PvType.I64:               
                if self._vn == 1: # single value 
                    assert type(value) is int                    
                    buffer = c_int64(value)
                else: # array of I64
                    buffer = (c_int64*self._vn)(*value)                                

            elif self._vt == PvType.F32:
                if self._vn == 1: # single value
                    assert type(value) is float                    
                    buffer = c_float(value)
                else: # array of F32
                    buffer = (c_float*self._vn)(*value)                

            elif self._vt == PvType.F64:              
                if self._vn == 1: # single value
                    assert type(value) is float
                    buffer = c_double(value)
                else: # array of F64
                    buffer = (c_double*self._vn)(*value)                

            elif self._vt == PvType.STRING:
                if self._vn == 1: # single value
                    if type(value) == bytes:
                        buffer = (c_char * self._vl)(*value)
                else: # array of STRING
                    if type(value[0]) == bytes:
                        buffer = ((c_char * self._vl) * self._vn)()
                        for n, v in enumerate(value):
                            s = (c_char*self._vl)(*v)
                            buffer[n] = s

            elif self._vt == PvType.WSTRING:
                ch = int(self._vl/2) # no of characters
                if self._vn == 1:
                    if type(value) == bytes:
                        value = value.decode()                
                    buffer = (c_wchar * ch )(*value)                
                else: # array of WSTRING
                    buffer = ((c_wchar * (ch)*self._vn))()
                    for n, v in enumerate(value):
                        if type(v) == bytes:
                            v = v.decode()
                        for j,c in enumerate(v):
                            buffer[n][j] = c
            else:
                raise RuntimeError( "data type " + str(self._vt) + " not implemented")
            
        except IndexError:
            raise IndexError(f'wrong length writing {value}\nto {repr(self._parentObject)}')            
        except BaseException as e:
            raise e
                    
        if buffer == None:
            raise ValueError(f'wrong data type {type(value)} used\nwriting {repr(self._parentObject)}')

        return buffer
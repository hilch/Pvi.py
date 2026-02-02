
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

from typing import List, Deque, Tuple, Union, Any
from enum import IntEnum
import datetime
from dataclasses import dataclass
from ctypes import c_bool, c_uint8, c_int8, c_uint16, c_int16, c_uint32, c_int32, c_uint64, c_int64, c_float, c_double
from ctypes import c_char, c_wchar
import re
import struct
from collections import deque
from .include import *


patternDataTypeInformation = re.compile(r"([A-Z]{2}=[\w\x2C\x3B\x2D]+)|(\{[^}]+\})") # pattern for variable definition
patternStructureMemberDefinition = re.compile(r"(\x2E[\w\x2E]+)|([A-Z]{2}=[\w\x2C\x3B\x2D]+)") # pattern for structure member definition
patternVSa = re.compile(r"((?:a,)(-?\d+),(-?\d+))") # pattern for parameter VS=a
patternVSe = re.compile(r"(e,(\d+),([a-zA-Z_]\w*))") # pattern for parameter VS=e
patternVSv = re.compile(r"(?:v,)(-?\d+),(-?\d+)") # pattern for parameter VS=v

@dataclass
class TypeDescription:
    name : str = ''
    at : str = ''  # access type
    sc : str = ''  # scope
    vt : PvType = PvType.UNKNOWN   # variable datatype
    vl : int = 0    # variable's length
    vn : int = 0    # number of elements    
    vs : str = ''   # variable's additional specification
    al : int = 1    # structure alignment
    sn : str = ''   # structure name if member is a struct itself
    tn : str = ''   # derived type name
    vo : int = 0    # variable's offset

    def parse( self, s : str):
        desc: dict[str, str] = {} # member's object descriptor
        for m in patternStructureMemberDefinition.finditer(s): # find matches
            ex = m.group()
            if ex.startswith('.'):
                desc.update({'name' : ex}) # member's name
            else:
                desc.update({ex[0:2]: ex[3:]}) # member's object descriptor

        self.at = str(desc.get('AT', ''))
        self.sc = str(desc.get('SC', ''))        
        self.vt = PvType(desc.get('VT'))
        self.vl = int(desc.get('VL',0)) 
        self.vn = int(desc.get('VN',0))               
        self.vs = str(desc.get('VS',''))
        self.al = int(desc.get('AL', 1))
        self.sn = str(desc.get('SN', ''))
        self.tn = str(desc.get('TN', ''))
        self.vo = int(desc.get('VO',0)) # variable offset in PLC but not in PVI !      
        self.name = desc.get('name','')


    def get_array_indices(self) -> Union[List[Tuple[int,int]], None]:
        if 'a' in self.vs:
            l = []
            for m in patternVSa.finditer(self.vs):
                l.append( (int(m.group(2)), int(m.group(3))) )
            return l
        elif self.vn > 1:
            return [(0, self.vn-1)]
        else:
            return None
        
    def get_enum_range(self) -> Union[dict,None]:
        if 'e' in self.vs:
            enum_values = dict()
            for m in patternVSe.finditer(self.vs):
                enum_values.update({ m.group(3) : m.group(2)})
            return enum_values
        else:
            return None
        
    def get_subrange(self) -> Union[Tuple[int,int],None]:
        if 'v' in self.vs:
            m = patternVSv.match(self.vs)
            if m:
                return (int(m.group(1)), int(m.group(2)))
        return None
        
    def get_buffer_size(self) -> int:
        return self.vn * self.vl
                
                
    def unpack_data_from_buffer(self, data : bytes):
        '''
        unpacks data returned by PVI_ACC_DATA or PVI_EVENT_DATA to the appropriate Python data type
        data: ctype raw data        
        '''        
        if self.vt == PvType.BOOLEAN:
            return bool(struct.unpack('<?', data )[0])
        elif self.vt == PvType.U8:
            return struct.unpack('<B', data )[0] 
        elif self.vt == PvType.I8:
            return struct.unpack('<b', data)[0] 
        elif self.vt == PvType.U16:
            return struct.unpack('<H', data)[0] 
        elif self.vt == PvType.I16:
            return struct.unpack('<h', data)[0] 
        elif self.vt == PvType.U32 or self.vt == PvType.DT  or self.vt == PvType.DATE or self.vt == PvType.TOD:
            value = struct.unpack('<L', data)[0]
            if self.vt == PvType.DT:
                date = datetime.datetime.fromtimestamp( value, tz = datetime.timezone.utc )
                return date.replace(tzinfo=None)
            elif self.vt == PvType.DATE:            
                return datetime.date.fromtimestamp(value)
            elif self.vt == PvType.TOD:
                hour = int(value / 3600000)
                value %= 3600000
                minute = int(value / 60000)
                value %= 60000
                second = int(value/1000)
                millisecond = value % 1000
                return datetime.time( hour = hour, minute = minute, second = second, microsecond=millisecond*1000 ) 
            else:
                return value           
        elif self.vt == PvType.I32 or self.vt == PvType.TIME:
            value = struct.unpack('<l', data)[0]
            if self.vt == PvType.TIME:
                absValue = abs(value)
                sgn = 1 if value >= 0 else -1
                days = int(absValue / 86400000 )
                absValue %= 86400000
                seconds = int(absValue/1000)
                milliseconds = absValue % 1000
                return sgn * datetime.timedelta( days = days, seconds = seconds, microseconds=milliseconds*1000 )           
            else:
                if 'e' in self.vs: # enum ?
                    enum_range = self.get_enum_range()
                    assert(enum_range)
                    dynamic_enum : IntEnum = IntEnum( self.sn, enum_range )
                    if value in dynamic_enum:
                        value = dynamic_enum(value) # type: ignore
                return value
        elif self.vt == PvType.U64:
            return struct.unpack('<Q', data)[0] 
        elif self.vt == PvType.I64:
            return struct.unpack('<q', data)[0] 
        elif self.vt == PvType.F32:
            return struct.unpack('<f', data)[0] 
        elif self.vt == PvType.F64:
            return struct.unpack('<d', data)[0] 
        elif self.vt == PvType.STRING:
            result = bytearray()
            for c in data:
                if c:
                    result.append(c)
                else:
                    break
            return bytes(result)
        elif self.vt == PvType.WSTRING:
            return ''.join( chr(int(data[_]) + int(data[_+1])) for _ in range(0,len(data),2) if int(data[_]))
        elif self.vt == PvType.STRUCT:
            return data
        else:
            raise BaseException("not implemented")                
        
        
    def pack_value_to_buffer(self, value) -> Any:
        '''
        packs Python data type to byte buffer
        value: value
        '''     
        buffer = None
        single_value = not(bool(self.get_array_indices()))

        if self.get_array_indices() and not isinstance(value, list) and not isinstance(value, tuple): # variable is an array
            value = [value for _ in range(0, self.vn)] # create a list with identical values

        try:
            if self.vt == PvType.BOOLEAN:
                if single_value: # single value
                    buffer = c_bool(value != 0)
                else: # array of BOOLEAN
                    buffer = (c_bool*self.vn)(*value)

            elif self.vt == PvType.U8:           
                if single_value: # single value
                    assert type(value) is int
                    buffer = c_uint8(value)
                else: # array of U8
                    buffer = (c_uint8*self.vn)(*value)

            elif self.vt == PvType.I8:              
                if single_value: # single value
                    assert type(value) is int                    
                    buffer = c_int8(value)
                else: # array of I8
                    buffer = (c_int8*self.vn)(*value)

            elif self.vt == PvType.U16:             
                if single_value: # single value
                    assert type(value) is int                    
                    buffer = c_uint16(value)
                else: # array of U16
                    buffer = (c_uint16*self.vn)(*value)

            elif self.vt == PvType.I16:              
                if single_value: # single value
                    assert type(value) is int                    
                    buffer = c_int16(value)
                else: # array of I16
                    buffer = (c_int16*self.vn)(*value)

            elif self.vt == PvType.U32:              
                if single_value: # single value
                    assert type(value) is int                    
                    buffer = c_uint32(value)
                else: # array of U32
                    buffer = (c_uint32*self.vn)(*value)

            elif self.vt == PvType.DT:
                if single_value: # single value
                    if type(value) == datetime.datetime:
                        v = int(value.replace(tzinfo=datetime.timezone.utc).timestamp())
                        buffer = c_uint32( v )
                    elif type(value) == int:
                        buffer = c_uint32(value)
                else: # array of DT
                    if type(value[0]) == datetime.datetime:
                        v = (int(v.replace(tzinfo=datetime.timezone.utc).timestamp()) for v in value)
                        buffer = (c_uint32*self.vn)( *v )
                    elif type(value[0]) == int:
                        buffer = (c_uint32*self.vn)(*value)

            elif self.vt == PvType.DATE:
                if single_value: # single value
                    if type(value) == datetime.date:
                        value = datetime.datetime.combine(value, datetime.time(), tzinfo=datetime.timezone.utc)
                        buffer = c_uint32( int(value.timestamp()) )
                    elif type(value) == int:
                        buffer = c_uint32(value)
                else: # array of DATE
                    if type(value[0]) == datetime.date:
                        v = (int(datetime.datetime.combine(v, datetime.time(), tzinfo=datetime.timezone.utc).timestamp()) for v in value)
                        buffer = (c_uint32*self.vn)( *v )
                    elif type(value[0]) == int:
                        buffer = (c_uint32*self.vn)(*value)            

            elif self.vt == PvType.TOD:
                if single_value: # single value
                    if type(value) == datetime.time:
                        buffer = c_uint32( value.hour * 3600000 + value.minute * 60000 + value.second * 1000 + int(value.microsecond / 1000) )
                    elif type(value) == int:
                        buffer = c_uint32(value)
                else: # array of TOD
                    if type(value[0]) == datetime.time:
                        v = (v.hour * 3600000 + v.minute * 60000 + v.second * 1000 + int(v.microsecond / 1000) for v in value)
                        buffer = (c_uint32*self.vn)( *v )
                    elif type(value[0]) == int:
                        buffer = (c_uint32*self.vn)(*value)

            elif self.vt == PvType.TIME:
                if single_value: # single value
                    if type(value) == datetime.timedelta: 
                        buffer = c_int32( int( value / datetime.timedelta(milliseconds=1)) )
                    elif type(value) == int:
                        buffer = c_int32(value)
                else: # array of TIME
                    if type(value[0]) == datetime.timedelta: 
                        v = (int( v / datetime.timedelta(milliseconds=1)) for v in value)
                        buffer = (c_int32*self.vn)( *v)
                    elif type(value[0]) == int:
                        buffer = (c_int32*self.vn)(value)

            elif self.vt == PvType.I32:
                if single_value: # single value
                    assert type(value) is int                    
                    buffer = c_int32(value)
                else: # array of I32
                    buffer = (c_int32*self.vn)(*value)                

            elif self.vt == PvType.U64:              
                if single_value: # single value
                    assert type(value) is int                    
                    buffer = c_uint64(value)
                else: # array of U64
                    buffer = (c_uint64*self.vn)(*value)                

            elif self.vt == PvType.I64:               
                if single_value: # single value 
                    assert type(value) is int                    
                    buffer = c_int64(value)
                else: # array of I64
                    buffer = (c_int64*self.vn)(*value)                                

            elif self.vt == PvType.F32:
                if single_value: # single value
                    assert type(value) is float                    
                    buffer = c_float(value)
                else: # array of F32
                    buffer = (c_float*self.vn)(*value)                

            elif self.vt == PvType.F64:              
                if single_value: # single value
                    assert type(value) is float
                    buffer = c_double(value)
                else: # array of F64
                    buffer = (c_double*self.vn)(*value)                

            elif self.vt == PvType.STRING:
                if single_value: # single value
                    if type(value) == bytes:
                        buffer = (c_char * self.vl)(*value)
                else: # array of STRING
                    if type(value[0]) == bytes:
                        buffer = ((c_char * self.vl) * self.vn)()
                        for n, v in enumerate(value):
                            s = (c_char*self.vl)(*v)
                            buffer[n] = s

            elif self.vt == PvType.WSTRING:
                ch = int(self.vl/2) # no of characters
                if single_value:
                    if type(value) == bytes:
                        value = value.decode()                
                    buffer = (c_wchar * ch )(*value)                
                else: # array of WSTRING
                    buffer = ((c_wchar * (ch)*self.vn))()
                    for n, v in enumerate(value):
                        if type(v) == bytes:
                            v = v.decode()
                        for j,c in enumerate(v):
                            buffer[n][j] = c
            else:
                raise RuntimeError( "data type " + str(self.vt) + " not implemented")
            
        except IndexError:
            raise IndexError('wrong length writing {value}')            
        except BaseException as e:
            raise e
                    
        if buffer == None:
            raise ValueError(f'wrong data type {type(value)} used.')

        return buffer        
                
          
    def as_dict( self ) -> dict:
        return {
            'name' : self.name,
            'at' : self.at,
            'sc' : self.sc,
            'vt' : self.vt,
            'vl' : self.vl,
            'vn' : self.vn,
            'vs' : self.vs,
            'al' : self.al,
            'sn' : self.sn,
            'tn' : self.tn,
            'vo' : self.vo
        }


class MemberStack:
    '''
    class for calculating byte offsets of internal members
    '''
    def __init__(self) -> None:
        self._items: Deque[TypeDescription] = deque()
        self._currentLevel = 0

    def clear(self):
        self._items.clear()
        self._currentLevel = 0

    def push(self, member : TypeDescription) -> None:       
        self._items.append(member)
        self._currentLevel += 1

    def pop(self) -> TypeDescription:
        if not self._items:
            raise IndexError("pop from empty stack")
        self._currentLevel -= 1
        return self._items.pop()
    
    def peek(self) -> TypeDescription :
        if not self._items:
            return TypeDescription()
        return self._items[-1]
    
    @property
    def level(self) -> int:
        return self._currentLevel
    
    

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

from typing import List, Tuple, Union, Any
from enum import IntEnum
import datetime
from dataclasses import dataclass
from ctypes import (c_bool, c_uint8, c_int8, c_uint16, c_int16, 
                    c_uint32, c_int32, c_uint64, c_int64, c_float, 
                    c_double, c_char, c_wchar)
import re
import struct
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
        self.vn = int(desc.get('VN',1))               
        self.vs = str(desc.get('VS',''))
        self.al = int(desc.get('AL', 1))
        self.sn = str(desc.get('SN', ''))
        self.tn = str(desc.get('TN', ''))
        self.vo = int(desc.get('VO',0)) # variable offset in PLC but not in PVI !      
        self.name = desc.get('name','')


    def get_array_indices(self) -> Union[List[Tuple[int,int]], None]:
        if 'a' in self.vs:
            indices = []
            for m in patternVSa.finditer(self.vs):
                indices.append( (int(m.group(2)), int(m.group(3))) )
            if len(indices) > 0:
                return indices
            else:
                return [(0,0)]
        elif self.vn > 1:
            return [(0, self.vn-1)]
        else:
            return None
        
    def get_enum_range(self) -> Union[dict,None]:
        if 'e' in self.vs:
            enum_values = dict()
            for m in patternVSe.finditer(self.vs):
                enum_values.update({ m.group(3) : int(m.group(2))})
            return enum_values
        else:
            return None
        
    def get_subrange(self) -> Union[Tuple[int,int],None]:
        if 'v' in self.vs:
            m = patternVSv.match(self.vs)
            if m:
                return (int(m.group(1)), int(m.group(2)))
        return None
        
    def get_order(self) -> int:
        return self.name.count('.')
        
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
                    try:
                        value = dynamic_enum(value) # type: ignore
                    except:
                        pass
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
            s = data.decode('utf-16-le').split('\x00')[0]
            return s
        elif self.vt == PvType.STRUCT:
            return data
        else:
            raise BaseException("not implemented")                
        
        

    # -----------------------------------------------------------------------
    # Per-type pack helpers 
    # -----------------------------------------------------------------------
    def _pack_dt(self, value, single_value):
        if single_value:
            if isinstance( value, datetime.datetime):
                v = int(value.replace(tzinfo=datetime.timezone.utc).timestamp())
                return c_uint32(v)
            elif isinstance(value, int):
                return c_uint32(value)
        else:
            if isinstance(value[0], datetime.datetime):
                v = (int(v.replace(tzinfo=datetime.timezone.utc).timestamp()) for v in value)
                return (c_uint32*self.vn)(*v)
            elif isinstance(value[0], int):
                return (c_uint32*self.vn)(*value)
        return None

    def _pack_date(self, value, single_value):
        if single_value:
            if isinstance(value, datetime.date):
                value = datetime.datetime.combine(value, datetime.time(), tzinfo=datetime.timezone.utc)
                return c_uint32(int(value.timestamp()))
            elif isinstance(value, int):
                return c_uint32(value)
        else:
            if isinstance(value[0], datetime.date):
                v = (int(datetime.datetime.combine(v, datetime.time(), tzinfo=datetime.timezone.utc).timestamp()) for v in value)
                return (c_uint32*self.vn)(*v)
            elif isinstance(value[0], int):
                return (c_uint32*self.vn)(*value)
        return None

    def _pack_tod(self, value, single_value):
        if single_value:
            if isinstance(value, datetime.time):
                return c_uint32(value.hour * 3600000 + value.minute * 60000 + value.second * 1000 + int(value.microsecond / 1000))
            elif isinstance(value, int):
                return c_uint32(value)
        else:
            if isinstance(value[0], datetime.time):
                v = (v.hour * 3600000 + v.minute * 60000 + v.second * 1000 + int(v.microsecond / 1000) for v in value)
                return (c_uint32*self.vn)(*v)
            elif isinstance(value[0], int):
                return (c_uint32*self.vn)(*value)
        return None

    def _pack_time(self, value, single_value):
        if single_value:
            if isinstance(value, datetime.timedelta):
                return c_int32(int(value / datetime.timedelta(milliseconds=1)))
            elif isinstance(value, int):
                return c_int32(value)
        else:
            if isinstance(value[0], datetime.timedelta):
                v = (int(v / datetime.timedelta(milliseconds=1)) for v in value)
                return (c_int32*self.vn)(*v)
            elif isinstance(value[0], int):
                return (c_int32*self.vn)(*value)
        return None

    def _pack_string(self, value, single_value):
        if single_value:
            if isinstance(value, bytes):
                return (c_char * self.vl)(*value)
        else:
            if isinstance(value[0], bytes):
                buffer = ((c_char * self.vl) * self.vn)()
                for n, v in enumerate(value):
                    s = (c_char*self.vl)(*v)
                    buffer[n] = s
                return buffer
        return None

    def _pack_wstring(self, value, single_value):
        ch = int(self.vl/2) # no of characters
        if single_value:
            if isinstance(value, bytes):
                value = value.decode()
            return (c_wchar * ch)(*value)
        else:
            buffer = ((c_wchar * (ch)*self.vn))()
            for n, v in enumerate(value):
                if isinstance(v, bytes):
                    v = v.decode()
                for j, c in enumerate(v):
                    buffer[n][j] = c
            return buffer

    # -----------------------------------------------------------------------
    # Generic pack helper 
    # -----------------------------------------------------------------------
    def _pack_ctype(self, ctype_class, value):
        '''Pack single value or array into the given ctype class.'''
        if self.get_array_indices():
            return (ctype_class * self.vn)(*value)
        return ctype_class(value)

    def pack_value_to_buffer(self, value : Any) -> Any:
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
                buffer = self._pack_ctype(c_bool, value != 0 if single_value else [v != 0 for v in value])  

            elif self.vt == PvType.U8:           
                buffer = self._pack_ctype(c_uint8, value)  

            elif self.vt == PvType.I8:              
                buffer = self._pack_ctype(c_int8, value)  

            elif self.vt == PvType.U16:             
                buffer = self._pack_ctype(c_uint16, value) 

            elif self.vt == PvType.I16:              
                buffer = self._pack_ctype(c_int16, value)  

            elif self.vt == PvType.U32:              
                buffer = self._pack_ctype(c_uint32, value)  

            elif self.vt == PvType.DT:
                buffer = self._pack_dt(value, single_value)  

            elif self.vt == PvType.DATE:
                buffer = self._pack_date(value, single_value)  

            elif self.vt == PvType.TOD:
                buffer = self._pack_tod(value, single_value)  

            elif self.vt == PvType.TIME:
                buffer = self._pack_time(value, single_value)  

            elif self.vt == PvType.I32:
                if single_value: # single value
                    try:
                        value = value.value # type: ignore
                    except:
                        pass
                    if isinstance(value, int):
                        buffer = c_int32(value)
                    else:
                        raise TypeError("Wrong Type. Expected 'int'")
                else: # array of I32
                    buffer = (c_int32*self.vn)(*value)                

            elif self.vt == PvType.U64:              
                buffer = self._pack_ctype(c_uint64, value)                 

            elif self.vt == PvType.I64:               
                buffer = self._pack_ctype(c_int64, value)                                 

            elif self.vt == PvType.F32:
                value = float(value) if single_value else value  # type: ignore
                buffer = self._pack_ctype(c_float, value)               

            elif self.vt == PvType.F64:              
                value = float(value) if single_value else value  # type: ignore
                buffer = self._pack_ctype(c_double, value)                

            elif self.vt == PvType.STRING:
                buffer = self._pack_string(value, single_value) 

            elif self.vt == PvType.WSTRING:
                buffer = self._pack_wstring(value, single_value)  
            else:
                raise RuntimeError( "data type " + str(self.vt) + " not implemented")
            
        except IndexError:
            raise IndexError('wrong length writing {value}')            
        except BaseException as e:
            raise e
                    
        if buffer == None:
            raise ValueError(f'wrong data type {type(value)} used.')

        return buffer        
                
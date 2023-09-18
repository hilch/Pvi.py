
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

import datetime

from ctypes import sizeof, create_string_buffer
from ctypes import c_bool, c_uint8, c_int8, c_uint16, c_int16, c_uint32, c_int32, c_uint64, c_int64, c_float, c_double
from ctypes import c_char, c_wchar
import re
import struct
from collections import namedtuple, OrderedDict
from .Error import PviError
from .Object import PviObject
from .include import *


patternDataTypeInformation = re.compile(r"([A-Z]{2}=\w+)|(\{[^}]+\})")
patternStructureElementDefinition = re.compile(r"(\x2E[a-zA-z0-9_.]+)|([A-Z]{2}=\w+)")

StructMember = namedtuple( 'StructMember', ['name', 'vt', 'vn', 'vo', 'vl'])
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
        self._parentObject = None
        self._members = None # let's assume a basic variable type
        '''
        list of all data type (structure) members if this variable is a struct
        '''

    def readFrom(self, object : PviObject ):
        '''
        read type description from object
        object: Variable object
        '''        
        self._parentObject = object

        s = create_string_buffer(b'\000' * 64*1024) 
        object._result = PviRead( self._parentObject._linkID, POBJ_ACC_TYPE_INTERN, None, 0, s, sizeof(s) )
        if self._parentObject._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
        else:
            raise PviError(self._parentObject._result, self._parentObject)

        self._parentObject._objectDescriptor.update({'VN' : '1', 'VL' : '1' })

        self._updateObjectDescriptor(s) # udpate objects descriptor
        vt = PvType( self._parentObject._objectDescriptor.get('VT')) 
        self._vt = vt

        vn = int( self._parentObject.descriptor.get('VN', 0) )
        assert vn > 0
        self._vn = vn

        vl = int( self._parentObject.descriptor.get('VL', 0) )
        assert vl > 0
        self._vl = vl
         
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
    def vt(self) -> PvType:
        '''
        PVI Variable Type : PvType
        '''        
        return self._vt

    def _updateObjectDescriptor(self, s):
        '''
        update object descriptor and find all members if this PV is a structure
        '''
        self._innerStructOffsets = dict() # save vo of inner structs to correct their members' offsets
        for m in patternDataTypeInformation.finditer(s) : # update object descriptor
            ex = m.group()
            if ex.startswith('{'): # structure member definition
                if self._members == None:
                    self._members = list()
                self._updateMemberList(ex)
            else:
                assert isinstance(self._parentObject, PviObject)
                self._parentObject._objectDescriptor.update({ex[0:2]: ex[3:]}) 
        del self._innerStructOffsets


    def _updateMemberList(self, s ):
        '''
        extract data type member's information
        s : member definition returned by POBJ_ACC_TYPE_INTERN
            e.g "{.ton.IN VT=boolean VL=1 VN=1 VO=16}"
        '''
        desc: dict[str, str] = {} # member's object descriptor
        for m in patternStructureElementDefinition.finditer(s): # find matches
            ex = m.group()
            if ex.startswith('.'):
                desc.update({'name' : ex}) # member's name
            else:
                desc.update({ex[0:2]: ex[3:]}) # member's object descriptor

        vt = PvType(desc.get('VT'))
        vo = desc.get('VO') # variable offset
        assert type(vo) is int
        vn = desc.get('VN')
        assert type(vn) is int
        vl = desc.get('VL')        
        assert type(vl) is int
        name = desc.get('name')
        assert type(name) is str
        parentStruct = name.rpartition('.')[0]

        if parentStruct in self._innerStructOffsets: # does member belong to an inner struct ?
            vo += self._innerStructOffsets[parentStruct]
 
        if vt == PvType.STRUCT: # is member itself an inner structure ?
            self._innerStructOffsets.update( { name :vo } )
        else:
            assert isinstance( self._members, list )
            self._members.append(  StructMember( name, vt, vn, vo, vl ) )


    def _unpackRawData(self, data : bytes, vt : PvType, vl :int):
        '''
        unpacks data returned by PVI_ACC_DATA or PVI_EVENT_DATA to the appropiate Python data type
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
        assert type(self.vl) is int
        arrayBuffers = ( buffer[_:_+self.vl] for _ in range(0,len(buffer), self.vl)) # split buffer into array elements
        result = list()

        for elementBuffer in arrayBuffers:
            if self.vt == PvType.STRUCT:
                structResult = OrderedDict()
                assert isinstance( self._members, list)
                for m in self._members:
                    if m.vn == 1: # struct member is asingle value
                        buf = elementBuffer[m.vo : m.vo+m.vl]
                        value = self._unpackRawData( buf, m.vt, m.vl )
                    else: # struct member is an array
                        memberBuffers = ( elementBuffer[_:_+m.vl] for _ in range( m.vo, m.vo + m.vl*m.vn, m.vl)) # split buffer
                        value = tuple( self._unpackRawData( _, m.vt, m.vl ) for _ in memberBuffers )
                    structResult.update( { m.name : value } )
                result.append( structResult )
            else:
                result.append( self._unpackRawData( elementBuffer, self.vt, self.vl ) )

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
            if self.vt == PvType.BOOLEAN:
                if self._vn == 1: # single value
                    buffer = c_bool(value != 0)
                else: # array of BOOLEAN
                    buffer = (c_bool*self._vn)(*value)

            elif self.vt == PvType.U8:           
                if self._vn == 1: # single value
                    assert type(value) is int
                    buffer = c_uint8(value)
                else: # array of U8
                    buffer = (c_uint8*self._vn)(*value)

            elif self.vt == PvType.I8:              
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_int8(value)
                else: # array of I8
                    buffer = (c_int8*self._vn)(*value)

            elif self.vt == PvType.U16:             
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_uint16(value)
                else: # array of U16
                    buffer = (c_uint16*self._vn)(*value)

            elif self.vt == PvType.I16:              
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_int16(value)
                else: # array of I16
                    buffer = (c_int16*self._vn)(*value)

            elif self.vt == PvType.U32:              
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_uint32(value)
                else: # array of U32
                    buffer = (c_uint32*self._vn)(*value)

            elif self.vt == PvType.DT:
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

            elif self.vt == PvType.DATE:
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

            elif self.vt == PvType.TOD:
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

            elif self.vt == PvType.TIME:
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

            elif self.vt == PvType.I32:
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_int32(value)
                else: # array of I32
                    buffer = (c_int32*self._vn)(*value)                

            elif self.vt == PvType.U64:              
                if self._vn == 1: # single value
                    assert type(value) is int                    
                    buffer = c_uint64(value)
                else: # array of U64
                    buffer = (c_uint64*self._vn)(*value)                

            elif self.vt == PvType.I64:               
                if self._vn == 1: # single value 
                    assert type(value) is int                    
                    buffer = c_int64(value)
                else: # array of I64
                    buffer = (c_int64*self._vn)(*value)                                

            elif self.vt == PvType.F32:
                if self._vn == 1: # single value
                    assert type(value) is float                    
                    buffer = c_float(value)
                else: # array of F32
                    buffer = (c_float*self._vn)(*value)                

            elif self.vt == PvType.F64:              
                if self._vn == 1: # single value
                    assert type(value) is float
                    buffer = c_double(value)
                else: # array of F64
                    buffer = (c_double*self._vn)(*value)                

            elif self.vt == PvType.STRING:
                if self._vn == 1: # single value
                    if type(value) == bytes:
                        buffer = (c_char * self.vl)(*value)
                else: # array of STRING
                    if type(value[0]) == bytes:
                        buffer = ((c_char * self.vl) * self._vn)()
                        for n, v in enumerate(value):
                            s = (c_char*self.vl)(*v)
                            buffer[n] = s

            elif self.vt == PvType.WSTRING:
                ch = int(self.vl/2) # no of characters
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
                raise RuntimeError( "data type " + str(self.vt) + " not implemented")
            
        except IndexError:
            raise IndexError(f'wrong length writing {value}\nto {repr(self._parentObject)}')            
        except BaseException as e:
            raise e
                    
        if buffer == None:
            raise ValueError(f'wrong data type {type(value)} used\nwriting {repr(self._parentObject)}')

        return buffer

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
import time
from ctypes import *
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


class VariableType():
    '''
    helper class for class Variable to parse data type information
    '''
    def __init__(self, object : PviObject ):
        '''
        object: Variable object
        '''        
        self._parentObject = object

        s = create_string_buffer(b'\000' * 64*1024) 
        object._result = PviRead( self._parentObject._linkID, POBJ_ACC_TYPE_INTERN, None, 0, s, sizeof(s) )
        if self._parentObject._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
        else:
            raise PviError(self._parentObject._result, self._parentObject)

 
        self._members = None # let's assume a basic variable type
        '''
        list of all data type (structure) members if this variable is a struct
        '''

        self._parentObject._objectDescriptor.update({'VN' : 1, 'VL' : 1 })

        self._updateObjectDescriptor(s) # udpate objects descriptor
        self.vt = PvType( self._parentObject._objectDescriptor.get('VT')) 
        '''
        PVI Variable Type : PvType
        '''

        self.vn = int(self._parentObject._objectDescriptor.get('VN'))
        '''
        number of array elements : int
        '''

        self.vl = int(self._parentObject._objectDescriptor.get('VL'))
        '''
        variable byte length : int
        '''


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
                self._parentObject._objectDescriptor.update({ex[0:2]: ex[3:]}) 
        del self._innerStructOffsets


    def _updateMemberList(self, s ):
        '''
        extract data type member's information
        s : member definition returned by POBJ_ACC_TYPE_INTERN
            e.g "{.ton.IN VT=boolean VL=1 VN=1 VO=16}"
        '''
        desc = dict() # member's object descriptor
        for m in patternStructureElementDefinition.finditer(s): # find matches
            ex = m.group()
            if ex.startswith('.'):
                desc.update({'name' : ex}) # member's name
            else:
                desc.update({ex[0:2]: ex[3:]}) # member's object descriptor

        vt = PvType(desc.get('VT'))
        vo = int(desc.get('VO'))
        vn = int(desc.get('VN'))
        vl = int(desc.get('VL'))        
        name = desc.get('name')
        parentStruct = name.rpartition('.')[0]

        if parentStruct in self._innerStructOffsets: # does member belong to an inner struct ?
            vo += self._innerStructOffsets[parentStruct]
 
        if vt == PvType.STRUCT: # is member itself an inner structure ?
            self._innerStructOffsets.update( { name :vo } )
        else:
            self._members.append(  StructMember( name, vt, vn, vo, vl ) )


    def _unpackRawData(self, data : bytes, vt : PvType, vl :int):
        '''
        unpacks data returned by PVI_ACC_DATA or PVI_EVENT_DATA to the appropiate Python data type
        data: ctype raw data        
        vt: PVI variable type
        vl: variable byte length 
        '''        
        if vt == PvType.BOOLEAN:
            return struct.unpack('<?', data )[0] 
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
            if self.vt == PvType.TIME:
                return time.gmtime(value)            
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
        arrayBuffers = ( buffer[_:_+self.vl] for _ in range(0,len(buffer), self.vl)) # split buffer into array elements
        result = list()

        for elementBuffer in arrayBuffers:
            if self.vt == PvType.STRUCT:
                structResult = OrderedDict()
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



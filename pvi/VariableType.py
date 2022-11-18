
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
from collections import namedtuple
from pvi.include.pvi_h import PvType

from ctypes import *

patternDataTypeInformation = re.compile(r"([A-Z]{2}=\w+)|(\{[^}]+\})")
patternStructureElementDefinition = re.compile(r"(\x2E[a-zA-z0-9_.]+)|([A-Z]{2}=\w+)")

StructMember = namedtuple( 'StructMember', ['sn', 'name', 'vt', 'vn', 'vo', 'vl'])
'''
helper class for structure member 
'''


class VariableType():
    '''
    helper class for class Variable to parse data type information
    '''
    def __init__(self, s : str):
        '''
        s: structure type definition returned by POBJ_ACC_TYPE_INTERN
           e.g. 'AT=rwe SC=l AL=1 VT=struct SN=MyStruct VL=84 VN=1 {.ton VT=struct SN=TON VL=20 VN=1 VO=0} { ...'
        '''
        self._members = None # let's assume a basic variable type
        '''
        list of all data type (structure) members if this variable is a struct
        '''

        self.objectDescriptor = dict({'VN' : 1, 'VL' : 1 })
        '''
        dict with extracted object description
        '''

        self._updateObjectDescriptor(s) # udpate objects descriptor
        self.vt = PvType( self.objectDescriptor.get('VT')) 
        '''
        PVI Variable Type : PvType
        '''

        self.vn = int(self.objectDescriptor.get('VN'))
        '''
        number of array elements : int
        '''

        self.vl = int(self.objectDescriptor.get('VL'))
        '''
        variable byte length : int
        '''
        if self.vt == PvType.STRUCT:
            pass


    def _updateObjectDescriptor(self, s):
        '''
        update object descriptor and find all members if this PV is a structure
        '''
        self._currentInnerStructTypeName = ""
        self._currentInnerStructName = ""
        self._currentInnerStructOffset = 0

        for m in patternDataTypeInformation.finditer(s) : # update object descriptor
            ex = m.group()
            if ex.startswith('{'): # ignore structure member definition
                if self._members == None:
                    self._members = list()
                self._updateMemberList(ex)
            else:
                self.objectDescriptor.update({ex[0:2]: ex[3:]}) 
        del(self._currentInnerStructTypeName)
        del(self._currentInnerStructName)
        del(self._currentInnerStructOffset)
        # self._members.sort( key = lambda _ : _.vo ) # sort members by offset



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

        if name.startswith(self._currentInnerStructName): # does member belong to an inner struct ?
            vo += self._currentInnerStructOffset
        else:
            self._currentInnerStructTypeName = ""

        if vt == PvType.STRUCT: # is member itself an inner structure ?
            self._currentInnerStructTypeName = desc.get('SN')
            self._currentInnerStructName = name + "." # then save it's name
            self._currentInnerStructOffset = vo
        else:
            self._members.append(  StructMember( self._currentInnerStructTypeName, name, vt, vn, vo, vl ) )


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


    def readFromBuffer(self, buffer : bytes):
        '''
        gets the value from raw buffer data
        buffer : raw buffer data from POBJ_ACC_DATA
        '''
        if self.vn == 1: # single value
            if self.vt == PvType.STRUCT:
                result = dict()
                for m in self._members:
                    buf = buffer[m.vo : m.vo+m.vl]
                    value = self._unpackRawData( buf, m.vt, m.vl )
                    result.update( { m.name : value } )
                return result
            else:
                return self._unpackRawData( buffer, self.vt, self.vl )
        else: # array: return a tuple
            buffers = ( buffer[_:_+self.vl] for _ in range(0,len(buffer), self.vl)) # split buffer
            if self.vt == PvType.STRUCT:
                pass
            else:
                return tuple( self._unpackRawData( _, self.vt, self.vl ) for _ in buffers )



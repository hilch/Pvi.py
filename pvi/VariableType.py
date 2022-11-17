
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

patternDataTypeInformation = re.compile(r"([A-Z]{2}=\w+)|(\{[^}]+\})")
patternStructureElementDefinition = re.compile(r"(\x2E[a-zA-z0-9_.]+)|([A-Z]{2}=\w+)")

StructMember = namedtuple( 'StructMember', ['sn', 'name', 'vt', 'vo'])
'''
helper class for structure member 
'''


class VariableType():
    '''
    helper class for class Variable to parse data type information
    '''
    def __init__(self, s : str):
        '''
        s: structure type definition returned by POBJ_ACC_TYPE_EXTERN
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

        self._unpackFormatString = '<' # little endian, no alignment 
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
        self._members.sort( key = lambda _ : _.vo ) # sort members by offset



    def _updateMemberList(self, s ):
        '''
        extract data type member's information
        s : member definition returned by POBJ_ACC_TYPE_EXTERN
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
            self._members.append(  StructMember( self._currentInnerStructTypeName, name, PvType(desc.get('VT')), vo ) )



    def _getUnpackFormat( self, vt : PvType, vl : int )->tuple:
        '''
        returns a tuple( <format character>, <sizeof> ) of given (basic) PVI data type as used by module 'struct'
        vt : PVI data type
        vt : PVI variable length
        '''
        if vt == PvType.BOOLEAN:
            return ('?', 1)
        elif vt == PvType.U8:
            return ('B', 1)
        elif vt == PvType.I8:
            return ('b', 1)
        elif vt == PvType.U16:
            return ('H', 2)
        elif vt == PvType.I16:
            return ('h', 2)
        elif vt == PvType.U32 or vt == PvType.DT or vt == PvType.TIME or vt == PvType.DATE or vt == PvType.TOD:
            return ('L', 4)
        elif vt == PvType.I32:
            return ('l', 4)
        elif vt == PvType.U64:
            return ('Q', 8)
        elif vt == PvType.I64:
            return ('q', 8)
        elif vt == PvType.F32:
            return ('f', 4)
        elif vt == PvType.F64:
            return ('d', 8)
        elif vt == PvType.STRING:
            return (str(vl) + 's', vl)
        elif vt == PvType.WSTRING:
            return (str(vl) + 's', vl)        
        elif vt == PvType.STRUCT:
            return (str(vl) + 'B', vl)
        else: # not handled data type
            return 'B'


    def _getCtype( self, vt : PvType, vl : int ):
        '''
        returns ctype internal data type of given (basic) PVI data type
        vt : PVI data type
        vt : PVI variable length
        '''
        if vt == PvType.BOOLEAN or vt == PvType.U8:
            return c_uint8
        elif vt == PvType.I8:
            return c_int8
        elif vt == PvType.U16:
            return c_uint16
        elif vt == PvType.I16:
            return c_int16
        elif vt == PvType.U32 or vt == PvType.DT or vt == PvType.TIME or vt == PvType.DATE or vt == PvType.TOD:
            return c_uint32
        elif vt == PvType.I32:
            return c_int32
        elif vt == PvType.U64:
            return c_uint64
        elif vt == PvType.I64:
            return c_int64
        elif vt == PvType.F32:
            return c_float
        elif vt == PvType.F64:
            return c_double
        elif vt == PvType.STRING:
            return c_char*vl
        elif vt == PvType.WSTRING:
            return c_wchar*vl
        elif vt == PvType.STRUCT:
            return c_uint8*vl
        else: # not handled data type
            return c_uint8


    def _unpackResponseData(self, data ):
        '''
        unpacks result data returned by PVI_ACC_DATA or PVI_EVENT_DATA to the appropiate Python
        data type
        > vt: PVI variable type
        > data: ctype raw data
        '''
        if self.vt == 'dt':
            return datetime.datetime.fromtimestamp(data)
        elif self.vt == 'date':
            return datetime.date.fromtimestamp(data)                    
        elif self.vt == 'time':
            return time.gmtime(data)
        elif self.vt == 'tod':
            hour = int(data / 3600000)
            data %= 3600000
            minute = int(data / 60000)
            data %= 60000
            second = int(data/1000)
            millisecond = data % 1000
            return datetime.time( hour = hour, minute = minute, second = second, microsecond=millisecond*1000 )
        elif self.vt == 'string':
            return b''.join(_ for _ in data if _ != b'\x00' )
        elif self.vt == 'wstring':
            return  ''.join(_ for _ in data if _ != '\x00' )
        elif self.vt == 'struct':
            return data
        else: # basic variable type, no need to unpack anything
            return data       


    def allocateBuffer(self, initValue = None):
        '''
        allocates the right buffer for reading bytes with POBJ_ACC_DATA
        initValue : initial Value (optional)
        '''
        if initValue == None:
            return (self._getCtype( self.vt, self.vl )*self.vn)()       
        else:
            return (self._getCtype( self.vt, self.vl )*self.vn)(initValue) 


    def readFromBuffer(self, buffer):
        '''
        gets the value from raw buffer data
        buffer : raw buffer data from POBJ_ACC_DATA
        '''
        if self.vn == 1: # single value
            return self._unpackResponseData(buffer[0])
        else: # array: send a tuple
            return tuple([ self._unpackResponseData(_) for _ in buffer])        


    def castRawData(self, data ):
        '''
        returns data types member values

        > data: byte data
        '''
        rawData = bytes(_ for _ in data)[0:self._sizeof] 
        dataValues = struct.unpack(self._unpackFormatString, rawData)                     
#        dataType = namedtuple( self.objectDescriptor.get('SN'), [ _.get('name') for _ in self._members] )
#        return dataType(*dataValues)                


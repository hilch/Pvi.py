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

from enum import Enum, unique
import os
import struct


@unique
class BrFileType(Enum):
    UNKNOWN = 0
    CYCLIC_RESOURCE = 0x11
    SYSTEM_OBJECT = 0x12
    IDLE_TIME_OBJECT = 0x13
    OBJECT_OF_A_TIMER_RESOURCE = 0x14
    INTERRUPT_OBJECT = 0x15
    EXCEPTION_OBJECT = 0x16
    AVT_LIBRARY = 0x21
    MATHTRAP_LIBRARY = 0x25
    TRAP_LIBRARY = 0x26
    ADVANCED_TRAP_LIBRARY = 0x28
    OPTIMIZED_IO_MODULE = 0x31
    IO_MAPPING = 0x32
    DATA_OBJECT = 0x41
    FIRMWARE_MODULE = 0x43
    NC_DRIVER = 0x45
    MOTION_DATA_OBJECT = 0x46
    PROFILER_DATA_OBJECT = 0x4c
    LOGGER_MODULE = 0x53
    TARGET_SYSTEM_CONFIGURATION = 0x81
    NETWORK_CONFIGURATION_MODULE = 0x82
    RUNTIME_CONFIGURATION = 0x84
    TEXT_CONFIG = 0x88
    TC_DATA = 0xd1
    UNIT_DEFINITION_MODULE = 0xd2
    
    @classmethod
    def _missing_(cls, value):
        return BrFileType.UNKNOWN

class BrFile():
    '''
    base class for all *.br files
    '''
    def __init__(self, filename : str ):
        self.__name = os.path.basename(filename)
        with open(filename, 'rb') as f:
            self._content = f.read()
        magicNumber, self._fileType, self._subType, self._fileSize  = struct.unpack_from('>HBB10xI', self._content, 0) # big-endian
        if magicNumber != 0x2b97:
            raise TypeError('content is not a B&R module !')


    @property
    def fileType(self):
        return BrFileType(self._fileType)


    def __repr__(self) -> str:
        return f'File ({str(self._fileType)})'




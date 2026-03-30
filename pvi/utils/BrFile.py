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

import os
import struct

from pvi_objects.Module import ModuleType as BrFileType

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




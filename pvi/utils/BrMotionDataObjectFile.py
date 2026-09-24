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


from pvi.utils.BrFile import *

class BrMotionDataObjectFile(BrFile):
    '''
    class for a *.br file containing data object
    '''
    def __init__(self, filename: str):
        super().__init__(filename)
        if self._fileType != ModuleType.MOTION_DATA_OBJECT:
            raise TypeError(f'content is not a B&R data module (Type is {self._fileType})')
        self._data_start_address = struct.unpack_from('>L', self._content, 0x24)[0]
        self._data_end_address = struct.unpack_from('>L', self._content, 0x2c)[0]

    @property
    def version(self) -> int:
        return struct.unpack_from('<H', self._content, 0x82)[0]

    @property
    def data(self) -> bytes:
        return self._content[self._data_start_address:self._data_end_address]




    @property
    def xmlHeader(self):
        header = bytearray()
        for x in self._content[0x30:]:
            if x != 0:
                header.append(x)
            else:
                break
        return header.decode('ascii')        
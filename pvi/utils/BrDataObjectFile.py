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


from .BrFile import *

class BrDataObjectFile(BrFile):
    '''
    class for a *.br file containing logger data
    '''
    def __init__(self, filename: str):
        super().__init__(filename)
        if self._fileType != BrFileType.DATA_OBJECT:
            raise TypeError(f'content is not a B&R data module (Type is {self._fileType})')

    @property
    def version(self) -> int:
        v = struct.unpack_from('<B', self._content, 0x82) + 256 * struct.unpack_from('<B', self._content, 0x82)
        return v

    @property
    def xmlHeader(self):
        header = bytearray()
        for x in self._content[0x30:]:
            if x != 0:
                header.append(x)
            else:
                break
        return header.decode('ascii')        
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

from datetime import datetime, timedelta
from collections import namedtuple
import struct
from .BrFile import *

BrLoggerFileEntry = namedtuple('LoggerEntry', [ 'RecordID', 'Time', 'Nanosec', 'ObjectID' , 'Severity', 'Code', 
                         'EventID', 'OriginID', 'AsciiData', 'BinaryData'])

class BrLoggerFile(BrFile):
    '''
    class for a *.br file containing logger data
    '''
    def __init__(self, filename: str):
        super().__init__(filename)
        if self._fileType != BrFileType.LOGGER_MODULE:
            raise TypeError(f'content is not a B&R logger module (Type is {self._fileType})')
        self._BASE_OFFSET = 0xc0        


    ## offset 0x80: b'83 B9 57 2A 9C F3 60 00 83 B9 57 2A 9C F3 60 00' ??

    @property
    def logDataLength(self) -> int:
        '''
        logger length (bytes)
        '''
        return struct.unpack_from('<I', self._content, 0x90)[0] # uint32


    @property
    def version(self) -> int:
        '''
        log format version
        '''
        return struct.unpack_from('<H', self._content, 0x94)[0] # uint16


    @property
    def actIndex(self) -> int:
        '''
        actual record id
        '''
        return struct.unpack_from('<I', self._content, 0x9c)[0] # uint32


    @property
    def actOffset(self) -> int:
        '''
        actual offset
        '''
        return struct.unpack_from('<I', self._content, 0xa0)[0] # uint32


    @property
    def writeOffset(self) -> int:
        '''
        write offset
        '''
        return struct.unpack_from('<I', self._content, 0xa4)[0] # uint32


    @property
    def refIndex(self) -> int:
        '''
        reference record id
        '''
        return struct.unpack_from('<I', self._content, 0xa8)[0] # uint32


    @property
    def refOffset(self) -> int:
        '''
        reference offset
        '''
        return struct.unpack_from('<I', self._content, 0xac)[0] # uint32


    @property
    def invalidLength(self) -> int:
        '''
        invalid length
        '''
        return struct.unpack_from('<I', self._content, 0xb0)[0] # uint32


    @property
    def numberOfEntries(self) -> int:
        '''
        number of logger entries
        '''
        return self.actIndex - self.refIndex


    def _readEntry(self) -> bytes:
        '''
        read and decode an entry
        '''
        readOffset = self._entryOffset
        entry = bytearray()
        for _ in range(12): # read header
            entry.append( self._content[readOffset] )
            readOffset += 1
        recordId, lengthOfPrevious, lengthOfEntry = struct.unpack_from('<III', entry, 0) # decode header fields
        for _ in range(12,lengthOfEntry): # read complete entry
            entry.append( self._content[readOffset] )
            readOffset += 1
        info1, info2, time, nanosecond, severity, code, objectId, eventId, originId \
             = struct.unpack_from('<HHIIII36sII', entry, 0x14)
        time = datetime.fromtimestamp( time )
        microsecond, nanosecond = divmod(nanosecond,1000)
        time += timedelta( microseconds= microsecond )
        if severity < 4:        
            severity = ('Success', 'Info', 'Warning', 'Error')[severity]
        else:
            severity = hex(severity)
        objectId = objectId[:objectId.find(b'\x00')].decode(encoding = 'utf-8', errors = 'ignore') 
        if code == 0 and eventId != 0: # new logger format ?
            code = eventId & 0xffff        

        binaryData =  bytes(entry[0x54:-8])
        asciiData = ''
        if info1 == 8 and info2 == 1: # binary data contains ASCII string -> remove trailing bytes
            asciiData = binaryData[:binaryData.find(b'\x00')].decode(encoding = 'utf-8', errors = 'ignore')
        elif info1 == 0 and info2 == 3: # 'old' format
            asciiData = binaryData[:binaryData.find(b'\x00')].decode(encoding = 'utf-8', errors = 'ignore')
            binaryData = binaryData[binaryData.find(b'\x00')+1:]

        # entry[-8:] = ??
        #print( f'{recordId}: {hex(self._entryOffset)}')

        if self._entryOffset == self._BASE_OFFSET:
            self._entryOffset = self._BASE_OFFSET - lengthOfPrevious + self.logDataLength - self.invalidLength
        elif (self._entryOffset - lengthOfPrevious) < self._BASE_OFFSET:
              self._entryOffset = self._entryOffset - lengthOfPrevious + self.logDataLength - self.invalidLength
        else:  
            self._entryOffset -= lengthOfPrevious # point to the previous entry

        previousId = struct.unpack_from('<I', self._content[self._entryOffset:self._entryOffset+4], 0)[0] # decode header fields
        if (previousId+1) == recordId: # check if previous Id is valid
            return BrLoggerFileEntry(
                    RecordID = int(recordId),
                    Time = time,
                    Nanosec= nanosecond,
                    ObjectID = objectId,
                    Severity = severity,
                    EventID= eventId,
                    OriginID = originId,
                    Code= code,
                    AsciiData = asciiData,
                    BinaryData = binaryData
                ) 
        else:
            return None              

    
    @property
    def entries(self) -> list:
        rows = 0
        self._entryOffset = self.actOffset + self._BASE_OFFSET
        self._lastOffset = self._entryOffset
        l = list()
        while True:
            entry = self._readEntry() 
            if entry:    
                l.append( entry )
                rows += 1
            else:
                break
        return l


    @property
    def xmlHeader(self):
        header = bytearray()
        for x in self._content[0x39:]:
            if x != 0:
                header.append(x)
            else:
                break
        return header.decode('ascii')
            

    def __repr__(self) -> str:
        return f'BrLoggerFile, Entries: {self.numberOfEntries}, Length {self.logDataLength}, RecordId: {self.refIndex} to {self.actIndex}'            
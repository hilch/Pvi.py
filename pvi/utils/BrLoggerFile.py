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
        if self.fileType != BrFileType.LOGGER_MODULE:
            raise TypeError(f'content is not a B&R logger module (Type is {self.fileType})')
        self.__entries = None
        self.__BASE_OFFSET = 0xc0
        self.__logDataLength = struct.unpack_from('<I', self._content, 0x90)[0] # uint32
        self.__version = struct.unpack_from('<H', self._content, 0x94)[0] # uint16
        self.__actIndex = struct.unpack_from('<I', self._content, 0x9c)[0] # uint32
        self.__actOffset = struct.unpack_from('<I', self._content, 0xa0)[0] # uint32
        self.__writeOffset = struct.unpack_from('<I', self._content, 0xa4)[0] # uint32
        self.__refIndex = struct.unpack_from('<I', self._content, 0xa8)[0] # uint32
        self.__refOffset = struct.unpack_from('<I', self._content, 0xac)[0] # uint32
        self.__invalidLength = struct.unpack_from('<I', self._content, 0xb0)[0] # uint32
        self.__offsetUtc = struct.unpack_from('<h', self._content, 0xb4)[0] # int16
        self.__daylightSaving = struct.unpack_from('<H', self._content, 0xb6)[0] # uint16

    ## offset 0x80: b'83 B9 57 2A 9C F3 60 00 83 B9 57 2A 9C F3 60 00' ??

    @property
    def logDataLength(self) -> int:
        '''
        configured logger length (bytes)
        '''
        return self.__logDataLength


    @property
    def version(self) -> int:
        '''
        log format version
        '''
        return self.__version


    @property
    def offsetUtc(self) -> int:
        '''
        offset to UTC in minutes
        '''
        return self.__offsetUtc


    @property
    def dst(self) -> bool:
        '''
        daylight saving time active ?
        '''
        return bool(self.__daylightSaving)


    @property
    def numberOfEntries(self) -> int:
        '''
        number of logger entries
        '''
        return len(self.entries)


    @property
    def lowestRecordID(self) -> int:
       '''
       lowest ID contained in this logger
       '''
       return self.entries[-1].RecordID

    @property
    def highestRecordID(self) -> int:
       '''
       highest ID contained in this logger
       '''       
       return self.entries[0].RecordID


    def __readEntry(self) -> bytes:
        '''
        (internal) read and decode an entry
        '''              
        recordId, lengthOfPrevious, lengthOfEntry, lengthOfBinaryData = struct.unpack_from('<IIII', self._content[self.__entryOffset:self.__entryOffset+0x10], 0) # decode header fields
        if recordId != (self.__lastRecordId - 1):
            return None # end of logger
        self.__lastRecordId = recordId # save for next call
        entry = bytes(self._content[self.__entryOffset:self.__entryOffset+lengthOfEntry])
        # entry[0x10:0x14] ?
        info1, info2, time, nanosecond, severity, code, objectId, eventId, originId, binaryData = struct.unpack_from(f'<HHIIII36sii{lengthOfBinaryData}s', entry, 0x14)
        time = datetime.utcfromtimestamp( time )
        microsecond, nanosecond = divmod(nanosecond,1000)
        time += timedelta( microseconds = microsecond, minutes = self.__offsetUtc)
        if severity < 4:        
            severity = ('Success', 'Info', 'Warning', 'Error')[severity]
        else:
            severity = hex(severity)
        objectId = objectId[:objectId.find(b'\x00')].decode(encoding = 'utf-8', errors = 'ignore') 
        if code == 0 and eventId != 0: # new logger format ?
            code = eventId & 0xffff         
        asciiData = ''
        if info1 == 8 and info2 == 1: # binary data contains ASCII string -> remove trailing bytes
            asciiData = binaryData[:binaryData.find(b'\x00')].decode(encoding = 'utf-8', errors = 'ignore')
        elif info1 == 0 and info2 == 3: # 'old' format
            asciiData = binaryData[:binaryData.find(b'\x00')].decode(encoding = 'utf-8', errors = 'ignore')
            binaryData = binaryData[binaryData.find(b'\x00')+1:]

        # entry[-8:] = ??

        if self.__entryOffset == self.__BASE_OFFSET:
            self.__entryOffset = self.__BASE_OFFSET - lengthOfPrevious + self.logDataLength - self.__invalidLength
        elif (self.__entryOffset - lengthOfPrevious) < self.__BASE_OFFSET:
              self.__entryOffset = self.__entryOffset - lengthOfPrevious + self.logDataLength - self.__invalidLength
        else:  
            self.__entryOffset -= lengthOfPrevious # point to the previous entry

        return BrLoggerFileEntry(
                    RecordID = recordId,
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
        


    
    @property
    def entries(self) -> list:
        if self.__entries == None:
            self.__entries = list()
            self.__entryOffset = self.__actOffset + self.__BASE_OFFSET
            self.__lastRecordId = self.__actIndex + 1    
            while entry := self.__readEntry():  
                self.__entries.append( entry )
        return self.__entries


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
        return f'BrLoggerFile V{self.version}, Entries: {self.numberOfEntries}, Length {self.logDataLength}, RecordId: {self.lowestRecordID} to {self.highestRecordID}'            
    
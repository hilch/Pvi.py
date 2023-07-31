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

BrProfilerEvent = namedtuple('ProfilerEvent', [ 'Microseconds', 'ObjectIdent', 'Event'])

class BrProfilerDataFile(BrFile):
	'''
	class for a *.br file containing profiler data
	'''
	SIZEOF_RECORD_ENTRY = 16
	OFFSET_TASKCLASS_ENTRY = 0x1cc
	SIZEOF_TASKCLASS_ENTRY = 70
	OFFSET_OBJECT_ENTRY = 0x442
	SIZEOF_OBJECT_ENTRY = 62

	def __init__(self, filename: str):
		super().__init__(filename)
		if self.fileType != BrFileType.PROFILER_DATA_OBJECT:
			raise TypeError(f'content is not a B&R profiler data module (Type is {self.fileType})')
		self.__offsetRecords = struct.unpack_from('<H', self._content, 0x2d)[0] + struct.unpack_from('<H', self._content, 0x2f)[0] # 2 x uint16
							
		self.__maxSize = struct.unpack_from('<I', self._content, 0xa4)[0] # uint32 maximal size of profiler data object
		self.__arversion = str(self._content[0x11c:0x11e], encoding = 'ascii') + '.' \
					+ str(self._content[0x11e:0x120], encoding = 'ascii')
		self.__bridcode = hex(struct.unpack_from('<I', self._content, 0x120)[0]) # uint32
		self.__firstRecordAtOffset = struct.unpack_from('<I', self._content, 0x124)[0] # uint32
		#self.__lastRecordAtOffset = struct.unpack_from('<I', self._content, 0x128)[0] # uint32
		self.__tickFrequencyMhz = struct.unpack_from('<I', self._content, 0x12c)[0] # uint32
		self.__profiledTargetType = str(self._content[0x16a:0x179], encoding='ascii').rstrip('\x00')
		self.__countEntries = int(self.__maxSize / __class__.SIZEOF_RECORD_ENTRY)
		self.__systemTick = 1 / (self.__tickFrequencyMhz)


	@property
	def info(self) -> dict:
		return({
			"profiledTarget" : self.__profiledTargetType,
			"targetIdCode"   : self.__bridcode,
			"tickFrequencyMhz"  : self.__tickFrequencyMhz,
			"entries" : self.__countEntries,
			"AR" : self.__arversion
		})


	@property
	def taskClasses(self) -> list:
		offset = __class__.OFFSET_TASKCLASS_ENTRY
		result = list()
		for n in range(9):
			ident, cycleTime, toleranceTime, unknown, name = struct.unpack_from('<I20xIII34s', self._content, offset)
			name = str(name, 'ascii').rstrip('\x00')
			result.append( { "ident" : ident, "name" : name, "cylceTime" : cycleTime, "toleranceTime" : toleranceTime} )
			offset += __class__.SIZEOF_TASKCLASS_ENTRY
		return result


	@property
	def objects(self) -> list:
		offset = __class__.OFFSET_OBJECT_ENTRY
		result = list()
		while True:
			ident, taskclass, name = struct.unpack_from('<I20xI34s', self._content, offset)
			if taskclass == 0:
				return result
			name = str(name, 'ascii').rstrip('\x00')
			result.append({ "ident": hex(ident), "name": name, "taskclass" : taskclass })
			offset += __class__.SIZEOF_OBJECT_ENTRY
		return result	
	

	@property
	def entries(self) -> list:
		offset = self.__offsetRecords + self.__firstRecordAtOffset * __class__.SIZEOF_RECORD_ENTRY
		maxOffset = self.__offsetRecords + (self.__countEntries-1) * __class__.SIZEOF_RECORD_ENTRY
		result = list()
		startticks = None
		for n in range( self.__countEntries):
			ticks, event, objectIdent = struct.unpack_from('<QII', self._content, offset)
			if not(startticks):
				startticks = ticks
			micros = (ticks-startticks) * self.__systemTick
			result.append( BrProfilerEvent( micros, objectIdent, event) )
			if offset >= maxOffset:
				offset = self.__offsetRecords
			else:
				offset += __class__.SIZEOF_RECORD_ENTRY
		return result


	def __repr__(self) -> str:
		return f'BrProfilerDataFile'            
    
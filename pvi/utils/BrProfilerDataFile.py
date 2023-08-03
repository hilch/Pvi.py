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

from datetime import datetime
from collections import namedtuple
import struct
from enum import IntEnum
from .BrFile import *

BrProfilerEvent = namedtuple('ProfilerEvent', [ 'microseconds', 'objectIdent', 'objectName', 'event', 'eventDescription'])

class BrProfilerObjectType(IntEnum):
	UNKNOWN = 0
	TASK_CLASS = 1
	CYCLIC_TASK = 2
	SYSTEM_TASK = 3
	INTERRUPT_VECTOR = 4


BrCyclicObjectEvents = {
	0x02000000 : 'cyclic task started',
	0x02000001 : 'cyclic task finished'
}

BrTaskClassObjectEvents = {
	0x1e000000 : 'taskclass started',
	0x1e000001 : 'taskclass stopped',
	0x1e000001 : 'input scheduler finished',
	0x1e000002 : 'end of cyclic programs',
	0x1e000003 : 'output scheduler started',
	0x1e000004 : 'output scheduler finished'
}


BrSystemObjectEvents = {
	0x00191902 : '#1 is now running',
	0x00252502 : '#2 is now running',
	0x00373704 : '#3 is now running',
	0x00414102 : '#8 is now running',	
	0x00020200 : 'IO Scheduler is now running',
	0x00fcfc02 : 'TcIdleFiller is now running',
	0x01000000 : 'system task started',
	0x01000001 : 'system task stopped',
	0x00212102 : 'system task is now running'
}

BrInterruptHandlerEvents = {
	0x01000000 : 'interrupt handler started',
	0x01000001 : 'interrupt handler finished'	
}

class BrProfilerDataFile(BrFile):
	'''
	class for a *.br file containing profiler data
	'''
	SIZEOF_RECORD_ENTRY = 16
	OFFSET_TASKCLASS_ENTRY = 0x1cc
	SIZEOF_TASKCLASS_ENTRY = 70
	OFFSET_OBJECT_ENTRY = 0x442
	SIZEOF_OBJECT_ENTRY = 62
	SIZEOF_SYSTEMOBJECT_ENTRY = 70

	def __init__(self, filename: str):
		super().__init__(filename)
		if self.fileType != BrFileType.PROFILER_DATA_OBJECT:
			raise TypeError(f'content is not a B&R profiler data module (Type is {self.fileType})')
		self.__offsetRecords = struct.unpack_from('<H', self._content, 0x2d)[0] + struct.unpack_from('<H', self._content, 0x2f)[0] # 2 x uint16
							
		self.__maxSize = struct.unpack_from('<I', self._content, 0xa4)[0] # uint32 maximal size of profiler data object
		self.__additionalDatasizePerEntry = struct.unpack_from('<I', self._content, 0xa8)[0] # uint32
		self.__bufferForCreatedTask = struct.unpack_from('<I', self._content, 0xac)[0] # uint32		
		self.__bufferForCreatedUserTask = struct.unpack_from('<I', self._content, 0xbc)[0] # uint32				
		self.__arversion = str(self._content[0x11c:0x11e], encoding = 'ascii') + '.' \
					+ str(self._content[0x11e:0x120], encoding = 'ascii')
		self.__bridcode = hex(struct.unpack_from('<I', self._content, 0x120)[0]) # uint32
		self.__firstRecordAtOffset = struct.unpack_from('<I', self._content, 0x124)[0] # uint32
		#self.__lastRecordAtOffset = struct.unpack_from('<I', self._content, 0x128)[0] # uint32
		self.__tickFrequencyMhz = struct.unpack_from('<I', self._content, 0x12c)[0] # uint32
		year, month, day, _ , hour, minute, second  = struct.unpack_from('<HBBBBBB', self._content, 0x130)
		self.__profilingTimestamp = datetime( year, month, day, hour, minute, second)
		self.__noOfCyclicTasks = struct.unpack_from('<I', self._content, 0x156)[0] # uint32
		self.__noOfSystemTasks = struct.unpack_from('<I', self._content, 0x15e)[0] # uint32		
		self.__profiledTargetType = str(self._content[0x16a:0x179], encoding='ascii').rstrip('\x00')
		self.__countEntries = int(self.__maxSize / (__class__.SIZEOF_RECORD_ENTRY + self.__additionalDatasizePerEntry))
		self.__systemTick = 1 / (self.__tickFrequencyMhz)
		self.__objects = None
		self.__entries = None


	@property
	def info(self) -> dict:
		return({
			"startDateOfProfiling" : self.__profilingTimestamp,
			"profiledTarget" : self.__profiledTargetType,
			"targetIdCode"   : self.__bridcode,
			"tickFrequencyMhz"  : self.__tickFrequencyMhz,
			"maxSize" : self.__maxSize,
			"additionalDataSizePerEntry" : self.__additionalDatasizePerEntry,
			"bufferForCreatedTask" : self.__bufferForCreatedTask,
			"bufferForCreatedUserTask" : self.__bufferForCreatedUserTask,
			"entries" : self.__countEntries,
			"AR" : self.__arversion
		})


	@property
	def objects(self) -> dict:
		if not( self.__objects):
			self.__objects = dict()
			# add task classes
			offset = __class__.OFFSET_TASKCLASS_ENTRY
			self.__taskClasses = list()
			for n in range(9):
				ident, cycleTime, toleranceTime, prio, name = struct.unpack_from('<I20xIII34s', self._content, offset)
				name = str(name, 'ascii').rstrip('\x00')
				objectPriority = 255- prio
				self.__objects.update( { ident : { 'type' : BrProfilerObjectType.TASK_CLASS, 'ident' : ident, 'name' : name, 'cycleTime' : cycleTime, 
				      											'toleranceTime' : toleranceTime, 'objectPriority' : objectPriority } })
				offset += __class__.SIZEOF_TASKCLASS_ENTRY

			# add cyclic tasks
			offset = __class__.OFFSET_OBJECT_ENTRY			
			for n in range(self.__noOfCyclicTasks):
				ident, taskclass, name = struct.unpack_from('<I20xI34s', self._content, offset)
				if ident:
					name = str(name, 'ascii').rstrip('\x00')
					self.__objects.update( { ident : { 'type' : BrProfilerObjectType.CYCLIC_TASK , 'name' : name, 'taskClass' : taskclass } } )
				offset += __class__.SIZEOF_OBJECT_ENTRY
			#offset += self.___bufferForCreatedUserTask * __class__.SIZEOF_OBJECT_ENTRY

			# add system tasks
			for n in range(self.__noOfSystemTasks):
				ident, prio, stackSize, freeStack, name = struct.unpack_from('<I20xIII34s', self._content, offset)
				if ident:
					name = str(name, 'ascii').rstrip('\x00')
					objectPriority = 255 - prio
					self.__objects.update( { ident : { 'type' : BrProfilerObjectType.SYSTEM_TASK, 'name' : name, 
				       				'objectPriority' : objectPriority, 'stackSize' : stackSize, 'freeStack' : freeStack} } )
				offset += __class__.SIZEOF_SYSTEMOBJECT_ENTRY

			#add interrupt vectors
			n = 0
			while offset < self.__offsetRecords - 32:
				n += 1
				if n == 224:
					n = n
				ident, interruptNr, length = struct.unpack_from('<I20xII', self._content, offset)
				offset += 32
				if ident != 0:
					name = bytearray()
					if length > 0:
						name = self._content[offset:offset+length]
						offset += length
					name = f'Interrupt {interruptNr} ({str( name, "ascii")})'
					self.__objects.update( { ident : { 'type' : BrProfilerObjectType.INTERRUPT_VECTOR, 'name' : name, 'interrupt' : interruptNr } } )
				else:
					break

		return self.__objects	
	
	

	@property
	def entries(self) -> list:
		if not(self.__entries):
			offset = self.__offsetRecords + self.__firstRecordAtOffset * __class__.SIZEOF_RECORD_ENTRY
			maxOffset = self.__offsetRecords + (self.__countEntries-1) * __class__.SIZEOF_RECORD_ENTRY
			self.__entries = list()
			startticks = None
			for n in range( self.__countEntries):
				ticks, event, objectIdent = struct.unpack_from('<QII', self._content, offset)
				if not(startticks):
					startticks = ticks
				micros = (ticks-startticks) * self.__systemTick
				object = self.objects.get( objectIdent, None )
				objectName = ''
				eventDescription = ''
				if n == 13:
					n = n
				if object:
					objectName = object['name']
					if object['type'] == BrProfilerObjectType.CYCLIC_TASK:
						eventDescription = BrCyclicObjectEvents.get(event, '')
					elif object['type'] == BrProfilerObjectType.TASK_CLASS:
						eventDescription = BrTaskClassObjectEvents.get(event, '')
					elif object['type'] == BrProfilerObjectType.SYSTEM_TASK:
						eventDescription = BrSystemObjectEvents.get(event, '')
					elif object['type']	== BrProfilerObjectType.INTERRUPT_VECTOR:
						eventDescription = BrInterruptHandlerEvents.get(event, '')
				self.__entries.append( BrProfilerEvent( micros, objectIdent, objectName, event, eventDescription) )
				if offset >= maxOffset:
					offset = self.__offsetRecords
				else:
					offset += __class__.SIZEOF_RECORD_ENTRY
		return self.__entries


	def __repr__(self) -> str:
		return f'BrProfilerDataFile'            
    
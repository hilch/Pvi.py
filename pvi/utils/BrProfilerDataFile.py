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

BrProfilerEvent = namedtuple('BrProfilerEvent', [ 'microseconds', 'objectIdent', 'objectName', 'event', 'eventDescription'])

class BrProfilerObjectType(IntEnum):
	UNKNOWN = 0
	LIBRARY_FUNCTION = 1
	TASK_CLASS = 2
	CYCLIC_TASK = 3
	SYSTEM_TASK = 4
	INTERRUPT_VECTOR = 5

BrLibraryFunctionEvents = {
	0x03000000 : 'library function started',
	0x03000001 : 'library function finished'
}


BrCyclicTaskEvents = {
	0x02000000 : 'cyclic task started',
	0x02000001 : 'cyclic task finished'
}

BrTaskClassEvents = {
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
	0x00212102 : 'system task is now running',
	0x11000001 : 'system task deleted'
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
	SIZEOF_LIBRARY_FUNCTION_ENTRY = 28
	SIZEOF_TASKCLASS_ENTRY = 70
	OFFSET_OBJECT_ENTRY = 0x442
	SIZEOF_OBJECT_ENTRY = 62
	SIZEOF_SYSTEMOBJECT_ENTRY = 70
	MIN_SIZE_INTERRUPT_VECTOR = 32

	def __init__(self, filename: str):
		super().__init__(filename)
		if self.fileType != BrFileType.PROFILER_DATA_OBJECT:
			raise TypeError(f'content is not a B&R profiler data module (Type is {self.fileType})')
		self.__offsetRecords = struct.unpack_from('<H', self._content, 0x2d)[0] + struct.unpack_from('<H', self._content, 0x2f)[0] # 2 x uint16
							
		self.__maxSize = struct.unpack_from('<I', self._content, 0xa4)[0] # uint32 maximal size of profiler data object
		self.__additionalDatasizePerEntry = struct.unpack_from('<I', self._content, 0xa8)[0] # uint32
		self.__bufferForCreatedTask = struct.unpack_from('<I', self._content, 0xac)[0] # uint32		
		self.__bufferForCreatedUserTask = struct.unpack_from('<I', self._content, 0xbc)[0] # uint32
		head = 0x116
		# optional library functions
		libraryFunctionsList = bytearray()
		while struct.unpack_from('<H', self._content, head)[0] != 0:
			c = self._content[head]
			libraryFunctionsList.append( self._content[head])
			head +=1
		if len(libraryFunctionsList) > 0:
			head +=1
			libraryFunctionsList = str(libraryFunctionsList, 'ascii').split('\0')
		self.__sgType = 'SG' + str(struct.unpack_from('<B', self._content, head+2)[0])
		self.__arversion = str(self._content[head+6:head+8], encoding = 'ascii') + '.' \
					+ str(self._content[head+8:head+10], encoding = 'ascii')
		self.__bridcode = hex(struct.unpack_from('<I', self._content, head+10)[0]) # uint32
		self.__firstRecordAtOffset = struct.unpack_from('<I', self._content, head+14)[0] # uint32
		self.__lastRecordAtOffset = struct.unpack_from('<I', self._content, head+18)[0] # uint32
		self.__tickFrequencyMhz = struct.unpack_from('<I', self._content, head+22)[0] # uint32
		year, month, day, _ , hour, minute, second  = struct.unpack_from('<HBBBBBB', self._content, head+26)
		self.__profilingTimestamp = datetime( year, month, day, hour, minute, second)
		self.__noOfCyclicTasks = struct.unpack_from('<I', self._content, head+64)[0] # uint32
		self.__noOfSystemTasks = struct.unpack_from('<I', self._content, head+72)[0] # uint32		
		self.__profiledTargetType = str(self._content[head+84:head+99], encoding='ascii').rstrip('\x00')
		self.__maxPossibleEntries = int(self.__maxSize / (__class__.SIZEOF_RECORD_ENTRY + self.__additionalDatasizePerEntry))
		self.__systemTick = 1000 / (self.__tickFrequencyMhz)
		self.__offsetObjectEntry = head + 0xb6

		# now get the profiled objects:
		self.__objectTypes = dict()
		# 1. optional library functions
		self.__libraryFunctions = dict()
		offset = self.__offsetObjectEntry
		# read the dummy entries for library functions
		for n in range( len(libraryFunctionsList) ):
			ident, nameIndex = struct.unpack_from('<I20xI', self._content, offset)
			fname = libraryFunctionsList[nameIndex]
			self.__libraryFunctions.update( { ident : { 'name' : fname } } )
			self.__objectTypes.update( { -ident : BrProfilerObjectType.LIBRARY_FUNCTION } ) # use negative ident since lib.func. use their own counting
			offset += __class__.SIZEOF_LIBRARY_FUNCTION_ENTRY


		self.__objectTypes = dict()
		# 2. task classes
		self.__taskClasses = dict()
		for n in range(9):
			ident, cycleTime, toleranceTime, prio, name = struct.unpack_from('<I20xIII34s', self._content, offset)
			name = str(name, 'ascii').rstrip('\x00')
			objectPriority = 255- prio
			self.__taskClasses.update( { ident : { 'name' : name, 'cycleTime' : cycleTime, 'toleranceTime' : toleranceTime, 'objectPriority' : objectPriority } })
			self.__objectTypes.update( { ident : BrProfilerObjectType.TASK_CLASS } )
			offset += __class__.SIZEOF_TASKCLASS_ENTRY			

		# 3. cyclic tasks	
		self.__cyclicTasks = dict()
		for n in range(self.__noOfCyclicTasks):
			ident, taskclass, name = struct.unpack_from('<I20xI34s', self._content, offset)
			if ident:
				name = str(name, 'ascii').rstrip('\x00')
				self.__cyclicTasks.update( { ident : { 'name' : name, 'taskClass' : taskclass } } )
				self.__objectTypes.update( { ident : BrProfilerObjectType.CYCLIC_TASK } )
			offset += __class__.SIZEOF_OBJECT_ENTRY

		# 4. system tasks
		self.__systemTasks = dict()
		for n in range(self.__noOfSystemTasks):
			ident, prio, stackSize, freeStack, name = struct.unpack_from('<I20xIII34s', self._content, offset)
			if ident:
				name = str(name, 'ascii').rstrip('\x00')
				objectPriority = 255 - prio
				self.__systemTasks.update( { ident : { 'name' : name, 'objectPriority' : objectPriority, 'stackSize' : stackSize, 'freeStack' : freeStack} } )
				self.__objectTypes.update( { ident : BrProfilerObjectType.SYSTEM_TASK } )				
			offset += __class__.SIZEOF_SYSTEMOBJECT_ENTRY

		# 3. interrupt handler
		self.__interruptHandler = dict()
		while offset < self.__offsetRecords - __class__.MIN_SIZE_INTERRUPT_VECTOR:
			ident, interruptNr, length = struct.unpack_from('<I20xII', self._content, offset)
			offset += __class__.MIN_SIZE_INTERRUPT_VECTOR
			if ident != 0:
				name = bytearray()
				if length > 0:
					name = self._content[offset:offset+length]
					offset += length
				name = f'Interrupt {interruptNr} ({str( name, "ascii")})'
				self.__interruptHandler.update( { ident : { 'name' : name, 'interrupt' : interruptNr } } )
				self.__objectTypes.update( { ident : BrProfilerObjectType.INTERRUPT_VECTOR } )				
			else:
				break

		self.__entries = None


	@property
	def info(self) -> dict:
		return({
			"startDateOfProfiling" : self.__profilingTimestamp,
			"sg" : self.__sgType,
			"profiledTarget" : self.__profiledTargetType,
			"targetIdCode"   : self.__bridcode,
			"tickFrequencyMhz"  : self.__tickFrequencyMhz,
			"maxSize" : self.__maxSize,
			"additionalDataSizePerEntry" : self.__additionalDatasizePerEntry,
			"bufferForCreatedTask" : self.__bufferForCreatedTask,
			"bufferForCreatedUserTask" : self.__bufferForCreatedUserTask,
			"entries" : self.__maxPossibleEntries,
			"AR" : self.__arversion
		})


	@property
	def libraryFunctions(self) -> dict:
		return self.__libraryFunctions	
	

	@property
	def taskClasses(self) -> dict:
		return self.__taskClasses

	@property
	def cyclicTasks(self) -> dict:
		return self.__cyclicTasks

	@property
	def systemTasks(self) -> dict:
		return self.__systemTasks

	@property
	def interruptHandler(self) -> dict:
		return self.__interruptHandler


	@property
	def entries(self) -> list:
		if not(self.__entries):
			offset = self.__offsetRecords + self.__firstRecordAtOffset * __class__.SIZEOF_RECORD_ENTRY
			maxOffset = self.__offsetRecords + (self.__maxPossibleEntries-1) * __class__.SIZEOF_RECORD_ENTRY
			noOfValidEntries = self.__maxPossibleEntries
			if self.__lastRecordAtOffset > self.__firstRecordAtOffset:
				noOfValidEntries = self.__lastRecordAtOffset - self.__firstRecordAtOffset + 1
			else:
				noOfValidEntries = self.__lastRecordAtOffset + self.__maxPossibleEntries - self.__firstRecordAtOffset + 1
			self.__entries = list()
			startticks = None
			for n in range( noOfValidEntries):
				ticks, event, objectIdent = struct.unpack_from('<QII', self._content, offset)
				if not(startticks):
					startticks = ticks
				micros = (ticks-startticks) * self.__systemTick

				objectName = ''
				eventDescription = ''

				if event in BrLibraryFunctionEvents and objectIdent in self.__libraryFunctions:
					object = self.__libraryFunctions[objectIdent]
					objectName = object['name']
					eventDescription = BrLibraryFunctionEvents[event]

				else:
					objectType = self.__objectTypes.get(objectIdent, BrProfilerObjectType.UNKNOWN )
					if objectType == BrProfilerObjectType.UNKNOWN:
						objectName = 'Unknown Object'
					elif objectType == BrProfilerObjectType.TASK_CLASS:
						object = self.__taskClasses[objectIdent]
						objectName = object['name']
						eventDescription = BrTaskClassEvents.get( event, '' )
					elif objectType == BrProfilerObjectType.CYCLIC_TASK:
						object = self.__cyclicTasks[objectIdent]
						objectName = object['name']
						eventDescription = BrCyclicTaskEvents.get( event, '' )
					elif objectType == BrProfilerObjectType.SYSTEM_TASK:
						object = self.__systemTasks[objectIdent]
						objectName = object['name']
						eventDescription = BrSystemObjectEvents.get( event, '' )
					elif objectType == BrProfilerObjectType.INTERRUPT_VECTOR:
						object = self.__interruptHandler[objectIdent]
						objectName = object['name']
						eventDescription = BrInterruptHandlerEvents.get( event, '' ) 
					else:
						raise ValueError("Unknown profiler object type")


				self.__entries.append( BrProfilerEvent( micros, objectIdent, objectName, event, eventDescription) )
				if offset >= maxOffset:
					offset = self.__offsetRecords
				else:
					offset += __class__.SIZEOF_RECORD_ENTRY
		return self.__entries


	def __repr__(self) -> str:
		return f'BrProfilerDataFile'            
    
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
from typing import Optional
from pvi.utils.BrFile import BrFile, ModuleType

class BrProfilerEvent(namedtuple('BrProfilerEvent', ['microseconds', 'objectIdent', 'objectName', 'event', 'eventDescription'])):
	cpuCore: Optional[int] = None
	additionalData: bytes = b''

	def __new__(cls, microseconds, objectIdent, objectName, event, eventDescription, *, cpuCore=None, additionalData=b''):
		entry = super().__new__(cls, microseconds, objectIdent, objectName, event, eventDescription)
		entry.cpuCore = cpuCore
		entry.additionalData = additionalData
		return entry

	def _replace(self, **fields):
		entry = super()._replace(**fields)
		entry.cpuCore = self.cpuCore
		entry.additionalData = self.additionalData
		return entry

class BrProfilerObjectType(IntEnum):
	UNKNOWN = 0
	LIBRARY_FUNCTION = 1
	TASK_CLASS = 2
	CYCLIC_TASK = 3
	SYSTEM_TASK = 4
	INTERRUPT_VECTOR = 5

BrLibraryFunctionEvents = {
	0x03000000 : "library function '{name}' started",
	0x03000001 : "library function '{name}' finished"
}


BrCyclicTaskEvents = {
	0x02000000 : "cyclic task '{name}' started",
	0x02000001 : "cyclic task '{name}' finished",
	0x02000002 : "init program '{name}' started",
	0x02000003 : "init program '{name}' finished",
	0x02000004 : "exit program '{name}' started",
	0x02000005 : "exit program '{name}' finished"
}

BrTaskClassEvents = {
	0x1e000000 : "task class '{name}' started",
	0x1e000001 : "input scheduler of task class '{name}' finished",
	0x1e000002 : "end of cyclic programs in task class '{name}'",
	0x1e000003 : "output scheduler of task class '{name}' started",
	0x1e000004 : "output scheduler of task class '{name}' finished"
}


BrSystemObjectEvents = {
	0x00191902 : 'task switch; outgoing task was waiting',
	0x00252502 : 'task switch; outgoing task was waiting',
	0x00373704 : 'task switch; outgoing task was delayed',
	0x00414102 : 'task switch; outgoing task was waiting',
	0x00020200 : 'task switch; outgoing task was ready',
	0x00fcfc02 : 'task switch; outgoing task was waiting',
	0x00333300 : 'task switch; outgoing task was ready',
	0x00494900 : 'task switch; outgoing task was ready',
	0x00fdfd02 : 'task switch; outgoing task was waiting',
	0x00212102 : 'task switch; outgoing task was waiting',
	0x11000000 : "task '{name}' created",
	0x11000001 : "task '{name}' deleted"
}

BrInterruptHandlerEvents = {
	0x01000000 : "interrupt handler '{name}' started",
	0x01000001 : "interrupt handler '{name}' finished"
}

BrProgramPhaseEvents = {
	0x1b000000 : "init program '{name}' started",
	0x1b000001 : "input scheduler of init program '{name}' finished",
	0x1b000002 : "end of cyclic programs in init program '{name}'",
	0x1b000004 : "output scheduler of init program '{name}' finished",
	0x1c000000 : "exit program '{name}' started",
	0x1c000002 : "end of cyclic programs in exit program '{name}'"
}

BrUserEvents = {
	0x1f000100 : "user event '{name}' started",
	0x1f000110 : 'non-calculable user event entry',
	0x1f000120 : 'non-calculable user event entry',
	0x1f000121 : 'non-calculable user event entry',
	0x1f0001d0 : 'non-calculable user event entry',
	0x1f0001d2 : 'non-calculable user event entry',
	0x1f0001f0 : 'non-calculable user event entry',
	0x1f000200 : "user event '{name}' started",
	0x1f000210 : 'non-calculable user event entry',
	0x1f000220 : 'non-calculable user event entry',
	0x1f000d00 : "user event '{name}' started",
	0x1f000d20 : 'non-calculable user event entry',
	0x1f00f101 : "user event '{name}' finished",
	0x1f00f102 : 'non-calculable user event entry',
	0x1f00f103 : 'non-calculable user event entry'
}

class BrProfilerDataFile(BrFile):
	'''
	Read the profiler layouts observed in the supplied 4.x and 6.x captures.
	Events retain their five tuple fields; cpuCore and additionalData are attributes.
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
		if self.fileType != ModuleType.PROFILER_DATA_OBJECT:
			raise TypeError(f'content is not a B&R profiler data module (Type is {self.fileType})')
		if self._subType not in (0, 3):
			raise ValueError('Unsupported profiler module subtype')
		config, metadata, self.__offsetRecords, self.__endRecords = struct.unpack_from('>4I', self._content, 0x24)
		if not (0x3c <= config and config + 0x84 <= metadata and metadata + 0xb4 <= self.__offsetRecords <= self.__endRecords <= len(self._content)):
			raise ValueError('Invalid profiler section pointers')
		self.__maxSize, self.__additionalDatasizePerEntry, self.__bufferForCreatedTask = struct.unpack_from('<III', self._content, config + 0x10)
		self.__bufferForCreatedUserTask = struct.unpack_from('<I', self._content, config + 0x28)[0]
		libraryNames = self._content[config + 0x82:metadata].rstrip(b'\0')
		libraryFunctionsList = libraryNames.decode('ascii').split('\0') if libraryNames else []
		self.__sgType = 'SG' + str(self._content[metadata])
		runtimeText = self._content[metadata + 4:metadata + 8]
		runtimeParts = struct.unpack_from('<III', self._content, metadata + 0x80)
		if runtimeText.strip(b'\0'):
			self.__arversion = runtimeText[:2].decode('ascii') + '.' + runtimeText[2:].decode('ascii')
			self.__hasCore = False
		elif runtimeParts[0] == 6:
			self.__arversion = '.'.join(str(part) for part in runtimeParts)
			self.__hasCore = self._subType == 0
		else:
			raise ValueError('Unsupported profiler record layout')
		self.__recordSize = (20 if self.__hasCore else 16) + self.__additionalDatasizePerEntry
		if self.__maxSize != self.__endRecords - self.__offsetRecords or self.__maxSize % self.__recordSize:
			raise ValueError('Profiler event-region length does not match record size')
		self.__bridcode = hex(struct.unpack_from('<I', self._content, metadata + 8)[0])
		self.__firstRecordAtOffset, self.__lastRecordAtOffset, self.__tickFrequencyKhz = struct.unpack_from('<III', self._content, metadata + 0x0c)
		if not self.__tickFrequencyKhz:
			raise ValueError('Profiler tick frequency must be positive')
		self.__tickFrequencyMhz = self.__tickFrequencyKhz / 1000
		year, month, day, _, hour, minute, second = struct.unpack_from('<HBBBBBB', self._content, metadata + 0x18)
		self.__profilingTimestamp = datetime( year, month, day, hour, minute, second)
		self.__noOfTaskClasses = struct.unpack_from('<I', self._content, metadata + 0x36)[0]
		self.__noOfCyclicTasks = struct.unpack_from('<I', self._content, metadata + 0x3e)[0]
		self.__noOfSystemTasks = struct.unpack_from('<I', self._content, metadata + 0x46)[0]
		self.__noOfInterrupts = struct.unpack_from('<I', self._content, metadata + 0x4e)[0]
		self.__profiledTargetType = self._content[metadata + 0x52:metadata + 0x80].split(b'\0', 1)[0].decode('ascii')
		self.__maxPossibleEntries = self.__maxSize // self.__recordSize
		if not (0 <= self.__firstRecordAtOffset < self.__maxPossibleEntries and 0 <= self.__lastRecordAtOffset < self.__maxPossibleEntries):
			raise ValueError('Profiler record index is outside the event region')
		self.__offsetObjectEntry = metadata + 0xb4
		objectTableSize = (len(libraryFunctionsList) * self.SIZEOF_LIBRARY_FUNCTION_ENTRY
			+ self.__noOfTaskClasses * self.SIZEOF_TASKCLASS_ENTRY
			+ self.__noOfCyclicTasks * self.SIZEOF_OBJECT_ENTRY
			+ self.__noOfSystemTasks * self.SIZEOF_SYSTEMOBJECT_ENTRY)
		if self.__offsetObjectEntry + objectTableSize > self.__offsetRecords:
			raise ValueError('Profiler object tables overlap the event region')

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


		# 2. task classes
		self.__taskClasses = dict()
		for n in range(self.__noOfTaskClasses):
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
		for interruptIndex in range(self.__noOfInterrupts):
			if offset + self.MIN_SIZE_INTERRUPT_VECTOR > self.__offsetRecords:
				raise ValueError('Profiler interrupt table overlaps the event region')
			ident, interruptNr, length = struct.unpack_from('<I20xII', self._content, offset)
			offset += __class__.MIN_SIZE_INTERRUPT_VECTOR
			if ident != 0:
				if length > self.__offsetRecords - offset:
					raise ValueError('Profiler interrupt name overlaps the event region')
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
		self.__cyclicStatisticsReady = False


	@property
	def info(self) -> dict:
		return({
			"startDateOfProfiling" : self.__profilingTimestamp,
			"sg" : self.__sgType,
			"profiledTarget" : self.__profiledTargetType,
			"targetIdCode"   : self.__bridcode,
			"tickFrequencyMhz"  : self.__tickFrequencyMhz,
			"tickFrequencyKhz" : self.__tickFrequencyKhz,
			"maxSize" : self.__maxSize,
			"additionalDataSizePerEntry" : self.__additionalDatasizePerEntry,
			"bufferForCreatedTask" : self.__bufferForCreatedTask,
			"bufferForCreatedUserTask" : self.__bufferForCreatedUserTask,
			"entries" : self.__maxPossibleEntries,
			"recordSize" : self.__recordSize,
			"hasCpuCore" : self.__hasCore,
			"firstRecordIndex" : self.__firstRecordAtOffset,
			"lastRecordIndex" : self.__lastRecordAtOffset,
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
		'''Task metadata, observed start counts, and complete-call runtimes in microseconds.'''
		if not self.__cyclicStatisticsReady:
			self.__calculateCyclicStatistics()
		return self.__cyclicTasks

	def __calculateCyclicStatistics(self):
		statistics = {ident: {'call_count': 0, 'completed_calls': 0, 'net_total': 0, 'gross_total': 0,
			'net_min': None, 'net_max': None, 'gross_min': None, 'gross_max': None}
			for ident in self.__cyclicTasks}
		classNames = {task['name']: ident for ident, task in self.__taskClasses.items()}
		schedulerClasses = {ident: classNames.get(task['name']) for ident, task in self.__systemTasks.items()}
		cores = {}
		count = (self.__lastRecordAtOffset - self.__firstRecordAtOffset) % self.__maxPossibleEntries + 1
		for entryIndex in range(count):
			physicalIndex = (self.__firstRecordAtOffset + entryIndex) % self.__maxPossibleEntries
			offset = self.__offsetRecords + physicalIndex * self.__recordSize
			ticks, event, ident = struct.unpack_from('<QII', self._content, offset)
			core = struct.unpack_from('<I', self._content, offset + 16)[0] if self.__hasCore else 0
			if core not in cores:
				cores[core] = {'ticks': ticks, 'class': None, 'interrupts': [], 'calls': [], 'phases': []}
			state = cores[core]
			elapsed = ticks - state['ticks']
			if not state['interrupts']:
				for call in reversed(state['calls']):
					if call['class'] == state['class']:
						call['net'] += elapsed
						break
			state['ticks'] = ticks
			if event >> 24 == 0:
				state['class'] = schedulerClasses.get(ident)
			elif event == 0x01000000:
				state['interrupts'].append(ident)
			elif event == 0x01000001:
				if state['interrupts'] and state['interrupts'][-1] == ident:
					state['interrupts'].pop()
			elif event == 0x1e000000:
				state['phases'].append((ident, state['class']))
				state['class'] = ident
			elif event == 0x1e000004:
				if state['phases'] and state['phases'][-1][0] == ident:
					_, state['class'] = state['phases'].pop()
			elif event == 0x02000000 and ident in statistics:
				statistics[ident]['call_count'] += 1
				state['calls'] = [call for call in state['calls'] if call['ident'] != ident]
				state['class'] = self.__cyclicTasks[ident]['taskClass']
				state['calls'].append({'ident': ident, 'class': state['class'], 'start': ticks, 'net': 0})
			elif event == 0x02000001 and ident in statistics:
				for callIndex in range(len(state['calls']) - 1, -1, -1):
					if state['calls'][callIndex]['ident'] != ident:
						continue
					call = state['calls'].pop(callIndex)
					result = statistics[ident]
					result['completed_calls'] += 1
					for kind, duration in (('net', call['net']), ('gross', ticks - call['start'])):
						result[kind + '_total'] += duration
						minimum, maximum = result[kind + '_min'], result[kind + '_max']
						result[kind + '_min'] = duration if minimum is None else min(minimum, duration)
						result[kind + '_max'] = duration if maximum is None else max(maximum, duration)
					if not state['phases']:
						state['class'] = state['calls'][-1]['class'] if state['calls'] else None
					break
		for ident, result in statistics.items():
			task = self.__cyclicTasks[ident]
			task['call_count'] = result['call_count']
			for kind in ('net', 'gross'):
				minimum, maximum = result[kind + '_min'], result[kind + '_max']
				task[f'minimal_{kind}_time'] = None if minimum is None else minimum * 1000 / self.__tickFrequencyKhz
				task[f'maximal_{kind}_time'] = None if maximum is None else maximum * 1000 / self.__tickFrequencyKhz
				task[f'average_{kind}_time'] = (None if minimum is None else
					result[kind + '_total'] * 1000 / self.__tickFrequencyKhz / result['completed_calls'])
		self.__cyclicStatisticsReady = True

	@property
	def systemTasks(self) -> dict:
		return self.__systemTasks

	@property
	def interruptHandler(self) -> dict:
		return self.__interruptHandler


	@property
	def entries(self) -> list:
		if self.__entries is None:
			noOfValidEntries = (self.__lastRecordAtOffset - self.__firstRecordAtOffset) % self.__maxPossibleEntries + 1
			self.__entries = list()
			startticks = struct.unpack_from('<Q', self._content, self.__offsetRecords + self.__firstRecordAtOffset * self.__recordSize)[0]
			for entryIndex in range(noOfValidEntries):
				physicalIndex = (self.__firstRecordAtOffset + entryIndex) % self.__maxPossibleEntries
				offset = self.__offsetRecords + physicalIndex * self.__recordSize
				ticks, event, objectIdent = struct.unpack_from('<QII', self._content, offset)
				micros = (ticks - startticks) * 1000 / self.__tickFrequencyKhz
				cpuCore = struct.unpack_from('<I', self._content, offset + 16)[0] if self.__hasCore else None
				baseSize = 20 if self.__hasCore else 16
				additionalData = self._content[offset + baseSize:offset + self.__recordSize]
				objectName = self.__objectName(event, objectIdent)
				eventDescription = self.__eventDescription(event, objectName)
				self.__entries.append(BrProfilerEvent(micros, objectIdent, objectName, event, eventDescription,
					cpuCore=cpuCore, additionalData=additionalData))
		return self.__entries

	def __objectName(self, event, ident):
		family = event >> 24
		if family == 3:
			objects = self.__libraryFunctions
		elif family == 1:
			objects = self.__interruptHandler
		elif family == 2:
			objects = self.__cyclicTasks
		elif family in (0x1b, 0x1c, 0x1e) or event == 0x15000003:
			objects = self.__taskClasses
		elif family in (0, 0x11):
			objects = self.__systemTasks
		elif family == 0x1f:
			return f'User Event 0x{ident:08x}'
		else:
			return 'Unknown Object'
		name = objects.get(ident, {}).get('name', 'Unknown Object')
		if name == 'Unknown Object':
			label = 'UnknownTaskClass' if event == 0x15000003 else {0: 'UnknownTask', 2: 'UnknownCyclicTask', 0x1e: 'UnknownTaskClass'}.get(family, 'UnknownObject')
			return f'{label} 0x{ident:08x}'
		if (family in (0, 0x11, 0x1b, 0x1c, 0x1e) or event == 0x15000003) and name.startswith('TC#'):
			return 'Cyclic #' + name[3:]
		if family == 1:
			name = name.replace('\0', '')
			if name.endswith(' ()'):
				name = name[:-3]
		return name

	@staticmethod
	def __eventDescription(event, objectName=None):
		family = event >> 24
		if family == 0:
			description = BrSystemObjectEvents.get(event)
			state = {0: 'ready', 1: 'suspended', 2: 'waiting', 4: 'delayed', 6: 'delayed and waiting'}.get(event & 0xff)
			if description is None and state is not None:
				description = f'task switch; outgoing task was {state}'
			if description is not None:
				if objectName is not None:
					return description.replace('task switch;', f"'{objectName}' is now running;", 1)
				return description
		for events in (BrLibraryFunctionEvents, BrCyclicTaskEvents, BrTaskClassEvents, BrInterruptHandlerEvents, BrProgramPhaseEvents, BrUserEvents, BrSystemObjectEvents):
			if event in events:
				description = events[event]
				return description.replace(" '{name}'", '') if objectName is None else description.format(name=objectName)
		if event == 0x15000003:
			return 'task class tolerance' if objectName is None else f'{objectName} is now in task class tolerance'
		if family in (0x12, 0x13, 0x14, 0x15):
			label = {0x12: 'system exception', 0x13: 'processor exception', 0x14: 'AR logger event', 0x15: 'system event'}[family]
			return f'{label} (0x{event:08X})'
		if family == 0x1f:
			return f'user event (0x{event:08X}); semantics unknown'
		return f'unknown event 0x{event:08X}'


	def __repr__(self) -> str:
		return f'BrProfilerDataFile'            
    
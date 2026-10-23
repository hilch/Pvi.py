# [Profiler](https://help.br-automation.com/#/en/4/diagnostics_support%2Fdiagnosis%2Fprofile%2Fdiagnosis_profile.html)

The Profiler can be used to measure and display important system data such as task runtimes, system and stack loads, etc. This can be necessary to determine how much idle time remains in a task class or which task generates a sporadic increased demand for time.

The profiler can also record and analyze events determined by the user (user events) such as interrupt service routine and library function time demands, as well as time differences between events.

## [Recording profiler data](https://help.br-automation.com/#/en/4/diagnostics_support%2Fdiagnosis%2Fprofile%2Frecord%2Fdiagnosis_profile_record.html)

To record profiler data, the configuration data has to be installed first before the profiler can be started. After the profiler stops and measurement ends, profiler-specific data should be erased on the target system so that memory is not used unnecessarily.

## Reading profiler data

In fact there is no real support in PviCom.dll for extracting the contents in a profiler module but this topic fits very well into the PVI category.
Handling profiler files is still beta since the file format is not public, the known structure was found out by reverse engineering.

`BrProfilerDataFile` supports known profiler 4.x and 6.x data formats,
including wrapped buffers and extended records. It follows the binary section
pointers rather than assuming an XML wrapper or fixed metadata offsets.
Record layout selection is limited to the observed runtime/subtype
combinations; subtype alone is not a general format discriminator.

```python
from pvi.utils import BrProfilerDataFile

profiler = BrProfilerDataFile('profiling.pd')
print(profiler.info)
for entry in profiler.entries:
	print(entry.microseconds, entry.objectName, hex(entry.event),
		  entry.cpuCore, entry.additionalData.hex())
```

Events retain the five tuple fields `microseconds`, `objectIdent`,
`objectName`, `event`, and `eventDescription`. `microseconds` is elapsed
time from the first chronological record, not a calendar timestamp.
The additional attribute `cpuCore` is `None` when the record has no core
field. `additionalData` contains the stored extra bytes, without interpreting
them or discarding possible alignment bytes. Existing five-value unpacking
continues to work.

`info['tickFrequencyMhz']` is now expressed in MHz, correcting the previous
kHz-valued result. `tickFrequencyKhz` exposes the original integer field.
`recordSize`, `hasCpuCore`, `firstRecordIndex`, and `lastRecordIndex` describe
the stored layout. `entries` in `info` is the number of slots in the binary
event region, not a requested recording-entry count; the actual chronological
events are in `profiler.entries`.

The stored `additionalDataSizePerEntry` may differ from the requested size,
so the stored record size and count are used when reading events rather than
the requested recording settings. Scheduler descriptions identify the outgoing
state but do not reconstruct its name. Unknown codes and IDs are retained;
undecoded event and payload meanings are not inferred. Timestamps are calculated
from the stored tick frequency and may differ slightly from the Profiler's CSV
export if that frequency does not preserve the full conversion precision.

## Cyclic task statistics

Each entry in `profiler.cyclicTasks` retains its `name` and `taskClass` and
provides these calculated fields:

| Field | Meaning |
| --- | --- |
| `call_count` | Number of recorded cyclic-task start events |
| `minimal_net_time` | Shortest complete call's execution time, excluding recorded interruptions |
| `average_net_time` | Total net time of complete calls divided by their count |
| `maximal_net_time` | Longest complete call's net execution time |
| `minimal_gross_time` | Shortest complete call's elapsed start-to-finish time |
| `average_gross_time` | Total gross time of complete calls divided by their count |
| `maximal_gross_time` | Longest complete call's elapsed start-to-finish time |

All times are in microseconds. Net time excludes recorded interrupt handlers
and execution of other task classes on the same CPU core. Interrupt nesting,
scheduler switches, and task-class phases are tracked separately for each
core. Gross time includes these interruptions, following the definitions in
[Evaluating Profiler data in a table](https://help.br-automation.com/#/en/6/diagnostics_support/diagnosis/profile/analyze/diagnosis_profile_analyze_table.html).

Only matched start/finish pairs contribute timing measurements. An unmatched
finish at the beginning of a recording is ignored; an unfinished start still
contributes to `call_count`, but not to the timing summaries. Consequently,
`call_count` can exceed the number of calls used for the averages at recording
boundaries. If no complete call was recorded, all six timing fields are
`None`. Tasks with no start event have a `call_count` of zero.

Statistics are calculated on first access and cached. Their accuracy depends
on recording the relevant task, scheduler, and interrupt events; unrecorded
interruptions cannot be subtracted from net time.

```python
for ident, task in profiler.cyclicTasks.items():
	print(hex(ident), task['name'], task['call_count'],
		  task['average_net_time'], task['average_gross_time'])
```

## Examples

find the following examples on GitHub [github.com/hilch/Pvi.py](https://github.com/hilch/Pvi.py/tree/main/examples)

### [profiler1.py](https://github.com/hilch/Pvi.py/tree/main/examples/profiler1.py)

extract all profiler data *.pd file and save it to csv

### [profiler2.py](https://github.com/hilch/Pvi.py/tree/main/examples/profiler2.py)

extract all profiler data from a systemdump container and save it to csv
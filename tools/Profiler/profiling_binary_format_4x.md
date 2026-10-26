# B&R Profiling 4.x Binary Format

## Scope and evidence

This describes files 1 and 10, their matching CSV exports, and information
reports. Both reports identify profiler application version `4.00.2`.
Interpretations are limited to these samples, not every possible 4.x file.
See [Profiling 6.x](profiling_binary_format_6x.md) for files 2-9 and 11.

| Binary file | CSV reference | Information report | Automation Runtime | Target |
| --- | --- | --- | --- | --- |
| `profiling_1.pd` | `profiling_1.csv` | `information_1.txt` | `S4.93` | `X20CP3687X` |
| `profiling_10.pd` | `profiling_10.csv` | `information_10.txt` | `E3.10` | `1A4000.00` |

Profiler and Automation Runtime versions are different properties. The
binary field storing the profiler application version remains unidentified.
Subtype `0x03` is not exclusive to 4.x: it also occurs in the 6.x file 2.
File 10 uses subtype `0x00` with 16-byte records, unlike the core-bearing
subtype-`0x00` records in the supplied 6.x files. Neither subtype alone nor
profiler major version alone establishes all container and record details.

## B&R module container

Offsets are absolute file offsets. Multi-byte container-header values and
pointers are big-endian unless stated otherwise.

The following table describes file 1; file 10's differing values follow.

| Offset | Size | Observed meaning |
| --- | ---: | --- |
| `0x00` | 2 | Module signature `0x2B97` |
| `0x02` | 1 | Module type `0x4C` |
| `0x03` | 1 | Module subtype `0x03` |
| `0x0E` | 4 | Total file size in bytes |
| `0x20` | 4 | Binary-payload offset `0x78` |
| `0x24` | 4 | Capture-configuration pointer `0x94` |
| `0x28` | 4 | Profiler-metadata pointer `0x118` |
| `0x2C` | 4 | Event-region start `0x7D60` |
| `0x30` | 4 | Event-region end, exclusive: `0xDB20` |
| `0x34` | 4 | Pointer into the post-event trailer; target meaning unknown |
| `0x38` | 4 | Pointer into the post-event trailer; target meaning unknown |
| `0x3C` | 4 | Constant bytes `00 3C 42 72`; meaning unknown |

In file 1, the module wrapper begins at `0x3D` with `<BrModul Version="1.0">`,
includes `<HeaderExt Scope="" />`, and ends with `</BrModul>` at `0x76`.
A zero byte at `0x77` precedes the binary payload at `0x78`.
The last three bytes of the constant at `0x3C` are also the opening `<Br`
of the wrapper; its meaning as a numeric field is not established.
Ranges `0x04`-`0x0D`, `0x12`-`0x1F`, and payload bytes `0x78`-`0x7F`
remain undecoded. Constant or zero bytes are not proven padding.

### File 10 container variant

File 10 is also reported as profiler `4.00.2`, but uses subtype `0x00`
and has no `<BrModul>` XML wrapper. Its payload starts at `0x60`, capture
configuration at `0x7C`, and metadata at `0x100`. Its event region is
`[0xACDA, 0x31DDA)`, containing 160,000 bytes. The report lists 10,000
events and zero additional bytes, verified against a 16-byte record stride,
not the subtype-`0x00` 20-byte layout observed in the 6.x captures.
Subtype alone therefore cannot select a record layout across all samples.

The file is 205,912 bytes long, matching the big-endian size at `0x0E`.
Bytes `0x3C`-`0x5F` are zero, rather than the XML opening in file 1.
Pointers at `0x34` and `0x38` are `0x31DE6` and `0x31E0C`, respectively;
both point into the post-event trailer, whose structure remains unresolved.
The binary configuration's event length also equals 160,000 bytes.

## Capture configuration

Let `C` be the big-endian pointer at `0x24`: `0x94` in file 1 and
`0x7C` in file 10. The following fields are little-endian 32-bit integers:

| Relative offset | Size | Observed meaning |
| --- | ---: | --- |
| `+0x10` | 4 | Event-region length: 24,000 bytes in file 1; 160,000 in file 10 |
| `+0x14` | 4 | Additional bytes per event record: zero in both files |
| `+0x18` | 4 | Buffer for created tasks: 20 in file 10 |
| `+0x28` | 4 | Buffer for created user tasks: 0 in file 10 |

In file 10, `C + 0x18` stores 20 and `C + 0x28` stores 0, matching
the reported created-task and created-user-task buffer sizes, respectively.
Unlike the supplied 6.x files 2-9 and 11, these reported settings differ,
providing evidence for the individual assignment of the two fields.
File 1 also stores unequal values, 50 and 0, but its information report
does not list either buffer setting, so it cannot independently establish
their meanings.

The observed stride is `16 + additional_bytes = 16` bytes in both files,
despite their different subtypes. It matches the event-region sizes and all
11,500 CSV events. Nonzero additional-byte counts have not been verified
for profiling 4.x. Other configuration fields remain unidentified.

## Profiler metadata

Let `M` be the big-endian pointer at `0x28`: `0x118` in file 1 and `0x100`
in file 10. The table below gives file 1's values.
Numeric fields in this block are little-endian.

| Relative offset | Size | Observed meaning |
| --- | ---: | --- |
| `+0x04` | 4 | ASCII `S493`, corresponding to Automation Runtime `S4.93`; absolute offset `0x11C` |
| `+0x0C` | 4 | First chronological record index: 368 |
| `+0x10` | 4 | Last chronological record index, inclusive: 367 |
| `+0x14` | 4 | Tick frequency: 1,596,000 kHz (1596.000 MHz) |
| `+0x18` | 2 | Capture start year |
| `+0x1A` | 1 | Month |
| `+0x1B` | 1 | Day of month |
| `+0x1C` | 1 | Weekday, consistent with Sunday = 0 |
| `+0x1D` | 1 | Hour, 24-hour clock |
| `+0x1E` | 1 | Minute |
| `+0x1F` | 1 | Second |
| `+0x52` | variable | Null-terminated ASCII target type `X20CP3687X` |
| `+0x80`, `+0x84`, `+0x88` | 4 each | Zero; these hold numeric runtime components in the 6.x samples, not here |

The encoded start timestamp `2026-06-30 21:46:52` matches the report.
Timezone and the absolute event-counter epoch are not established.
The report lists 606 known objects; their binary count field is unidentified.
Neither that count nor profiler version `4.00.2` should be inferred from
the constant metadata prefix alone.

File 10 retains the same relative offsets. `M + 0x04` contains ASCII
`E310`, matching runtime `E3.10`; numeric runtime components at `M + 0x80`,
`M + 0x84`, and `M + 0x88` are all zero. The target at `M + 0x52` is
`1A4000.00`. The encoded date `2026-10-23 13:37:42` matches the report,
including weekday 5 (Friday). First/last indexes are 0 and 9,999, and the
frequency is 1,000 kHz (1.00 MHz). The report lists 85 known objects;
this count has not been assigned a binary field.

## Traced objects

The CSV `Times` section lists `Name` and `Object Priority`. It is
hierarchical: task-class names appear in `Name`, while child names can
occupy the adjacent unnamed column. Both columns matter.

The supplied priority semantics are **255 highest, 0 lowest** on the
profiler's exported VxWorks task-priority scale. A higher-priority task can
preempt a lower-priority task on the same core. Equal-priority ordering
cannot be deduced from priority alone. Empty priority cells are not zero.
For example, `an_fastTas` has priority 230 and `allg` has 218.
These semantics are supplied domain information, not inferred binary fields;
the binary priority location remains unknown.

### Names, spacing, and identifiers

Names are null-terminated ASCII strings before the event region. These
consecutive name starts are 62 bytes (`0x3E`) apart:

| Name | Absolute name offset |
| --- | --- |
| `cmax_com_4` | `0x518` |
| `restlfz` | `0x556` |
| `an_fastTas` | `0x594` |
| `Testpult` | `0x5D2` |
| `init_sys` | `0x610` |
| `allg` | `0x64E` |
| `konf_rd` | `0x68C` |
| `daten_rw` | `0x6CA` |
| `cms_open` | `0x708` |

Two identifier layouts were verified against unique CSV event name/ID pairs.
Each ID is a little-endian 32-bit integer. The counts below refer to file 1:

| Layout | ID location | Matching name/ID pairs | Adjacent matched-name stride | Adjacent pairs at that stride |
| --- | --- | ---: | --- | ---: |
| A | `name_offset - 0x1C` | 46 | 62 bytes (`0x3E`) | 42 |
| B | `name_offset - 0x24` | 46 | 70 bytes (`0x46`) | 16 |

| Name | Name offset | ID offset | Object ID | ID bytes |
| --- | --- | --- | --- | --- |
| `an_fastTas` | `0x594` | `0x578` | `0x0129B1DC` | `DC B1 29 01` |
| `Testpult` | `0x5D2` | `0x5B6` | `0x0129B228` | `28 B2 29 01` |
| `allg` | `0x64E` | `0x632` | `0x0129B2C0` | `C0 B2 29 01` |
| `tJobTask` | `0x305C` | `0x3038` | `0x0107FBD0` | `D0 FB 07 01` |
| `$arlogconn00000001` | `0x3FAC` | `0x3F88` | `0x06608350` | `50 83 60 06` |
| `_TEVCYCLIC_0d9a14b0_0000c350` | `0x5ED8` | `0x5EB4` | `0x130EDB88` | `88 DB 0E 13` |

All 92 located pairs match one of these layouts, with zero mismatches.
The remaining 41 of 133 unique CSV name/ID pairs have no literal
null-terminated name match. Searches covered all occurrences before the
event region; counts refer to name/ID pairs, not necessarily distinct names.
Missing literal names do not prove that their metadata is absent.
Stride counts cover consecutive matched names, not the full object table.
Table boundaries, layout selection, other entry fields, and complete
identifier-namespace rules remain unresolved.

File 10 has 19 unique CSV name/ID pairs: ten match layout A, one matches
layout B, and eight have no literal null-terminated name before the event
region. Every located pair matches its ID; there are zero located-name/ID
mismatches. The missing pairs are `Cyclic #1` through `Cyclic #4`, each
with a task-class ID and a different scheduler-object ID. Preserve event
context rather than using the displayed name as a unique object key.

There are nine adjacent matched layout-A names 62 bytes apart. The single
layout-B match is `WINDOWS`, name at `0x127C` and ID `0x0396BDD0` at
`0x1258`, so no adjacent B stride can be tested. For example,
`Acp10CyclicTC1` has its name at `0x636` and ID `0x0102AF30` at `0x61A`.

## Event records

Both files contain packed 16-byte records. One record corresponds to one
CSV event row.

| File | Subtype | Event region, end exclusive | Bytes | Records |
| --- | --- | --- | ---: | ---: |
| `profiling_1.pd` | `0x03` | `[0x7D60, 0xDB20)` | 24,000 | 1,500 |
| `profiling_10.pd` | `0x00` | `[0xACDA, 0x31DDA)` | 160,000 | 10,000 |

Names and descriptions are not inline. There is no per-record delimiter
or length field in this layout.

All fields are unsigned little-endian integers (Python `struct`: `<QII`):

| Record offset | Size | Observed field |
| --- | ---: | --- |
| `0x00` | 8 | Event tick counter |
| `0x08` | 4 | Event code; CSV `Event` |
| `0x0C` | 4 | Object identifier; CSV `Object Ident` |

There is no CPU-core field, and neither CSV has a `CPU Core` column.
Physical record `i` occupies `[start + i * size, start + (i + 1) * size)`;
the count is `(end - start) / size`, using the pointers at `0x2C` and `0x30`.

### Ordering and byte example

File 1's buffer is wrapped: physical order has one counter decrease. Chronological
CSV row `j` maps to physical record `(368 + j) % 1500`. The report's
"record at offset" means a record index, not a byte offset. Rotating at
the decrease or sorting by unsigned counter reproduces all 1,500 CSV
event-code/object-ID pairs with zero mismatches.

Physical record 368, at absolute offset `0x9460`, is the first chronological
event:

```text
Record offset  Bytes                    Decoded value
0x00           EC CB C7 30 15 00 00 00  Counter = 91,012,713,452
0x08           01 00 00 02              Event   = 0x02000001
0x0C           28 B2 29 01              Object  = 0x0129B228
```

The object is `Testpult`: its metadata ID at `0x5B6` matches this record.
The name is not part of the 16 record bytes.

### File 10 ordering and validation

Counters are nondecreasing in physical order with no wrap. All 10,000
slots are occupied; none is entirely zero. First/last counters are
103,090,001 and 108,150,007. Direct physical order reproduces every CSV
event-code/object-ID pair without mismatches. The first event is a
ready-state scheduler switch, code `0x00878700`, object `0x00B18020`
(`Cyclic #1`); the final event is cyclic task `mainlogic` finished,
code `0x02000001`, object `0x0102AD70`.

## Counter and CSV time conversion

Let `F` be the little-endian kHz value at `M + 0x14`, `T` an unsigned
counter, and `T0` the first chronological counter selected using `M + 0x0C`:

```text
ticks_per_microsecond = F / 1000
relative_time_us = (T - T0) * 1000 / F
absolute_time_us = T * 1000 / F
```

In file 1 the scale is 1,596 ticks per microsecond. All 1,500 events were
checked with the metadata ring index and configuration-derived stride.
Maximum relative and absolute errors are each below 0.000499 microseconds,
consistent with CSV three-decimal rounding. CSV absolute time is a scaled
counter, not a calendar timestamp formed from the capture date. Its epoch
is unknown. These observations do not specify unobserved 4.x variants.

In file 10 the scale is exactly one tick per microsecond. Decimal arithmetic
confirms zero relative and absolute timestamp error across all 10,000 CSV
events. The relative span is 5,060,006 microseconds. This also supports
using metadata frequency rather than assuming an x86-specific tick scale.

## Events and their meaning

The little-endian 32-bit field at record offset `0x08` matches CSV `Event`.
File 1 has 106 distinct event codes; file 10 has ten. Their union contains
109 codes. Descriptions below are based on the CSV exports, not a universal
dictionary for all 4.x captures.
Hexadecimal prefixes refer to the decoded integer, not its first stored byte.

### Scheduler switches

Codes `0x00xxxxss` describe `'<incoming>' is now running - '<outgoing>'
was <state>`. CSV `Name` and `Object Ident` identify the incoming object.
The outgoing name appears in the description, not in a separate known
record field.

| Low byte `ss` | Outgoing task state |
| --- | --- |
| `0x00` | ready: runnable but no longer running, potentially preempted |
| `0x01` | suspended |
| `0x02` | waiting for a resource or event |
| `0x04` | delayed |
| `0x06` | delayed and waiting |

Middle bytes `xxxx` remain undecoded and must be
preserved. Ready alone does not prove higher-priority preemption.

File 10 adds three scheduler codes relative to file 1:

| Code | Count in file 10 | Outgoing state |
| --- | ---: | --- |
| `0x00878700` | 507 | ready |
| `0x009D9D00` | 41 | ready |
| `0x00FDFD02` | 547 | waiting |

The first two are new relative to all supplied files 1-9; `0x00FDFD02`
already occurs in 6.x evidence. These are new code values, not a new family.
File 10's other seven codes are cyclic-task start/finish and all five
task-class phase codes listed below. No interrupt, diagnostic, lifecycle,
or user-event code is present in file 10.

### Execution, phases, and diagnostics

| Code or family | Meaning from the supplied 4.x CSV evidence |
| --- | --- |
| `0x01000000` / `0x01000001` | Interrupt handler started / finished |
| `0x02000000` / `0x02000001` | Cyclic task started / finished |
| `0x11000001` | Task deleted |
| `0x1E000000` | Task class started |
| `0x1E000001` | Input scheduler of task class finished |
| `0x1E000002` | End of cyclic programs in task class |
| `0x1E000003` | Output scheduler of task class started |
| `0x1E000004` | Output scheduler of task class finished |
| `0x12000098` | System Exception; subcode unresolved |
| `0x14000003`, `0x14000501` | AR Logger Event; lower fields undecoded |
| `0x15000000` | System Event; no further meaning established |
| `0x15000003` | `Cyclic #2 is now in task class tolerance`, observed in file 1 |
| `0x1F00F102`, `0x1F00F103` | `Non calculateable user event entry` |

Started/finished intervals need not be uninterrupted execution, and capture
boundaries can leave unpaired events. Task-class phases are distinct from
individual cyclic-task activity. Additional init/exit phase families
`0x1B...` and `0x1C...` were observed only in the 6.x file 4 and are not
established for either 4.x sample.

No user-event started/finished code was observed in either sample. The payload
and timing semantics of file 1's two user-event codes are unresolved; do not
infer start/finish from low-byte parity. Preserve unknown numeric codes.

## Remaining unknowns

- Complete object tables, layout selection, priority and remaining entry
  fields, identifier namespaces, and unmatched object-name mappings.
- Scheduler middle bytes, exception subcodes, user-event payloads, and
  meanings beyond CSV descriptions.
- Counter epoch and capture-date timezone.
- Undecoded header, configuration, and metadata fields, including binary
  known-object count and profiler application version.
- Trailer structures referenced by `0x34` and `0x38`.
- Binary-only selection between the observed subtype-`0x00` 16-byte layout
  and the 6.x core-bearing layout; subtype alone is insufficient.
- Other 4.x variants, nonzero additional-byte areas, and generality beyond
  the two supplied 4.x samples.
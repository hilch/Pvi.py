# B&R Profiling 6.x Binary Format

## Scope and evidence

This describes files 2-9 and their matching CSV exports and information
reports. The reports independently provide profiler versions, frequency,
record indexes, target identity, and capture dates.

| Binary file | CSV reference | Information report | Profiler application version |
| --- | --- | --- | --- |
| `profiling_2.pd` | `profiling_2.csv` | `information_2.txt` | `6.0.0.0` |
| `profiling_3.pd` | `profiling_3.csv` | `information_3.txt` | `6.1.0.0` |
| `profiling_4.pd` | `profiling_4.csv` | `information_4.txt` | `6.1.0.0` |
| `profiling_5.pd` | `profiling_5.csv` | `information_5.txt` | `6.1.0.0` |
| `profiling_6.pd` | `profiling_6.csv` | `information_6.txt` | `6.1.0.0` |
| `profiling_7.pd` | `profiling_7.csv` | `information_7.txt` | `6.1.0.0` |
| `profiling_8.pd` | `profiling_8.csv` | `information_8.txt` | `6.1.0.0` |
| `profiling_9.pd` | `profiling_9.csv` | `information_9.txt` | `6.1.0.0` |

See [Profiling 4.x](profiling_binary_format_4x.md) for files 1 and 10.
Profiler application versions differ from Automation Runtime versions;
their binary field remains unidentified. Subtype is not a profiler-major-
version discriminator: file 2 uses `0x03`, also observed in profiling 4.x.
Within these 6.x samples, file 2 has 16-byte records and files 3-9 have
core-bearing records of 20, 32, or 120 bytes. These are observations, not a
universal version-to-layout rule.
In particular, 4.x file 10 uses subtype `0x00` with 16-byte records and
no core field; the base-size rule below is limited to these 6.x captures.

## B&R module container

Offsets are absolute. Multi-byte container-header values and pointers are
big-endian unless stated otherwise.

| Offset | Size | Observed meaning |
| --- | ---: | --- |
| `0x00` | 2 | Module signature `0x2B97` |
| `0x02` | 1 | Module type `0x4C` |
| `0x03` | 1 | Subtype `0x03` in file 2; `0x00` in files 3-9 |
| `0x0E` | 4 | Total file size in bytes |
| `0x20` | 4 | Binary-payload offset `0x78` |
| `0x24` | 4 | Capture-configuration pointer `0xAC` |
| `0x28` | 4 | Profiler-metadata pointer `0x130` |
| `0x2C` | 4 | Event-region start |
| `0x30` | 4 | Event-region end, exclusive |
| `0x34` | 4 | Pointer into the post-event trailer; target meaning unknown |
| `0x38` | 4 | Pointer into the post-event trailer; target meaning unknown |
| `0x3C` | 4 | Constant bytes `00 3C 42 72`; meaning unknown |

The module wrapper begins at `0x3D` with `<BrModul Version="1.0">`,
includes `<HeaderExt Scope="" />`, and ends with `</BrModul>` at `0x76`.
A zero byte at `0x77` precedes the binary payload at `0x78`.
The last three bytes of the constant at `0x3C` are also the opening `<Br`
of the wrapper; its meaning as a numeric field is not established.
Ranges `0x04`-`0x0D`, `0x12`-`0x1F`, and payload bytes `0x78`-`0x7F`
remain undecoded. Constant or zero bytes are not proven padding.

## Capture configuration

Let `C` be the big-endian pointer at `0x24`, here `0xAC`.
These little-endian 32-bit fields explain the event length and record stride:

| Relative offset | Size | Observed meaning |
| --- | ---: | --- |
| `+0x10` | 4 | Event-region length; equals end minus start in all eight samples |
| `+0x14` | 4 | Stored additional bytes per record: 100 in file 5, 12 in file 9, zero otherwise |
| `+0x18` | 4 | Buffer for created tasks; assignment distinguished by 4.x file 10 |
| `+0x28` | 4 | Buffer for created user tasks; assignment distinguished by 4.x file 10 |

For observed subtypes, `record_size = base_size + additional_bytes`, with
base size 16 for `0x03` and 20 for `0x00`. File 5 therefore uses
`20 + 100 = 120` bytes. This binary-only rule was checked against every
CSV event; it does not establish extra-area contents or unobserved layouts.
Other configuration fields remain unidentified. Use the stored additional
size, not the report's requested size, to compute the binary stride.

### Files 7-9: requested versus stored sizes

File 9 reports 10 additional bytes per entry, but `C + 0x14` stores 12.
Its 300,000-byte event region contains 9,375 records of 32 bytes, matching
the reported first/last indexes 0 and 9,374. The report's 10,000 recording
entries therefore must not be used as the stored record count. The numbers
are consistent with a requested `10,000 * (20 + 10)` byte budget and a
stored stride of `20 + 12`; the allocation algorithm is not yet established.
The stored extra size is consistent with four-byte rounding, not proof
of an alignment rule for all captures.

Files 7 and 8 each contain 10,000 records of 20 bytes. Across files 7-9,
little-endian fields `C + 0x18` and `C + 0x28` both match the
reports' buffers for created tasks and created user tasks: 50, 256, and 123.
Both settings change together, so these 6.x captures alone cannot distinguish
their individual assignment. The additional 4.x file 10 stores unequal
values 20 and 0, respectively matching its report's created-task and
created-user-task settings. This supports the assignments in the table;
an unequal-setting 6.x capture would independently confirm them for 6.x.

| File | Reported entries | Reported extra bytes | Stored extra bytes | Stored stride | Stored records | Both buffer fields |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `profiling_7.pd` | 10,000 | 0 | 0 | 20 | 10,000 | 50 |
| `profiling_8.pd` | 10,000 | 0 | 0 | 20 | 10,000 | 256 |
| `profiling_9.pd` | 10,000 | 10 | 12 | 32 | 9,375 | 123 |

Files 7 and 8 have identical event-region boundaries despite changing
both buffer settings from 50 to 256. These settings therefore do not
directly give pre-event object-table sizes in these samples.

## Profiler metadata

Let `M` be the big-endian pointer at `0x28`, here `0x130`.
Numeric fields in this block are little-endian.

| Relative offset | Size | Observed meaning |
| --- | ---: | --- |
| `+0x04` | 4 | Zero in these samples; the 4.x sample uses this location for ASCII runtime text |
| `+0x0C` | 4 | First chronological record index, zero-based |
| `+0x10` | 4 | Last chronological record index, inclusive |
| `+0x14` | 4 | Tick frequency in kHz; divide by 1,000 for reported MHz |
| `+0x18` | 2 | Capture start year |
| `+0x1A` | 1 | Month |
| `+0x1B` | 1 | Day of month |
| `+0x1C` | 1 | Weekday, consistent with Sunday = 0 |
| `+0x1D` | 1 | Hour, 24-hour clock |
| `+0x1E` | 1 | Minute |
| `+0x1F` | 1 | Second |
| `+0x52` | variable | Null-terminated ASCII target type |
| `+0x80`, `+0x84`, `+0x88` | 4 each | Automation Runtime major, minor, patch; absolute offsets `0x1B0`, `0x1B4`, `0x1B8` |

| File | Frequency (kHz) | Reported MHz | First index | Last index | Known objects reported |
| --- | ---: | ---: | ---: | ---: | ---: |
| `profiling_2.pd` | 2,416,666 | 2416.666 | 2,337 | 2,336 | 258 |
| `profiling_3.pd` | 2,900,000 | 2900.000 | 0 | 49,999 | 372 |
| `profiling_4.pd` | 2,610,125 | 2610.125 | 0 | 499,999 | 581 |
| `profiling_5.pd` | 2,610,125 | 2610.125 | 0 | 149,999 | 347 |
| `profiling_6.pd` | 10,000 | 10.00 | 0 | 499,999 | 169 |
| `profiling_7.pd` | 10,000 | 10.00 | 0 | 9,999 | 170 |
| `profiling_8.pd` | 10,000 | 10.00 | 0 | 9,999 | 170 |
| `profiling_9.pd` | 10,000 | 10.00 | 0 | 9,374 | 170 |

| File | Capture start | Automation Runtime | Target |
| --- | --- | --- | --- |
| `profiling_2.pd` | `2025-08-13 07:34:30` | `6.3.4` | `5APC4100.TGL1-000` |
| `profiling_3.pd` | `2026-09-10 12:39:39` | `6.7.7` | `5APC3100.KBU3-000` |
| `profiling_4.pd` | `2026-10-07 10:26:43` | `6.8.1` | `5APC4100.TGL2-000` |
| `profiling_5.pd` | `2026-07-13 13:01:37` | `6.7.5` | `5APC4100.TGL2-000` |
| `profiling_6.pd` | `2026-10-23 10:48:24` | `6.1.1` | `X20CP3684` |
| `profiling_7.pd` | `2026-10-23 13:15:01` | `6.8.1` | `X20CP3684` |
| `profiling_8.pd` | `2026-10-23 13:20:30` | `6.8.1` | `X20CP3684` |
| `profiling_9.pd` | `2026-10-23 13:25:01` | `6.8.1` | `X20CP3684` |

Dates and times match the reports, including corrected `information_6.txt`.
Timezone and an absolute event-counter epoch are not established.
Known-object counts are report values, not identified binary count fields
or CSV object totals. Profiler application versions have not been mapped
to binary fields and must not be inferred from a constant metadata prefix.

The first/last indexes identify the wrapped buffer in file 2. In these
full buffers, CSV row `j` corresponds to physical record
`(first_index + j) % record_count`. The reports' "record at offset" refers
to a record index, not a byte offset.

## Traced objects

CSV `Times` is hierarchical: group names such as `Cyclic #1` appear in
`Name`, while child names occupy an adjacent unnamed column. Both columns
must be considered. Names and priorities are object metadata, not inline
event-record fields.

Supplied domain information defines exported VxWorks task priority as
**255 highest, 0 lowest**. Higher-priority tasks can preempt lower-priority
tasks on the same core; equal-priority ordering is not determined by this
alone. Empty priority cells are not zero. The binary priority field has not
been located; these semantics are not inferred from the entry bytes.

### Binary names and object identifiers

Null-terminated ASCII names occur before the event region. For example,
`FG_ColM` starts at `0x566` in file 3 and `0x4A4` in file 4.
Two observed layouts hold little-endian 32-bit IDs:

| Layout | ID location relative to name start | Observed adjacent-name stride |
| --- | --- | --- |
| A | `name_offset - 0x1C` (28 bytes before name) | 62 bytes (`0x3E`) |
| B | `name_offset - 0x24` (36 bytes before name) | 70 bytes (`0x46`) |

All unique CSV event name/`Object Ident` pairs were checked using literal
null-terminated ASCII searches before the event region. Every occurrence
of repeated names was considered, not just the first.

| File | CSV name/ID pairs | Layout A | Layout B | Name not located | Located name, no matching ID |
| --- | ---: | ---: | ---: | ---: | ---: |
| `profiling_2.pd` | 126 | 27 | 62 | 37 | 0 |
| `profiling_3.pd` | 212 | 22 | 101 | 89 | 0 |
| `profiling_4.pd` | 286 | 63 | 185 | 38 | 0 |
| `profiling_5.pd` | 210 | 84 | 93 | 33 | 0 |
| `profiling_6.pd` | 25 | 8 | 1 | 16 | 0 |
| `profiling_7.pd` | 25 | 8 | 1 | 16 | 0 |
| `profiling_8.pd` | 25 | 8 | 1 | 16 | 0 |
| `profiling_9.pd` | 25 | 8 | 1 | 16 | 0 |

Counts refer to name/ID pairs, not necessarily distinct names. Every located
pair matches a layout; missing literal names do not establish absent metadata.
Names are not unique keys: files 3-5 contain multiple IDs for `OpcUa_Task`.
Later occurrences resolve `FxDeviceMonitoring` in file 3 and `FG_GlD`,
`FG_Glue`, and `FG_WPr` in file 4.

Object IDs are not necessarily globally unique across event families:
file 6 exports `0x00000001` for both `WINDOWS` and `Cyclic #1`. Retain
the event code and context; complete namespace rules remain unresolved.

| File | Adjacent matched layout-A names 62 bytes apart | Adjacent matched layout-B names 70 bytes apart |
| --- | ---: | ---: |
| `profiling_2.pd` | 23 | 31 |
| `profiling_3.pd` | 16 | 57 |
| `profiling_4.pd` | 55 | 143 |
| `profiling_5.pd` | 82 | 56 |
| `profiling_6.pd` | 6 | 0 |
| `profiling_7.pd` | 6 | 0 |
| `profiling_8.pd` | 6 | 0 |
| `profiling_9.pd` | 6 | 0 |

Stride counts include only consecutive matched name offsets, not all entries.
Files 6-9 each have only one matched B entry, so no adjacent B stride can
be tested in those files.
Repeated spacing supports fixed-size layouts in these regions, not complete
table boundaries or a binary-only layout-selection rule.

## Event records

The event region is `[start, end)`, using the big-endian pointers at
`0x2C` and `0x30`. One record is one CSV event row. Records are packed,
fixed-size within each sample, with no separate delimiter or record-length
field. Names and descriptions are not inline.

| File | Subtype | Records | Bytes per record | Event-region bytes |
| --- | --- | ---: | ---: | ---: |
| `profiling_2.pd` | `0x03` | 5,000 | 16 | 80,000 |
| `profiling_3.pd` | `0x00` | 50,000 | 20 | 1,000,000 |
| `profiling_4.pd` | `0x00` | 500,000 | 20 | 10,000,000 |
| `profiling_5.pd` | `0x00` | 150,000 | 120 | 18,000,000 |
| `profiling_6.pd` | `0x00` | 500,000 | 20 | 10,000,000 |
| `profiling_7.pd` | `0x00` | 10,000 | 20 | 200,000 |
| `profiling_8.pd` | `0x00` | 10,000 | 20 | 200,000 |
| `profiling_9.pd` | `0x00` | 9,375 | 32 | 300,000 |

### Packed structure

All known fields are unsigned little-endian integers:

| Record offset | Size | Observed field |
| --- | ---: | --- |
| `0x00` | 8 | Tick counter |
| `0x08` | 4 | Event code; CSV `Event` |
| `0x0C` | 4 | Object identifier; CSV `Object Ident` |
| `0x10` | 4 | CPU core; subtype `0x00` only; CSV `CPU Core` |

| Variant | Python `struct` format | Size |
| --- | --- | ---: |
| Subtype `0x03`, file 2 | `<QII` | 16 bytes |
| Subtype `0x00`, files 3-4 and 6-8 | `<QIII` | 20 bytes |
| Subtype `0x00`, file 5 | `<QIII100x` | 120 bytes |
| Subtype `0x00`, file 9 | `<QIII12x` | 32 bytes |

File 2 has no CPU-core field and exports `-` in that CSV column. File 5's
extra 100 bytes at record offsets `0x14`-`0x77` are zero in every inspected
record. File 9's 12 extra bytes at offsets `0x14`-`0x1F` are likewise
zero in all 9,375 records. Its CSV `Additional Data (hex)` cells are empty,
as are those of files 7 and 8. The `100x` and `12x` skip these areas;
they do not prove that all skipped bytes are semantic padding or distinguish
requested payload bytes from alignment bytes.
The configuration additional-byte field, not subtype alone, selects stride
for these samples.

Physical record `i` occupies `[start + i * size, start + (i + 1) * size)`;
the record count is `(end - start) / size`. Physical and chronological
indexes need not coincide.

### File 2 ordering and validation

File 2 has a single physical counter decrease, consistent with a wrapped
circular buffer. First chronological index is 2,337, absolute offset
`0xDD14`. Rotating at that index or sorting by unsigned counter reproduces
all 5,000 CSV event-code/object-ID pairs with zero mismatches.
The first chronological event is `0x01000000`, object `0x4AD60EB0`
(interrupt 18 in the CSV).

### Updated file 6 validation

The updated file is 10,097,728 bytes long, matching header `0x0E`. Its
event region `[0x496C, 0x98DFEC)` contains 10,000,000 bytes and 500,000
occupied 20-byte records. No slot is entirely zero. The updated CSV also
contains 500,000 events; the earlier, shorter export is not used here.

Counters are nondecreasing in physical order without wrap. Direct CSV
comparison gives zero event-code/object-ID/core mismatches across all rows;
every core is 0. First/last counters are 57,856,765,840 and 59,419,046,106.
The relative span is 156,228,026.6 microseconds: exactly 10 ticks per
microsecond. Every row confirms `(counter - first_counter) / 10` exactly.

Of 25 name/ID pairs, eight match A and one matches B. The B entry is
`WINDOWS`, name at `0x143C`, ID `0x00000001` at `0x1418`. The other 16
pairs are `Cyclic #1` through `Cyclic #8`, each with two IDs; their literal
names were not found. No located-name/ID mismatch remains.

### Files 7-9 validation

| File | File size | Event region, end exclusive | First counter | Last counter | Relative span (us) |
| --- | ---: | --- | ---: | ---: | ---: |
| `profiling_7.pd` | 213,976 | `[0x2FE8, 0x33D28)` | 145,412,761,714 | 145,442,685,709 | 2,992,399.5 |
| `profiling_8.pd` | 213,976 | `[0x2FE8, 0x33D28)` | 148,697,794,262 | 148,727,729,319 | 2,993,505.7 |
| `profiling_9.pd` | 314,764 | `[0x2FE8, 0x4C3C8)` | 151,404,652,255 | 151,432,746,108 | 2,809,385.3 |

Each size matches header `0x0E`. All stored slots are occupied; no slot
is entirely zero. Counters are nondecreasing in physical order without
wrap, and every core is 0. All 29,375 CSV events match the binary
event-code/object-ID/core fields at configuration-derived strides.
Both relative and absolute CSV times match exactly using 10 ticks per
microsecond, checked with decimal arithmetic rather than float tolerance.

Each capture has 25 CSV name/ID pairs: eight match layout A, one matches
layout B, and 16 have no literal name before the event region. No located
name has an unmatched ID. This repeats file 6's aggregate mapping results.
All three captures contain the same 16 event codes as updated file 6;
none introduces a new code or event family relative to files 2-6.

The CSV preambles for files 8 and 9 name `profiler.pd`, rather than the
numbered binary filenames. Pairing here is verified by all event rows and
timestamps, not by the preamble filename. The corresponding `.state`
files store XML viewer state (columns, selection, and graph bounds), not
capture-buffer settings; their `FileVersion="5.0"` is not evidence of a
5.x profiler application version.

## Counter and CSV time conversion

Let `F` be the little-endian kHz value at `M + 0x14`, `T` an unsigned
counter, and `T0` the first chronological counter selected using `M + 0x0C`:

```text
ticks_per_microsecond = F / 1000
relative_time_us = (T - T0) * 1000 / F
absolute_time_us = T * 1000 / F
```

CSV absolute time behaves as a scaled counter, not the capture date plus
elapsed time. Its epoch is unknown. Every event was checked using metadata
ring indexes and configuration-derived strides:

| File | Rows checked | Event/ID/core mismatches | Maximum relative error (us) | Maximum absolute error (us) |
| --- | ---: | ---: | ---: | ---: |
| `profiling_2.pd` | 5,000 | 0 | < 0.002632 | < 0.404518 |
| `profiling_3.pd` | 50,000 | 0 | < 0.000483 | < 0.000483 |
| `profiling_4.pd` | 500,000 | 0 | < 0.000501 | < 0.000501 |
| `profiling_5.pd` | 150,000 | 0 | < 0.000501 | < 0.000505 |
| `profiling_6.pd` | 500,000 | 0 | 0 | 0 |
| `profiling_7.pd` | 10,000 | 0 | 0 | 0 |
| `profiling_8.pd` | 10,000 | 0 | 0 | 0 |
| `profiling_9.pd` | 9,375 | 0 | 0 | 0 |

Core comparisons apply only to subtype `0x00`. Files 6-9's 10,000 kHz field
explains the exact 10-tick conversion. Files 3-5 agree within three-decimal
CSV rounding, allowing small floating-point effects. File 2 does not: its
stored/reported 2416.666 MHz needs additional precision or conversion details
to reproduce the CSV exactly. Testing `7250/3 MHz` did not resolve this.
Do not treat file 2's reported frequency as an exact constant or these
formulas as a universal specification for unobserved variants.

## Events and their meaning

The event code at record offset `0x08` is an unsigned little-endian 32-bit
integer matching CSV `Event`. Meanings are derived from CSV descriptions,
not a complete dictionary for all profiler versions. Files 2-9 contain
282 distinct codes in total. Hexadecimal prefixes below refer to decoded
integers, not first stored bytes. Not every listed code occurs in every
6.x sample.

### Scheduler switches

Codes `0x00xxxxss` describe `'<incoming>' is now running - '<outgoing>'
was <state>`. CSV `Name` and `Object Ident` identify the incoming object;
the outgoing name is in the description, not a separate known record field.

| Low byte `ss` | Outgoing task state |
| --- | --- |
| `0x00` | ready: runnable but no longer running, potentially preempted |
| `0x01` | suspended |
| `0x02` | waiting for a resource or event |
| `0x04` | delayed |
| `0x06` | delayed and waiting |

Middle bytes `xxxx` remain undecoded; preserve them.
A ready-state switch does not alone prove higher-priority preemption.

Updated file 6 contains 16 distinct codes. Fifteen were already present
in files 1-5; the new `0x00414100` occurs 14,988 times and describes a
ready-state switch. All its codes belong to scheduler, cyclic-task
start/finish, and task-class phase families, not a new event family.

### Execution and lifecycle events

| Code | Observed meaning |
| --- | --- |
| `0x01000000` / `0x01000001` | Interrupt handler started / finished |
| `0x02000000` / `0x02000001` | Cyclic task started / finished |
| `0x02000002` / `0x02000003` | Init program started / finished |
| `0x02000004` / `0x02000005` | Exit program started / finished |
| `0x11000000` / `0x11000001` | Task created / deleted |

Started/finished intervals need not be uninterrupted CPU execution:
scheduler switches and interrupts can intervene. Capture boundaries can
leave a start or finish without its counterpart.

### Task-class and program phases

| Code | Observed meaning |
| --- | --- |
| `0x1E000000` | Task class started |
| `0x1E000001` | Input scheduler of task class finished |
| `0x1E000002` | End of cyclic programs in task class |
| `0x1E000003` | Output scheduler of task class started |
| `0x1E000004` | Output scheduler of task class finished |
| `0x1B000000` | Init program started |
| `0x1B000001` | Input scheduler of init program finished |
| `0x1B000002` | End of cyclic programs in init program |
| `0x1B000004` | Output scheduler of init program finished |
| `0x1C000000` | Exit program started |
| `0x1C000002` | End of cyclic programs in exit program |

Task-class phases differ from individual cyclic-task execution. Init/exit
phase codes were observed only in file 4; missing codes are not inferred.

### Diagnostics and user events

| Code or family | Meaning and limits in the 6.x evidence |
| --- | --- |
| `0x12000098`, `0x12000099`, `0x1200009B` | System Exception; subcodes unresolved |
| `0x1300000E` | Processor Exception; cause unresolved |
| `0x14xxxxxx` | AR Logger Event; lower fields undecoded |
| `0x15000000` | System Event; no further meaning supplied |
| `0x1Fxxxxxx` | User-event family |

The separate tolerance code `0x15000003` was observed in the 4.x file 1,
not established here as a 6.x observation.
In these samples, `0x1F000100`, `0x1F000200`, and `0x1F000D00`
mean user event started; `0x1F00F101` means finished. Other observed user
codes are labelled `Non calculateable user event entry`. Payload and timing
semantics are unresolved. Do not infer start/finish from low-byte parity;
retain unknown numeric codes.

## Remaining unknowns

- Complete object tables, entry-layout selection, priority and other entry
  fields, identifier namespaces, and unmatched object-name mappings.
- Scheduler middle bytes, exception subcodes, user-event payloads, and
  meanings beyond observed CSV descriptions.
- Exact file-2 time conversion, counter epoch, and capture-date timezone.
- Remaining header, capture-configuration, and metadata fields, binary
  known-object counts and profiler application versions.
- Independent 6.x confirmation of the two task-buffer field assignments
  using unequal settings; the supplied 6.x settings are always equal,
  while the individual assignment is distinguished by 4.x file 10.
- Trailer structures referenced by `0x34` and `0x38`.
- File-5 and file-9 extra-area semantics, exact alignment/allocation rules
  behind file 9's requested/stored size difference, and unobserved layouts.
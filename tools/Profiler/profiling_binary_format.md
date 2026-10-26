# B&R Profiling Binary Formats

The binary-format descriptions are separated by the profiler application
version reported in the corresponding `information_<n>.txt` file:

| Profiler version | Evidence | Format description |
| --- | --- | --- |
| 4.x (`4.00.2`) | `profiling_1.pd` and `profiling_10.pd`, their CSV exports and information reports | [Profiling 4.x binary format](profiling_binary_format_4x.md) |
| 6.x (`6.0.0.0`, `6.1.0.0`) | `profiling_2.pd` through `profiling_9.pd` and `profiling_11.pd`, their CSV exports and information reports | [Profiling 6.x binary format](profiling_binary_format_6x.md) |

Profiler application versions are distinct from Automation Runtime versions.
The profiler-version field in the binary has not yet been identified; use
the information reports to classify these samples. The module subtype is
not a profiler-major-version discriminator: subtype `0x03` occurs in both
the 4.x file 1 and the 6.x file 2. File 10 uses subtype `0x00` but retains
16-byte records without a core field, unlike the supplied subtype-`0x00`
6.x captures. It also lacks the XML wrapper present in files 1-9. Follow
section pointers and validate layout rather than assuming fixed offsets or
selecting record stride from subtype alone.

File 11 confirms the 6.x 32-byte layout on target `1A4000.00` running
Automation Runtime `6.8.1`: 20 base bytes plus 12 stored additional bytes,
despite 10 requested additional bytes. Its new scheduler codes are described
in the 6.x specification; they do not introduce a new record layout.
# B&R Network Command Trace Binary Format

## Scope and evidence

This document describes observations made directly from these files:

| Binary file | ASCII reference file |
| --- | --- |
| `nwcmdtrace1.br` | `NetworkCommandTrace1.txt` |
| `nwcmdtrace2.br` | `NetworkCommandTrace2.txt` |
| `nwcmdtrace3.br` | `NetworkCommandTrace3.txt` |

The conclusions below are limited to these three samples. Fields marked
**observed** matched all applicable samples. Fields marked **tentative** are
based on only one sample or do not have enough examples to establish a general
rule. This document does not assume that every field in the ASCII output can be
reconstructed from the binary record alone.

## B&R module container

All offsets in this section are absolute file offsets. Multi-byte container
header values are big-endian unless stated otherwise.

| Offset | Size | Observed meaning |
| --- | ---: | --- |
| `0x00` | 2 | Module signature `0x2B97` |
| `0x02` | 1 | Module type `0x46` in all samples |
| `0x03` | 1 | Module subtype `0x02` in all samples |
| `0x0E` | 4 | Total file size in bytes |
| `0x20` | 4 | Pointer to a 40-byte region immediately preceding the data area |
| `0x24` | 4 | Data-start address |
| `0x28` | 4 | Duplicate of the data-start address |
| `0x2C` | 4 | Data-end address (exclusive) |

The region pointed to by `0x20` ends at `data_start`. Its byte at offset `+29`
is `0x80` in all three samples. The two bytes at region offset `+36` decode as
the displayed module revision when read as a big-endian unsigned 16-bit value:

```text
revision = hex(u16_be(region[36:38])) formatted as H,HHH
```

This yields `5,313`, `5,062`, and `5,310`, matching the reference headers.

| Sample | Region start | Data start | Data end | Bytes after data end |
| --- | ---: | ---: | ---: | ---: |
| 1 | `0x30` | `0x58` | `0x7694` | 240 |
| 2 | `0x30` | `0x58` | `0x424AC` | 2,140 |
| 3 | `0x3C` | `0x64` | `0x185984` | 316,320 |

The bytes after `data_end` are outside the trace data area. They vary in size
and must not be included when locating the records.

## Trace data area

`data` is the half-open file range `[data_start, data_end)`. Its first 12 bytes
are the ASCII signature `MTrcBinDat01` in every sample. The data-start offsets
observed are `0x58` for samples 1 and 2 and `0x64` for sample 3; these
correspond to the reference versions `2,0` and `3,0` respectively.

The reference header provides `RECCNT`. With that value, all three samples
confirm that the fixed-size record array begins at:

```text
record_start = data_end - RECCNT * 20
```

| Sample | RECCNT | Record start (file offset) | Record start relative to data |
| --- | ---: | ---: | ---: |
| 1 | 1,500 | `0x164` | `0x10C` |
| 2 | 13,500 | `0x5FC` | `0x5A4` |
| 3 | 79,500 | `0x1694` | `0x1630` |

For a binary-only parser, `RECCNT` and the record start must be found together:
scan aligned candidate metadata positions, derive a candidate record start,
and accept it only when the record array ends exactly at `data_end`, its length
is divisible by 20, and the metadata capacity equals that record count. The
ASCII header is useful as independent validation, not as a required binary
field.

## Ring metadata

Metadata is immediately before `record_start`. Metadata integers are
little-endian in the observed samples.

### Version 2 (`data_start == 0x58`)

At `record_start - 0x10`, a little-endian 32-bit word contains:

```text
bits 31..16: RECCNT
bits 15..0:  NEXTREC
```

At `record_start - 0x0C`, `RINGBUFIDX` is the high 16 bits of the next
little-endian 32-bit word. The low 16 bits were `0x0700` in both V2 samples;
their meaning is unknown.

### Version 3 (`data_start == 0x64`)

The three little-endian 32-bit words immediately before the records are:

| Relative offset | Field |
| --- | --- |
| `record_start - 0x0C` | `NEXTREC` |
| `record_start - 0x08` | `RECCNT` |
| `record_start - 0x04` | `RINGBUFIDX` |

This layout is observed in sample 3 only.

### Values confirmed against the references

| Sample | Version | RECCNT | NEXTREC | RINGBUFIDX | FIRSTREC | LASTREC |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 2,0 | 1,500 | 1,135 | 326 | 326 | 1,134 |
| 2 | 2,0 | 13,500 | 2,255 | 1,875 | 2,255 | 2,254 |
| 3 | 3,0 | 79,500 | 16,406 | 87 | 87 | 16,405 |

`LASTREC` agrees with `(NEXTREC - 1) modulo RECCNT` in all samples.
`FIRSTREC` equals `RINGBUFIDX` in the two partially filled samples and equals
`NEXTREC` in the full sample. This rule is an observation from these files,
not yet a general statement for every trace version.

## Record layout

Each record is exactly 20 bytes. The following layout matches every inspected
record and the raw `Frame-data` bytes in the ASCII references:

| Record offset | Size | Type | Meaning |
| --- | ---: | --- | --- |
| `+0` | 4 | unsigned little-endian 32-bit | Timestamp counter, in microseconds |
| `+4` | 4 | unsigned little-endian 32-bit | Network ID |
| `+8` | 12 | byte array | Raw frame |

The raw frame can be split as follows:

| Frame offset | Size | Observed content |
| --- | ---: | --- |
| `+0` | 2 | Little-endian frame/parameter identifier |
| `+2` | 10 | Payload bytes |

The first two frame bytes agree with the first parameter ID in ordinary
reference rows. However, some frames expand to multiple ASCII parameter rows;
the expanded rows can have different parameter IDs while repeating the same
raw frame. Therefore, the 16-bit frame identifier is not sufficient to
reconstruct every ASCII `Parameter-Id`.

`Frame-data` in the references displays the 12 frame bytes as 20 hex digits,
a space, two hex digits, a space, and two hex digits. No byte reordering is
needed.

## Record slots and ordering

The records are physically stored in slots `0 .. RECCNT-1`.

In samples 1 and 3, timestamps are nonzero in slots `0 .. NEXTREC-1` and zero
from `NEXTREC` onward. The ASCII references contain those `NEXTREC` records in
ascending slot order.

In sample 2, all 13,500 slots have nonzero timestamps, including the slot at
`NEXTREC`. The reference contains every slot once, but its distinct
`Recordindex` order is:

```text
0 .. RINGBUFIDX-1,
NEXTREC .. RECCNT-1,
RINGBUFIDX .. NEXTREC-1
```

This ordering exactly matches sample 2. Its generalization to other full-ring
traces is tentative because only one full sample is available.

The reference can contain several ASCII rows with the same `Recordindex`.
Those rows repeat the same binary frame and represent higher-level decoding,
not additional 20-byte records. The unique reference record counts are 1,135,
13,500, and 16,406 for samples 1, 2, and 3; the corresponding ASCII row counts
are 1,301, 32,857, and 17,964.

## Timestamp comparison

The first binary timestamp in each sample equals the ASCII `Time` value in
seconds multiplied by one million, plus 10 microseconds. Across all records,
the observed difference between the binary timestamp and the rounded ASCII
time ranges from 0 to 11 microseconds. A constant correction is therefore not
supported by the samples.

The binary timestamp is 32 bits. In sample 1, values pass from about 4.0
billion to a few hundred million while the records continue, which is
consistent with a wrapping counter. The ASCII references also contain values
on both sides of that wrap. No epoch or wrap-count field has been identified.

## ASCII projection observed in the references

The following network-ID-to-node families match all 326 unique `PLK[0]` IDs
in the three references. They are empirical mappings; only the ranges actually
present in the samples have been validated.

| Network-ID range or value | Node formula |
| --- | --- |
| `1000254..1000428` | `network_id - 1000253` |
| `1001286..1001985` | `(network_id - 1001282) // 4` |
| `1002414..1003113` | `(network_id - 1002410) // 4` |
| `1006000..1006255` | `network_id - 1006000` |
| `1006338..1006430` | `network_id - 1006254` |
| `1006509` | `1` (single observed ID) |

All other observed IDs were `6000`, named `NCMAN` with node 0. These mappings
are preferable to classifying only `1006000..1006255` as `PLK[0]`: for example,
`1002416` maps to `PLK[0]`, node 1. IDs outside these observed families remain
unclassified by this evidence.

The raw records alone do not establish complete rules for these reference
The reference `Type` field is consistently determined by observed network-ID
families:

| Network-ID family | Type |
| --- | --- |
| `6000`, `1006000..1006255`, `1006338..1006430` | `MAN_INF` |
| `1000254..1000428` | `STATE` |
| `1001282..1001985`, `1002410..1003113` | By `(network_id - family_base) mod 4`: `WR_REQ`, `WR_RSP`, `RD_REQ`, `RD_RSP` |
| `1006509` | `PAR_SEQ` |

These rules classify every reference row in the three samples. They do not
claim that unobserved IDs belong to the same families.

The references contain 339 unique parameter IDs and 339 unique descriptions.
The ACOPOS parameter names and IEC data types come from `acp10par.py`. The
trace exporter uses those database entries for parameter names and scalar
decoding, with a small fallback for network/runtime IDs not present in that
database and trace-specific formatting overrides. The mappings are validated
against the supplied references; a parameter ID may have additional behavior
outside these samples.

The ASCII files are not a one-record/one-row dump. A binary record can expand
to multiple parameter rows, each repeating the same index, type, network, time,
and raw frame. The implemented templates cover the composite frame IDs
observed in these samples; they are not a complete protocol definition.

The last empty TSV field is not serialized uniformly. In these references an
empty `Value` field retains its final tab for `MAN_INF`, `WR_REQ`, and
`RD_RSP`, and for `WR_RSP` parameter ID `65535`. For `RD_REQ` and other
`WR_RSP` rows, the trailing empty field is omitted. Matching this convention
is necessary to reproduce the original text-file lengths.

The two date/time parameters `TARGET_DATE_TIME` (`65398`) and `BRMOD_DATE_TIME`
(`1011`) remain unresolved. Their raw payloads do not match ordinary integer,
float, or Unix-time interpretations. The exported ASCII `Time` values also
differ from the binary timestamp by 0..11 microseconds in these samples; the
binary timestamps are preserved rather than adjusted by an unsupported fixed
offset.

The reference header says `COLS=9`, while its tab-separated column header and
non-empty data rows contain 10 fields. Preserve the observed header value
rather than assuming it is the number of tab-separated fields.

## Parsing checks

A parser for these samples should verify at least:

1. Module signature, type, and subtype match the observed values.
2. `data_start` and `data_end` lie within the file and `data_start < data_end`.
3. The 12-byte signature at `data_start` is `MTrcBinDat01`.
4. `record_start + RECCNT * 20 == data_end`.
5. Each metadata candidate has a valid capacity and in-range ring indexes.
6. Parsing all slots reproduces the 12 raw frame bytes shown for matching
   `Recordindex` values in the reference.

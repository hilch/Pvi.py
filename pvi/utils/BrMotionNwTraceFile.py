#
# Pvi.py
# Python connector for B&R Pvi (process visualization interface)
#
#  https://github.com/hilch/Pvi.py
# Permission is hereby granted, free of charge,
# to any person obtaining a copy of this software and associated documentation files (the 'Software'),
# to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import struct
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP, localcontext
from typing import List, Optional, Tuple
from pvi.utils.BrFile import *
from pvi.utils.acp10par import ACP10PAR

_MAGIC          = b'MTrcBinDat01'
_RECORD_SIZE    = 20


# Parameter IDs rendered as hexadecimal; values specify payload width in bytes.
_TRACE_HEX_WIDTHS = {
    1010: 2, 10288: 2, 65431: 2, 65432: 2, 65465: 2,
    65472: 1, 65473: 1, 65476: 1,
}
# Parameter IDs rendered as byte-grouped bit strings instead of numeric values.
_BIT_FIELD_IDS = frozenset({178, 179, 1126, 727, 184, 185, 186, 583})
# Parameter IDs whose trace rows intentionally omit values.
_EMPTY_VALUE_IDS = frozenset({
    389, 402, 403, 544, 1171, 65535,
})
_SIGNED_WIDTHS = {'SINT': 1, 'INT': 2, 'DINT': 4}
_UNSIGNED_WIDTHS = {'USINT': 1, 'UINT': 2, 'UDINT': 4}
_TRACE_UNSIGNED_WIDTHS = {10257: 1}


@dataclass
class NwCmdRecord:
    "Single record from nwcmdtrace.log (20 bytes)"
    index:        int
    timestamp_us: int
    network_id:   int
    frame_data:   bytes
    param_id:     int

    @property
    def time_seconds(self) -> float:
        return self.timestamp_us / 1_000_000

    def _plk_node(self) -> Optional[int]:
        network_id = self.network_id
        if 1000254 <= network_id <= 1000428:
            return network_id - 1000253
        if 1001286 <= network_id <= 1001985:
            return (network_id - 1001282) // 4
        if 1002414 <= network_id <= 1003113:
            return (network_id - 1002410) // 4
        if 1006000 <= network_id <= 1006255:
            return network_id - 1006000
        if 1006338 <= network_id <= 1006430:
            return network_id - 1006254
        if network_id == 1006509:
            return 1
        return None

    @property
    def message_type(self) -> Optional[str]:
        network_id = self.network_id
        if network_id == 6000 or 1006000 <= network_id <= 1006255:
            return 'MAN_INF'
        if 1006338 <= network_id <= 1006430:
            return 'MAN_INF'
        if 1000254 <= network_id <= 1000428:
            return 'STATE'
        for base in (1001282, 1002410):
            offset = network_id - base
            if 0 <= offset <= 703:
                return ('WR_REQ', 'WR_RSP', 'RD_REQ', 'RD_RSP')[offset % 4]
        if network_id == 1006509:
            return 'PAR_SEQ'
        return None

    @property
    def network_name(self) -> str:
        if self.network_id == 6000:
            return 'NCMAN'
        if self._plk_node() is not None:
            return 'PLK[0]'
        return f'NET[{self.network_id}]'

    @property
    def node(self) -> int:
        if self.network_id == 6000:
            return 0
        return self._plk_node() or 0

    @property
    def frame_hex(self) -> str:
        return self.frame_data.hex().upper()

    @property
    def frame_display(self) -> str:
        h = self.frame_hex
        return f'{h[:20]} {h[20:22]} {h[22:24]}'

    @property
    def value_bytes(self) -> bytes:
        return self.frame_data[2:]

    def _parameter_definition(self) -> Optional[ACP10PAR]:
        try:
            return ACP10PAR(self.param_id)
        except ValueError:
            return None

    @property
    def parameter_name(self) -> str:
        definition = self._parameter_definition()
        if definition is None:
            return ''

        instance_suffix = f'_INSTANCE_{definition.instance_number}'
        if definition.instance_number and definition.name.endswith(instance_suffix):
            base_name = definition.name[:-len(instance_suffix)]
            return f'{base_name}+{definition.instance_number}'
        if ACP10PAR(self.param_id).function_block:
            return f'{definition.name}+{ACP10PAR(self.param_id).instance_number}'
        return definition.name

    def decode_value(self) -> str:
        vb = self.value_bytes
        definition = self._parameter_definition()
        data_type = definition.data_type if definition is not None else ''
        if (self.message_type == 'RD_REQ' or self.param_id in _EMPTY_VALUE_IDS
                or data_type == 'NIL'):
            return ''
        if self.message_type == 'WR_RSP' and self.param_id not in (180, 181):
            return ''
        if data_type.startswith('STR'):
            return vb.split(b'\0', 1)[0].decode('ascii', errors='replace').replace('.', ',')
        if data_type == 'BYTES6':
            size = 6
            return ' '.join(f'{value:02X}' for value in vb[:size])
        if self.param_id in _BIT_FIELD_IDS:
            size = _UNSIGNED_WIDTHS[data_type]
            value = int.from_bytes(vb[:size], 'little')
            bits = f'{value:0{size * 8}b}'
            return ' '.join(bits[i:i + 8] for i in range(0, len(bits), 8))
        if data_type == 'REAL':
            value = struct.unpack_from('<f', vb)[0]
            if value == 0:
                return '0'
            with localcontext() as context:
                context.rounding = ROUND_HALF_UP
                decimal_value = Decimal.from_float(value)
                exponent = decimal_value.adjusted()
                quantum = Decimal(1).scaleb(exponent - 5)
                rounded = decimal_value.quantize(quantum)
                if exponent < -4 or exponent >= 6:
                    mantissa = format(rounded.scaleb(-exponent), 'f').rstrip('0').rstrip('.')
                    exponent_text = f'{exponent:+03d}'
                    formatted = f'{mantissa}e{exponent_text}'
                else:
                    formatted = format(rounded, 'f')
                    if '.' in formatted:
                        formatted = formatted.rstrip('0').rstrip('.')
                return formatted.replace('.', ',')
        if self.param_id in _TRACE_HEX_WIDTHS:
            size = _TRACE_HEX_WIDTHS[self.param_id]
            value = int.from_bytes(vb[:size], 'little')
            return f'0x{value:0{size * 2}X}'
        if data_type in _SIGNED_WIDTHS:
            size = _SIGNED_WIDTHS[data_type]
            return str(int.from_bytes(vb[:size], 'little', signed=True))
        if data_type in _UNSIGNED_WIDTHS:
            size = _UNSIGNED_WIDTHS[data_type]
            return str(int.from_bytes(vb[:size], 'little'))
        if self.param_id in _TRACE_UNSIGNED_WIDTHS:
            size = _TRACE_UNSIGNED_WIDTHS[self.param_id]
            return str(int.from_bytes(vb[:size], 'little'))
        v32 = struct.unpack_from('<I', vb)[0]
        return str(v32)

    def decoded_rows(self) -> List[Tuple[int, str, str]]:
        "Return decoded parameter rows (parameter ID, description, value)."
        frame = self.frame_data

        def u16(offset: int) -> int:
            return struct.unpack_from('<H', frame, offset)[0]

        def i32(offset: int) -> int:
            return struct.unpack_from('<i', frame, offset)[0]

        def float32(offset: int) -> str:
            value = struct.unpack_from('<f', frame, offset)[0]
            return format(value, '.6g').replace('.', ',')

        def hex16(offset: int) -> str:
            return f'0x{u16(offset):04X}'

        frame_id = frame[:2]
        is_response = self.message_type in ('WR_RSP', 'RD_RSP')
        if frame_id == b'\xD1\xFF':
            return [(65489, 'NC_ACTION_MotionComp', ''),
                    (65493, 'subject', str(u16(2))),
                    (65494, 'action', hex16(4))]
        if frame_id == b'\xD3\xFF':
            return [(65491, 'NC_ACTION_PLCopen_MC', ''),
                    (65495, 'PLCopen_FB', str(u16(2))),
                    (65493, 'subject', str(u16(4))),
                    (65494, 'action', hex16(6))]
        if frame_id == b'\xBE\xFF':
            return [(65470, 'PLCopen_FB_Error', ''),
                    (65495, 'PLCopen_FB', str(u16(2))),
                    (65468, 'ErrorID', str(u16(4)))]
        if frame_id == b'\xBF\xFF':
            return [(65471, 'PLCopen_FB_Aborted', ''),
                    (65495, 'PLCopen_FB', str(u16(2))),
                    (65469, 'Aborted_by', str(u16(4)))]
        if frame_id == b'\x79\xFF':
            return [(65401, 'McCmd', ''),
                    (65437, 'McCommand', hex16(2)),
                    (65399, 'McFacility', hex16(4))]
        is_error_record = frame_id == b'\xB7\x00' and self.message_type in ('RD_RSP', 'MAN_INF')
        is_error_response = frame_id == b'\xFF\xFF' and self.message_type == 'WR_RSP'
        if is_error_record or is_error_response:
            header_id = 183 if is_error_record else 65535
            header_name = 'ERROR_REC' if header_id == 183 else 'ERROR_RESPONSE'
            return [(header_id, header_name, ''),
                    (180, 'ERROR_NUMBER', str(u16(2))),
                    (181, 'ERROR_INFO', str(i32(4)))]
        if frame_id in (b'\x92\x01', b'\x93\x01'):
            positive = frame_id == b'\x92\x01'
            command_id, value_id = (402, 404) if positive else (403, 405)
            command = 'CMD_POS_MOVE_VAX1' if positive else 'CMD_NEG_MOVE_VAX1'
            value_name = 'BASIS_MOVE_V_POS_VAX1' if positive else 'BASIS_MOVE_V_NEG_VAX1'
            value = '' if is_response else float32(2)
            return [(command_id, command, ''), (value_id, value_name, value)]
        if frame_id == b'\x74\x00':
            value = '' if is_response else str(u16(2))
            acceleration = '' if is_response else str(u16(4))
            return [(116, 'OVERRIDE', ''),
                    (117, 'V_OVERRIDE', value),
                    (118, 'A_OVERRIDE', acceleration)]
        if frame_id == b'\xA7\x00':
            values = ('', '', '', '') if is_response else (
                '', str(i32(2)), str(frame[6]), f'{frame[7]:08b}')
            return [(167, 'CMD_HOMING', values[0]),
                    (152, 'HOMING_S', values[1]),
                    (156, 'HOMING_MODE', values[2]),
                    (157, 'HOMING_MODE_BITS', values[3])]
        if frame_id == b'\xA9\x00':
            value = '' if is_response else float32(2)
            mode = '' if is_response else str(u16(6))
            return [(169, 'CMD_POS_MOVE', ''),
                    (161, 'BASIS_MOVE_V_POS', value),
                    (419, 'BASIS_MOVE_MODE', mode)]
        if frame_id == b'\xB0\x00':
            value = '' if is_response else str(u16(6))
            return [(176, 'CMD_MOVEMENT_STOP', ''),
                    (171, 'STOP_CMD_CONF_INDEX', value)]
        if frame_id == b'\x20\x02':
            index = '' if is_response else str(u16(2))
            sequence = '' if is_response else str(u16(4))
            return [(544, 'PAR_SEQU_INDEX_DATA', ''),
                    (751, 'PAR_SEQU_INDEX', index),
                    (750, 'PAR_SEQU', sequence)]
        return [(self.param_id,
            self.parameter_name,
             self.decode_value())]


class BrMotionNwTraceFile(BrFile):
    'class for a *.br file containing data object'
    def __init__(self, filename: str):
        super().__init__(filename)
        if self._fileType != ModuleType.MOTION_DATA_OBJECT or self._subType != 0x02:
            raise TypeError(f'content is not a B&R NwTrace module (Type is {self._fileType})')
        self._data_start_address = struct.unpack_from('>L', self._content, 0x24)[0]
        self._data_end_address = struct.unpack_from('>L', self._content, 0x2c)[0]
        if self.data[:12] != _MAGIC:
            raise TypeError(f'B&R NwTrace module: Magic string not found.')

        # Auto-detect format version from data_start_address offset
        if self._data_start_address == 0x58:
            self._format_version = '2.0'
        elif self._data_start_address == 0x64:
            self._format_version = '3.0'
        else:
            raise ValueError(
                f'Unknown file format: data_start_address=0x{self._data_start_address:04x} '
                f'(expected 0x0058 for V2.0 or 0x0064 for V3.0)'
            )

        self._find_ring_buffer_metadata()
 

    @property
    def data(self) -> bytes:
        return self._content[self._data_start_address:self._data_end_address]


    def _find_ring_buffer_metadata(self) -> None:
        "Locate RECCNT, NEXTREC, FIRSTREC by scanning content region"
        best_reccnt = 0
        best = {}

        content_len = len(self.data)
        search_start = 64
        search_end   = content_len - _RECORD_SIZE

        if self._format_version == '2.0':
            # V2.0: Packed metadata at (rec_start - 0x10): (RECCNT<<16)|NEXTREC
            for probe in range(search_start, search_end, 4):
                packed = struct.unpack_from('<I', self.data, probe)[0]
                reccnt_cand  = (packed >> 16) & 0xFFFF
                nextrec_cand = packed & 0xFFFF
                if reccnt_cand == 0 or nextrec_cand >= reccnt_cand:
                    continue
                rs = probe + 0x10  # rec_start in content region
                if rs < 0 or rs > content_len:
                    continue
                rem = content_len - rs
                if rem > 0 and rem % _RECORD_SIZE == 0 and rem // _RECORD_SIZE == reccnt_cand:
                    if reccnt_cand > best_reccnt:
                        p2 = struct.unpack_from('<I', self.data, rs - 0x0C)[0]
                        ringbufidx = (p2 >> 16) & 0xFFFF
                        if ringbufidx >= reccnt_cand:
                            continue
                        best_reccnt = reccnt_cand
                        best = {
                            'rec_start':  rs,
                            'reccnt':     reccnt_cand,
                            'nextrec':    nextrec_cand,
                            'ringbufidx': ringbufidx,
                        }
        else:
            # V3.0: Separate metadata at (rec_start - 0x0C/0x08/0x04)
            for probe in range(search_start + 8, search_end, 4):
                reccnt_cand = struct.unpack_from('<I', self.data, probe)[0]
                if reccnt_cand == 0:
                    continue
                rs = probe + 8  # rec_start in content region
                if rs < 0 or rs > content_len:
                    continue
                rem = content_len - rs
                if rem > 0 and rem % _RECORD_SIZE == 0 and rem // _RECORD_SIZE == reccnt_cand:
                    if reccnt_cand > best_reccnt:
                        nextrec_cand = struct.unpack_from('<I', self.data, rs - 0x0C)[0]
                        ringbufidx_cand = struct.unpack_from('<I', self.data, rs - 0x04)[0]
                        if nextrec_cand >= reccnt_cand or ringbufidx_cand >= reccnt_cand:
                            continue
                        best_reccnt = reccnt_cand
                        best = {
                            'rec_start':  rs,
                            'reccnt':     reccnt_cand,
                            'nextrec':    nextrec_cand,
                            'ringbufidx': ringbufidx_cand,
                        }

        if not best:
            raise ValueError('Could not locate ring-buffer metadata in content region')

        self._rec_start  = best['rec_start']
        self._reccnt     = best['reccnt']
        self._nextrec    = best['nextrec']
        self._ringbufidx = best['ringbufidx']

    @property
    def format_version(self) -> str:
        "Format version: '2.0' or '3.0' (auto-detected)"
        return self._format_version

    @property
    def manid(self) -> int:
        "Module ID derived from region @ 0x20 (offset +29 or -11)"
        region_start = struct.unpack_from('>I', self._content, 0x20)[0]
        region = self._content[region_start : self._data_start_address]
        return region[29]  # or region[-11]

    @property
    def reccnt(self) -> int:
        "Ring-buffer capacity"
        return self._reccnt

    @property
    def nextrec(self) -> int:
        "Next write slot"
        return self._nextrec

    @property
    def firstrec(self) -> int:
        "Oldest record slot reported by the trace ring buffer"
        if self.active_record_count == self._reccnt:
            return self._nextrec
        return self._ringbufidx

    @property
    def lastrec(self) -> int:
        "Newest record slot: (nextrec - 1) mod reccnt"
        return (self._nextrec - 1 + self._reccnt) % self._reccnt

    @property
    def module_revision(self) -> str:
        "Module revision as string (e.g., '5,313')"
        region_start = struct.unpack_from('>I', self._content, 0x20)[0]
        region = self._content[region_start : self._data_start_address]
        # MANREV is last 4 bytes of 40 Bytes region
        raw = struct.unpack_from('>H', region, -4)[0]
        s = f'{raw:04x}'
        return f'{s[0]},{s[1:]}'

    @property
    def active_record_count(self) -> int:
        "Number of valid records in the ring buffer"
        if self._parse_record(self._nextrec).timestamp_us:
            return self._reccnt
        return self._nextrec

    def _parse_record(self, slot: int) -> NwCmdRecord:
        "Parse single record by slot index from content region"
        offset = self._rec_start + slot * _RECORD_SIZE
        ts     = struct.unpack_from('<I', self.data, offset)[0]
        net_id = struct.unpack_from('<I', self.data, offset + 4)[0]
        frame  = self.data[offset + 8 : offset + 20]
        param  = struct.unpack_from('<H', frame, 0)[0]
        return NwCmdRecord(
            index        = slot,
            timestamp_us = ts,
            network_id   = net_id,
            frame_data   = frame,
            param_id     = param,
        )

    def records(self) -> List[NwCmdRecord]:
        "Return valid records in the order used by the trace text export"
        if self.active_record_count == self._reccnt:
            lower = min(self._ringbufidx, self._nextrec)
            upper = max(self._ringbufidx, self._nextrec)
            slots = (*range(lower), *range(upper, self._reccnt), *range(lower, upper))
        else:
            slots = range(self._nextrec)
        return [self._parse_record(slot) for slot in slots]

    def export_text(self, output_file: str) -> None:
        "Export to NetworkCommandTrace.txt format"
        recs = self.records()
        header = (
            f'TYPE=CAN-TRACE-ASCII '
            f'V={self._format_version.replace(".", ",")} '
            f'MANREV={self.module_revision} '
            f'MANID={self.manid} TTS=0,000001 COLS=9 '
            f'RECCNT={self._reccnt} NEXTREC={self._nextrec} '
            f'DATAFORMAT=I386 TRACETYPE=NET DISPLAYCFG=7 '
            f'RINGBUFIDX={self._ringbufidx} FIRSTREC={self.firstrec} '
            f'LASTREC={self.lastrec} '
        )
        col_hdr = ('Recordindex\tNetwork[Index]\tTime\tType\t'
                   'Node\tNetwork-Id\tFrame-data\tParameter-Id\t'
                   'Description\tValue')
        with open(output_file, 'w', encoding='utf-8') as fh:
            fh.write(header + '\n')
            fh.write(col_hdr + '\n')
            for rec in recs:
                time_str = f'{rec.time_seconds:.6f}'.replace('.', ',')
                for param_id, description, value in rec.decoded_rows():
                    fields = [
                        str(rec.index),
                        rec.network_name,
                        time_str,
                        rec.message_type or 'UNKNOWN',
                        str(rec.node),
                        str(rec.network_id),
                        rec.frame_display,
                        str(param_id),
                        description,
                    ]
                    if value or rec.message_type in ('MAN_INF', 'WR_REQ', 'RD_RSP') or param_id == 65535:
                        fields.append(value)
                    fh.write('\t'.join(fields) + '\n')
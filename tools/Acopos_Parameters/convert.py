COPYRIGHT = """#
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
"""

import re
from enum import IntEnum
from pathlib import Path

script_dir = Path(__file__).resolve().parent
repo_root = script_dir.parents[1]

class TraceParameter(IntEnum):
    """Supplemental trace definitions; acp10par.h remains authoritative.

    Types follow explicit decoding rules in BrMotionNwTraceFile.py, not its
    generic u32 fallback. STR has unknown capacity; an empty type is unconfirmed.
    """

    data_type: str

    def __new__(cls, value: int, data_type: str) -> "TraceParameter":
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.data_type = data_type
        return obj

    TARGET_DATE_TIME = 65398, ''
    McFacility = 65399, 'UINT'
    McCmd = 65401, 'NIL'
    MODEL_NUMBER = 65406, 'STR'
    CommunicationState = 65426, ''
    ParRead_NoNetTraceUsed = 65429, ''
    McAcpDrv = 65430, ''
    MC_VERSION = 65431, 'UINT'
    ACP_VERSION = 65432, 'UINT'
    McCommand = 65437, 'UINT'
    MC_BROADCAST_EXTDAT = 65447, ''
    NETWORK_PHASE = 65449, ''
    POWERLINK_PRODUCT_CODE = 65456, ''
    HW_REVISION = 65457, 'STR'
    HW_PRODUCT_CODE = 65458, 'STR'
    TASKCL_CycDat_PLCopen = 65459, ''
    ACOPOS_SUB_SLOT = 65460, ''
    ACOPOS_TYP = 65464, ''
    POWERLINK_PLSTATE = 65465, 'UINT'
    POWERLINK_MUX_STATION = 65466, 'BOOL'
    POWERLINK_MUX_PRESCALE = 65467, 'USINT'
    ErrorID = 65468, 'UINT'
    Aborted_by = 65469, 'UINT'
    PLCopen_FB_Error = 65470, 'NIL'
    PLCopen_FB_Aborted = 65471, 'NIL'
    NCSYS_HW_REV = 65472, 'USINT'
    NCSYS_HW_TYPE = 65473, 'USINT'
    ACOPOS_ID_NR = 65474, 'UINT'
    ACOPOS_ID = 65475, 'UINT'
    NCSYS_BRMOD_TYPE = 65476, 'USINT'
    BRMOD_NCMAN = 65477, 'UINT'
    POWERLINK_IF_FW_VERSION = 65478, ''
    POWERLINK_VERSION = 65479, ''
    POWERLINK_CYCLE_TIME = 65480, ''
    AR_VERSION = 65481, 'STR'
    AR_SYSTEM_TICK = 65482, ''
    NET_TRACE_RING_STARTIDX = 65483, ''
    NC_TASKCLASS_TOLERANCE = 65484, ''
    NC_TASKCLASS_CYCLE_TIME = 65485, ''
    NC_TASKCLASS = 65486, ''
    PLCopen_MC_AxisState = 65487, ''
    NC_ACTION_MotionComp = 65489, 'NIL'
    NC_ACTION_PLCopen_MC = 65491, 'NIL'
    subject = 65493, 'UINT'
    action = 65494, 'UINT'
    PLCopen_FB = 65495, 'UINT'


with (script_dir / 'acp10par.h').open('r', encoding='utf-8') as f:
    content = f.read()

pattern = r'#define\s+(ACP10PAR_\w+)\s+(\d+)\s+/\*\s*\(([^)]+)\)\s+(.+?)\s*\*/'
matches = re.findall(pattern, content)

# https://help.br-automation.com/#/de/6/ncsoftware/acp10_drivefunctions/acopos_funktionsbausteine/ubersicht.html
function_block_types = {
    'AIO', 'ARITH', 'BIT', 'CALC', 'CAMCON', 'CMP', 'COUNT', 'CURVE',
    'DELAY', 'DIO', 'DYNSYS', 'EPROM', 'EVWR', 'FIFO', 'FILTER', 'IPL',
    'LATCH', 'LOGIC', 'MCURVE', 'MINMAX', 'MPGEN', 'MUX', 'PID', 'VARITH', 'VAR',
}
parameter_ids = {int(match[1]) for match in matches}
generated_ids = set(parameter_ids)
generated_names = {match[0].replace('ACP10PAR_', '') for match in matches}

lines = []
lines.append( COPYRIGHT )
lines.append('"""')
lines.append('B&R ACOPOS Parameter Definitions')
lines.append('Auto-generated from acp10par.h and supplemental trace names in convert.py -- do not edit manually.')
lines.append('Supplemental types follow explicit decoding rules in BrMotionNwTraceFile.py.')
lines.append('UINT/USINT are unsigned 2/1-byte values; NIL marks commands with no scalar value.')
lines.append('STR denotes ASCII with unknown capacity; data_type="" means the type is unconfirmed.')
lines.append('Generic 32-bit trace fallback decoding is not treated as evidence of a parameter type.')
lines.append('Supplemental parameters use their trace name as description.')
lines.append('')
lines.append('Function-block parameters support instances 0 through 7: ID = base ID + instance.')
lines.append('Existing names refer to instance 0; explicit names use the _INSTANCE_0 ... _INSTANCE_7 suffix.')
lines.append('Example: ACP10PAR.ARITH_MODE.instance(3) is ACP10PAR.ARITH_MODE_INSTANCE_3.')
lines.append('The corresponding block must be created on the drive via FUNCTION_BLOCK_CREATE before use.')
lines.append('See https://help.br-automation.com/#/de/6/ncsoftware/acp10_drivefunctions/acopos_funktionsbausteine/funktion.html')
lines.append('"""')
lines.append('')
lines.append('from enum import IntEnum')
lines.append('')
lines.append('')
lines.append('class ACP10PAR(IntEnum):')
lines.append('    """ACOPOS parameter IDs with IEC data type and description."""')
lines.append('')
lines.append('    data_type: str')
lines.append('    description: str')
lines.append('    function_block: str')
lines.append('    instance_number: int')
lines.append('')
lines.append('    def __new__(cls, value: int, data_type: str = "", description: str = "",')
lines.append('                function_block: str = "", instance_number: int = 0) -> "ACP10PAR":')
lines.append('        obj = int.__new__(cls, value)')
lines.append('        obj._value_ = value')
lines.append('        obj.data_type = data_type')
lines.append('        obj.description = description')
lines.append('        obj.function_block = function_block')
lines.append('        obj.instance_number = instance_number')
lines.append('        return obj')
lines.append('')
lines.append('    def instance(self, number: int) -> "ACP10PAR":')
lines.append('        """Select FB instance 0..7; this does not create the block on the drive."""')
lines.append('        if not self.function_block:')
lines.append('            raise ValueError(f"{self.name} is not a multi-instance function-block parameter")')
lines.append('        if isinstance(number, bool) or not isinstance(number, int):')
lines.append('            raise TypeError("Instance number must be an integer")')
lines.append('        if not 0 <= number <= 7:')
lines.append('            raise ValueError("Instance number must be between 0 and 7")')
lines.append('        return ACP10PAR(int(self) - self.instance_number + number)')
lines.append('')

for match in matches:
    param_name = match[0].replace('ACP10PAR_', '')
    param_id = match[1]
    data_type = match[2].strip()
    description = match[3].strip().replace("'", "\\'")
    prefix = param_name.split('_', 1)[0]
    is_function_block = prefix in function_block_types and match[3].strip().startswith(f'FB {prefix}:')
    metadata = f"'{data_type}', '{description}'"
    if is_function_block:
        if int(param_id) % 8:
            raise ValueError(f'Function-block base ID must be aligned to 8: {param_name}={param_id}')
        metadata += f", '{prefix}'"
    lines.append(f"    {param_name} = {param_id}, {metadata}")
    if is_function_block:
        for instance in range(8):
            instance_id = int(param_id) + instance
            if instance and instance_id in parameter_ids:
                raise ValueError(f'Instance ID collides with a header parameter: {param_name}={instance_id}')
            lines.append(f"    {param_name}_INSTANCE_{instance} = {instance_id}, {metadata}, {instance}")
            generated_ids.add(instance_id)
            generated_names.add(f'{param_name}_INSTANCE_{instance}')

for parameter in TraceParameter:
    param_id = parameter.value
    param_name = parameter.name
    if param_id in generated_ids:
        continue
    if not param_name.isidentifier() or param_name in generated_names:
        raise ValueError(f'Invalid or conflicting supplemental parameter name: {param_name}')
    data_type = parameter.data_type
    lines.append(f"    {param_name} = {param_id}, {data_type!r}, {param_name!r}")
    generated_ids.add(param_id)
    generated_names.add(param_name)

output_path = repo_root / 'pvi' / 'utils' / 'acp10par.py'
with output_path.open('w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

with (script_dir / 'ncglobal.h').open('r', encoding='utf-8') as f:
    ncglobal_content = f.read()

try:
    constants_block = ncglobal_content.split('#ifdef _REPLACE_CONST', 1)[1].split('#else', 1)[0]
except IndexError as exc:
    raise ValueError('Could not find the constant definitions in ncglobal.h') from exc

constant_pattern = r'^\s*#define\s+(\w+)\s+(.+?)\s*$'
constants = []
for line_number, line in enumerate(constants_block.splitlines(), start=1):
    match = re.fullmatch(constant_pattern, line)
    if match is None:
        continue

    name, raw_value = match.groups()
    value_match = re.fullmatch(r'\(?\s*(-?0[xX][0-9A-Fa-f]+|-?\d+)\s*\)?[uUlL]*', raw_value)
    if value_match is None:
        raise ValueError(
            f'Unsupported ncglobal.h constant on line {line_number}: {name} {raw_value}'
        )

    value = value_match.group(1)
    constants.append((name, int(value, 16 if value.lower().startswith('0x') else 10)))

ncglobal_lines = [
    COPYRIGHT,
    '"""',
    'B&R ACOPOS constants from ncglobal.h.',
    'Auto-generated by tools/Acopos_Parameters/convert.py -- do not edit manually.',
    '"""',
    '',
]
ncglobal_lines.extend(f'{name} = {value}' for name, value in constants)

ncglobal_output_path = repo_root / 'pvi' / 'utils' / 'ncglobal.py'
with ncglobal_output_path.open('w', encoding='utf-8') as f:
    f.write('\n'.join(ncglobal_lines) + '\n')

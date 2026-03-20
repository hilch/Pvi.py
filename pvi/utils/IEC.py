import re
import datetime
import math
from typing import Union, Any



limits = {
    'u8': (0,255),
    'i8': (-128,+127),
    'u16': (0,65535),
    'i16': (-32768,+32767),
    'u32': (0,4294967295),
    'i32': (-2147483648, +2147483647),
}
    
def limit_integer( value : Any, datatype : str ) -> int:
    min_value, max_value = limits[datatype]
    return max( min_value, min(value, max_value))    


def toIEC( value: Any ) -> str:
    """
    converts a Python datatype to IEC string
    
    Parameters:
        value: text to scan
        
    Returns:
        Python datatype
    """    
    if isinstance( value, bool):
        return 'TRUE' if value else 'FALSE'
    elif isinstance( value, datetime.timedelta):
        # convert datetime.timedelta to TIME
        # Get total seconds (can be negative)
        total_seconds = value.total_seconds()
        
        # Determine sign
        negative = total_seconds < 0
        total_seconds = abs(total_seconds)
        
        # Extract components
        days = int(total_seconds // 86400)
        remaining = total_seconds % 86400
        
        hours = int(remaining // 3600)
        remaining = remaining % 3600
        
        minutes = int(remaining // 60)
        remaining = remaining % 60
        
        seconds = int(remaining)
        milliseconds = int((remaining - seconds) * 1000)
        
        # Build the string with only non-zero components
        parts = []
        if days > 0:
            parts.append(f"{days}d")
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0:
            parts.append(f"{minutes}m")
        if seconds > 0:
            parts.append(f"{seconds}s")
        if milliseconds > 0:
            parts.append(f"{milliseconds}ms")
        
        # Handle zero duration
        if not parts:
            parts.append("0s")
        
        # Join with underscore
        result = "_".join(parts)
    
        # Add prefix and sign
        sign = "-" if negative else ""
        return f"T#{sign}{result}"
    elif isinstance( value, datetime.datetime):
        # convert datetime.datetime to DT
        return value.strftime("DT#%Y-%m-%d-%H:%M:%S")
    elif isinstance( value, datetime.date):
        #convert datetime.time to DATE
        return value.strftime("D#%Y-%m-%d")
    elif isinstance( value, datetime.time ):
        # convert datetime.time to TOD
        millisecond = value.microsecond // 1000  # Convert microseconds to milliseconds
        return value.strftime(f"TOD#%H:%M:%S.{millisecond:03d}")
    elif isinstance( value, bytes ):
        return str( value, 'ascii')
    elif isinstance( value, str ):
        return value
    elif isinstance( value, int ):
        return str(value)
    elif isinstance( value, float ):
        if math.isinf(value) and value > 0:
            return 'positive infinite (inf)'
        elif math.isinf(value) and value < 0:
            return 'negative infinite (inf)'
        if math.isnan(value):
            return 'not a number (NaN)'
        # show float in an engineering format
        decimals = 7     
        if value == 0:
            return f"0{' ' if decimals > 0 else ''}"
        # Get sign
        sign = '-' if value < 0 else ''
        value = abs(value)
        # Get exponent
        exponent = math.floor(math.log10(value))
        # Find the nearest multiple of 3
        exp_3 = (exponent // 3) * 3
        if exp_3 < 5:
            exp_3 = 0
        # Scale the value
        scaled = value / (10 ** exp_3)
        # Format with specified decimals
        if decimals == 0:
            if exp_3 != 0:
                return f"{sign}{scaled:.0f}e{exp_3}"
            else:
                return f"{sign}{scaled:.0f}"
        else:
            if exp_3 != 0:
                return f"{sign}{scaled:.{decimals}f}e{exp_3}" 
            else:
                return f"{sign}{scaled:.{decimals}f}" 
    else:
        return str(value)



def parseIEC( value: str, datatype: str ) -> Union[bool, int, 
                                            datetime.datetime, datetime.date, datetime.time, 
                                            datetime.timedelta, float,
                                            bytes, str]:
    """
    parses text with IEC literals and returns a Python datatype
    
    Parameters:
        value: text to scan
        
    Returns:
        Python datatype
    """
    if not isinstance(value, str):
        raise TypeError("Input must be a string")
    
    # Boolean conversion
    if datatype == 'boolean':
        # Regex: case-insensitive true/false, yes/no, 1/0
        if re.match(r'^(true|yes|1)$', value, re.IGNORECASE):
            return True
        elif re.match(r'^(false|no|0)$', value, re.IGNORECASE):
            return False
        else:
            raise ValueError(f"Cannot convert '{value}' to bool")
    
    # Signed Integer conversion
    elif datatype in ('i8','i16','i32','i64'):
        # Regex: optional sign, digits only
        if re.match(r'^[+-]?\d+$', value):
            return limit_integer( value = int(value), datatype = datatype)
        else:
            raise ValueError(f"Cannot convert '{value}' to int")
    
    # Unsigned Integer conversion    
    elif datatype in ('u8','u16','u32','u64'):
        # Regex: optional sign, digits only
        if re.match(r'^[+]?\d+$', value):
            return int(value)
        else:
            raise ValueError(f"Cannot convert '{value}' to int")    
    
    # Datetime conversion
    elif datatype == 'dt':
        """Parse 'DT#YYYY-MM-DD-HH:MM:SS' to datetime.datetime object"""
        match = re.match( r"DT#(\d{4})-(\d{2})-(\d{2})-(\d{2}):(\d{2}):(\d{2})", value)
        if match:
            year, month, day, hour, minute, second = map(int, match.groups())
            return datetime.datetime(year, month, day, hour, minute, second)
        raise ValueError(f"Invalid DATE_AND_TIME format: {value}")
    
    # Date conversion
    elif datatype == 'date':
        """Parse 'D#YYYY-MM-DD' to datetime.date object"""
        match = re.match( r"D#(\d{4})-(\d{2})-(\d{2})", value)
        if match:
            year, month, day = map(int, match.groups())
            return datetime.date(year, month, day)
        raise ValueError(f"Invalid DATE format: '{value}'")
    
    # Time conversion
    elif datatype == 'tod':
        """Parse 'TOD#HH:MM:SS.mmm' to datetime.time object"""
        match = re.match(r"TOD#(\d{2}):(\d{2}):(\d{2})\.(\d{3})", value)
        if match:
            hour, minute, second, millisecond = map(int, match.groups())
            microsecond = millisecond * 1000  # Convert milliseconds to microseconds
            return datetime.time(hour, minute, second, microsecond)
        raise ValueError(f"Invalid TOD format: '{value}'")
    
    # Timedelta conversion
    elif datatype == 'time':
        """Parse 'T#-##d_##h_##m_##s_###ms' to datetime.timedelta object"""
        match = re.match(r"T#(-?)(?:(\d+)d)?(?:_(\d+)h)?(?:_(\d+)m)?(?:_(\d+)s)?(?:_(\d+)ms)?\s*", value)
        if match:
            sign, days, hours, minutes, seconds, milliseconds = match.groups()
            
            # Convert to integers, default to 0 if None
            days = int(days) if days else 0
            hours = int(hours) if hours else 0
            minutes = int(minutes) if minutes else 0
            seconds = int(seconds) if seconds else 0
            milliseconds = int(milliseconds) if milliseconds else 0
            
        # Create timedelta
            td = datetime.timedelta(
                days=days,
                hours=hours,
                minutes=minutes,
                seconds=seconds,
                milliseconds=milliseconds
            )            
            if sign == '-':
                td = -td
            return td            
        else:
            raise ValueError(f"Invalid TIME format: {value}")
        
    elif datatype == 'f32' or datatype == 'f64':
        # parse floats in decimal or engineering format
        if re.match( r"^-?(?:(?:\d+\.?\d*|\d*\.\d+)(?:[eE][-+]?\d+)?|[eE][-+]?\d+)$", value):
            return float(value)
        else:
            raise ValueError(f"Invalid floating point format: '{value}'")
    
    # Bytes conversion
    elif datatype == 'string':
        # Regex: hex string (optional 0x prefix, even number of hex digits)
        if re.match(r'^(0x)?([0-9a-fA-F]{2})+$', value):
            # Remove 0x prefix if present
            hex_str = value[2:] if value.startswith('0x') else value
            return bytes.fromhex(hex_str)
        # Or direct UTF-8 encoding
        elif re.match(r'^.+$', value):
            return value.encode('utf-8')
        else:
            raise ValueError(f"Cannot convert '{value}' to string")
        
    elif datatype == 'wstring':
        return value 
    
    else:
        raise TypeError(f"Unsupported target type: '{datatype}'")

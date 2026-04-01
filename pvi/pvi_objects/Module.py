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

from datetime import datetime, timezone
from typing import Union, Callable, Dict, Any, Optional, List
from enum import IntEnum, unique
import xml.etree.ElementTree as ET
import re
import inspect
from ctypes import create_string_buffer, byref, sizeof
from .include import *
from .Object import PviObject
from .Error import PviError
from .Helpers import dictFromParameterPairString


@unique
class ModuleType(IntEnum):
    UNKNOWN = 0
    CYCLIC_RESOURCE = 0x11
    SYSTEM_OBJECT = 0x12
    IDLE_TIME_OBJECT = 0x13
    OBJECT_OF_A_TIMER_RESOURCE = 0x14
    INTERRUPT_OBJECT = 0x15
    EXCEPTION_OBJECT = 0x16
    REACTION_TASK_MODULE = 0x17
    AVT_LIBRARY = 0x21
    MATHTRAP_LIBRARY = 0x25
    TRAP_LIBRARY = 0x26
    ADVANCED_TRAP_LIBRARY = 0x28
    OPTIMIZED_IO_MODULE = 0x31
    IO_MAPPING = 0x32
    DATA_OBJECT = 0x41
    CONTAINER_MODULE = 0x43
    SAFETY_APP = 0x44
    NC_DRIVER = 0x45
    MOTION_DATA_OBJECT = 0x46
    SAFETY_CONFIGURATION = 0x47
    PROFILER_DEFINITION = 0x4b
    PROFILER_DATA_OBJECT = 0x4c
    TRACER_DEFINITION = 0x4d
    TRACER_DATA = 0x4e
    NC_UPDATE = 0x4f
    LOGGER_MODULE = 0x53
    TARGET_SYSTEM_CONFIGURATION = 0x81
    NETWORK_CONFIGURATION_MODULE = 0x82
    IO_CONFIGURATION = 0x84
    OPCUA_CONFIGURATION = 0x86
    REDUNDANCY_CONFIGURATION = 0x87
    XML_BASED_CONFIGURATION = 0x88
    XML_BASED_CONFIGURATION_NON_VOLATILE = 0x89
    DB_SQLITE_TEXT_DEFINITION = 0xd1
    DB_SQLITE_UNIT_DEFINITION = 0xd2
    DB_SQLITE_RELOADABLE_TEXT = 0xd3

    @classmethod
    def _missing_(cls, value):
        return ModuleType.UNKNOWN


@unique
class MemoryType(IntEnum):
    SYSROM = 0
    SYSRAM = 1
    USRROM = 2
    USRRAM = 3
    MEMCARD = 4
    FIXRAM = 5
    DRAM = 65
    UNKNOWN = 256

    @classmethod
    def _missing_(cls, value):
        return MemoryType.UNKNOWN


class Module(PviObject):
    '''class representing modules

    SNMP : can be used but is not necessary

    Typical usage example:
    ```
    cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
    module = Module( cpu, 'bigmod' )
    ```
    '''

    _BUFFER_SIZE_SMALL: int = 1024
    _BUFFER_SIZE_MEDIUM: int = 4096
    _ANSL_LOGGER_ACCESS_NOT_SUPPORTED: int = 12058

    # ------------------------------------------------------------------

    def __init__(self, parent: PviObject, name: str, **objectDescriptor: Union[str, int, float]):
        '''
        Args:
            parent : CPU object
            name : name of module
            objectDescriptor : see PVI documentation for more details
        '''
        if parent.type != T_POBJ_TYPE.POBJ_CPU:
            raise PviError(12009, self)
        if 'CD' not in objectDescriptor:
            objectDescriptor.update({'CD': name})
        super().__init__(parent, T_POBJ_TYPE.POBJ_MODULE, name, **objectDescriptor)
        self._uploaded: Optional[Callable] = None
        self._progress: Optional[Callable] = None


    def __repr__(self) -> str:
        return f"Module( name={self._name}, linkID={self._linkID} )"


    def _call_callback(self, callback: Optional[Callable], *args) -> None:
        """
        Call a callback with flexible signature (1 or 2 parameters).
        If callback accepts 2 params: callback(self, *args).
        If callback accepts 1 param:  callback(*args).
        Does nothing when callback is None.
        """
        if callback is None:
            return
        sig = inspect.signature(callback)
        if len(sig.parameters) == 2:
            callback(self, *args)
        else:
            callback(*args)


    def _read_response_bytes(self, wParam, dataLen: int, extra: int = 0) -> bytes:
        """
        Read PVI response into a buffer and return raw bytes.

        Args:
            wParam:   wParam from the event
            dataLen:  number of bytes reported by the event
            extra:    optional extra bytes added to the buffer (default 0)
        Raises:
            PviError: if PviXReadResponse returns non-zero
        """
        s = create_string_buffer(dataLen + extra)
        self._result = PviXReadResponse(self._hPvi, wParam, s, sizeof(s))
        if self._result != 0:
            raise PviError(self._result, self)
        return s.raw


    @staticmethod
    def _parse_xml(data: Union[str, bytes]) -> ET.Element:
        """
        Parse XML and return root Element.
        Raises:
            ValueError: wraps ET.ParseError with descriptive message
        """
        try:
            return ET.fromstring(data)
        except ET.ParseError as exc:
            raise ValueError(f"Invalid XML data: {exc}") from exc

    # ------------------------------------------------------------------

    def _eventUploadStream(self, wParam, responseInfo, dataLen: int) -> None:
        '''(internal) upload a data module as stream'''
        raw = self._read_response_bytes(wParam, dataLen)        
        self._call_callback(self._uploaded, raw)                


    def _eventUploadLogData(self, wParam, responseInfo, dataLen: int) -> None:
        '''(internal) upload XML logger data (ANSL only)'''
        raw = self._read_response_bytes(wParam, dataLen, extra=256)  
        cleaned = raw.replace(b'\x00', b'')
        logger = self._parse_xml(cleaned)                            

        entries: List[Dict[str, Any]] = []
        for entry in logger:
            cols = {'Version', 'RecordId', 'OriginRecordId', 'EventId',
                    'AddDataSize', 'AddDataFormat', 'Severity', 'Info'}
            for c in cols:
                try:
                    entry.attrib[c] = str(int(entry.attrib[c]))
                except (KeyError, ValueError):
                    pass
            try:
                entry.attrib['TimestampUtc'] = str(
                    datetime.fromtimestamp(float(entry.attrib['TimestampUtc'])))
            except (KeyError, ValueError):
                pass
            entries.append(entry.attrib)

        self._call_callback(self._uploaded, entries)           


    def _eventUploadModData(self, wParam, responseInfo, dataLen: int) -> None:
        '''(internal) upload logger data (INA2000)
        see GUID 75bf0748-45f2-4610-a68d-53760ab5fa98
        '''
        patternParameterPairs = re.compile(r'\s*([A-Z]{1,4}=\w*)\s*')
        raw = self._read_response_bytes(wParam, dataLen)        

        entries: List[Dict[str, Any]] = []
        data = raw.split(b'\x00')
        n = 0
        noOfEntries = int(data[0][3:])
        while n < noOfEntries * 3:
            n += 1
            entry: Dict[str, Any] = {}
            for m in patternParameterPairs.findall(str(data[n])):
                if m.startswith('TIME'):    entry['date']  = datetime.fromtimestamp(int(m[5:]))
                elif m.startswith('ID'):    entry['id']    = int(m[3:])
                elif m.startswith('E'):     entry['error'] = int(m[2:])
                elif m.startswith('INFO'):  entry['info']  = int(m[5:])
                elif m.startswith('LEV'):   entry['level'] = int(m[4:])
                elif m.startswith('TASK'):  entry['task']  = str(data[5:])
            n += 1; entry['ascii'] = data[n]
            n += 1; entry['bin']   = data[n]
            entries.append(entry)

        self._call_callback(self._uploaded, entries)            


    def _eventProceeding(self, wParam, responseInfo) -> None:
        '''(internal) return proceeding info'''
        proceedingInfo = T_PROCEEDING_INFO()
        self._result = PviXReadResponse(self._hPvi, wParam, byref(proceedingInfo), sizeof(proceedingInfo))
        if self._result == 0:
            self._call_callback(self._progress, int(proceedingInfo.Percent))  
        else:
            raise PviError(self._result, self)


    def upload(self, **kwargs: Union[str, Callable]) -> None:
        '''
        uploadLoggerData
        loads logger data if module is a logger module else load binary data

        Args:
            kwargs:
                uploaded - callback - is fired when module was uploaded
                progress - callback(int) - returns percentage of progress
                MT - Moduletype e.g. 'BRT', '_LOGM'
        '''
        arguments = ''
        loggerModule = False
        for key, value in kwargs.items():
            if key == 'uploaded':
                if callable(value):
                    self._uploaded = value
                else:
                    raise TypeError("only type 'callable' for argument 'uploaded' allowed !")
            elif key == 'progress':
                if callable(value):
                    self._progress = value
                else:
                    raise TypeError("only type 'callable' for argument 'progress' allowed !")
            elif key == 'MT' and value == '_LOGM':
                loggerModule = True
            else:
                arguments += f"{key}={value}"

        if loggerModule:
            s = create_string_buffer(b'\000' * self._BUFFER_SIZE_MEDIUM)         
            self._result = PviXRead(self._hPvi, self._linkID, POBJ_ACC_LN_XML_LOGM_INFO,
                                    None, 0, byref(s), sizeof(s))
            if self._result == 0:
                xmlTree = self._parse_xml(str(s, 'ascii').rstrip('\x00'))        
                loggerVersion = xmlTree.attrib.get('Version', '1000').encode('ascii')
                s = create_string_buffer(b'DN=10000000 VI=' + loggerVersion)
                self._result = PviXReadArgumentRequest(self._hPvi, self._linkID,
                    POBJ_ACC_LN_XML_LOGM_DATA, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0)
                if self._result:
                    raise PviError(self._result)
            elif self._result == self._ANSL_LOGGER_ACCESS_NOT_SUPPORTED:        
                s = create_string_buffer(b'DN=100000')  # maximum possible is undocumented
                self._result = PviXReadArgumentRequest(self._hPvi, self._linkID,
                    POBJ_ACC_MOD_DATA, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0)
                if self._result:
                    raise PviError(self._result)
            else:
                raise PviError(self._result)
        else:
            s = create_string_buffer(bytes(arguments, 'ascii'))
            self._result = PviXReadArgumentRequest(self._hPvi, self._linkID,
                POBJ_ACC_UPLOAD_STM, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0)
            if self._result:
                raise PviError(self._result)


    def delete(self) -> None:
        """
        delete Module from CPU

        Raises:
            PviError

        Returns:
            None
        """
        s = create_string_buffer(b'LD=Delete')        
        self._result = PviXWrite( self._hPvi, self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )  
        # if self._result:
        #     raise PviError(self._result, self)        

    @property
    def moduleInfo(self) -> dict:
        """read the Module type information"""
        s = create_string_buffer(b'\000' * self._BUFFER_SIZE_SMALL)              
        self._result = PviXRead(self._hPvi, self._linkID, POBJ_ACC_MOD_TYPE,
                                None, 0, byref(s), sizeof(s))
        if self._result == 0:
            ret: Dict[str, Any] = {}
            ret.update(dictFromParameterPairString(str(s, 'ascii').rstrip('\x00')))
            ret['MT'] = ModuleType(int(ret.get('MT', 0)))
            return ret
        else:
            raise PviError(self._result, self)

    @property
    def moduleInfoExtended(self) -> dict:
        """read the extended Module type information"""
        s = create_string_buffer(b'\000' * self._BUFFER_SIZE_MEDIUM)             
        self._result = PviXRead(self._hPvi, self._linkID, POBJ_ACC_LN_XML_MOD_INFO,
                                None, 0, byref(s), sizeof(s))
        if self._result == 0:
            root = self._parse_xml(str(s, 'ascii').rstrip('\x00'))               
            module_info: Dict[str, Any] = {}
            if root.tag == 'ModInfo':
                module_info = dict(root.attrib)
                module_info['ModulType'] = ModuleType(int(module_info.get('ModulType', '0x00'), 16)).name
                module_info['MemType']   = MemoryType(int(module_info.get('MemType',   '0x100'), 16)).name
                module_info['Time']      = datetime.strptime(module_info.get('Time', ''), "%Y-%m-%d-%H-%M-%S.%f")
                version  = f"{int(module_info.get('Version',  '0')):02x}"
                version += f"{int(module_info.get('Revision', '0')):02x}"
                module_info['Version'] = f'{version[0]}.{version[1]}{version[2]}.{version[3]}'
                del module_info['Revision']
            return module_info
        else:
            raise PviError(self._result, self)

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
from typing import Union, Callable, Dict, Any
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
    def __init__( self, parent : PviObject, name : str, **objectDescriptor: Union[str,int, float]):
        '''
        Args:
            parent : CPU object
            name : name of module
            objectDescriptor : see PVI documentation for more details
        '''
        if parent.type != T_POBJ_TYPE.POBJ_CPU:
            raise PviError(12009, self)
        if 'CD' not in objectDescriptor:
            objectDescriptor.update({'CD':name})                    
        super().__init__( parent, T_POBJ_TYPE.POBJ_MODULE, name, **objectDescriptor)
        self._uploaded = None
        self._progress = None


    def __repr__(self):
        return f"Module( name={self._name}, linkID={self._linkID} )"

  
    def _eventUploadStream( self, wParam, responseInfo, dataLen : int ):
        '''
        (internal) upload a data module as stream
        '''
        s = create_string_buffer(dataLen)       
        self._result = PviXReadResponse( self._hPvi, wParam, s, sizeof(s) )
        if self._result == 0:
            if self._uploaded:
                sig = inspect.signature(self._uploaded)
                if len(sig.parameters) == 2:
                    self._uploaded(self, s.raw)
                elif len(sig.parameters) == 1:
                    self._uploaded(s.raw)                      
        else:
            raise PviError(self._result, self)


    def _eventUploadLogData( self, wParam, responseInfo, dataLen : int ):
        '''
        (internal) upload XML logger data (ANSL only)
        '''
        s = create_string_buffer(dataLen+256)       
        self._result = PviXReadResponse( self._hPvi, wParam, s, sizeof(s) )
        s = s.raw.replace(b'\x00',b'')
        if self._result == 0:
            logger = ET.fromstring(s) 
            entries = list()
            for entry in logger:
                cols = {'Version','RecordId', 'OriginRecordId', 'EventId', 'AddDataSize', 'AddDataFormat', 'Severity', 'Info'}
                for c in cols:
                    try: # try to convert columns into integer values
                        value = int(entry.attrib[c])
                        entry.attrib.update({c : str(value)} )
                    except:
                        pass
                try: # try to convert timestamp into Python datatype
                    value = datetime.fromtimestamp( float(entry.attrib['TimestampUtc']) )
                    entry.attrib.update({ 'TimestampUtc' : str(value)} )
                except:
                    pass
                entries.append(entry.attrib)
            if self._uploaded:
                sig = inspect.signature(self._uploaded)
                if len(sig.parameters) == 2:
                    self._uploaded(self, entries)
                elif len(sig.parameters) == 1:
                    self._uploaded(entries)      
        else:
            raise PviError(self._result, self)


    def _eventUploadModData( self, wParam, responseInfo, dataLen : int ):
        '''
        (internal) upload logger data (INA2000)
        see GUID 75bf0748-45f2-4610-a68d-53760ab5fa98
        '''
        patternParameterPairs = re.compile(r"\s*([A-Z]{1,4}=\w*)\s*")        
        s = create_string_buffer(dataLen)       
        self._result = PviXReadResponse( self._hPvi, wParam, s, sizeof(s) )
        if self._result == 0:
            entries = list()            
            data = s.raw.split(b'\00')                    
            n = 0
            noOfEntries = int(data[0][3:])
            while n <  noOfEntries*3:
                n += 1 # point to next entry
                entry = dict()
                # read info string
                matches = patternParameterPairs.findall(str(data[n]))            
                for m in matches:
                    if str(m).startswith('TIME'):
                        dt = datetime.fromtimestamp( int(m[5:]))
                        entry.update({ 'date' : dt})
                    elif str(m).startswith('ID'):
                        id = int(m[3:])
                        entry.update({ 'id' : id})
                    elif str(m).startswith('E'):
                        error = int(m[2:])
                        entry.update({ 'error' : error })                        
                    elif str(m).startswith('INFO'):
                        info = int(m[5:])                        
                        entry.update({ 'info' : info })
                    elif str(m).startswith('LEV'):
                        level = int(m[4:])                        
                        entry.update({ 'level' : level })
                    elif str(m).startswith('TASK'):
                        entry.update({ 'task' : str(data[5:]) })
                # read ascii data
                n += 1
                entry.update({'ascii': data[n] })
                # read binary data
                n += 1
                entry.update({'bin': data[n] })   
                entries.append(entry) 
            if self._uploaded:
                sig = inspect.signature(self._uploaded)
                if len(sig.parameters) == 2:
                    self._uploaded(self, entries)
                elif len(sig.parameters) == 1:
                    self._uploaded(entries)                    
        else:
            raise PviError(self._result, self)


    def _eventProceeding( self, wParam, responseInfo : T_RESPONSE_INFO ):  
        '''
        (internal) return proceeding info
        '''  
        proceedingInfo = T_PROCEEDING_INFO()
        self._result = PviXReadResponse( self._hPvi, wParam, byref(proceedingInfo), sizeof(proceedingInfo) )
        if self._result == 0:
            if self._progress:
                sig = inspect.signature(self._progress)
                if len(sig.parameters) == 2:
                    self._progress(self, int(proceedingInfo.Percent))
                elif len(sig.parameters) == 1:                         
                    self._progress(int(proceedingInfo.Percent))
        else:
            raise PviError(self._result, self)               


    def upload(self, **kwargs : Union[str, Callable]):
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
                loggerModule = True # interpret as logger module
            else:
                arguments += f"{key}={value}"

        # check if module is a logger module
        if loggerModule:
            # try ANSL logger module
            s = create_string_buffer(b'\000' * 4096)   
            self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_LN_XML_LOGM_INFO, None, 0, byref(s), sizeof(s) )
            if self._result == 0:
                s = str(s, 'ascii').rstrip('\x00')
                xmlTree = ET.fromstring(s)
                loggerVersion = xmlTree.attrib.get('Version', '1000').encode('ascii')
                s = create_string_buffer(b'DN=10000000 VI=' + loggerVersion )   
                self._result = PviXReadArgumentRequest( self._hPvi, self._linkID, POBJ_ACC_LN_XML_LOGM_DATA, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0 )            
                if self._result:
                    raise PviError(self._result)           
            elif self._result == 12058: # access not aupported ?
                s = create_string_buffer(b'DN=100000') # maximum possible is undocumented.
                self._result = PviXReadArgumentRequest( self._hPvi, self._linkID, POBJ_ACC_MOD_DATA, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0    ) 
                if self._result:
                    raise PviError(self._result)           
            else:
                raise PviError(self._result)
        else:
            s = create_string_buffer(bytes(arguments, 'ascii'))
            self._result = PviXReadArgumentRequest( self._hPvi, self._linkID, POBJ_ACC_UPLOAD_STM, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0    ) 
            if self._result:
                raise PviError(self._result)           
                            
    @property       
    def moduleInfo(self) -> dict:
        """
        read the Module type information
         example:

        ```
        module = Module( cpu, '$$sysconf' )
        ...
        print("info =", module.moduleInfo )
        ```

        results in:

        ```
        info = {'MT': <ModuleType.TARGET_SYSTEM_CONFIGURATION: 129>, 'ML': '70720'}
        ```

        """    
        s = create_string_buffer(b'\000' * 1024)             
        self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_MOD_TYPE , None, 0, byref(s), sizeof(s) )     
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            ret = dict()
            ret.update( dictFromParameterPairString(s)  )
            type_number = int(ret.get('MT',0))
            ret.update( {'MT' : ModuleType(type_number)})
            return ret          
        else:
            raise PviError(self._result, self)    


        
    @property       
    def moduleInfoExtended(self) -> dict:
        """
        read the Module type information
         example:

        ```
        module = Module( cpu, '$$sysconf' )
        ...
        print("info =", module.moduleInfoExtended )
        ```

        results in:

        ```
        info = {'Name': '$$sysconf', 
                'Size': '70720', 
                'Address': '0x038B70A0', 
                'MemType': <MemoryType.USRROM: 2>, 
                'Version': '73', 
                'Revision': '48', 
                'ModulType': <ModuleType.TARGET_SYSTEM_CONFIGURATION: 129>, 
                'Time': datetime.datetime(2024, 1, 5, 11, 0, 8), 
                'RawTimeErzT5': 'f8-25-58-04-00', 
                'RawTimeAenT5': 'fc-72-75-12-00', 
                'TaskClass': '0', 
                'InstallNo': '0', 
                'ModulState': '1', 
                'DomainOvIndex': '1793', 
                'DomainModulState': '6', 
                'Listed': '3'}
        ```

        """    
        s = create_string_buffer(b'\000' * 4096)             
        self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_LN_XML_MOD_INFO  , None, 0, byref(s), sizeof(s) )     
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            """Parse Module Info XML and return as dictionary"""
            root = ET.fromstring(s)
            module_info : Dict[str, Any]= dict()
            if root.tag == 'ModInfo':        
                module_info = dict(root.attrib)
                type_number = int(module_info.get('ModulType', '0x00'),16)
                module_info.update( {'ModulType' : ModuleType(type_number).name } ) 
                memory_type = int(module_info.get('MemType', '0x100'),16)
                module_info.update( {'MemType' : MemoryType(memory_type).name } )
                time_created = datetime.strptime(module_info.get('Time','') , "%Y-%m-%d-%H-%M-%S.%f")
                module_info.update( {'Time' : time_created } ) 
                version = f'{int(module_info.get('Version','0')):02x}'
                version += f'{int(module_info.get('Revision','0')):02x}'
                version = f'{version[0]}.{version[1]}{version[2]}.{version[3]}'
                module_info.update({'Version': version})  
                del module_info['Revision']                                 
            return module_info      
        else:
            raise PviError(self._result, self)    
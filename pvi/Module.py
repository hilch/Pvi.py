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

from typing import Union, Callable
import xml.etree.ElementTree as ET
import re
import datetime
import inspect
from ctypes import create_string_buffer, byref, sizeof
from .include import *
from .Object import PviObject
from .Error import PviError


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
        self._result = PviReadResponse( wParam, s, sizeof(s) )
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
        self._result = PviReadResponse( wParam, s, sizeof(s) )
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
                    value = datetime.datetime.fromtimestamp( float(entry.attrib['TimestampUtc']) )
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
        self._result = PviReadResponse( wParam, s, sizeof(s) )
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
                        dt = datetime.datetime.fromtimestamp( int(m[5:]))
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
        self._result = PviReadResponse( wParam, byref(proceedingInfo), sizeof(proceedingInfo) )
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
            self._result = PviRead( self._linkID, POBJ_ACC_LN_XML_LOGM_INFO, None, 0, byref(s), sizeof(s) )
            if self._result == 0:
                s = str(s, 'ascii').rstrip('\x00')
                xmlTree = ET.fromstring(s)
                loggerVersion = xmlTree.attrib.get('Version', '1000').encode('ascii')
                s = create_string_buffer(b'DN=10000000 VI=' + loggerVersion )   
                self._result = PviReadArgumentRequest( self._linkID, POBJ_ACC_LN_XML_LOGM_DATA, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0 )            
                if self._result:
                    raise PviError(self._result)           
            elif self._result == 12058: # access not aupported ?
                s = create_string_buffer(b'DN=100000') # maximum possible is undocumented.
                self._result = PviReadArgumentRequest( self._linkID, POBJ_ACC_MOD_DATA, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0    ) 
                if self._result:
                    raise PviError(self._result)           
            else:
                raise PviError(self._result)
        else:
            s = create_string_buffer(bytes(arguments, 'ascii'))
            self._result = PviReadArgumentRequest( self._linkID, POBJ_ACC_UPLOAD_STM, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0    ) 
            if self._result:
                raise PviError(self._result)           
                            

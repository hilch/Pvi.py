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

import datetime
import inspect
from typing import List, Union
from ctypes import create_string_buffer, byref, sizeof
from .include import *
from .Object import PviObject
from .Error import PviError
from .Helpers import dictFromParameterPairString

# ----------------------------------------------------------------------------------
class Cpu(PviObject):
    '''representing a PVI CPU object
    ANSL & INA2000 : specifies a cpu
    SNMP : can be used but is not necessary
    see PVI documentation for more details

    Typical usage example:
    ```
    device = Device( line, 'TCP', CD='/IF=TcpIp' )
    cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
    task1 = Task( cpu, 'mainlogic')
    ```        
    '''
    def __init__( self, parent : PviObject, name : str, **objectDescriptor : Union[str,int, float]):
        '''
        Args:
            parent : the device (or station) object  
            name : name of the CPU in PVI hierarchy  
            objectDescriptor : see PVI documentation for more details
                ANSL : e.g. CD='/IP=127.0.0.1 /COMT=2500'  
                INA2000 : e.g. CD='/DAIP=10.49.40.222'
                SNMP : ''
        '''
        if parent.type != T_POBJ_TYPE.POBJ_DEVICE and parent.type != T_POBJ_TYPE.POBJ_STATION:
            raise PviError(12009, self )                    
        super().__init__( parent, T_POBJ_TYPE.POBJ_CPU, name, **objectDescriptor) 
        self._downloaded = None
        self._progress = None  
  

    def __repr__(self):
        return f"Cpu( name={self._name}, linkID={self._linkID} )" 


    def _eventStatus( self, wParam, responseInfo ):
        '''         
        (internal) handle status events
        '''      
        self._result = PviXReadResponse( self._hPvi, wParam, None, 0 ) 


    def _eventDownloadStream( self, wParam, responseInfo : T_RESPONSE_INFO): 
        '''
        (internal) handle stream download
        '''   
        self._result = PviXWriteResponse( self._hPvi, wParam )
        if self._result == 0:
            if self._downloaded:
                sig = inspect.signature(self._downloaded)
                if len(sig.parameters) == 0:
                    self._downloaded()
                elif len(sig.parameters) == 1:
                    self._downloaded(self)
        else:
            raise PviError(self._result, self)      


    def _eventProceeding( self, wParam, responseInfo : T_RESPONSE_INFO ):    
        proceedingInfo = T_PROCEEDING_INFO()
        self._result = PviXReadResponse( self._hPvi, wParam, byref(proceedingInfo), sizeof(proceedingInfo) )
        if self._result == 0:
            if self._progress:
                sig = inspect.signature(self._progress)
                if len(sig.parameters) == 1:
                    self._progress(int(proceedingInfo.Percent))
                elif len(sig.parameters) == 2:
                    self._progress(self, int(proceedingInfo.Percent))                    
        else:
            raise PviError(self._result, self)   


    def warmStart(self) -> None:
        '''
        executes a warm restart
        '''
        self.status = "WarmStart"


    def coldStart(self) -> None:
        '''
        executes a cold restart
        '''        
        self.status = "ColdStart"


    def stopTarget(self) -> None:
        '''
        executes a SERV stop
        '''        
        self.status = "Reset"


    def diagnostics(self) -> None:
        '''
        executes a DIAG stop
        '''        
        self.status = "Diagnose"


    def downloadModule(self, data : bytes, **kwargs )->None:
        '''
        download given bytes as module

        Args:
            data : bytes  - data content
            kwargs : 
                MT - module type e.g. 'BRT'
                MN - module name
                MV - module version
                LD - memory type e.g. 'Ram', 'Dram', 'Rom'
                downloaded - callback() or callback(Cpu) if module was downloaded
                progress - callback(p) or callback (Cpu, p) to show progress
        '''
        currentFrame = inspect.currentframe()
        currentFunctionName = ''
        if currentFrame:
            currentFunctionName = currentFrame.f_code.co_name

        if not(isinstance(data, bytes)):
            raise TypeError(currentFunctionName + " - data: only bytes accepted !")
        if 'MT' not in kwargs:
            kwargs.update( { 'MT' : 'BRT' } )
        if 'MN' not in kwargs:
            raise KeyError( currentFunctionName + " - argument 'MN' is missing !")

        arguments = ''
        for key, value in kwargs.items():
            if key == 'downloaded':
                if callable(value):
                    self._downloaded = value
                else:
                    raise TypeError("only type function for argument 'downloaded' allowed !")
            elif key == 'progress':
                if callable(value):
                    self._progress = value
                else:
                    raise TypeError("only type function for argument 'progress' allowed !")
            else:
                arguments += f"{key}={value} "
        s = create_string_buffer(bytes(arguments,'ascii') + b'\0' + bytes(data) )            
        self._result = PviXWriteRequest( self._hPvi, self._linkID, POBJ_ACC_DOWNLOAD_STM, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0)
        if self._result:
            raise PviError( self._result, self )


    @property
    def modules(self)->List[str]:
        """    
        list of all modules on this CPU

        example:

        ```
        cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
        ...
        print("cpu.modules=", cpu.modules)
        ```

        results in:

        ```
        cpu.modules= ['$$sysconf', '$arlogsys', '$arlogusr', '$fieldbus',
                    ..... 'visTrend', 'visapi', 'visvc']
        ```
        """
        s = create_string_buffer(b'\000' * 4096)   
        self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_LIST_MODULE, None, 0, byref(s), sizeof(s) )
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            return s.split('\t')
        else:
            raise PviError(self._result, self)


    @property
    def tasks(self)->List[str]:
        '''     
        get a list of all tasks

        example:

        ```
        cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
        ...
        print("cpu.tasks=", cpu.tasks)
        ```

        results in:

        ```
        cpu.tasks= ['brewing', 'conveyor', 'feeder', 'heating', 'mainlogic', 'myProg', 'visAlarm', 'visCtrl', 'visTrend']
        ```
        '''
        s = create_string_buffer(b'\000' * 4096)   
        self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_LIST_TASK, None, 0, byref(s), sizeof(s) )
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            return s.split('\t')
        else:
            raise PviError(self._result, self)


    @property
    def variables(self)->List[str]:
        '''     
        get a list of global variables

        example:
        ```
        cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
        ...
        print("cpu.variables=", cpu.variables)
        ```

        results in:

        ```
        cpu.variables= ['LCRPID_D_MODE_X', 'LCRPID_FBK_MODE_INTERN', 'LCRPID_MODE_AUTO', 'LCRPID_MODE_CLOSE', 'aoHeating', 
                ...... 'sdm_APPMODE_ERROR', 'sdm_APPMODE_OK', 'sdm_APPMODE_WARNING']
        ```
        '''
        s = create_string_buffer(b'\000' * 65536)   
        self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_LIST_PVAR, None, 0, byref(s), sizeof(s) )
        if( self._result == 0 ):
            s = str(s, 'ascii').rstrip('\x00')
            variables = [v.split(' ')[0] for v in s.split('\t')]
            return variables
        else:
            raise PviError(self._result, self)


    @property       
    def status(self) -> dict:
        """
        read the CPU status
         example:

        ```
        cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
        ...
        print("status=", cpu.status )
        ```

        results in:

        ```
        cpu.status= {'ST': 'WarmStart', 'RunState': 'RUN'}
        ```

        possible values of 'ST' are: 'WarmStart', 'ColdStart', 'Diagnose', 'Error', 'Reset' and '<unknown>'
        possible values of 'RunState' are: 'RUN', 'DIAG', 'SERV'

        """    
        st = super().status
        runState = { "WarmStart" : "RUN", "ColdStart" : "RUN", "Diagnose" : "DIAG", "Error" : "SERV", "Reset" : "SERV"}.get(st.get("ST", "<unknown>"))
        st.update({"RunState" : runState})
        return st


    @status.setter
    def status(self, status : str ):
        '''
        sets the CPU status
        '''        
        s = create_string_buffer(b"ST=" + status.encode())
        self._result = PviXWrite( self._hPvi, self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result, self)


    @property       
    def cpuInfo(self) -> dict:
        """
        Returns:
            dict with memory information

        example:
        ```
        ```

        """    
        s = create_string_buffer(b'\000' * 1024)             
        self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_CPU_INFO  , None, 0, byref(s), sizeof(s) )     
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            ret = dict()
            ret.update( dictFromParameterPairString(s)  )
            return ret          
        else:
            raise PviError(self._result, self)     


    @property
    def time(self) -> datetime.datetime:
        """
        Returns:
            datetime : CPU's current clock time

        example:

        ```
        cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
        ...
        print("cpu.time=", cpu.time)
        ```

        results in:

        ```
        cpu.time= 2023-11-09 13:44:02
        ```
        """
        t = struct_tm()       
        self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_DATE_TIME , None, 0, byref(t), sizeof(t) )
        if self._result == 0:
            try:
                time =  datetime.datetime( year = t.tm_year+1900, month = t.tm_mon+1, day=t.tm_mday, hour=t.tm_hour, minute = t.tm_min, second = t.tm_sec)
            except ValueError:
                time = datetime.datetime( year = 1970, month = 1, day = 1 )            
            return time            
        else:
            raise PviError(self._result, self)
         
            
    @time.setter
    def time(self, time : datetime.datetime):
        '''
        sets the CPU time
        '''        
        t = struct_tm()
        t.tm_year = time.year - 1900
        t.tm_mon = time.month - 1
        t.tm_mday = time.day
        t.tm_hour = time.hour
        t.tm_min = time.minute
        t.tm_sec = time.second
        self._result = PviXWrite( self._hPvi, self._linkID, POBJ_ACC_DATE_TIME, byref(t), sizeof(t), None, 0 )
        if self._result != 0:
            raise PviError(self._result, self)
     

            
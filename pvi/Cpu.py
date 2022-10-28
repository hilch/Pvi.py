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

from ctypes import *
import datetime
import inspect
from .include import *
from .Object import PviObject
from .Error import PviError


# ----------------------------------------------------------------------------------
class Cpu(PviObject):
    def __init__( self, parent, name, **objectDescriptor ):
        if parent._type != T_POBJ_TYPE.POBJ_DEVICE and parent._type != T_POBJ_TYPE.POBJ_STATION:
            raise PviError(12009, self )                    
        super().__init__( parent, 'POBJ_CPU', name, **objectDescriptor) 
        self._downloaded = None
        self._progress = None       

    def __repr__(self):
        return f"Cpu( name={self._name}, linkID={self._linkID} )" 

    def _eventStatus( self, wParam, responseInfo ):
        """         
        handle status events
        """      
        self._result = PviReadResponse( wParam, None, 0 ) 
        if callable(self._statusChanged):
            self._statusChanged( responseInfo )


    def _eventDownloadStream( self, wParam, responseInfo : T_RESPONSE_INFO):    
        self._result = PviWriteResponse( wParam )
        if self._result == 0:
            if self._downloaded:
                self._downloaded()
        else:
            raise PviError(self._result, self)      

    def _eventProceeding( self, wParam, responseInfo : T_RESPONSE_INFO ):    
        proceedingInfo = T_PROCEEDING_INFO()
        self._result = PviReadResponse( wParam, byref(proceedingInfo), sizeof(proceedingInfo) )
        if self._result == 0:
            if self._progress:
                self._progress(int(proceedingInfo.Percent))
        else:
            raise PviError(self._result, self)   

    def warmStart(self) -> None:
        '''
        Cpu.warmstart() -> None
        executes a warm restart
        '''
        s = create_string_buffer(b"ST=WarmStart")
        self._result = PviWrite( self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result, self)

    def coldStart(self) -> None:
        '''
        Cpu.coldStart() -> None
        executes a cold restart
        '''        
        s = create_string_buffer(b"ST=ColdStart")
        self._result = PviWrite( self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result, self)

    def downloadModule(self, data : bytes, **kwargs ):
        '''
        Cpu.downloadModule( data, **args )
        download given bytes as module

        Parameters:
        data : bytes  - data content
        kwargs : MT - module type e.g. 'BRT'
               MN - module name
               MV - module version
               LD - memory type e.g. 'Ram', 'Dram', 'Rom'
               downloaded - callback() if module was downloaded
               progress - callback(p) to show progress
        '''
        if not(isinstance(data, bytes)):
            raise TypeError(inspect.currentframe().f_code.co_name + " - data: only bytes accepted !")
            return
        if 'MT' not in kwargs:
            kwargs.update( { 'MT' : 'BRT' } )
        if 'MN' not in kwargs:
            raise KeyError( inspect.currentframe().f_code.co_name + " - argument 'MN' is missing !")
            return            

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
        self._result = PviWriteRequest( self._linkID, POBJ_ACC_DOWNLOAD_STM, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0)
        if self._result:
            raise PviError( self._result, self )


    @property
    def modules(self):
        """     
        Cpu.modules : list of str
        get a list a modules 
        """
        s = create_string_buffer(b'\000' * 4096)   
        self._result = PviRead( self._linkID, POBJ_ACC_LIST_MODULE, None, 0, byref(s), sizeof(s) )
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            return s.split('\t')
        else:
            raise PviError(self._result, self)


    @property       
    def status(self) -> dict:
        """
        Cpu.status
        read the CPU status
        """
        st = super().status
        runState = { "WarmStart" : "RUN", "ColdStart" : "RUN", "Diagnose" : "DIAG", "Error" : "SERV", "Reset" : "SERV"}.get(st.get("ST"), "<unknown>")
        st.update({"RunState" : runState})
        return st
        

    @property
    def time(self) -> datetime.datetime:
        """
        Cpu: read the CPU's clock
        """
        t = struct_tm()       
        self._result = PviRead( self._linkID, POBJ_ACC_DATE_TIME , None, 0, byref(t), sizeof(t) )
        if self._result == 0:
            try:
                time =  datetime.datetime( year = t.tm_year+1900, month = t.tm_mon+1, day=t.tm_mday, hour=t.tm_hour, minute = t.tm_min, second = t.tm_sec)
            except ValueError:
                time = datetime.datetime( year = 1970, month = 1, day = 1 )            
            return time            
        else:
            raise PviError(self._result, self)
            



     

            
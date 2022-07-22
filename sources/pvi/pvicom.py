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
import re
from sqlite3 import Date
from pvi.pvi_h import *
from pvi.common_h import *

# ----------------------------------------------------------------------------------
class PviError(Exception):
    def __init__(self, error):
        PviErrorMessages = { 12009 : 'wrong object hierarchy !'}
        super().__init__( PviErrorMessages.get(error, "") )
        print(f'PviError: {error}')

# ----------------------------------------------------------------------------------
class PviObject():
    """
    the base of all objects
    """
    def __init__(self, parent , type, name, **objectDescriptor ):
        parentName = re.findall('(\S+)',parent.name)[0]+'/' if parent else ''
        self._name = f'{parentName}{name}'
        self._linkID = 0
        self._objectDescriptor = objectDescriptor
        self._type = T_POBJ_TYPE[type]
        self._result = int(0)      
        self._pviError = int(0)
        self.errorChanged = None
        self.statusChanged = None
        if parent: # all objects but '@Pvi' have a parent
            self._pviConnection = parent._pviConnection
            self._pviConnection.link(self)

    def __hash__(self):
        return hash( (self._name, self._type) )

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        return f"{self._name}"

    def __repr__(self):
        return f"PviObject( name={self._name}, linkID={self._linkID} )"

    @property
    def name(self):
        return self._name


    def _eventData( self, wParam, responseInfo ):
        """
        handle data events
        """
        self._result = PviReadResponse( wParam, None, 0 )
        if callable(self.errorChanged):
            self.errorChanged(0)             

    def _eventDataType( self, wParam, responseInfo ):
        """
        handle data type events
        """        
        self._result = PviReadResponse( wParam, None, 0 ) 
       

    def _eventUploadStream( self, wParam, responseInfo, dataLen : int ):      
        self._result = PviReadResponse( wParam, None, 0 ) 

    def _eventStatus( self, wParam, responeInfo ):
        """         
        handle status events
        """      
        self._result = PviReadResponse( wParam, None, 0 ) 
        if callable(self.statusChanged):
            pass

    def _eventError( self, wParam, responseInfo ):
        """         
        handle error events
        """      
        self._result = PviReadResponse( wParam, None, 0 ) 
#        print(f'ERROR_EVENT {self._name} : {responseInfo.ErrCode}')
        if callable(self.errorChanged):
            self.errorChanged(responseInfo.ErrCode)

    def _createAndLink(self, pvi):
        descriptor_items = []
        for key, value in self._objectDescriptor.items():
            quote = '"' if re.search( "[\/\.\s]", str(value) ) is not None else ''
            descriptor_items += [f'{key}={quote}{value}{quote}']
        descr = ' '.join(descriptor_items) 
        linkID = DWORD(0)
        self._result = PviCreate( byref(linkID), bytes(self._name, 'ascii'),
            self._type, bytes(descr, 'ascii'), PVI_HMSG_NIL, SET_PVIFUNCTION, 0, None)
        if self._result == 0: # object creation successful
            self._linkID = linkID.value
            PviReadRequest( self._linkID, POBJ_ACC_TYPE, PVI_HMSG_NIL, SET_PVIFUNCTION, 0 )
            pvi._linkIDs[self._linkID] = self # store object for backward reference  
#            print( self._name, self._linkID )
        else:
            print( f"PviCreate {self.name} = {self._result}")
            raise PviError(self._result)
        return self._result                

    def unlink(self):
        if self._linkID != 0:
            self._pviConnection._linkIDs.remove(self._linkID) # remove from linkIDs
            self._pviConnection._pviObjects.remove(self) # remove from PviObjects
            self._result = PviUnlink(self._linkID)
            self._linkID = 0
            if self._result != 0:
                raise PviError(self._result)

# ----------------------------------------------------------------------------------
class Line(PviObject):
    def __init__( self, parent, name, **objectDescriptor ):
        if parent._type != T_POBJ_TYPE.POBJ_PVI:
            raise PviError(12009)         
        super().__init__( parent, 'POBJ_LINE', name, **objectDescriptor)

    def __repr__(self):
        return f"Line( name={self._name}, linkID={self._linkID} )"

# ----------------------------------------------------------------------------------
class Device(PviObject):
    def __init__( self, parent, name, **objectDescriptor ):
        if parent._type != T_POBJ_TYPE.POBJ_LINE:
            raise PviError(12009)            
        super().__init__( parent, 'POBJ_DEVICE', name, **objectDescriptor)

    def __repr__(self):
        return f"Device( name={self._name}, linkID={self._linkID} )"

# ----------------------------------------------------------------------------------
class Station(PviObject):
    def __init__( self, parent, name, **objectDescriptor ):
        if parent._type != T_POBJ_TYPE.POBJ_DEVICE:
            raise PviError(12009)          
        super().__init__( parent, 'POBJ_STATION', name, **objectDescriptor)

    def __repr__(self):
        return f"Station( name={self._name}, linkID={self._linkID} )"

# ----------------------------------------------------------------------------------
class Cpu(PviObject):
    def __init__( self, parent, name, **objectDescriptor ):
        if parent._type != T_POBJ_TYPE.POBJ_DEVICE and parent._type != T_POBJ_TYPE.POBJ_STATION:
            raise PviError(12009)                    
        super().__init__( parent, 'POBJ_CPU', name, **objectDescriptor) 
        self._downloaded = None
        self._progress = None  

    def __repr__(self):
        return f"Cpu( name={self._name}, linkID={self._linkID} )"

    def warmStart(self):
        s = create_string_buffer(b"ST=WarmStart")
        self._result = PviWrite( self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result) 

    def coldStart(self):
        s = create_string_buffer(b"ST=ColdStart")
        self._result = PviWrite( self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result)  

    def downloadModule(self, data : bytes, **args ):
        if not(isinstance(data, bytes)):
            raise TypeError("data: only bytes accepted !")
            return
        arguments = ''
        for key, value in args.items():
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
        s = create_string_buffer(bytes(arguments,'ascii') + b'\0' + data)            
        self._result = PviWriteRequest( self._linkID, POBJ_ACC_DOWNLOAD_STM, byref(s), sizeof(s)-1, PVI_HMSG_NIL, SET_PVIFUNCTION, 0)


    @property
    def modules(self):
        """     
        get a list a modules 
        """
        s = create_string_buffer(b'\000' * 4096)   
        self.result = PviRead( self._linkID, POBJ_ACC_LIST_MODULE, None, 0, byref(s), sizeof(s) )
        if self.result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            return s.split('\t')

    @property       
    def status(self):
        """
        read the CPU's status
        """
        s = create_string_buffer(b'\000' * 64)             
        self._result = PviRead( self._linkID, POBJ_ACC_STATUS, None, 0, byref(s), sizeof(s) )
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            if s == "ST=WarmStart" or s == "ST=ColdStart":
                return "RUN"
            elif s == "ST=Diagnose":
                return "DIAG"
            elif s == "ST=Error" or s == "ST=Reset":
                return "SERV"
            else:
                return s[3:]

    @property
    def time(self) -> datetime.datetime:
        """
        read the CPU's clock
        """
        t = struct_tm()       
        self._result = PviRead( self._linkID, POBJ_ACC_DATE_TIME , None, 0, byref(t), sizeof(t) )
        try:
            return datetime.datetime( year = t.tm_year+1900, month = t.tm_mon+1, day=t.tm_mday, hour=t.tm_hour, minute = t.tm_min, second = t.tm_sec)
        except ValueError:
            return datetime.datetime( year = 1970, month = 1, day = 1 )


    def _eventDownloadStream( self, wParam, responseInfo ):    
        self._result = PviWriteResponse( wParam )
        if self._result == 0:
            if self._downloaded:
                self._downloaded()
        else:
            raise PviError(self._result)            

# ----------------------------------------------------------------------------------
class Task(PviObject):
    def __init__( self, parent, name, **objectDescriptor ):
        if parent._type != T_POBJ_TYPE.POBJ_CPU:
            raise PviError(12009)
        objectDescriptor.update({'CD':name})
        super().__init__( parent, 'POBJ_TASK', name, **objectDescriptor)

    def start(self):
        s = create_string_buffer(b"ST=Start")
        self._result = PviWrite( self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result)  

    def resume(self):
        s = create_string_buffer(b"ST=Resume")
        self._result = PviWrite( self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result)                         

    def stop(self):
        s = create_string_buffer(b"ST=Stop")
        self._result = PviWrite( self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result)                  

    def __repr__(self):
        return f"Task( name={self._name}, linkID={self._linkID} )"

# ----------------------------------------------------------------------------------
class Module(PviObject):
    def __init__( self, parent, name, **objectDescriptor ):
        if parent._type != T_POBJ_TYPE.POBJ_CPU:
            raise PviError(12009)
        objectDescriptor.update({'CD':name})                    
        super().__init__( parent, 'POBJ_MODULE', name, **objectDescriptor)
        self._uploaded = None
        self._progress = None

    def __repr__(self):
        return f"Module( name={self._name}, linkID={self._linkID} )"

    def startUpload(self, **args ):
        arguments = ''
        for key, value in args.items():
            if key == 'uploaded':
                if callable(value):
                    self._uploaded = value
                else:
                    raise TypeError("only type function for argument 'uploaded' allowed !")
            elif key == 'progress':
                if callable(value):
                    self._progress = value
                else:
                    raise TypeError("only type function for argument 'progress' allowed !")
            else:
                arguments += f"{key}={value}"
        s = create_string_buffer(bytes(arguments, 'ascii'))
        self._result = PviReadArgumentRequest( self._linkID, POBJ_ACC_UPLOAD_STM, byref(s), sizeof(s), PVI_HMSG_NIL, SET_PVIFUNCTION, 0    )

    def _eventUploadStream( self, wParam, responseInfo, dataLen : int ):
        s = create_string_buffer(dataLen)       
        self._result = PviReadResponse( wParam, s, sizeof(s) )
        if self._result == 0:
            if self._uploaded:
                self._uploaded(s.raw)
        else:
            raise PviError(self._result)

# ----------------------------------------------------------------------------------
class Variable(PviObject):
    def __init__( self, parent, name, **objectDescriptor ):
        if parent._type != T_POBJ_TYPE.POBJ_CPU and  parent._type != T_POBJ_TYPE.POBJ_TASK:
            raise PviError(12009)        
        self._value = None 
        self._valueChanged = None 
        objectDescriptor.update({'CD':name})
        if not('RF' in objectDescriptor):
            objectDescriptor.update({'RF':0}) # do not cyclic refrehs variables by default       
        super().__init__( parent, 'POBJ_PVAR', name, **objectDescriptor)

    def __repr__(self):
        return f"Variable( name={self._name}, linkID={self._linkID}, VT={self._objectDescriptor.get('VT')} )"

    def _readRawData(self, wParam, responseInfo):
        vt = self._objectDescriptor.get('VT') # variable data type

        if vt == None:
            self._value = None
            if responseInfo: # data is answer of a request
                data = c_uint8()
                self._result = PviReadResponse( wParam, byref(data), sizeof(data) )
            return

        vl = int(self._objectDescriptor.get('VL')) # sizeof(variable)
        vn = int(self._objectDescriptor.get('VN')) # number of array elements
        
        data = None

        if vt == 'boolean':
            data = c_uint8()
        elif vt == 'u8':
            data = c_uint8()
        elif vt == 'i8':
            data = c_int8()
        elif vt == 'u16':
            data = c_uint16()
        elif vt == 'i16':
            data = c_int16()
        elif vt == 'u32':
            data = c_uint32()
        elif vt == 'i32':
            data = c_int32()
        elif vt == 'string':
            data = create_string_buffer(b'\000' * vl)
        else: # not handled data type
            data = c_uint8()
            self._value = None
            self._result = PviReadResponse( wParam, None, 0 ) # just acknowledge
            if callable(self.errorChanged):
                self.errorChanged(0)               

        if responseInfo: # data is answer of a request
            self._result = PviReadResponse( wParam, byref(data), sizeof(data) )
            if vt == 'string':
                self._value = data.value.decode('ascii')
            else:
                self._value = data.value

            if callable(self.errorChanged):
                self.errorChanged(0)       
        else: # data shall be immediately read
            self._result = PviRead( self._linkID, POBJ_ACC_DATA, None, 0, byref(data), sizeof(data) )
            if self._result == 0:
                self._value = data.value
            else:
                raise PviError(self._result)

    def _eventData( self, wParam, responseInfo ):
        self._readRawData( wParam, responseInfo )
        if callable(self._valueChanged):
            self._valueChanged(self._value)


    def _eventDataType( self, wParam, responseInfo ):
        s = create_string_buffer(b'\000' * 64)       
        self._result = PviReadResponse( wParam, s, sizeof(s) )
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            for x in  re.findall( "([A-Z]{2}=[a-zA-z0-9]+)", s ):
                self._objectDescriptor.update({ x[0:2]: x[3:]}) 
            pass  
        else:
            raise PviError(self._result)

    @property
    def value(self):
        self._readRawData( 0, None )
        return self._value

    @value.setter
    def value(self,v):
        vt = self._objectDescriptor.get('VT') # variable data type
        if vt == 'boolean':
            data = c_uint8(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'u8':
            data = c_uint8(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'i8':
            data = c_int8(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'u16':
            data = c_uint16(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'i16':
            data = c_int16(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'u32':
            data = c_uint32(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )
        elif vt == 'i32':
            data = c_int32(v)
            self._result = PviWrite( self._linkID, POBJ_ACC_DATA, byref(data), sizeof(data), None, 0 )

    @property
    def valueChanged(self):
        return self._valueChanged

    @valueChanged.setter
    def valueChanged(self, cb):
        if callable(cb):
            self._valueChanged = cb
        else:
            raise ValueError

# ----------------------------------------------------------------------------------

class Pvi():
    # ----------------------------------------------------------------------------------
    def __init__(self):
        self._objectsArranged = False
        self._pviObjects = []
        self._rootObject = PviObject(None, 'POBJ_PVI', '@Pvi')
        self._rootObject._pviConnection = self
        self.link(self._rootObject)
        self._linkIDs = {}
        self._result = PviInitialize( 0, 0, "", None )
        if self._result == 0:
            # set global events
            for m in (POBJ_EVENT_PVI_CONNECT, POBJ_EVENT_PVI_DISCONN, POBJ_EVENT_PVI_ARRANGE):
                self._result = PviSetGlobEventMsg( m, PVI_HMSG_NIL, SET_PVIFUNCTION, 0 )
                if self._result != 0:
                    raise PviError(self._result)
        else:
            raise PviError(self._result)

    # ----------------------------------------------------------------------------------
    @property
    def root(self):
        return self._rootObject

    @property
    def license(self):
        """
        read license information
        """
        li = T_PVI_INFO_LICENCE()
        self._result = PviRead( self.root._linkID, POBJ_ACC_INFO_LICENCE  , None, 0, byref(li), sizeof(li) )
        if self._result == 0:
            try: 
                state = ('undefined', 'trial', 'runtime', 'developer', 'locked')[li.PviWorkState0]
                hardware = 'B&R IPC' if li.PviWorkState1 and 0x01 else 'PC'
                burlicence = 'B&R License' if li.PviWorkState1 and 0x02 else ''
                dongle = 'Pvi Dongle' if li.PviWorkState1 and 0x04 else ''
                return state, hardware, burlicence, dongle, str(li.LcName)
            except IndexError:
                pass
        return ('undefined', '', '', '', '', '' )

    # ----------------------------------------------------------------------------------
    def link(self, *args ):
        """
        registers new PviObject(s)

        *args : PviObject of list of PviObjects
        """
        for o in args:
            if isinstance(o, PviObject):
                self._pviObjects.append(o)
                if self._objectsArranged:
                    o._createAndLink(self)
            elif isinstance(o, list ):
                for oo in o:
                    self.link(oo)
            else:
                raise ValueError("only PviObject of list of PviObjects allowed !")
    # ----------------------------------------------------------------------------------

    def findObjectByName(self, name) ->PviObject :
        for o in self._pviObjects:
            if o.name == name:
                return o
        return None


    # ----------------------------------------------------------------------------------
    def __del__(self):
        print("PviDeinitialize")
        PviDeinitialize()

    # ----------------------------------------------------------------------------------
    def _eventPviConnect( self, wParam, responseInfo ):
        """
        handle PVI connect event
        """
        print("POBJ_EVENT_PVI_CONNECT")
        self._result = PviReadResponse( wParam, None, 0 )     

    # ----------------------------------------------------------------------------------
    def _eventPviDisconnect( self, wParam, responseInfo ):
        """
        handle PVI disconnect event
        """  
        self._result = PviReadResponse( wParam, None, 0 )
        self._pviObjects.clear()
        self._linkIDs.clear()
        self._objectsArranged = False

    # ----------------------------------------------------------------------------------
    def _eventPviArrange( self, wParam, responseInfo ): 
        """
        handle pvi arrange event
        """
        self._result = PviReadResponse( wParam, None, 0 )                
        print("POBJ_EVENT_PVI_ARRANGE")
        #link @Pvi
        # linkID = DWORD(0)
        # self._result = PviLink( byref(linkID), bytes(self.root.name, 'ascii'),PVI_HMSG_NIL, SET_PVIFUNCTION, 0, None) 
        # self.root._linkID = linkID
        # create and link objects
        for po in self._pviObjects:
            po._createAndLink(self)
        self._objectsArranged = True 


    # ----------------------------------------------------------------------------------
    def _eventOther( self, wParam, responseInfo ):
        """
        handle other events
        """
        self._result = PviReadResponse( wParam, None, 0 )                
        print("self.Info.nType", responseInfo.nType)      

    # ----------------------------------------------------------------------------------
    def doEvents(self):
        """         
        event loop 
        """
        wParam = WPARAM()
        lParam = LPARAM()
        hMsg = HANDLE()
        dataLen = c_uint32()        
        self._result = PviGetNextResponse( byref(wParam), byref(lParam), byref(hMsg), None )

        if wParam.value != 0:
            responseInfo = T_RESPONSE_INFO()
            self._result = PviGetResponseInfo( wParam, None, byref(dataLen), byref(responseInfo), sizeof(responseInfo) )

            if responseInfo.nType == POBJ_EVENT_PVI_CONNECT:
                self._eventPviConnect( wParam, responseInfo )
            elif responseInfo.nType == POBJ_EVENT_PVI_DISCONN:
                self._eventPviDisconnect( wParam, responseInfo )
            elif responseInfo.nType == POBJ_EVENT_PVI_ARRANGE:
                self._eventPviArrange( wParam, responseInfo )
            elif responseInfo.nType == POBJ_ACC_TYPE:
                po = self._linkIDs.get(responseInfo.LinkID, None )
                if po:
                    po._eventDataType( wParam, responseInfo )
                else:
                    raise ValueError("linkID not found !")
            elif responseInfo.nType == POBJ_EVENT_DATA:
                po = self._linkIDs.get(responseInfo.LinkID, None )
                if po:
                    po._eventData( wParam, responseInfo )
                else:
                    raise ValueError("linkID not found !")                    
            elif responseInfo.nType == POBJ_ACC_UPLOAD_STM:
                po = self._linkIDs.get(responseInfo.LinkID, None )
                if po:
                    po._eventUploadStream( wParam, responseInfo, dataLen.value ) 
                else:
                    raise ValueError("linkID not found !")
            elif responseInfo.nType == POBJ_ACC_DOWNLOAD_STM:
                po = self._linkIDs.get(responseInfo.LinkID, None )
                if po:
                    po._eventDownloadStream( wParam, responseInfo ) 
                else:
                    raise ValueError("linkID not found !") 
            elif responseInfo.nType == POBJ_EVENT_STATUS or responseInfo.nType == POBJ_ACC_STATUS:
                po = self._linkIDs.get(responseInfo.LinkID, None )
                if po:
                    po._eventStatus( wParam, responseInfo )
                else:
                    raise ValueError("linkID not found !")                   
            elif responseInfo.nType == POBJ_EVENT_ERROR:
                po = self._linkIDs.get(responseInfo.LinkID, None )
                if po:
                    po._eventError( wParam, responseInfo )
                else:
                    raise ValueError("linkID not found !")
            else:
                self._eventOther( wParam, responseInfo )
    





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

from ctypes import c_uint64 as WPARAM, c_int64 as LPARAM, c_void_p as HANDLE, byref, sizeof
from .include import *
from .Error import PviError
from .Object import PviObject
import datetime

class Connection():
    '''
    class representing a connection to PVI manager

    Typical usage example:

    ```
        pviConnection = Connection() # start a Pvi connection

        line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')    
    ```
    '''
    # ----------------------------------------------------------------------------------
    def __init__(self, debug : bool = False, timeout: float = 5 ):
        """Initializes the connection to PVI manager

        Args:
            debug : True = verbose messages for debugging
            timeout : timeout in [s] to PVI manager instance
        """
        self._startTime = datetime.datetime.now()
        self._pviTrialTimeCheck = datetime.timedelta(seconds=timeout +1)
        self._debug = debug
        self._objectsArranged = False
        self._pviObjects = []
        self._rootObject = PviObject(None, T_POBJ_TYPE.POBJ_PVI, '@Pvi')
        self._rootObject._connection = self
        self.link(self._rootObject)
        self._linkIDs = {}
        self._result = PviInitialize( timeout, 0, "", None )
        if self._result == 0:
            # set global events
            for m in (POBJ_EVENT_PVI_CONNECT, POBJ_EVENT_PVI_DISCONN, POBJ_EVENT_PVI_ARRANGE):
                self._result = PviSetGlobEventMsg( m, PVI_HMSG_NIL, SET_PVIFUNCTION, 0 )
                if self._result != 0:
                    raise PviError(self._result)
        else:
            raise PviError(self._result)

    # ----------------------------------------------------------------------------------
    def __repr__(self):
        return f"Connection()"

    # ----------------------------------------------------------------------------------
    def __del__(self):
        if self._debug:
            print("PviDeinitialize")
        PviDeinitialize()

    # ----------------------------------------------------------------------------------
    @property
    def root(self) ->PviObject:
        """
        Returns:
           PviObject: the base object 'Pvi'
        """
        return self._rootObject

    @property
    def license(self) -> tuple:
        """read PVI license information

        Returns:
            A tuple( state, hardware, license, dongle, license-name )

        where    
        state is 'undefined' or 'trial' or 'runtime' or 'developer' or 'locked',  
        hardware is = 'B&R IPC' or 'PC',  
        license is 'B&R License' or '',  
        dongle is 'Pvi Dongle' or '',  
        license-name is a string  

        result may be ```('undefined', '', '', '', '', '')``` if PVI root object is not yet linked.

        """
        li = T_PVI_INFO_LICENCE()
        if self.root._linkID == 0: # root object not yet valid
            return ('undefined', '', '', '', '', '' )

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
        else:
            raise PviError(self._result, self )
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
                raise ValueError("only PviObject or list of PviObjects allowed !")
    # ----------------------------------------------------------------------------------

    def findObjectByName(self, name : str) ->PviObject :
        for o in self._pviObjects:
            if o.name == name:
                return o
        raise KeyError('PviObject not found by name')

    # ----------------------------------------------------------------------------------

    def findObjectByLinkID(self, linkID : DWORD) ->PviObject :
        for o in self._pviObjects:
            if o._linkID == linkID:
                return o
        raise KeyError('PviObject not found by LinkID')      

    # ----------------------------------------------------------------------------------
    def _eventPviConnect( self, wParam, responseInfo ):
        """
        handle PVI connect event
        """
        if self._debug:
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
        self._pviTrialTimeCheck = None

        self._result = PviReadResponse( wParam, None, 0 )                
        if self._debug:
            print("POBJ_EVENT_PVI_ARRANGE")

        # create and link objects
        for po in self._pviObjects:
            po._createAndLink(self)
        self._objectsArranged = True

        if self._debug:
            license = self.license            
            print(f'PVI license: {license[0]} - running on {license[1]}' ) 

    # ----------------------------------------------------------------------------------
    def _eventOther( self, wParam, responseInfo ):
        """
        handle other events
        """
        self._result = PviReadResponse( wParam, None, 0 )

    # ----------------------------------------------------------------------------------
    def doEvents(self):
        """         
        event loop - must be cyclically called

        typical usage example:

        ```
        while run:  
            pviConnection.doEvents()  
        ```
        """
        wParam = WPARAM()
        lParam = LPARAM()
        hMsg = HANDLE()
        dataLen = c_uint32()        
        self._result = PviGetNextResponse( byref(wParam), byref(lParam), byref(hMsg), None )

        if wParam.value != 0:
            responseInfo = T_RESPONSE_INFO()
            self._result = PviGetResponseInfo( wParam, None, byref(dataLen), byref(responseInfo), sizeof(responseInfo) )

            if self._debug:
                if responseInfo.ErrCode != 0:
                    po = self.findObjectByLinkID(responseInfo.LinkID)
                    print(f'{po.name} : nMode = {responseInfo.nMode}, nType = {responseInfo.nType}, ErrCode = {responseInfo.ErrCode}')

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
            elif responseInfo.nType == POBJ_EVENT_PROCEEDING:
                po = self._linkIDs.get(responseInfo.LinkID, None )
                if po:
                    po._eventProceeding( wParam, responseInfo ) 
                else:
                    raise ValueError("linkID not found !")   
            elif responseInfo.nType == POBJ_ACC_LN_XML_LOGM_DATA:
                po = self._linkIDs.get(responseInfo.LinkID, None )
                if po:
                    po._eventUploadLogData( wParam, responseInfo, dataLen.value ) 
                else:
                    raise ValueError("linkID not found !") 
            elif responseInfo.nType == POBJ_ACC_MOD_DATA:
                po = self._linkIDs.get(responseInfo.LinkID, None )
                if po:
                    po._eventUploadModData( wParam, responseInfo, dataLen.value ) 
                else:
                    raise ValueError("linkID not found !")                                                                    
            elif responseInfo.nType == POBJ_EVENT_ERROR:
                po = self._linkIDs.get(responseInfo.LinkID, None )
                if po:
                    if self._debug and responseInfo.ErrCode != 0:
                        print( f'{repr(po)}: error {responseInfo.ErrCode}')
                    po._eventError( wParam, responseInfo )
                else:
                    raise ValueError("linkID not found !")
            else:
                self._eventOther( wParam, responseInfo )
                if self._debug:
                    po = self.findObjectByLinkID(responseInfo.LinkID)
                    print(f'{po.name} : nMode = {responseInfo.nMode}, nType = {responseInfo.nType}, ErrCode = {responseInfo.ErrCode}')                
        
        if self._pviTrialTimeCheck:
            if datetime.datetime.now() - self._startTime > self._pviTrialTimeCheck:
                raise PviError(12040)



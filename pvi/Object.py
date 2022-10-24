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
import re
from .include import *
from .Error import PviError

class PviObject():
    __patternParameterPairs = re.compile(r"\s*([A-Z]{2}=\w*)\s*")

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
        self._errorChanged = None
        self._debug = False
        if parent: # all objects but '@Pvi' have a parent
            self._pviConnection = parent._pviConnection
            self._pviConnection.link(self)
            self._debug = self._pviConnection._debug

    def __hash__(self):
        return hash( (self._name, self._type) )

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        return f"{self._name}"

    def __repr__(self):
        return f"PviObject( name={self._name}, linkID={self._linkID} )"

    @property
    def name(self) -> str:
        '''
        PviObject: hierarchical object name
        '''
        return self._name


    @property
    def descriptor(self) -> str:
        '''
        PviObject: object descriptor string
        '''
        return self._objectDescriptor

    @property
    def errorChanged(self) -> callable:
        '''
        PviObject: callback for 'error changed'
        '''
        return self._errorChanged

    @errorChanged.setter
    def errorChanged(self, cb : callable):
        '''
        PviObject: set callback for 'error changed'
        '''
        if callable(cb):
            self._errorChanged = cb
        else:
            raise TypeError("only callable allowed for 'errorChanged'")


    def _eventData( self, wParam, responseInfo ):
        """
        handle data events
        """
        self._result = PviReadResponse( wParam, None, 0 )
        if callable(self._errorChanged):
            self._errorChanged(0)             

    def _eventDataType( self, wParam, responseInfo ):
        """
        handle data type events
        """        
        self._result = PviReadResponse( wParam, None, 0 ) 
       

    def _eventUploadStream( self, wParam, responseInfo, dataLen : int ):      
        self._result = PviReadResponse( wParam, None, 0 ) 


    def _eventStatus( self, wParam, responseInfo ):
        pass


    def _eventError( self, wParam, responseInfo ):
        """         
        handle error events
        """      
        self._result = PviReadResponse( wParam, None, 0 )
        if callable(self.errorChanged):
            self.errorChanged(responseInfo.ErrCode)
 
    def _createAndLink(self, pvi):
        descriptor_items = []
        for key, value in self._objectDescriptor.items():
            quote = '"' if re.search( "[\/\.\s]", str(value) ) is not None else ''
            descriptor_items += [f'{key}={quote}{value}{quote}']
        descr = ' '.join(descriptor_items) 
        linkID = DWORD(0)
        linkDescriptor = None
        if self._type == T_POBJ_TYPE.POBJ_CPU or self._type == T_POBJ_TYPE.POBJ_MODULE:
            linkDescriptor = b'EV=ep' # need this for downloading proceeding info
        self._result = PviCreate( byref(linkID), bytes(self._name, 'ascii'),
            self._type, bytes(descr, 'ascii'), PVI_HMSG_NIL, SET_PVIFUNCTION, 0, linkDescriptor)
        if self._result == 0: # object creation successful
            self._linkID = linkID.value
            if self._type == T_POBJ_TYPE.POBJ_PVAR: # read variable's data type
                PviReadRequest( self._linkID, POBJ_ACC_TYPE, PVI_HMSG_NIL, SET_PVIFUNCTION, 0 )
            pvi._linkIDs[self._linkID] = self # store object for backward reference  
        else:
            print( f"PviCreate {self.name} = {self._result}")
            raise PviError(self._result)
        return self._result                


    @property
    def externalObjects(self):
        """     
        PviObject.externalObjects : list of dict
        get a list of external objects
        """    
        s = create_string_buffer(b'\000' * 65536)   
        self.result = PviRead( self._linkID, POBJ_ACC_LIST_EXTERN, None, 0, byref(s), sizeof(s) )
        if self.result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            li1 = [r.split(' OT=') for r in s.split('\t')]
            li2 = [{ 'name': r[0], 'type' : r[1] } for r in li1]
            return li2
        else:
            return []


    @property       
    def status(self) -> dict:
        """
        PviObject.status
        read the object's status () 
        """
        s = create_string_buffer(b'\000' * 64)             
        self._result = PviRead( self._linkID, POBJ_ACC_STATUS, None, 0, byref(s), sizeof(s) )
        st = dict()        
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            matches = PviObject.__patternParameterPairs.findall(s)
            if matches:
                for m in matches: 
                    token = m.split("=")
                    st.update( {token[0]:token[1]})
        else:
            raise PviError(self._result)  
        return st    


    def kill(self):
        '''
        PviObject.kill: kills this object
        '''
        if self._linkID != 0:
            self._pviConnection._linkIDs.pop(self._linkID) # remove from linkIDs
            self._pviConnection._pviObjects.remove(self) # remove from PviObjects
            self._result = PviUnlink(self._linkID)
            self._linkID = 0
            if self._result != 0:
                raise PviError(self._result)
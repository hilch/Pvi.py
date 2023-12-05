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

from __future__ import annotations
from typing import Dict, Any
from ctypes import create_string_buffer, byref, sizeof
from ctypes import c_uint32, c_int32, c_uint64, c_int64, c_void_p, c_char_p
from typing import Callable, Union
import re
import inspect
from .include import *
from .Error import PviError

class PviObject():
    '''super class representing a PVI object 

    '''
    __patternParameterPairs = re.compile(r"\s*([A-Z]{2}=\w*)\s*")

    def __init__(self, parent : Union[PviObject,None], objType : T_POBJ_TYPE, name : str, **objectDescriptor : Dict[str, Any]):
        '''
        Args: 
            parent: the parent Pvi Object
            objType:   Pvi Object Type
            name: name of object in PVI hierarchy
            objectDescriptor: e.g. AT=rwe, CD="/RO=View::TempValue" see PVI documentation
        '''
        parentName = re.findall('(\\S+)',str(parent.name))[0]+'/' if parent else ''
        self._name = f'{parentName}{name}'
        self._linkID = 0
        self._objectDescriptor = objectDescriptor
        self._type = objType
        self._result = int(0)      
        self._pviError = int(0)
        self._errorChanged = None
        self._debug = False
        self._parent = parent
        if parent: # all objects but '@Pvi' have a parent
            self._connection = parent._connection # type: ignore
            self._connection.link(self) 
            self._debug = self._connection._debug
            
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
        hierarchical PVI object name

        example:
        ```
        temperature = Variable( task1, 'gHeating.status.actTemp' )
        ...
        print( "name=", temperature.name)
        ```
        results in:

        ```
        name= @Pvi/LNANSL/TCP/myArsim/mainlogic/gHeating.status.actTemp
        ```
        '''
        return self._name

    @property
    def objectName(self) -> str:
        '''
        object name

        example:
        ```
        temperature = Variable( task1, 'gHeating.status.actTemp' )
        ...
        print( "oname=", temperature.name)
        ```
        results in:

        ```
        oname= gHeating.status.actTemp
        ```
        '''         
        x = self._name.rpartition('/')
        try:
            return x[2]
        except IndexError:
            return self._name
        

    @property
    def descriptor(self) -> dict:
        '''
        object descriptor
        example:
        ```
        temperature = Variable( task1, 'gHeating.status.actTemp' )
        ...
        print( "descriptor=", temperature.name)
        ```
        results in:

        ```
        descriptor= {'CD': 'gHeating.status.actTemp', 'RF': 0}
        ```
        '''         
        return self._objectDescriptor


    @property
    def type(self) -> T_POBJ_TYPE:
        '''
        object type 

        example:
        ```
        temperature = Variable( task1, 'gHeating.status.actTemp' )
        ...
        print( "type=", temperature.type)
        ```
        results in:

        ```
        type= T_POBJ_TYPE.POBJ_PVAR
        ```
        '''                 
        return self._type



    @property
    def errorChanged(self) -> Callable:
        """
        callback for 'error changed'

        It is advisable to always check the error status '0' before accessing an object.

            Args:
                cb: callback( PviObject, int ) or callback( int )

        typical example:

        ```
        cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
        ...
        def cpuErrorChanged( error : int ):
            if error != 0:
                raise PviError(error)
  
        cpu.errorChanged = cpuErrorChanged
        ```        
        """
        if self._errorChanged:
            return self._errorChanged
        else:
            raise ValueError("Object.errorChanged is empty")


    @errorChanged.setter
    def errorChanged(self, cb : Callable):
        """
        set callback for 'error changed'.

        It is advisable to always check the error status '0' before accessing an object.

            Args:
                cb: callback( PviObject, int ) or callback( int )

        typical example:

        ```
        cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
        ...
        def cpuErrorChanged( error : int ):
            if error != 0:
                raise PviError(error)
  
        cpu.errorChanged = cpuErrorChanged
        ```

        """
        if callable(cb):
            self._errorChanged = cb
        else:
            raise TypeError("only callable allowed for Object.errorChanged")


    def _eventData( self, wParam, responseInfo ):
        """
        (internal) handle data events
        """
        self._result = PviReadResponse( wParam, None, 0 )
        if callable(self._errorChanged):
            self._errorChanged(0)             

    def _eventDataType( self, wParam, responseInfo ):
        """
        (internal) handle data type events
        """        
        self._result = PviReadResponse( wParam, None, 0 ) 
       

    def _eventUploadStream( self, wParam, responseInfo, dataLen : int ):  
        """
        (internal) handle uploading data streams
        """                   
        self._result = PviReadResponse( wParam, None, 0 ) 


    def _eventStatus( self, wParam, responseInfo ):
        pass


    def _eventError( self, wParam, responseInfo ):
        """         
        (internal) handle error events
        """      
        self._result = PviReadResponse( wParam, None, 0 )
        if callable(self._errorChanged):
            sig = inspect.signature(self._errorChanged)
            if len(sig.parameters) == 1:
                self._errorChanged(responseInfo.ErrCode)
            elif len(sig.parameters) == 2:
                self._errorChanged( self, responseInfo.ErrCode)
 
    def _createAndLink(self, connection):
        """
        (internal) create object and link it
        """
        descriptor_items = []
        for key, value in self._objectDescriptor.items():
            quote = '"' if re.search( r"[\/\.\s]", str(value) ) is not None else ''
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
            # if self._type == T_POBJ_TYPE.POBJ_PVAR: # read variable's data type
            #     PviReadRequest( self._linkID, POBJ_ACC_TYPE, PVI_HMSG_NIL, SET_PVIFUNCTION, 0 )
            connection._linkIDs[self._linkID] = self # store object for backward reference  
        else:
            print( f"PviCreate {self.name} = {self._result}")
            raise PviError(self._result, self)
        return self._result                


    @property
    def externalObjects(self):
        """     
        PviObject.externalObjects : list of dict
        get a list of external objects retrieved by POBJ_ACC_LIST_EXTERN
        # only available with ANSL, not with INA2000

        example:

        ```
        cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
        ...
        print("external objects", cpu.externalObjects )
        ```

        results in:

        ```
        external objects [{'name': '$$sysconf', 'type': 'Module'}, {'name': '$arlogsys', 'type': 'Module'}
                    ...... name': 'visvc', 'type': 'Module'}]

        ```

        """    
        s = create_string_buffer(b'\000' * 65536)   
        self._result = PviRead( self._linkID, POBJ_ACC_LIST_EXTERN, None, 0, byref(s), sizeof(s) )
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            li1 = [r.split(' OT=') for r in s.split('\t')]
            li2 = [{ 'name': r[0], 'type' : r[1] } for r in li1]
            return li2
        else: 
            raise PviError(self._result, self)


    @property       
    def status(self) -> dict:
        """
        PviObject.status
        read the object's status

        example:

        ```
        cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
        task1 = Task( cpu, 'mainlogic')
        temperature = Variable( task1, 'gHeating.status.actTemp' )
        ...
        print("status=", cpu.status )
        ```

        results in:

        ```
        cpu.status= {'ST': 'WarmStart', 'RunState': 'RUN'}
        task1.status {'ST': 'Running'}
        temperature.status= {'ST': 'Var', 'SC': 'g'}
        ```
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
            raise PviError(self._result, self)  
        return st    

    
    @status.setter
    def status(self, st : bytes):
        s = create_string_buffer(st)
        self._result = PviWrite( self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 ) 
        if self._result:
            raise PviError(self._result, self)        

    def __del__(self):
        self.kill

    def kill(self):
        '''
        PviObject.kill: kills this object
        this should be called when object is not beeing used anymore
        to save PVI resources
        '''
        if self._linkID != 0 and self._connection != None:
            self._connection._linkIDs.pop(self._linkID) # remove from linkIDs
            self._connection._pviObjects.remove(self) # remove from PviObjects
            self._result = PviUnlink(self._linkID)
            self._linkID = 0
            if self._result != 0:
                raise PviError(self._result, self)

    
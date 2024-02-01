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
from typing import Callable, Union
import re
import ast
import inspect
import logging
from .include import *
from .Error import PviError
from .Helpers import dictFromParameterPairString, debuglog



class PviObject():
    '''super class representing a PVI object 

    '''

    def __init__(self, parent : Union[PviObject,None], objType : T_POBJ_TYPE, name : str, **objectDescriptor : Dict[str, Any]):
        '''
        Args: 
            parent: the parent Pvi Object
            objType:   Pvi Object Type
            name: name of object in PVI hierarchy
            objectDescriptor: e.g. AT=rwe, CD="/RO=View::TempValue" see PVI documentation
            LinkDescriptor: eg. "EV=eds" or {"EV":"eds"}
        '''
        self._logger = logging.getLogger("pvipy")
        parentName = re.findall('(\\S+)',str(parent.name))[0]+'/' if parent else ''
        self._name = f'{parentName}{name}'        
        self._userName = name
        if 'CD' in objectDescriptor and (objType == T_POBJ_TYPE.POBJ_MODULE or objType == T_POBJ_TYPE.POBJ_TASK or objType == T_POBJ_TYPE.POBJ_PVAR):
            cd = str(objectDescriptor['CD']).lstrip()
            m = re.match(r"(\/RO\s*=\s*)?(\w[\w\.]*)", cd)
            if m: # PLC object name is entered in CD
                ro = m[2]
                if ro != name:
                    self._name = f'{parentName}{ro}'                    
            else: # pLC object name is not given so derive it from user assigned name
                self._name = f'{parentName}{self._userName}'
        self._linkID = 0
        self._linkDescriptor = {'EV':'ed'}
        if objType == T_POBJ_TYPE.POBJ_CPU or objType == T_POBJ_TYPE.POBJ_MODULE:
            self._linkDescriptor.update({ 'EV' : 'ep' }) # need this for downloading proceeding info

        # pick the link descriptor if given
        if 'LinkDescriptor' in objectDescriptor:
            cn = str(objectDescriptor['LinkDescriptor'])
            try: # try if link descriptor is given as dict
                ld = ast.literal_eval(cn)
                for key, value in ld.items:
                    self._linkDescriptor.update({str.upper(key) : value})              
            except SyntaxError: # otherwise it is given as str            
                self._linkDescriptor.update( dictFromParameterPairString(cn))
            del objectDescriptor['LinkDescriptor']  # 'LinkDescriptor' must not occur in object descriptor 

        self._objectDescriptor = objectDescriptor

        self._type = objType
        self._result = int(0)      
        self._pviError = int(0)
        self._errorChanged = None
        self._parent = parent
        debuglog(f'{self._objectDescriptor} - {self._linkDescriptor}')
        if parent: # all objects but '@Pvi' have a parent
            self._connection = parent._connection # type: ignore
            self._connection.link(self) 
            
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
        name= @Pvi/LNANSL/TCP/myArsim/mainlogic/gHeating.status.actTemp
        ```
        '''
        return self._name


    @property
    def userName(self) -> str:
        '''
        user defined object name
        defaults to .objectName
        '''
        return self._userName


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
    def evmask(self) -> str:
        '''
        event mask in link descriptor

        "e": Change in error state
        "d": Data changes
        "f": Change to the data format 
        "c": Change to the connection description
        "p": Progress information about active requests 
        "s": Status changes
        "u": Change in the user tag string        
        '''
        s = create_string_buffer(b'\000' * 10)   
        self._result = PviRead( self._linkID, POBJ_ACC_EVMASK , None, 0, byref(s), sizeof(s) )
        if self._result == 0:
            s = str(s, 'ascii')
            self._linkDescriptor.update( {'EV': str(s)})
            return(s)
        else:
            raise PviError(self._result, self)         

    @evmask.setter
    def evmask(self, mask : str ):
        s = create_string_buffer(mask.encode())

        self._result = PviWrite( self._linkID, POBJ_ACC_EVMASK, byref(s), sizeof(s), None, 0 ) 
        if self._result == 0:
            self._linkDescriptor.update( {'EV': str(s)})
        else:
            raise PviError(self._result, self)      


    @property
    def userTag(self) -> str:
        '''
        user tag

        Typical usage example:
        ```
        temperature = Variable( task1, name='gHeating.status.actTemp', UT="actual water temperature" )        
        ```
        '''
        s = create_string_buffer(b'\000' * 4096)   
        self._result = PviRead( self._linkID, POBJ_ACC_USERTAG , None, 0, byref(s), sizeof(s) )
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
            self._objectDescriptor.update({ 'UT': s}) # type: ignore
            return s            
        else:
            raise PviError(self._result, self)  

    @userTag.setter
    def userTag(self, tag : str ):
        '''
        user tag
        '''
        s = create_string_buffer(tag.encode('ascii'))
        self._result = PviWrite( self._linkID, POBJ_ACC_USERTAG, byref(s), sizeof(s), None, 0 ) 
        if self._result:
            raise PviError(self._result, self)  
        self._objectDescriptor.update({ 'UT': tag}) # type: ignore

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
        ld = ''
        for key, value in self._linkDescriptor.items():
            ld += f'{key}={value} '
        self._result = PviCreate( byref(linkID), bytes(self._name, 'ascii'),
            self._type, bytes(descr, 'ascii'), PVI_HMSG_NIL, SET_PVIFUNCTION, 0, ld.encode())
        debuglog(f'PviCreate({self.name}, { T_POBJ_TYPE(self._type)  }, {self._objectDescriptor}) = {self._result}, linkID={linkID.value}')          
        if self._result == 0: # object creation successful
            self._linkID = linkID.value
            # if self._type == T_POBJ_TYPE.POBJ_PVAR: # read variable's data type
            #     PviReadRequest( self._linkID, POBJ_ACC_TYPE, PVI_HMSG_NIL, SET_PVIFUNCTION, 0 )
            connection._linkIDs[self._linkID] = self # store object for backward reference
        else:
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
    def version(self) ->str:
        """
        PviObject.version
        read the object's version

        """    
        s = create_string_buffer(b'\000' * 1024)             
        self._result = PviRead( self._linkID, POBJ_ACC_VERSION, None, 0, byref(s), sizeof(s) )     
        if self._result == 0:
            s = str(s, 'ascii').rstrip('\x00')
        else:
            raise PviError(self._result, self)  
        return s    



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
            st.update( dictFromParameterPairString(s))
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

    
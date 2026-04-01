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

from inspect import signature
from typing import cast, Union, List, Dict, Callable, Optional
from ctypes import create_string_buffer, byref, sizeof, wintypes
import re
import ast
import logging
from .include import *
from .Error import PviError
from .Helpers import dictFromParameterPairString, debuglog


class PviObject():
    '''super class representing a PVI object'''

    # Buffer size constants 
    _BUFFER_SIZE_SMALL: int = 64
    _BUFFER_SIZE_MEDIUM: int = 1024
    _BUFFER_SIZE_LARGE: int = 4096
    _BUFFER_SIZE_XLARGE: int = 65536

    def __init__(self, parent: Union['PviObject', None], objType: T_POBJ_TYPE, name: str, 
                 **objectDescriptor: Union[str, int, float]):
        self._logger = logging.getLogger("pvipy")
        parentName = re.findall(r'(\S+)', str(parent.name))[0] + '/' if parent else ''
        self._name = f'{parentName}{name}'
        self._userName = name
        self._linkID = 0
        self._linkDescriptor = {'EV': 'ed'}
        if objType == T_POBJ_TYPE.POBJ_CPU or objType == T_POBJ_TYPE.POBJ_MODULE:
            self._linkDescriptor.update({'EV': 'ep'})

        if 'LinkDescriptor' in objectDescriptor:
            cn = str(objectDescriptor['LinkDescriptor'])
            try:
                ld = ast.literal_eval(cn)
                for key, value in ld.items():  
                    self._linkDescriptor.update({str.upper(key): value})
            except (SyntaxError, ValueError, TypeError):  
                self._linkDescriptor.update(dictFromParameterPairString(cn))
            del objectDescriptor['LinkDescriptor']

        self._objectDescriptor = objectDescriptor
        self._type = objType
        self._result = int(0)
        self._pviError = int(0)
        self._errorChanged: Optional[Callable] = None  
        self._errorChangedArgCount = 0
        
        def statusResponse(o: 'PviObject', st: Dict[str, str]) -> None:
            pass
        self._statusResponse = statusResponse
        self._parent = parent
        self._hPvi = wintypes.DWORD()
        debuglog(f'{self._objectDescriptor} - {self._linkDescriptor}')
        if parent is not None:  
            self._connection = parent._connection
            self._hPvi = self._connection._hPvi
            self._connection.link(self)

    def __hash__(self) -> int:
        return hash((self._name, self._type))

    def __eq__(self, other) -> bool:
        return self.__hash__() == other.__hash__()

    def __str__(self) -> str:
        return f"{self._name}"

    def __repr__(self) -> str:
        return f"PviObject( name={self._name}, linkID={self._linkID} )"

    def _read_string_property(self, access_type: int, buffer_size: int) -> str:
        '''Generic helper to read string property from PVI'''
        s = create_string_buffer(b'\000' * buffer_size)
        self._result = PviXRead(self._hPvi, self._linkID, access_type, None, 0, byref(s), sizeof(s))
        if self._result != 0:
            raise PviError(self._result, self)
        return str(s, 'ascii').rstrip('\x00')

    @property
    def name(self) -> str:
        return self._name

    @property
    def userName(self) -> str:
        return self._userName

    @property
    def objectName(self) -> str:
        x = self._name.rpartition('/')
        return x[2] if x[2] else self._name

    @property
    def descriptor(self) -> dict:
        return self._objectDescriptor

    @property
    def evmask(self) -> str:
        result = self._read_string_property(POBJ_ACC_EVMASK, self._BUFFER_SIZE_SMALL)
        self._linkDescriptor.update({'EV': result})
        return result

    @evmask.setter
    def evmask(self, mask: str) -> None:
        s = create_string_buffer(mask.encode())
        self._result = PviXWrite(self._hPvi, self._linkID, POBJ_ACC_EVMASK, byref(s), sizeof(s), None, 0)
        if self._result == 0:
            self._linkDescriptor.update({'EV': str(s)})
        else:
            raise PviError(self._result, self)

    @property
    def userTag(self) -> str:
        result = self._read_string_property(POBJ_ACC_USERTAG, self._BUFFER_SIZE_LARGE)
        self._objectDescriptor.update({'UT': result})
        return result

    @userTag.setter
    def userTag(self, tag: str) -> None:
        s = create_string_buffer(tag.encode('ascii'))
        self._result = PviXWrite(self._hPvi, self._linkID, POBJ_ACC_USERTAG, byref(s), sizeof(s), None, 0)
        if self._result != 0:
            raise PviError(self._result, self)
        self._objectDescriptor.update({'UT': tag})

    @property
    def type(self) -> T_POBJ_TYPE:
        return self._type

    @property
    def errorChanged(self) -> Union[Callable[['PviObject', int], None], Callable[[int], None]]:
        if self._errorChanged is not None:  
            return self._errorChanged
        raise ValueError("Object.errorChanged is empty")

    @errorChanged.setter
    def errorChanged(self, cb: Union[Callable[['PviObject', int], None], Callable[[int], None]]) -> None:
        if callable(cb):
            self._errorChanged = cb
            self._errorChangedArgCount = len(signature(cb).parameters)
        else:
            raise TypeError("only callable allowed for Object.errorChanged")

    def _eventData(self, wParam, responseInfo) -> None:
        self._result = PviXReadResponse(self._hPvi, wParam, None, 0)
        if self._errorChanged is not None:  
            if self._errorChangedArgCount == 1:
                self._errorChanged(0)
            elif self._errorChangedArgCount == 2:
                self._errorChanged(self, 0)

    def _eventDataType(self, wParam, responseInfo) -> None:
        self._result = PviXReadResponse(self._hPvi, wParam, None, 0)

    def _eventUploadStream(self, wParam, responseInfo, dataLen: int) -> None:
        self._result = PviXReadResponse(self._hPvi, wParam, None, 0)

    def _eventStatus(self, wParam, responseInfo) -> None:
        s = create_string_buffer(self._BUFFER_SIZE_SMALL)  
        self._result = PviXReadResponse(self._hPvi, wParam, byref(s), sizeof(s))
        st = dict()
        if self._result == 0:
            s_str = str(s, 'ascii').rstrip('\x00')
            st.update(dictFromParameterPairString(s_str))
            self._statusResponse(self, st)

    def _eventError(self, wParam, responseInfo) -> None:
        self._result = PviXReadResponse(self._hPvi, wParam, None, 0)
        if self._errorChanged is not None:  
            if self._errorChangedArgCount == 1:
                cast(Callable[[int], None], self._errorChanged)(responseInfo.ErrCode)
            elif self._errorChangedArgCount == 2:
                cast(Callable[['PviObject', int], None], self._errorChanged)(self, responseInfo.ErrCode)

    def _createAndLink(self, connection) -> int:
        descriptor_items = []
        for key, value in self._objectDescriptor.items():
            quote = '"' if re.search(r'[\/\.\s]', str(value)) is not None else ''
            descriptor_items += [f'{key}={quote}{value}{quote}']
        descr = ' '.join(descriptor_items)
        linkID = wintypes.DWORD(0)
        ld = ''
        for key, value in self._linkDescriptor.items():
            ld += f'{key}={value} '
        self._result = PviXCreate(self._hPvi, byref(linkID), bytes(self._name, 'ascii'),
            self._type, bytes(descr, 'ascii'), PVI_HMSG_NIL, SET_PVIFUNCTION, 0, ld.encode())
        if self._result == 0:
            self._linkID = linkID.value
            connection._linkIDs[self._linkID] = self
        else:
            raise PviError(self._result, self)
        return self._result

    @property
    def externalObjects(self) -> List[Dict[str, str]]:
        s = create_string_buffer(b'\000' * self._BUFFER_SIZE_XLARGE)  
        self._result = PviXRead(self._hPvi, self._linkID, POBJ_ACC_LIST_EXTERN, None, 0, byref(s), sizeof(s))
        if self._result == 0:
            s_str = str(s, 'ascii').rstrip('\x00')
            li1 = [r.split(' OT=') for r in s_str.split('\t')]
            li2 = [{'name': r[0], 'type': r[1]} for r in li1]
            return li2
        raise PviError(self._result, self)

    @property
    def version(self) -> str:
        return self._read_string_property(POBJ_ACC_VERSION, self._BUFFER_SIZE_MEDIUM)

    @property
    def status(self) -> dict:
        s = create_string_buffer(b'\000' * self._BUFFER_SIZE_SMALL)  
        self._result = PviXRead(self._hPvi, self._linkID, POBJ_ACC_STATUS, None, 0, byref(s), sizeof(s))
        st = dict()
        if self._result == 0:
            s_str = str(s, 'ascii').rstrip('\x00')
            st.update(dictFromParameterPairString(s_str))
        else:
            raise PviError(self._result, self)
        return st

    @status.setter
    def status(self, st: bytes) -> None:
        s = create_string_buffer(st)
        self._result = PviXWrite(self._hPvi, self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0)
        if self._result != 0:
            raise PviError(self._result, self)

    def readRequestStatus(self, callback: Callable[['PviObject', Dict[str, str]], None]) -> None:
        if callable(callback):
            self._statusResponse = callback
            self._result = PviXReadRequest(self._hPvi, self._linkID, POBJ_ACC_STATUS, 1, SET_PVIFUNCTION, 0)
            if self._result != 0:
                raise PviError(self._result, self)
        else:
            raise TypeError("Wrong type for Parameter 'callback'")

    def __del__(self) -> None:
        self.kill()

    def kill(self) -> None:
        if self._linkID != 0 and self._connection is not None:  
            self._connection._linkIDs.pop(self._linkID)
            self._connection._pviObjects.remove(self)
            self._result = PviXUnlink(self._hPvi, self._linkID)
            self._linkID = 0
            if self._result != 0 and self._result != 12045:
                raise PviError(self._result, self)
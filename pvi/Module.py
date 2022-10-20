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
from .include import *
from .Object import PviObject
from .Error import PviError


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

  
    def _eventUploadStream( self, wParam, responseInfo, dataLen : int ):
        s = create_string_buffer(dataLen)       
        self._result = PviReadResponse( wParam, s, sizeof(s) )
        if self._result == 0:
            if self._uploaded:
                self._uploaded(s.raw)
        else:
            raise PviError(self._result)


    def _eventProceeding( self, wParam, responseInfo : T_RESPONSE_INFO ):    
        proceedingInfo = T_PROCEEDING_INFO()
        self._result = PviReadResponse( wParam, byref(proceedingInfo), sizeof(proceedingInfo) )
        if self._result == 0:
            if self._progress:
                self._progress(int(proceedingInfo.Percent))
        else:
            raise PviError(self._result)               


    def upload(self, **args ):
        '''
        Module: upload
        '''
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
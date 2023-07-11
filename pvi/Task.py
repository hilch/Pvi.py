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


class Task(PviObject):
    def __init__( self, parent, name, **objectDescriptor ):
        if parent._type != T_POBJ_TYPE.POBJ_CPU:
            raise PviError(12009, self)
        objectDescriptor.update({'CD':name})
        super().__init__( parent, 'POBJ_TASK', name, **objectDescriptor)

    def start(self):
        '''
        Task: start a task
        '''
        s = create_string_buffer(b"ST=Start")
        self._result = PviWrite( self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result, self)  

    def resume(self):
        '''
        Task: resume a stopped task
        '''
        s = create_string_buffer(b"ST=Resume")
        self._result = PviWrite( self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result, self)                         

    def stop(self):
        '''
        Task: stop task
        '''
        s = create_string_buffer(b"ST=Stop")
        self._result = PviWrite( self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result, self)                  

    @property
    def variables(self):
        """     
        Task.variables : list of str
        get a list of local variables
        """
        s = create_string_buffer(b'\000' * 65536)   
        self._result = PviRead( self._linkID, POBJ_ACC_LIST_PVAR, None, 0, byref(s), sizeof(s) )
        if( self._result == 0 ):
            s = str(s, 'ascii').rstrip('\x00')
            variables = [v.split(' ')[0] for v in s.split('\t')]
            return variables
        else:
            raise PviError(self._result, self)


    def __repr__(self):
        return f"Task( name={self._name}, linkID={self._linkID} )"


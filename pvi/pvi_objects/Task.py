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

from typing import List, Union
from ctypes import create_string_buffer, byref, sizeof
from .include import *
from .Object import PviObject
from .Error import PviError


class Task(PviObject):
    '''representing a task object

    SNMP : can be used but is not necessary

    Typical usage example:
    ```
    cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
    task1 = Task( cpu, 'mainlogic')
    temperature = Variable( task1, 'gHeating.status.actTemp' )
    ```       
    '''
    def __init__( self, parent : PviObject, name : str, **objectDescriptor: Union[str,int, float]):
        '''
        Args:
            parent: CPU object  
            name : name of the task in PVI hierarchy. Will be used for name of task in plc if possible.
            objectDescriptor : 
                ANSL & INA2000 : see PVI documentation for details  
            
        '''
        if parent.type != T_POBJ_TYPE.POBJ_CPU:
            raise PviError(12009, self)
        if 'CD' not in objectDescriptor:
            objectDescriptor.update({'CD':name})
        super().__init__( parent, T_POBJ_TYPE.POBJ_TASK, name, **objectDescriptor)


    @property
    def status(self) -> dict:
        '''
        read the task status        
        '''
        return super().status


    @status.setter
    def status(self, status : str ):
        '''
        sets the task status
        
        Args:
            status: 'Start', 'Stop', 'Resume', 'Cycle(<x<)'
        '''        
        s = create_string_buffer(b"ST=" + status.encode())
        self._result = PviXWrite( self._hPvi, self._linkID, POBJ_ACC_STATUS, byref(s), sizeof(s), None, 0 )
        if self._result != 0:
            raise PviError(self._result, self)


    def start(self)->None:
        '''
        start a task

        Returns:
            True if status was changed
        '''
        try:
            self.status = "Start"
        except PviError as e:
            if e.number != 11166:
                raise e


    def cycle(self, numberOfCycles : int = 1)->None:
        '''
        defines cycles for resume

        Args:
            numberOfCycles: number of single steps
        '''
        self.status = f"Cycle({numberOfCycles})"


    def resume(self)->None:
        '''
        resume a stopped task
        '''
        try:
            self.status = "Resume"
        except PviError as e:
            if e.number != 11166:
                raise e


    def stop(self)->None:
        '''
        stop task
        '''
        try:
            self.status = "Stop" 
        except PviError as e:
            if e.number != 11166:
                raise e


    @property
    def variables(self)-> List[str]:
        '''
        list of local variables
        '''
        s = create_string_buffer(b'\000' * 65536)   
        self._result = PviXRead( self._hPvi, self._linkID, POBJ_ACC_LIST_PVAR, None, 0, byref(s), sizeof(s) )
        if( self._result == 0 ):
            s = str(s, 'ascii').rstrip('\x00')
            variables = [v.split(' ')[0] for v in s.split('\t')]
            return variables
        else:
            raise PviError(self._result, self)


    def __repr__(self):
        return f"Task( name={self._name}, linkID={self._linkID} )"


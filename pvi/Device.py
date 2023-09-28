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

from .include import *
from .Object import PviObject, PviObjectDescriptor
from .Error import PviError


class Device(PviObject):
    '''class representing a device

        Typical usage example:
        ```
        line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
        device = Device( line, 'TCP', CD='/IF=TcpIp' )
        ```    
    '''
    def __init__( self, parent : PviObject, name : str, **objectDescriptor : PviObjectDescriptor):
        '''
        Args:
            parent : line object  
            name : the device's name in PVI hierarchy, e.g. 'TCP'  
            objectDescriptor :  see PVI documentation for details
                ANSL : CD='/IF=TcpIp'
                INA2000 : e.g. CD='/IF=com1' or CD='/IF='tcpip /SA=113' or CD='inacan1'
                SNMP : CD='/IF=snmp' 
        '''
        if parent._type != T_POBJ_TYPE.POBJ_LINE:
            raise PviError(12009)            
        super().__init__( parent, 'POBJ_DEVICE', name, **objectDescriptor)


    def __repr__(self):
        return f"Device( name={self._name}, linkID={self._linkID} )"


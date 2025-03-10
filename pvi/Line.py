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

from typing import Union
from .include import *
from .Object import PviObject
from .Error import PviError

# ----------------------------------------------------------------------------------
class Line(PviObject):
    '''class representing a PVI Line

        Typical usage example:
        ```
        pviConnection = Connection()
        line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
        device = Device( line, 'TCP', CD='/IF=TcpIp' )
        ```
    '''
    def __init__( self, parent : PviObject, name : str, **objectDescriptor: Union[str,int, float]):
        '''
        Args: 
            parent : PVI connection's root object
            name : name of the line in PVI hierarchy, e.g. 'LNANSL'
            objectDescriptor: 
                ANSL : CD='LNANSL'  
                INA2000 : CD='LNINA2'  
                SNMP : CD='LNSNMP'

        '''
        if parent.type != T_POBJ_TYPE.POBJ_PVI:
            raise PviError(12009, self)         
        super().__init__( parent, T_POBJ_TYPE.POBJ_LINE, name, **objectDescriptor)

    def __repr__(self):
        return f"Line( name={self._name}, linkID={self._linkID} )"
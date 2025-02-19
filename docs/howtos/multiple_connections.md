# Connections to multiple PVI managers

starting with V 1.2.4 Pvi.py allows the application to be able to communicate with several PVI Managers on different computers.
see [Online Help](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Fcore%2Fpvifuncinitialize.htm) for details.

e.g.

```python
from pvi import *

pviConnection1 = Connection() # start a Pvi connection to local PVI manager
pviConnection2 = Connection(IP='192.168.182.128', PN=20000 ) # start a remote Pvi
```

## Examples

### [multiple1.py](https://github.com/hilch/Pvi.py/tree/main/examples/multiple1.py) (ANSL)

this example demonstrates how to connect to two PVI managers simultaneously.

### [multiple2.py](https://github.com/hilch/Pvi.py/tree/main/examples/multiple2.py) (ANSL)

this example demonstrates how to connect to two PVI managers simultaneously.
this is similar to multiple1.py but CPU2 connection now runs in a separate thread

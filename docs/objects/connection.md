# Overview

A 'Connection' represents the connection to the ['PVI manager'](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Fcore%2Fpvimanager.htm) (PviMan.exe).

It is responsible for managing all types of process data -- from simple process variables to lists and program/data objects. PVI Manager organizes process data with regard to both timing and direction. That means PVI Manager uses the specifications from the application to determine which data is transferred via which device and medium from or to a certain station.

The PVI Manager usually runs on the local machine, either as a normal Windows task or as a Windows service.

The 'Connection' is the parent object of a ['Line'](line.md).
(more precisely: the PVI Manager basis object 'Pvi' is actually the root object, but it is accessible via the 'Connection' )

Example:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
```

Reference: [Connection object](../reference/connection.md)

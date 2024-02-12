# Overview

A 'Cpu' represents a PLC in a network.

The 'Cpu' is the parent of a ['Task'](task.md) or a (global) ['Variable'](variable.md) or a ['Module'](module.md).

Furthermore a 'Cpu' can be restarted (cold/warm) or be used to create a module on the PLC.

It is advisable to always use callback 'errorChanged' and check for status '0' before accessing an Object that is located on an Cpu e.g.

```python
cpu = Cpu( device, 'myCpu', CD='/IP=10.43.50.244 /COMT=3000' )
    ...

def cpuErrorChanged( error : int):

    if error == 0:
        # do something useful
        ....
    else:
        # not yet connected or in error state
        ...

cpu.errorChanged = cpuErrorChanged

pviConnection.start()
```

## [ANSL](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnansl%2Fpvilnanslcpu.htm)

The ANSL CPU object is used to define the PLC within a network and to set the parameters of the ANSL communication connection.

Example:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myCpu', CD='/IP=10.43.50.244 /COMT=3000' )
```

Connect to IP address 10.43.50.244 with a communication timeout of 3000 ms.

## [INA2000](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2cpu.htm)

The INA2000 CPU object is used to identify the PLC in a network or using (INA-) Routing and to set the connection parameters for communication.

### [Serial connected PLC](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2cpuserial.htm)

Example:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'serial', CD='/IF=com1 /BD=57600 /PA=2' )
cpu = Cpu( device, 'myCpu', CD='/RT=400' )
```

Use COM1 to connect with 57600 Baud and Even Parity.
Connect with a response timeout of 400 ms.

### [Ethernet UDP communication](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2cpuethernet.htm)

Example 1:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'TCP', CD='/IF=TcpIp /SA=113' )
cpu = Cpu( device, 'myPP65', CD='/DA=5 /RT=200' )
```

Connect to INA node 5 with a response timeout of 200 ms. Since we use broadcasting an IP address is not required.

Example 2:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'TCP', CD='/IF=TcpIp /SA=113' )
cpu = Cpu( device, 'myPP65', CD='/DAIP=10.43.50.244 /RT=200' )
```

Connect to IP address 10.43.50.244 ignoring INA node numbers with a response timeout of 200 ms.
Even INA node addressing is not used we need to define a unique 'source address' /SA for the device.

### [CAN station](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2cpucan.htm)

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'inacan', CD='/IF=inacan3 /CNO=1 /SA=3' )
cpu = Cpu( device, 'myPP65', CD='/DA=13 /RT=600' )
```

Use channel '1' of local installed B&R CAN Adapter as configured via the "CAN devices" menu item in the Control Panel.
Act as INA node 3. Connects to INA node 13 with a response timeout of 600 ms.

## SNMP

Can be specified as an additional locical level but not required.

Reference: [Cpu object](../reference/cpu.md)
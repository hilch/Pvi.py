# Overview

A 'Device' represents the physics of the network communication or a communication device.

The 'Device' is the parent for a ['Cpu'](cpu.md).

Depending on the 'Line' used there are different 'Devices' possible:

## [ANSL](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnansl%2Fpvilnansldevice.htm) 

### [`tcpip`](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnansl%2Fpvilnanslcommethernet.htm)

ANSL only supports Ethernet TCP/IP communication.

Example:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
```

Use ANSL Tcp/Ip communication.

### [ArSim](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnansl%2Fpvilnanslcommar000.htm)

Communication with ARsim takes place via an Ethernet TCP device and with local IP address 127.0.0.1

## [INA2000](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2device.htm)

### [`com<x>`](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2deviceserial.htm)

Serial device. Serial communication can only be operated as a point-to-point connection (RS232 or RS422).
A RS485 connection (two-wire) is not possible.

Example:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'serial', CD='/IF=com1 /BD=57600 /PA=2' )
```

Use COM1 to connect with 57600 Baud and Even Parity.

### [`tcpip`](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2deviceethernet.htm)

INA2000 Ethernet UDP/IP communication.

Example:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'TCP', CD='/IF=TcpIp /SA=13' )
```

Use UDP/IP communication and operate with node INA number 13.

### [`modem<x>`](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2devicemodem.htm)

TAPI modem device.

Example:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'modem', CD="/IF=modem1 /MO='ZyXEL MODEM Omni 288S' /TN='+43(7748)999'" )
```

Use local installed Modem as it appears in the Setup dialog box (Control Panel -> Modems) and connect to the given telephone number.

### [`inacan<x>`](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2devicecan.htm)

CAN communication is operated as an INA2000 network with a maximum of 32 stations (can be expanded to 255). 
CAN node numbers are used to differentiate between individual stations.

Example:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'inacan', CD='/IF=inacan3 /CNO=1 /SA=3' )
```

Use channel '1' of local installed B&R CAN Adapter as configured via the "CAN devices" menu item in the Control Panel.
Act as INA node 3.

## [SNMP](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnsnmp%2Fpvilnsnmpcomm.htm)

### [`snmp`](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnsnmp%2Fpvilnsnmpdevice.htm)

SNMP (UDP) communication

Example:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNSNMP', CD='LNSNMP')
device = Device( line, 'Device', CD='/IF=snmp /RT=2000' )
```

Use SNMP communication with a response timeout of 2000 ms

Reference: [Device object](../reference/device.md)

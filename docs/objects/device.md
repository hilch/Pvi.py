# Overview

A 'Device' represents the physics of the network communication or a communication device.

The 'Device' is the parent for a 'Cpu'.

Depending on the 'Line' used there are different 'Devices' possible:

## ANSL 
### `tcpip`
ANSL only supports Ethernet TCP/IP communication.

Example: 
```
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
```

Use ANSL Tcp/Ip communication.


## INA2000     
### `com<x>`
Serial device. Serial communication can only be operated as a point-to-point connection (RS232 or RS422).
A RS485 connection (two-wire) is not possible.

Example: 
```
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'serial', CD='/IF=com1 /BD=57600 /PA=2' )
```
Use COM1 to connect with 57600 Baud and Even Parity.


### `tcpip`
INA2000 Ethernet UDP/IP communication.

Example: 
```
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'TCP', CD='/IF=TcpIp /SA=13' )
```
Use UDP/IP communication and operate with node INA number 13.


### `modem<x>`
TAPI modem device.

Example: 
```
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'modem', CD="/IF=modem1 /MO='ZyXEL MODEM Omni 288S' /TN='+43(7748)999'" )
```

Use local installed Modem as it appears in the Setup dialog box (Control Panel -> Modems) and connect to the given telephone number.

### `inacan<x>`

CAN communication is operated as an INA2000 network with a maximum of 32 stations (can be expanded to 255). 
CAN node numbers are used to differentiate between individual stations.

Example: 
```
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'inacan', CD='/IF=inacan3 /CNO=1 /SA=3' )
```

Use channel '1' of local installed B&R CAN Adapter as configured via the "CAN devices" menu item in the Control Panel.
Act as INA node 3.

## SNMP

### `snmp`

SNMP (UDP) communication 

Example:

```
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNSNMP', CD='LNSNMP')
device = Device( line, 'Device', CD='/IF=snmp /RT=2000' )
```

Use SNMP communication with a response timeout of 2000 ms

Reference: [Device object](../reference/device.md)

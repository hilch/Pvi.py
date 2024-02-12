# Overview

A 'Station' represents a station in a network.

## ANSL

Can be specified as an additional logical level, but is not really required.

## INA2000

Can be specified as an additional logical level, but is not really required.

## [SNMP](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnsnmp%2Fpvilnsnmpstation.htm)

Represents the MAC address and specifies a particular PLC.

Example:

```python
from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNSNMP', CD='LNSNMP')
device = Device( line, 'Device', CD='/IF=snmp /RT=2000' )
station = Station( device, 'station', CD='/CN=00-60-65-02-f0-2c' )
```

Use SNMP communication with a response timeout of 2000 ms.
Connect to the PLC ETH port with MAC 00-60-65-02-f0-2c

Reference: [Station object](../reference/station.md)

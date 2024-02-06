# Overview

A 'PVI Line' is a protocol driver.

The basic task of a 'PVI Line' is to connect PVI objects (service objects) with objects outside of PVI. 

The line is also responsible for communicating with B&R controllers (PLCs) and determines the communication protocol to be used to do so.

The represention of a PVI Line is a 'Line' Object

The 'Line' is the parent of a ['Device'](device.md).

[PVI contains the following lines (line servers)](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Fpvilineserver.htm)

Line name        | Name             | usage
-----------------|------------------|------------------
LNANSL           | ANSL line:       | Communication with the ANSL protocol (was introduced with PVI 4.1.03; is only available for SG4 targets from AR version 4.08).  
LNINA2           | INA2000 line     | Communication with the INA2000 protocol (SG3, SGC, SG4).  
LNNET2           | NET2000 line     | Communication with the NET2000 protocol (SG3, SGC, SG4).  
LNMINI           | MININET line     | Communication with the MININET protocol (SG2)  
LNDCAN           | Direct CAN line  | Sending and receiving CAN messages  
LNSNMP           | SNMP line        | Access to the SNMP variables of a B&R PLC.  
LNADI            | ADI line         | Access to B&R Automation Device Interface (ADI) functions.  
LNMTC            | MTC line         | Access to Maintenance Controller (MTC) functions  
LNMODBUS         | MODBUS line      | Communication with MODBUS TCP controller.  

Currently Pvi.py supports LNANSL, LNINA2 and LNSNMP only.

## [ANSL](https://help.br-automation.com/#/en/4/automationnet/pvibase/lines/lnansl/pvilnansl.htm)

Example:

```python
from pvi import *
pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
```

## [INA2000](https://help.br-automation.com/#/en/4/automationnet/pvibase/lines/lnina2/pvilnina2.htm)

Example:

```python
from pvi import *
pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
```

## [SNMP](https://help.br-automation.com/#/en/4/automationnet/pvibase/lines/lnsnmp/pvilnsnmp.htm)

Example:

```python
from pvi import *
pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNSNMP', CD='LNSNMP')
```

Reference: [Line object](../reference/line.md)
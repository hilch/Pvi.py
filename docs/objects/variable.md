# Overview

A 'Variable' represents PLC variables (PVs) or link nodes when using ANSL or INA2000.
A link node represents the status of a connection between a PV and an I/O point.

When using SNMP a 'Variable' represents an SNMP variable or a PLC or service object in the SNMP library.

The 'Variable' is used to read and/or write the corresponding variable object on a PLC.

The parameter CD is used to specify the name of the variable on the PLC.
IF CD is omitted the PVI object name is used instead.

The parameter RF is used to specify the refresh rate given in milliseconds.
If RF is omitted RF=0 is used which means the variable will be read only once.

The parameter AF can be used to specify the access type.
If AT os omitted AT=rw is used which allows reading and writing.

## [ANSL](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnansl%2Fpvilnansl.htm)

Example:

```python
temperature = Variable( task1, 'gHeating.status.actTemp', RF=1000 )
```

Get read and write access to PLC variable 'gHeating.status.actTemp' and defines a refresh rate of 1000 ms.

## [INA2000](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2pvar.htm)

Example:

```python
temperature = Variable( task1, 'gHeating.status.actTemp', RF=1000  )
```

Get read and write access to PLC variable 'gHeating.status.actTemp' and defines a refresh rate of 1000 ms.

## [SNMP](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnsnmp%2Fpvilnsnmppvar.htm)

An SNMP variable object represents an SNMP variable or a PLC or service object in the SNMP library. 

The SNMP variable or the service object is determined by the connection name of the variable object. 
Case sensitive. All names are predefined in the SNMP line.

see GUID ed28a386-f8af-475e-a114-9e6ba72d00ac for more details.

Example:

```python
snmpVariable1 = Variable( station, 'ipAddress')
```

snmpVariable1 points to the predefined SNMP variable 'ipAddress' which contains the current IP address.

Reference: [Variable object](../reference/variable.md)
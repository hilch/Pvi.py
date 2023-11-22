# Overview

A 'Module' represents a module that *exists* on the PLC.

The parameter CD is used to specify the name of the module on the PLC.
IF CD is omitted the PVI object name is used instead.


## ANSL

Example:

```
module = Module( cpu, 'bigmod' )
```

## INA2000

Example:

```
module = Module( cpu, 'bigmod' )
```

## SNMP

Can be specified, but not required.

Reference: [Module object](../reference/module.md)
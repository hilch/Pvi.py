# Overview

A 'Task' represents a PLC task.

The 'Task' is the parent of a 'Variable'.

Furthermore a 'Task' can be stopped, started or resumed.

The parameter CD is used to specify the name of the task on the PLC.
IF CD is omitted the PVI object name is used instead.

## ANSL

Example:

```
task1 = Task( cpu, 'task1', CD ='mainlogic')
```

Create a PVI Object named 'task1' to connect to PLC task 'mainlogic'.

In most cases we can use the taskname on PLC as PVI object name so the parameter CD can be omitted:
```
task1 = Task( cpu, 'mainlogic')
```


## INA2000

Example:

```
task1 = Task( cpu, 'task1', CD ='mainlogic')
```

Create a PVI Object named 'task1' to connect to PLC task 'mainlogic'.

In most cases we can use the taskname on PLC as PVI object name so the parameter CD can be omitted:
```
task1 = Task( cpu, 'mainlogic')
```


## SNMP

Can be specified, but not required.


Reference: [Task object](../reference/task.md)
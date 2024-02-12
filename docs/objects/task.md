# Overview

A 'Task' represents a [PLC task](https://help.br-automation.com/#/en/4/automationruntime%2Ftaskclasses%2Ftasks%2Ftasks.html).

The 'Task' is the parent of a ['Variable'](variable.md).

Furthermore a 'Task' can be stopped, started or resumed.

The parameter CD is used to specify the name of the task on the PLC.
IF CD is omitted the PVI object name is used instead.

## [ANSL](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnansl%2Fpvilnansltask.htm)

Example:

```python
task1 = Task( cpu, 'task1', CD ='mainlogic')
```

Create a PVI Object named 'task1' to connect to PLC task 'mainlogic'.

In most cases we can use the taskname on PLC as PVI object name so the parameter CD can be omitted:

```python
task1 = Task( cpu, 'mainlogic')
```

## [INA2000](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2task.htm)

Example:

```python
task1 = Task( cpu, 'task1', CD ='mainlogic')
```

Create a PVI Object named 'task1' to connect to PLC task 'mainlogic'.

In most cases we can use the taskname on PLC as PVI object name so the parameter CD can be omitted:

```python
task1 = Task( cpu, 'mainlogic')
```

## SNMP

Can be specified, but not required.

Reference: [Task object](../reference/task.md)
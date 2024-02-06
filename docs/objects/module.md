# Overview

A 'Module' represents a module that *exists* on the PLC.

The parameter CD is used to specify the name of the module on the PLC.
IF CD is omitted the PVI object name is used instead.

## [ANSL](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnansl%2Fpvilnanslmodule.htm)

Example:

```python
module = Module( cpu, 'bigmod' )
```

Some module types can be translated during upload / download. See ['Translating BR modules'](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnansl%2Fpvilnanslmodtranslation.htm) for more info.

## [INA2000](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2module.htm)

Example:

```python
module = Module( cpu, 'bigmod' )
```

Some module types can be translated during upload / download. See ['Translating BR modules'](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2modtranslation.htm) for more info.

## SNMP

Can be specified, but not required.

Reference: [Module object](../reference/module.md)
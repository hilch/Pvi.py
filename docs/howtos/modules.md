# Modules

A Module is a data container for code or data. The file representation of a Module is a *.br file.

## [Data Objects](https://help.br-automation.com/#/en/4/programming%2Fdataobjects%2Fprogrammingmodel_dataobjects.html)

A data object is a data container in the form of a B&R module. It can be used by other software objects on the target system as a data table (e.g. for configuration) or as data memory. Automation Studio provides functions for handling data objects in the [DataObj library](https://help.br-automation.com/#/en/4/libraries%2Fdataobj%2Fdataobj.html).

Data objects can be used for e.g. a [simple recipe system](https://github.com/hilch/dataobj-recipe)

There are some system data objects available:

- [CNC data objects](https://help.br-automation.com/#/en/4/programming/dataobjects/cnc/programming_externalconfiguration_cncdataobjects_general.html)
- [NC data objects](https://help.br-automation.com/#/en/4/programming/dataobjects/nc/programming_externalconfiguration_ncdataobjects_general.html)
- [Cams](https://help.br-automation.com/#/en/4/programming/dataobjects/camprofiles/programming_externalconfiguration_camprofiles_general.html)

[ANSL](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnansl%2Fpvilnanslmodtranslation.htm) and [INA2000](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2modtranslation.htm) provide some functionality to translate modules.

## Examples

find the following examples on GitHub [github.com/hilch/Pvi.py](https://github.com/hilch/Pvi.py/tree/main/examples)

### [modules1.py](https://github.com/hilch/Pvi.py/tree/main/examples/modules1.py) (ANSL)

this simple example creates a module on CPU by downloading a bytestream and checks if it exists

### [modules2.py](https://github.com/hilch/Pvi.py/tree/main/examples/modules2.py) (ANSL)

this simple example creates a module on CPU by downloading a bytestream and afterwards uploads it again

### [modules3.py](https://github.com/hilch/Pvi.py/tree/main/examples/modules3.py)

in this example we search for BR files (*.br) in a folder and read the type of content

# [Process Objects](https://help.br-automation.com/#/en/4/automationnet/pvibase/core/pviobjectprocess.htm)

Process objects are divided into different object types. Each object type either represents a certain logical or physical part of the communication connection or an object within the line or on the PLC.

PVI Object        | corresponding class/object in Pvi.py | Usage
------------------|--------------------------------------|------------------------
POBJ_PVI          | [Connection.root](connection.md)     | PVI Manager base object
POBJ_LINE         | [Line](line.md)                      | Represents the PVI line being used (line server)
POBJ_DEVICE       | [Device](device.md)                  | Represents the physics of the network communication or a communication device
POBJ_STATION      | [Station](station.md)                | Represents a station in a network
POBJ_CPU          | [Cpu](cpu.md)                        | Represents a PLC in a network
POBJ_MODULE       | [Module](module.md)                  | Represents a module in a station or a CPU (PLC object)
POBJ_TASK         | [Task](task.md)                      | Represents a task or process in a station, CPU, or module (PLC object)
POBJ_PVAR         | [Variable](variable.md)              | Represents a variable in a station, CPU, module, or task (PLC task), or a PVI-internal variable

The order in which the object types are listed in the table corresponds to the object hierarchy. Starting from the PVI base object, each process object is assigned to another process object.

However according to the object hierarchy, only objects with a higher-level object type can be assigned.

This means that a variable object can be assigned to all other process objects except a variable object.
A line object can only be assigned to the PVI base object.

These assignments lead to a tree structure with the PVI base object as the root

The connection name is the name of the service object being used in PVI Manager.
The connection description is defined with the CD parameter.

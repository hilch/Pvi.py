# Version history

## V1.2.1

- fix: reading arrays of structures only returned first element
- fix: Object.__del__ did not call Object.kill()
- new: Variable.dataType returns name of structure type
- new: Variable.dataType returns `<data type>[<lower index>..<higher index>]` now

## V1.2.0

- Object: the objectDescriptor can now contain a field 'LinkDescriptor'
- add Object.evmask to change link descriptor event mask
- add Object.userTag to read/write usertag string
- add Object.userName which returns the user given object name
- add Object.version
- add Cpu.stopTarget() and Cpu.diagnostics()
- add Task.cycle() for single step execution
- add Variable.hysteresis to read/write event hysteresis
- add Variable.refresh to read/write cyclic refresh time
- add Variable.attributes to read/write object attributes
- Variable.valueChanged now accepts a callback with signature ( value, Object )
- Variable/Task/Module: use name as userName if 'CD' is used for defining plc object
- add PviError.number
- fix: Variable/Task/Module c'tor: content of 'CD' was overwritten with 'name'
- add basic logging

## V1.1.0

- add parameters to Connection constructor to enable a PVI remote connection

## V1.0.0

- add mkdocs online help
- add start() and stop() to Connection to make doEvents() obsolete in many cases
- fix: parameter CD was ignored in Task and Variable and Module

## V0.0.5

- add parser for profiler files
- add examples: profiler1.py, profiler2.py

## V0.0.4

- property Object.externalObjects now throws an error if not supported (e.g. INA2000)
- add property Cpu.tasks
- add property Cpu.variables
- add property task.variables
- add examples: simple3.py, list_objects4.py, list_objects5.py, list_objects6.py, logger3.py

## V0.0.3

- uploading logger data
- converting br files with logger data
- extend signature of some callbacks
- add property 'objectName' for all objects

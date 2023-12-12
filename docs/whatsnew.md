# Version history

*V1.1.0*

- add parameters to Connection constructor to enable a PVI remote connection

*V1.0.0*

- add mkdocs online help
- add start() and stop() to Connection to make doEvents() obsolete in many cases
- fix: parameter CD was ignored in Task and Variable and Module

*V0.0.5*

- add parser for profiler files
- add examples: profiler1.py, profiler2.py

*V0.0.4*

- property Object.externalObjects now throws an error if not supported (e.g. INA2000)
- add property Cpu.tasks
- add property Cpu.variables
- add property task.variables
- add examples: simple3.py, list_objects4.py, list_objects5.py, list_objects6.py, logger3.py

*V0.0.3*

- uploading logger data
- converting br files with logger data
- extend signature of some callbacks
- add property 'objectName' for all objects


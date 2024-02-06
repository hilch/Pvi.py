# [Logger](https://help.br-automation.com/#/en/4/diagnostics_support%2Fdiagnosis%2Flogger%2Fdiagnosis_logger.html)

The Logger window in Automation Studio displays information about events that occur on a controller within the framework of an application.

## Writing loggers

These events are severe errors (e.g. cycle time violation), warnings and system messages (e.g. warm/cold restart) logged by Automation Runtime. In addition, the [ArEventLog library](https://help.br-automation.com/#/en/4/libraries/areventlog/areventlog.html) can be used to record information about processes in an application that can then be analyzed in the Logger.

## Reading from loggers

There is some support for extracting logger data from a file with [PviTransUtil.dll](https://help.br-automation.com/#/en/4/automationnet%2Fpvitransfer%2Foperation%2Flogbookint%2Fdll%2Fpvitransfer_logbookint_dll_functions.html) which comes with PviTransfer.exe e.g. [Runtime Utiliy Center](https://help.br-automation.com/#/en/4/automationnet%2Fpvitransfer%2Fpvitransfer.html)

If it is not available, Pvi.py could be an alternative.
Handling logger files is still beta since the file format is not public.
The known structure was found out by reverse engineering.

## Examples

find the following examples on GitHub [github.com/hilch/Pvi.py](https://github.com/hilch/Pvi.py/tree/main/examples)

### [logger1.py](https://github.com/hilch/Pvi.py/tree/main/examples/logger1.py) (ANSL)

this example uploads some loggers from CPU

### [logger2.py](https://github.com/hilch/Pvi.py/tree/main/examples/logger2.py) 

extract all logger from a systemdump container and save them as csv.

### [logger3.py](https://github.com/hilch/Pvi.py/tree/main/examples/logger3.py) (INA2000)

this example uploads some loggers from CPU

This is similar to logger1.py but since we use a control running < AR 4.x ANSL is not available here and we change to good old INA2000
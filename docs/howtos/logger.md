find the following examples on GitHub [github.com/hilch/Pvi.py](https://github.com/hilch/Pvi.py/tree/main/examples)


### [logger1.py](https://github.com/hilch/Pvi.py/tree/main/examples/logger1.py) (ANSL)
this example uploads some loggers from CPU

### [logger2.py](https://github.com/hilch/Pvi.py/tree/main/examples/logger2.py) 
extract all logger from a systemdump container and save them as csv.

There is some support for extracting logger data from a file with PviTransUtil.dll which comes with PviTransfer.exe.
If it is not available, Pvi.py could be an alternative.
Handling logger files is still beta since the file format is not public.
The known structure was found out by reverse engineering.

### [logger3.py](https://github.com/hilch/Pvi.py/tree/main/examples/logger3.py) (INA2000)
this example uploads some loggers from CPU

This is similar to logger1.py but since we use a control running < AR 4.x ANSL is not available here and we change to good old INA2000
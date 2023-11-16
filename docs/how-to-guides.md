
find the following examples on GitHub [github.com/hilch/Pvi.py](https://github.com/hilch/Pvi.py/tree/main/examples)

## Basics
### basics1.py (ANSL)
shows reading and writing of basic data types

## Create Lists of objects
### list_objects1.py (ANSL)
this example lists objects with 'global scope' (modules, task and global variables)
from 'coffee machine' cpu and returns status information about them

### list_objects2.py (ANSL)
this example lists global and local variables and their content

### list_objects3.py (ANSL)
this example lists all local variables of a specific task and their content

### list_objects4.py (INA2000)
this example lists objects with 'global scope' (modules, task and global variables)
from 'coffee machine' cpu and returns status information about them

This is similar to list_objects1.py but since we use a control running < AR 4.x ANSL is not available here and we change to good old INA2000

### list_objects5.py (INA2000)
this example lists global and local variables and their content

This is similar to list_objects2.py but since we use a control running < AR 4.x ANSL is not available here and we change to good old INA2000

### list_objects6.py (INA2000)
this example lists all local variables of a specific task and their content

This is similar to list_objects3.py but since we use a control running < AR 4.x ANSL is not available here and we change to good old INA2000


## Handling modules
### modules1.py (ANSL)
this simple example creates a module on CPU by downloading a bytestream and checks if it exists

### modules2.py (ANSL)
this simple example creates a module on CPU by downloading a bytestream and afterwards uploads it again

### modules3.py 
in this exammple we search for BR files (*.br) in a folder and read the type of content

## Handling logger data

### logger1.py (ANSL)
this example uploads some loggers from CPU

### logger2.py 
extract all logger from a systemdump container and save them as csv.
Handling logger files is still beta since the file format is not public.
The known structure was found out by reverse engineering.

### logger3.py (INA2000)
this example uploads some loggers from CPU

This is similar to logger1.py but since we use a control running < AR 4.x ANSL is not available here and we change to good old INA2000

## Handling profiler data

handling profiler files is still beta since the file format is not public.
The known structure was found out by reverse engineering.

### profiler1.py
extract all profiler data *.pd file and save it to csv

### profiler2.py
extract all profiler data from a systemdump container and save it to csv

## GUI
### gui1.py (ANSL)
this example shows the usage of Pvi.py in tkinter

## IO
### linknode1.py (ANSL)
this simple example just toggles an forced output

## Simple Network Managament Protocol (SNMP)
(if you are looking for a 'real' program consider to use [brsnmp](https://github.com/hilch/brsnmp) )

### browse_for_targets.py
this example searches for B&R plc in local network with PVI's 'SNMP' line and lists their properties

### set_ip_address.py
this example searches for a specific B&R plc in local network with PVI's 'SNMP' line and changes its IP address

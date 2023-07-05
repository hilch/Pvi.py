[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Made For B&R](https://github.com/hilch/BandR-badges/blob/main/Made-For-BrAutomation.svg)](https://www.br-automation.com)

# Pvi.py
Python wrapper for [B&amp;R Pvi (process visualization interface)](https://www.br-automation.com/en/products/software/automation-software/automation-netpvi/).

In times of more modern protocols like OPC-UA, this may seem a bit old-fashioned. 
But PVI has some hidden strengths and is also very versatile. 
Have a look into the documentation of the 'Lines' (ANSL, INA2000, NET2000, MTC, ADI, DCAN, SNMP, MODBUS, MININET) and what they are used for.
In most cases it is used just to communicate with B&R PLCs with 'ANSL' and 'SNMP'.
Unfortunately its native C-language interface is very complex and also PVI Services (C#) can be a high barrier to entry.
It's a lot more fun with Python !

# PVI installation and license
PVI needs a previous installation of 'PVI Development Setup' from [B&R's homepage](https://www.br-automation.com).
Without a PVI license 1TG0500.02 (+ TG Guard e.g. 0TG1000.02) PVI will run for two hours ("Trial license")
). 
After this period all PVI based programs will stop working (or will not even start).
In that case PVI-Manager must be stopped and restarted again. 
This can be very annoying if Automation Studio is being used in the background at the same time, because it then has to be restarted as well.
Contact your local B&R office to buy a valid license if trial license is not sufficient for you.

# Installation
```
pip install pvipy
```

# Usage
PVI uses a complex interface to define objects and their parameters but it is well documented
in its online help system and also in Automation Studio help system.
There is no point in repeating this here since most of its parameters still apply in this Python interface.
Instead, look at the examples to use parts from this for your programs.

# Examples

## Start here
### [simple1.py](examples/simple1.py) (ANSL)
this simple example just registers a variable, reads its value and then exit after a few seconds

### [simple2.py](examples/simple2.py) (ANSL)
this simple example just registers a variable for reading and another for writing. In fact we switch on the 'coffee machine' and watch its temperature ...

### [simple3.py](examples/simple3.py) (INA2000)
this simple example just registers a variable for reading and another for writing. In fact we switch on the 'coffee machine' and watch its temperature ...
This is similar to simple2.py but we use a control running AR 3.x. ANSL is not available here and we change to good old INA2000


## Basics
### [basics1.py](examples/basics1.py) (ANSL)
shows reading and writing of basic data types

## Create Lists of objects
### [list_objects1.py](examples/list_objects1.py) (ANSL)
this example lists objects with 'global scope' (modules, task and global variables)
from 'coffe machine' cpu and returns status information about them

### [list_objects2.py](examples/list_objects2.py) (ANSL)
this example lists global and local variables and their content

### [list_objects3.py](examples/list_objects3.py) (ANSL)
this example lists all local variables of a specific task and their content

## Handling modules
### [modules1.py](examples/modules1.py) (ANSL)
this simple example creates a module on CPU by downloading a bytestream and checks if it exists

### [modules2.py](examples/modules2.py) (ANSL)
this simple example creates a module on CPU by downloading a bytestream and afterwards uploads it again

### [modules3.py](examples/modules3.py) 
in this exammple we search for BR files (*.br) in a folder and read the type of content

## Handling logger data

### [logger1.py](examples/logger1.py) (ANSL)
this example uploads some loggers from CPU

### [logger2.py](examples/logger2.py) 
extract all logger from a systemdump container and save them as csv


## GUI
### [gui1.py](examples/gui1.py) (ANSL)
this example shows the usage of Pvi.py in tkinter

## IO
### [linknode1.py](examples/linknode1.py) (ANSL)
this simple example just toggles an forced output

## Simple Network Managament Protocol (SNMP)
(if you are looking for a 'real' program consider to use [brsnmp](https://github.com/hilch/brsnmp) )

### [browse_for_targets.py](examples/browse_for_targets.py)
this example searches for B&R plc in local network with PVI's 'SNMP' line and lists their properties

### [set_ip_address.py](examples/set_ip_address.py)
this example searches for a specific B&R plc in local network with PVI's 'SNMP' line and changes its IP address

## Test environment
Current test environment is AS4.1.17.113 / PVI 4.1.12 which can be [downloaded from B&R website](https://www.br-automation.com/en/downloads/software/automation-studio/automation-studio-41/automation-studio-v41/) and Python 3.8



[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Made For B&R](https://github.com/hilch/BandR-badges/blob/main/Made-For-BrAutomation.svg)](https://www.br-automation.com)

# Pvi.py
Python connector for B&amp;R Pvi (process visualization interface).
PVI is a complex software layer. In most cases it is used to communicate with B&R PLCs.

# PVI installation and license
PVI needs a previous installation of 'PVI Development Setup' from [B&R's homepage](https://www.br-automation.com).
Without a PVI license 1TG0500.02 (+ TG Guard e.g. 0TG1000.02) PVI will run for two hours ("Trial license")
). 
After this period all PVI based programs will stop working (or will not even start).
In that case PVI-Manager must be stopped and restarted again. 
This can be very annoying if Automation Studio is being used in the background at the same time, because it then has to be restarted as well.
Contact your local B&R office to buy a valid license if trial license is not sufficient for you.

# Usage
PVI uses a complex interface to define objects and their parameters but it is well documented
in its online help system and also in Automation Studio help system.
There is no point in repeating this here.
Instead, look at the examples to use parts from this for your programs.

# Examples

## ['simple1.py'](simple1.py)
this simple example just registers a variable, reads its value and then exit after a few seconds

## ['simple2.py'](simple2.py)
this simple example just registers a variable for reading and another for writing. In fact we switch on the 'coffee machine' and watch its temperature ...

## ['modules1.py'](modules1.py)
this simple example creates a module on CPU by downloading a bytestream and checks if it exists





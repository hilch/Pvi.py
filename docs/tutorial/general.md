# General

## Prerequisites

Of course, you have to install Python first (>= 3.8).
Pip should come with Python so install the wrapper with it:

```bash
pip install pvipy
```

PVI only makes sense if you also have a B&R PLC available.
In the simplest case, start the 'CoffeeMachine' demo project that comes with the installation of Automation Studio and run it on an ArSim Simulation.
Some examples require a few more variables, so it is easier to use the included 'CoffeeMachine' project from the [Github repository](https://github.com/hilch/Pvi.py/tree/main/tools/CoffeeMachine) in folder 'tools'.

This project was created with the not-so-new Automation Studio version 4.1.17. This version can be downloaded for free from the B&R homepage and does not require a license. If you prefer a newer version, the project must be converted, which is not always easy.

## Examples in repository

PVI uses a complex interface to define objects and their parameters but it is well documented in its online help system and also in Automation Studio help system. There is no point in repeating this here since most of its parameters still apply in this Python interface. Instead, look at the examples to use parts from this for your programs.

find the following examples on GitHub [github.com/hilch/Pvi.py](https://github.com/hilch/Pvi.py/tree/main/examples)

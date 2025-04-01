# Pvi.py

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Made For B&R](https://github.com/hilch/BandR-badges/blob/main/Made-For-BrAutomation.svg)](https://www.br-automation.com)

Python wrapper for [B&amp;R PVI (process visualization interface)](https://www.br-automation.com/en/products/software/automation-software/automation-netpvi/).

In times of more modern protocols like OPC-UA, this may seem a bit old-fashioned.
But PVI has some hidden strengths and is also very versatile.
Have a look into the documentation of the 'Lines' (ANSL, INA2000, NET2000, MTC, ADI, DCAN, SNMP, MODBUS, MININET) and what they are used for.
In most cases it is used just to communicate with B&R PLCs with 'ANSL' and 'SNMP'.
Unfortunately its native C-language interface is very complex and also PVI Services (C#) can be a high barrier to entry.
It's a lot more fun with Python !

## PVI installation and license

PVI needs a previous installation of 'PVI Development Setup' from [B&R's homepage](https://www.br-automation.com).
Without a PVI license 1TG0500.02 (+ TG Guard e.g. 0TG1000.02) PVI will run for two hours ("Trial license")).  

After this period all PVI based programs will stop working (or will not even start).
In that case PVI-Manager must be stopped and restarted again.
This can be very annoying when Automation Studio is being used in the background at the same time, because it then has to be restarted as well.
Contact your local B&R office to buy a valid license if trial license is not sufficient for you.

## Installation

```bash
pip install pvipy
```

## Usage

find the online help here: [https://hilch.github.io/Pvi.py/](https://hilch.github.io/Pvi.py/)

or just jump to the [examples](https://github.com/hilch/Pvi.py/tree/main/examples) in this repository.

## Test environment

Current test environment is AS4.1.17.113 / PVI 4.1.12 which can be [downloaded from B&R website](https://www.br-automation.com/en/downloads/software/automation-studio/automation-studio-41/automation-studio-v41/) and Python 3.8

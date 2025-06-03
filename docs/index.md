# Pvi.py

Python wrapper for [B&amp;R PVI (process visualization interface)](https://help.br-automation.com/#/en/4/automationnet%2Fpvi%2Fpvi.htm).
This documentation applies to version 1.2.x.

In times of more modern protocols like [OPC-UA](https://help.br-automation.com/#/en/4/communication%2Fopcua%2Fopcua.html), this may seem a bit old-fashioned.
But PVI has some hidden strengths and is also very versatile.
Have a look into the documentation of the 'Lines' (ANSL, INA2000, NET2000, MTC, ADI, DCAN, SNMP, MODBUS, MININET) and what they are used for.
In most cases it is used just to communicate with B&R PLCs with 'ANSL' and 'SNMP'.
Unfortunately its [native C-language interface](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Fcore%2Fpvicominterface.htm) is very complex and also [PVI Services (.NET)](https://help.br-automation.com/#/en/4/automationnet%2Fpviservices%2Frefmanual%2Ffiles%2Fpviservices_intro.html) can be a high barrier to entry.
It's a lot more fun with Python !

## PVI installation and license

PVI needs a previous installation of 'PVI Development Setup' from [B&R's homepage](https://www.br-automation.com).
Without a PVI license 1TG0500.02 (+ TG Guard e.g. 0TG1000.02) PVI will run for two hours ("Trial license")).  

After this period all PVI based programs will stop working (or will not even start).
In that case PVI-Manager must be stopped and restarted again.
This can be very annoying if Automation Studio is being used in the background at the same time, because it then has to be restarted as well.
Contact your local B&R office to buy a valid license if trial license is not sufficient for you.

Pvi.py is tested with PVI 4.1 - 64 Bit version (PviCom64.dll). Older version might work but 32 Bit versions won't.

Pvi.py will search in the path given by environment variable 'PVIPY_PVIDLLPATH' for PviCom64.dll.
If this is not set it will search in Windows registry which is the most common way.

And: PVI is only available for Microsoft Windows, so Pvi.py is also restricted to the Windows operating system.

## Python

Pvi.py is tested with 3.8 so it could not run on Windows XP or earlier.

## Installation

```console
pip install pvipy
```

## Command Line Usage

pvi.py contains some modules for usage in a terminal.

### Snmpscan

This module is used to scan for CPU with ANSL protocol activated.

```console
Snmpscan
```

### Anslscan

This module is used to scan for CPU with ANSL protocol activated since SNMP might be disabled due to security risks.
The idea is to scan for open TCP port 11169 within a given IP range

```console
Anslscan <network>
```

where network is an [IP4 network address specification](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network).
For example, the following address specifications are equivalent: 192.168.1.0/24, 192.168.1.0/255.255.255.0 and 192.168.1.0/0.0.0.255.

### Inascan

This module is used to scan for CPU with ANSL protocol activated since SNMP might be disabled due to security risks
The idea is to scan for reaction on UDP port 11159 within a given IP range

```console
Inascan <network>
```

where network is an [IP4 network address specification](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network).
For example, the following address specifications are equivalent: 192.168.1.0/24, 192.168.1.0/255.255.255.0 and 192.168.1.0/0.0.0.255.

## Source Code

Find it on GitHub [github.com/hilch/Pvi.py](https://github.com/hilch/Pvi.py)

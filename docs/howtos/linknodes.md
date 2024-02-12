# Linknodes

A link node represents the status of a connection between a PV and an I/O point.

Link node variables in PVI can be used for observation (e.g. evaluating the link node status) or monitoring (e.g. displaying data from inputs regardless of the force state).

## [ANSL](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnansl%2Fpvilnansllinknode.htm)

In the ANSL line, the data and status of a link node are accessed using ANSL variable objects.

## [INA2000](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnina2%2Fpvilnina2linknode.htm)

In the INA2000 line, the data and status of a link node are accessed using INA2000 variable objects.

## Examples

find the following examples on GitHub [github.com/hilch/Pvi.py](https://github.com/hilch/Pvi.py/tree/main/examples)

### [linknode1.py](https://github.com/hilch/Pvi.py/tree/main/examples/linknode1.py) (ANSL)

this simple example just toggles an forced output
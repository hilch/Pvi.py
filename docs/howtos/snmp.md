# [SNMP](https://help.br-automation.com/#/en/4/automationnet%2Fpvibase%2Flines%2Flnsnmp%2Fpvilnsnmp.htm)

The SNMP line maps SNMP (Simple Network Management Protocol) variables from an SG4 PLC to PVI variable objects.

The SNMP line is intended mainly for commissioning a new PLC via the Ethernet interface. SNMP variables can be used to make or call up settings such as host name, IP address, node number, etc..

## Examples

find the following examples on GitHub [github.com/hilch/Pvi.py](https://github.com/hilch/Pvi.py/tree/main/examples)

(if you are looking for a 'real' program consider to use [brsnmp](https://github.com/hilch/brsnmp) )

### [browse_for_targets.py](https://github.com/hilch/Pvi.py/tree/main/examples/browse_for_targets.py)

this example searches for B&R plc in local network with PVI's 'SNMP' line and lists their properties

### [set_ip_address.py](https://github.com/hilch/Pvi.py/tree/main/examples/set_ip_address.py)

this example searches for a specific B&R plc in local network with PVI's 'SNMP' line and changes its IP address

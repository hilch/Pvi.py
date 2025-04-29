#
# Pvi.py
# Python connector for B&R Pvi (process visualization interface)
#
#  https://github.com/hilch/Pvi.py
# Permission is hereby granted, free of charge, 
# to any person obtaining a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# This module is used to scan for CPU with ANSL protocol activated 
# since SNMP might be disabled due to security risks
# The idea is to scan for open TCP port 11169 within a given IP range

import socket
from collections import namedtuple
from typing import List
import argparse
import sys
import ipaddress

from pvi import Connection
from pvi import Line
from pvi import Device
from pvi import Cpu

ScanResult = namedtuple('ScanResult', ['target','AR', 'ip', 'node', 'status'])

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNINA2', CD='LNINA2')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
network_to_scan = ipaddress.IPv4Network('127.0.0.1')
cpu_list = list()


# Function to check if a ANSL server is reachable
def check_server(broadcast : ipaddress.IPv4Address, node, port = 11159): 
    message = bytes([2, 0, 0, 0, 0, 0, node  ] )
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(.1) # Set the timeout
    try:
        # Send the message
        sock.sendto(message, (str(broadcast), port))
        
        # Receive the response
        response, server = sock.recvfrom(4096)
        if len(response) == 6 and len(server) == 2:
            if response[0] == 3 and response[1] == node:
                return server[0]
    except socket.timeout:
        return None
    except Exception as e:
        print(f"Error during checking {str(broadcast)}/Node {node}: {e}")
        sys.exit(1)
    finally:
        # Close the socket
        sock.close()


def cpu_error_change( cpu : Cpu, error : int ):
    global cpu_list

    if error == 0:
        cpu_list.append( ScanResult( 
                            target= cpu.cpuInfo.get('CT', 'unknown'),
                            AR = cpu.version,
                            ip = cpu.ip_address, # type: ignore
                            node = cpu.node, # type: ignore
                            status = cpu.status.get('RunState','unknown')
                            )
                        )
        cpu.checked = True # type: ignore
    elif error == 11020:
        print()
        cpu.checked = True # type: ignore               


def objectsArranged():
    global network_to_scan
    
    # Check servers
    results = []
    for node in range(0,255):
        if node %5 == 0:
            print(".", end="")
        host = check_server( network_to_scan.broadcast_address, node)
        if host:
            results.append( (host,node) )
    print()    
    
    # connect to all CPUs found with PVI to get further information
    for host, node in results:          
        cpu = Cpu( device, 'newCpu', CD='/DAIP=' + str(host) )
        cpu.ip_address = host # type: ignore ,add dynamic member for IP address
        cpu.node = node # type: ignore ,add dynamic member for INA node
        cpu.checked = False # type: ignore , add dynamic member for 'checked' state
        cpu.errorChanged = cpu_error_change
        while not(cpu.checked): # type: ignore
            pviConnection.doEvents()
        cpu.kill()
        del cpu

    pviConnection.stop()


def ina_scan( network : ipaddress.IPv4Network )->List[ScanResult] :
    """Initializes the connection to PVI manager

    Args:
        network : IP4 network, e.g. 192.168.100.0/24 or 192.168.100.0/255.255.255.0

    Returns:
        list with scan results, namedtuple('ScanResult', ['target','AR', 'ip', 'node', 'status'])
    """    
    global pviConnection, ip, cpu_list, network_to_scan
    cpu_list.clear()
    network_to_scan = network
    pviConnection.objectsArranged = objectsArranged
    pviConnection.start() 
    return cpu_list   


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser( prog= "Inascan", description="perform a scan with the INA2000 protocol")

    # Add arguments
    parser.add_argument('network', type=str, help='IP4 network, e.g. 192.168.100.0/24 or 192.168.100.0/255.255.255.0 ')

    # Parse the arguments
    args = parser.parse_args()

    try:
        network = ipaddress.IPv4Network(args.network)
    except (ipaddress.AddressValueError, ValueError, TypeError) as e:
        print( "Inascan: Wrong syntax for IP Address ! " + str(e))
        sys.exit(1)
    
    results = ina_scan(network)
    if network.num_addresses > 1:
        print(f"{network.num_addresses} hosts were checked.")    
    for result in results:
        print(f"Target: {result.target}, AR: {result.AR}, IP: {result.ip}, Node: {result.node}, Status: {result.status}")
        
    if len(results) > 0:
        print(f"{len(results)} target{'s' if len(results) > 1 else '' } found")
    else:
        print( "no targets found")
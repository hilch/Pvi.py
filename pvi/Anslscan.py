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
from concurrent.futures import ThreadPoolExecutor
import re
from collections import namedtuple
from typing import List
import argparse
import sys

from pvi import Connection
from pvi import Line
from pvi import Device
from pvi import Cpu

ScanResult = namedtuple('ScanResult', ['target','AR', 'ip','status'])

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
ip = '127.0.0.1'
cpu_list = list()


# Regular expression for validating an IP address
def is_valid_ip(ip):
    pattern = re.compile( r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$" )
    # Check if the IP address matches the pattern
    if pattern.match(ip):
        return True
    else:
        return False


# Function to check if a ANSL server is reachable
def check_server(host):
    try:
        with socket.create_connection((host, 11169), timeout=1):
            return host
    except (socket.timeout, ConnectionRefusedError):
        return None
    except OSError as e:
        print(f"{host}: {e}")
        return None

def cpu_error_change( cpu : Cpu, error : int ):
    global cpu_list

    if error == 0:
        cpu_list.append( ScanResult( 
                            target= cpu.cpuInfo.get('CT', 'unknown'),
                            AR = cpu.version,
                            ip = cpu.ip_address, # type: ignore
                            status = cpu.status.get('RunState','unknown')
                            )
                        )
        cpu.checked = True # type: ignore
    elif error == 11020:
        print()
        cpu.checked = True # type: ignore               

def objectsArranged():
    global ip    
    servers = (re.sub(r'\.\w+$', f'.{i}', ip) for i in range(0,254))

    # Check servers simultaneously using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=255) as executor:
        results = executor.map(lambda server: check_server(server), servers)
        results = [item for item in results if item is not None]

    # connect to all CPUs found with PVI to get further information
    for result in results:          
        cpu = Cpu( device, 'newCpu', CD='/IP=' + result )
        cpu.ip_address = result # type: ignore ,add dynamic member for IP address
        cpu.checked = False # type: ignore , add dynamic member for 'checked' state
        cpu.errorChanged = cpu_error_change
        while not(cpu.checked): # type: ignore
            pviConnection.doEvents()
        cpu.kill()
        del cpu

    pviConnection.stop()


def ansl_scan( ipAddress = '127.0.0.1')->List[ScanResult] :
    """Initializes the connection to PVI manager

    Args:
        ipAddress : IP address to define address range

    Returns:
        list with scan results, namedtuple('ScanResult', ['target','AR', 'ip','status'])
    """    
    global pviConnection, ip, cpu_list
    cpu_list.clear()
    ip = ipAddress
    pviConnection.objectsArranged = objectsArranged
    pviConnection.start() 
    return cpu_list   


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser( prog= "Anslscan", description="perform a scan with the ANSL protocol")

    # Add arguments
    parser.add_argument('ip', type=str, help='ip address')

    # Parse the arguments

    args = parser.parse_args()

    if not is_valid_ip(args.ip):
        print( "Anslscan: Wrong syntax for IP Address !")
        sys.exit(1)
    
    results = ansl_scan(args.ip)
    for result in results:
        print(f"Target: {result.target}, AR: {result.AR}, IP:{result.ip}, Status:{result.status}")
        
    if len(results) > 0:
        print(f"{len(results)} target{'s' if len(results) > 1 else '' } found")
    else:
        print( "no targets found")
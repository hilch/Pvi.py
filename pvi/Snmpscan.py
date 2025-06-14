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

# This module is used to scan for CPUs with SNMP protocol activated 

import sys
from dataclasses import dataclass
import argparse
from typing import List
from pvi import Connection, Line, Device, Station, Variable

@dataclass
class ScanResult:
    """Snmpscan's result
    """
    target : str # CPU type
    AR : str # Automation Runtime Version
    ip : str # IP Address
    subnet : str # Subnet mask
    serial_number : str # hardware serial number
    status: str # Automation Runtime status
    
pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNSNMP', CD='LNSNMP')
device = Device( line, 'Device', CD='/IF=snmp /RT=1000' )
cpu_list = list()


def deviceErrorChanged( error : int ):
    global cpu_list
    
    if error == 0:
        macs = [ x['name'] for x in device.externalObjects if x['type'] == 'Station']
        for mac in macs:
            station = Station( device, 'station', CD=f'/CN={mac}' )
            vars = station.externalObjects
            data = {}
            for var in vars:
                pvar = Variable( station, var['name'], CD=var['name'] )
                try:
                    value = pvar.value
                    if type(value) == bytes:
                        data.update( { var['name'] : value.decode('ascii') } )
                    elif type(value) == int:
                        data.update( { var['name'] : str(value) } )
                    else:
                        pass
                except BaseException as e:
                    pass
                pvar.kill()
            station.kill()
            arState = int(data.get("arState", -1))
            cpu_list.append( ScanResult( 
                                    target = data.get("targetTypeDescription","unknown"), 
                                    AR = data.get("arVersion", "unknown"), 
                                    ip = data.get("ipAddress", ""),
                                    subnet = data.get("subnetMask", ""),
                                    serial_number = data.get("serialNumber", ""),
                                    status = {-1:"undefined", 1:"BOOT", 2:"DIAG", 3:"SERV", 4:"RUN"}.get(arState, "undefined")
                                )
                    )
            
    device.kill()
    line.kill()
    pviConnection.stop()



def snmp_scan()->List[ScanResult] :
    """scans for CPUs with SNMP protocol activated

    Returns:
        list with scan results, namedtuple 'ScanResult'
    """    
    
    global pviConnection, cpu_list, device
    
    device.errorChanged = deviceErrorChanged
    cpu_list.clear()
    pviConnection.start() 
    return cpu_list   


def main_cli():   
    # Create the parser
    parser = argparse.ArgumentParser( prog= "Snmpscan", description="perform a scan with the SNMP protocol")

    
    # Parse the arguments
    args = parser.parse_args()    
    
    results = snmp_scan()
    for result in results:
        print(f"Target: {result.target}, AR: {result.AR}, ip: {result.ip}, subnet: {result.subnet},\
 serial: {result.serial_number}, Status:{result.status}"
            )
        
    if len(results) > 0:
        print(f"{len(results)} target{'s' if len(results) > 1 else '' } found")
    else:
        print( "no targets found")

    sys.exit(0)

if __name__ == "__main__":
    main_cli()      
# set_ip_address.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# this example searches for a specific B&R plc in local network with PVI's 'SNMP' line
# and changes its IP address
#

from time import sleep
import json
from pvi import *

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
#

line = Line( pviConnection.root, 'LNSNMP', CD='LNSNMP')
device = Device( line, 'Device', CD='/IF=snmp /RT=1000' )

def deviceErrorChanged( error : int ):
    global run

    if error == 0:
        macs = [ x['name'] for x in device.externalObjects if x['type'] == 'Station']
        for mac in macs:
            if mac == '00-60-65-14-d6-da':
                station = Station( device, 'station', CD=f'/CN={mac}' )
                # there is no freedom how to name the internal SNMP variables
                ipAddress = Variable( station, 'ipAddress')
                ipAddress.value = b'192.168.0.10' # must be a byte string
                ipAddress.kill()
                run = False
    device.kill()
    line.kill()
    run = False

device.errorChanged = deviceErrorChanged

run = True

while run:
    pviConnection.doEvents() # must be cyclically called
    sleep(0.1)


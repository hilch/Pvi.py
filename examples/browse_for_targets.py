# browse_for_targets.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# this example searches for B&R plc in local network with PVI's 'SNMP' line
# and lists their properties
#

import json
from pvi import *

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
#

line = Line( pviConnection.root, 'LNSNMP', CD='LNSNMP')
device = Device( line, 'Device', CD='/IF=snmp /RT=1000' )

def deviceErrorChanged( error : int ):

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
                    data.update( { var['name'] : value.decode('ascii') } )
                except:
                    pass
                pvar.kill()
            station.kill()
            print( json.dumps(data) + "\n\n") # pretty print dict
    device.kill()
    line.kill()
    pviConnection.stop()

device.errorChanged = deviceErrorChanged

pviConnection.start()



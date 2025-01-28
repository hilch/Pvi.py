# cpu3.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# in this example we set and check the CPU's clock
# this requires Pvi.py >= V1.2.2
#

from pvi import *
import datetime

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )

def cpuErrorChanged( cpu : Cpu,  error : int ):
    if error == 11020:
        print("Unabled to establish connection")
        pviConnection.stop() # exit
    elif error != 0:
        raise PviError(error)
    else:
        print( "cpu time: " + cpu.time.isoformat() )
        cpu.time = datetime.datetime.now()
        print( "cpu time: " + cpu.time.isoformat() )
        pviConnection.stop() # exit

cpu.errorChanged = cpuErrorChanged
pviConnection.start()
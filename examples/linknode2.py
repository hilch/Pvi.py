# linknode2.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# this example reads information about an PLC input via LinkNode
#
# remark: force status must be set with Automation Studio !

import time
from pvi import *
            
pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myCpu', CD='/IP=127.0.0.1' )
# syntax for linknode variables: GUID a9ec8ee2-87d2-463f-9a30-a2d0eac71cf7
force_value = Variable( cpu, 'F+%IX.IF6.ST13.ModuleOk')
producer_value = Variable( cpu, 'P+%IX.IF6.ST13.ModuleOk')
consumer_value = Variable( cpu, 'C+%IX.IF6.ST13.ModuleOk')


run = True
cpuInRun = False


def cpuErrorChanged( error : int ):
    global run
    global cpuInRun

    if error != 0:
        raise PviError(error)
    else:
        force_value.value = False
        wait = time.time()
        while (time.time() - wait) < 5: # wait until value is written to CPU
            pviConnection.doEvents()
        print( f'force value : {force_value.value}' )            
        print( f'producer value : {producer_value.value}' )            
        print( f'consumer value : {consumer_value.value}' )
        forcing_enabled = force_value.status.get('FC', 0)
        print( f'forcing enabled : {'yes' if forcing_enabled == '1' else 'No'}' )
   

startTime = time.time()
cpu.errorChanged = cpuErrorChanged

def runtimeMonitor( init : bool ):
    if time.time() - startTime > 10:
        print("done !")
        pviConnection.stop() # exit

pviConnection.start( runtimeMonitor )





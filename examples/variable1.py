# variable1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this simple example just sets and reads back some variable info


from pvi import *
from datetime import datetime, timedelta

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
task1 = Task( cpu, 'mainlogic')
var1 = Variable( task1, 'a-nicer-variable-name', CD ='gHeating.status.actTemp', UT='shows temperature in degree Celsius', RF=200, HY = 10 )

def cpuErrorChanged( cpu : Cpu,  error : int ):

    if error == 11020:
        print("Unable to establish connection")
        pviConnection.stop() # exit
    elif error != 0:
        raise PviError(error)
    else:
        print("Variable name in PVI: " + var1.name  )
        print(".. objectName: " + var1.objectName )
        print(".. dataType: ", var1.dataType)
        arraySize = str(var1.descriptor.get('VN'))
        if arraySize != '1':
            print( ".. is an array of size " + arraySize)
        print(".. lenght in bytes: " + var1.descriptor.get('VL', 'unknown'))
        print(".. userName: ", var1.userName )
        print(".. userTag: ", var1.userTag ) 
        print(".. refresh time [ms]: " +  str(var1.refresh) )
        print(".. hysteresis: " +  str(var1.hysteresis) )        
        pviConnection.stop() # exit


cpu.errorChanged = cpuErrorChanged


pviConnection.start()




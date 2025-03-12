# simple1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this simple example just registers a variable, reads its value and then
# exit after a few seconds
#


import datetime
from pvi import *

pviConnection = Connection(IP="192.168.182.128") # start a Pvi connection

# all PVI objects must be registered hierarchically
# line ANSL is the 'modern' way to access PLC variables
# (compared to the older INA2000 line)
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
task1 = Task( cpu, 'mainlogic')
# we register a variable with refresh time of 0 seconds by default
temperature = Variable( task1, 'gHeating.status.actTemp' )
# we register a callback to get variable's value
temperature.valueChanged = lambda value : print(f'{temperature.name} = {value}')

startTime = datetime.datetime.now()

def cpuErrorChanged( error : int ):

    if error != 0:
        raise PviError(error)

cpu.errorChanged = cpuErrorChanged

def runtimeMonitor( init : bool ):
    if datetime.datetime.now() - startTime > datetime.timedelta(seconds = 180):
        print("done !")
        pviConnection.stop() # exit

pviConnection.start( runtimeMonitor )






# debug1.py

import datetime
from pvi import *

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
# line ANSL is the 'modern' way to access PLC variables
# (compared to the older INA2000 line)
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=192.168.0.10' )
task1 = Task( cpu, 'Program')
# we register a variable with refresh time of 0 seconds by default
mydate = Variable( task1, 'myDateAndTime' )
mydateArray = Variable( task1, 'myDateAndTimeArray' )
# we register a callback to get variable's value


def mydateValueChanged( value ):
    print(f'{mydate.name} = {value}')

mydate.valueChanged = mydateValueChanged


def mydateArrayValueChanged( value ):
    print(f'{mydateArray.name} = {value}')

mydateArray.valueChanged = mydateArrayValueChanged

startTime = datetime.datetime.now()

def cpuErrorChanged( error : int ):

    if error != 0:
        raise PviError(error)
    else:
        mydate.value = datetime.datetime(2025, 1, 5)
        #mydateArray.value = [datetime.datetime(2021, 1, 1, 12, 0, 0), datetime.datetime(2021, 2, 1, 12, 0, 0)]
        pass


cpu.errorChanged = cpuErrorChanged

def runtimeMonitor( init : bool ):
    if datetime.datetime.now() - startTime > datetime.timedelta(seconds = 10):
        print("done !")
        pviConnection.stop() # exit

pviConnection.start( runtimeMonitor )






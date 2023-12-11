# basics2.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this simple example just registers a variable for reading and another
# for writing. In fact we switch on the 'coffee machine' and watch its temperature ...
#
# in fact this example is identical to simple2.py but uses a PVI remote connection to
# the ArSim installation on a remote PC

from pvi import *

pviConnection = Connection( timeout=15, IP='172.20.43.59', PN=20000 ) # start a remote Pvi connection

# all PVI objects must be registered hierarchically
# line ANSL is the 'modern' way to access PLC variables
# (compared to the older INA2000 line)
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
task1 = Task( cpu, 'mainlogic')
# we register the variable containing the temperature 
temperature = Variable( task1, 'gHeating.status.actTemp', RF=2000 )
# we register a callback to get temperature value
temperature.valueChanged = lambda value : print(f'\rTemperature = {value}', end="")
# we then register a variable to switch on the machine
switch = Variable( task1, 'gMainLogic.cmd.switchOnOff' )




def cpuErrorChanged( error : int ):

    if error != 0:
        raise PviError(error)

cpu.errorChanged = cpuErrorChanged


warmUp = False
coolDown = False

def checkTemperature( init : bool ):
    global warmUp, coolDown
    if temperature.readable and switch.writable:
        if temperature.value < 25 and not warmUp and not coolDown:
            switch.value = 1 # switch on machine
            warmUp = True
            coolDown = False
            print('warming up...')
        elif temperature.value > 70 and warmUp:
            warmUp = False
            coolDown = True
            switch.value = False # switch off
            print('\ncooling down...')        
        if coolDown and not warmUp and temperature.value < 25:
            print("\nit's cool guys !")
            pviConnection.stop() # exit the loop


pviConnection.start( checkTemperature )






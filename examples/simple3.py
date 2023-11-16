# simple3.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on PP65 with AR 3.x
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this simple example just registers a variable for reading and another
# for writing. In fact we switch on the 'coffee machine' and watch its temperature ...
#
# This is similar to simple2.py but since we use a control running < AR 4.x
# ANSL is not available here and we change to good old INA2000


from pvi import *

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
# ANSL is not available and we use INA2000
#
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
device = Device( line, 'TCP', CD='/IF=TcpIp /SA=113' ) # always use a unique node number for PVI client even though you won't use node numbers
cpu = Cpu( device, 'myPP65', CD='/DAIP=10.49.40.222' )

# alternative: use 'INA node number' instead of IP address. INA node numbers must be unique in network !
# cpu = Cpu( device, 'myPP65', CD='/DA=32' )

task1 = Task( cpu, 'mainlogic')
# we register the variable containing the temperature 
temperature = Variable( task1, 'gHeating.status.actTemp', RF=2000 )
# we register a callback to get temperature value
temperature.valueChanged = lambda value : print(f'\rTemperature = {value}', end="")
# we then register a variable to switch on the machine
switch = Variable( task1, 'gMainLogic.cmd.switchOnOff' )

warmUp = False
coolDown = False


def cpuErrorChanged( error : int ):

    if error != 0:
        raise PviError(error)

cpu.errorChanged = cpuErrorChanged


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




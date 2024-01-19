
# simple4.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this simple example just registers a variable for reading and another
# for writing. In fact we switch on the 'coffee machine' and watch its temperature ...
#
# this is almost identical to simple2.py
# once you have the process data in the Python world, you can use other ingenious libraries 
# to get even more functionality out of it. 
# In this case, we will plot the temperature curve with matplotlib.
#

import matplotlib.pyplot as plt
import datetime
from pvi import *

# trace
trace = {
    'time' : [0.0],
    'temp' : [0.0],
    'switch' : [0]
}

startTime = datetime.datetime.now()

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
# line ANSL is the 'modern' way to access PLC variables
# (compared to the older INA2000 line)
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
task1 = Task( cpu, 'mainlogic')
# we register the variable containing the temperature 
temperature = Variable( task1, name='gHeating.status.actTemp' )

# we then register a variable to switch on the machine
switch = Variable( task1, 'gMainLogic.cmd.switchOnOff' )

# callback for errors
def errorChanged( error : int ):

    if error != 0:
        raise PviError(error )

cpu.errorChanged = errorChanged
temperature.errorChanged = errorChanged

# callback for process value
def temperatureChanged( value : float ):
    t = datetime.datetime.now() - startTime

    print(f'\rTemperature = {round(value,1)}', end="")
    trace['time'].append( t.seconds + t.microseconds / 1e6 )
    trace['temp'].append( value )
    trace['switch'].append( switch.value )

# we register a callback to get temperature value
temperature.valueChanged = temperatureChanged


warmUp = False
coolDown = False


def checkTemperature( init : bool ):
    global warmUp, coolDown
    if temperature.readable and switch.writable:   
 
        if temperature.value < 25 and not warmUp and not coolDown:
            switch.value = 1 # switch on machine
            warmUp = True
            coolDown = False
            print('\nwarming up...\n')
        elif temperature.value > 70 and warmUp:
            warmUp = False
            coolDown = True
            switch.value = False # switch off
            print('\ncooling down...\n')        
        if coolDown and not warmUp and temperature.value < 25:
            print("\nit's cool guys !\n")
            # plot
            plt.subplot(2,1,1)
            plt.plot( trace['time'], trace['switch'] )
            plt.xlabel("time [s]")
            plt.ylabel("switch")

            plt.subplot(2,1,2)
            plt.plot( trace['time'], trace['temp'] )
            plt.xlabel("time [s]")
            plt.ylabel("water temperature [°C]")
            plt.show()

            pviConnection.stop() # exit the loop


pviConnection.start( checkTemperature )






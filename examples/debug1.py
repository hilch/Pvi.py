# debug1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
#  This example shows how to switch on debugging for Pvi.py applications


from pvi import *
import logging

logger = logging.getLogger("debug1.py")
logging.basicConfig(filename="debug.log", filemode="w", level = logging.DEBUG)
logger.info("startup")


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
# we register a callback to get temperature value
temperature.valueChanged = lambda value  : print(f'\rTemperature = {round(value,1)}', end="")
# we then register a variable to switch on the machine
switch = Variable( task1, 'gMainLogic.cmd.switchOnOff' )


def cpuErrorChanged( object: PviObject, error : int ):

    if error != 0:
        #logger.critical(f"{object.descriptor} - PviError({error})")
        logger.critical("application stopped")
        pviConnection.stop()
    else:
        print(object.descriptor, "connected")

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
            print('\nwarming up...\n')
            logger.info("warming up")
        elif temperature.value > 70 and warmUp:
            warmUp = False
            coolDown = True
            switch.value = False # switch off
            print('\ncooling down...\n')        
            logger.info("cooling down")            
        if coolDown and not warmUp and temperature.value < 25:
            print("\nit's cool guys !\n")
            print('\n' + temperature.name + ' - ' + temperature.userName)
            logger.info("ready")                        
            pviConnection.stop() # exit the loop


pviConnection.start( checkTemperature )






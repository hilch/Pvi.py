# modules3.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example uploads some loggers from CPU
#

from time import sleep
from pprint import pprint
from pvi import *

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
# line ANSL is the 'modern' way to access PLC variables
# (compared to the older INA2000 line)
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
run = True
loggerModules = {'$arlogsys', '$arlogusr', '$fieldbus'}
uploadedLoggerModules = 0

def callback_progress( percent):
    print( f'progress: {percent} %\r', end="")   


def callback_uploaded( module : str, data ):
    global run
    global uploadedLoggerModules

    print(f"{ module } uploaded, len={len(data)} !")
    # write content to file
    filename = f'{module}.txt'
    with open( filename, 'w') as f: 
        pprint(data, stream=f, indent = 4)
    print(f"{ filename } saved !")

    uploadedLoggerModules = uploadedLoggerModules + 1
    if uploadedLoggerModules == len(loggerModules) :
        run = False


def cpuErrorChanged( error : int):
    global run

    if error == 0:
        # read content
        allObjects = cpu.externalObjects

        # read module names
        moduleNames = {_['name'] for _ in allObjects if _['type'] == 'Module' } & loggerModules
        for name in moduleNames:  # read the modules' status
            module = Module( cpu, name )             
            module.upload( uploaded = callback_uploaded, progress = callback_progress, MT = '_LOGM' )
            print(f"start uploading {name} ...")     
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged


while run:
    pviConnection.doEvents() # must be cyclically called
    sleep(0.1)






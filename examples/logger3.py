# logger3.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on PP65 with AR 3.x
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example uploads some loggers from CPU
#
# This is similar to logger1.py but since we use a control running < AR 4.x
# ANSL is not available here and we change to good old INA2000


from pprint import pprint
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

loggerModules = {'$arlogsys', '$arlogusr', '$fieldbus'}
uploadedLoggerModules = 0

def callback_progress( percent):
    print( f'progress: {percent} %\r', end="")   


def callback_uploaded( module : Module, data ):
    global uploadedLoggerModules

    print(f"{ module } uploaded, len={len(data)} !")
    # write content to file
    filename = f'{module.objectName}.txt'
    with open( filename, 'w') as f: 
        pprint(data, stream=f, indent = 4)
    print(f"{ filename } saved !")

    uploadedLoggerModules = uploadedLoggerModules + 1
    if uploadedLoggerModules == len(loggerModules) :
        pviConnection.stop()


def cpuErrorChanged( error : int):

    if error == 0:

        # read module names
        for name in cpu.modules:  # read the modules' status
            if name in loggerModules:
                module = Module( cpu, name )
                x = module.status
                module.upload( uploaded = callback_uploaded, progress = callback_progress, MT = '_LOGM' )
                print(f"start uploading {name} ...")     
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged

pviConnection.start()







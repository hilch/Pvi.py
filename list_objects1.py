# list_objects1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example lists objects with 'global scope' (modules, task and global variables)
# from 'coffe machine' cpu
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

def cpuErrorChanged( error : int):
    global run

    if error == 0:
        # read content
        allObjects = cpu.externalObjects
        modules = [ _['name'] for _ in allObjects if _['type'] == 'Module']  # read module names
        tasks = [ _['name'] for _ in allObjects if _['type'] == 'Task'] # read task names
        globalVars = [ _['name'] for _ in allObjects if _['type'] == 'Pvar'] # read names of global variables

        # write content to file
        with open('content.txt', 'w') as f:
            f.write("Modules =\n")
            pprint(modules, stream=f)
            f.write("\nTasks =\n")
            pprint(tasks, stream=f)            
            f.write("\nglobalVars =\n")
            pprint(globalVars, stream=f)  
        print('content.txt was created !')                      
        run = False
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged


while run:
    pviConnection.doEvents() # must be cyclically called
    sleep(0.1)






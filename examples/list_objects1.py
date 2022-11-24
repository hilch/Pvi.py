# list_objects1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example lists objects with 'global scope' (modules, task and global variables)
# from 'coffe machine' cpu and returns status information about them
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

        # read module names
        moduleNames = [_['name'] for _ in allObjects if _['type'] == 'Module' ]  

        modules = list()
        for name in moduleNames:  # read the modules' status
            module = Module( cpu, name )
            status = { "Name" : name }
            status.update( module.status )
            modules.append(status)
            module.kill()

        # read task names
        taskNames = [ _['name'] for _ in allObjects if _['type'] == 'Task'] 
        tasks = list()
        for name in moduleNames:  # read the tasks' status
            task = Task( cpu, name )
            status = { "Name" : name }
            status.update( task.status )
            tasks.append(status)
            task.kill()

        # read names of global variables
        globalVarnames = [ _['name'] for _ in allObjects if _['type'] == 'Pvar'] 
        globalVariables = list()
        for name in globalVarnames:  # read the variables' status, data type and value
            variable = Variable( cpu, name )
            status = { "Name" : name }
            status.update( variable.status )
            status.update( { "Value" : variable.value} )
            status.update( { "Type" : variable.dataType} )            
            globalVariables.append(status)
            variable.kill()

 #      write content to file
        with open('content.txt', 'w') as f:
            f.write("Modules =\n")
            pprint(modules, stream=f, indent = 4)
            f.write("\nTasks =\n")
            pprint(tasks, stream=f, indent = 4)            
            f.write("\nglobalVars =\n")
            pprint(globalVariables, stream=f, indent = 4)  
        print('content.txt was created !')                      
        run = False
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged


while run:
    pviConnection.doEvents() # must be cyclically called
    sleep(0.1)






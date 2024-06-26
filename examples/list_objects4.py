# list_objects4.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on PP65 with AR 3.x
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example lists objects with 'global scope' (modules, task and global variables)
# from 'coffe machine' cpu and returns status information about them
#
# This is similar to list_objects1.py but since we use a control running < AR 4.x
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



def cpuErrorChanged( error : int):

    if error == 0:
 
        # read module names

        moduleNames = cpu.modules
        modules = list()
        for name in moduleNames: # read the modules' status
            module = Module( cpu, name )
            status = { "Name" : name }
            status.update( module.status )
            modules.append(status)
            module.kill()        
 
        # read task names
        taskNames = cpu.tasks
        tasks = list()
        for name in taskNames:  # read the tasks' status
            task = Task( cpu, name )
            status = { "Name" : name }
            status.update( task.status )
            tasks.append(status)
            task.kill()
 
        # read names of global variables
        globalVariables = list()
        for name in cpu.variables:  # read the variables' status, data type and value
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
        pviConnection.stop()
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged

pviConnection.start()







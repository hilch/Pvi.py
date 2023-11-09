# list_objects5.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on PP65 with AR 3.x
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example lists global and local variables and their content
#
# This is similar to list_objects2.py but since we use a control running < AR 4.x
# ANSL is not available here and we change to good old INA2000


from time import sleep
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


run = True

def cpuErrorChanged( error : int):
    global run

    if error == 0:

        tasks = dict()
        for taskName in cpu.tasks:
            task = Task( cpu, taskName )
            variables = list()                    
            for variableName in task.variables:
                variable = Variable(task, variableName)
                try:
                    dataType = variable.dataType
                    value = variable.value
                    variables.append( { "Name" : variableName, "Type" : dataType, "Value" : value} )
                except PviError as e:
                    print(e)

                variable.kill()
            tasks.update({ taskName : variables })
            task.kill
        # write content to file
        with open('content.txt', 'w') as f: 
            pprint(tasks, stream=f, indent = 4)

        variables = list()
        for variableName in cpu.variables:
            variable = Variable(cpu, variableName)
            try:
                dataType = variable.dataType
                value = variable.value
                variables.append( { "Name" : variableName, "Type" : dataType, "Value" : value} )
            except PviError as e:
                print(e)

            variable.kill()

        # append the content to existing file
        with open('content.txt', 'a') as f: 
            f.write("\nglobalVars =\n")
            pprint( variables, stream=f) 

        print('content.txt was created !')                      
        run = False
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged


while run:
    pviConnection.doEvents() # must be cyclically called
    sleep(0.1)






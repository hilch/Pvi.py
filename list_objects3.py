# list_objects3.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example lists all local variables of a specific task and their content
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
task = Task( cpu, 'NewProgram' )


run = True

def cpuErrorChanged( error : int):
    global run

    if error == 0:
        variableNames = [ _['name'] for _ in task.externalObjects]
        variables = list()                        
        for variableName in variableNames:
            variable = Variable(task, variableName)
            try:
                dataType = variable.dataType
                value = variable.value
            except PviError as e:
                print(e)
            variables.append( { "Name" : variableName, "DataType" : dataType, "Value" : value} )
            variable.kill()

        # write content to file
        with open('content.txt', 'w') as f: 
            pprint(variables, stream=f, indent = 4)
        print('content.txt was created !')                      
        run = False
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged


while run:
    pviConnection.doEvents() # must be cyclically called
    sleep(0.1)






# list_objects3.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example lists all local variables of a specific task and their content
#


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
task = Task( cpu, 'conveyor' )


def cpuErrorChanged( error : int):

    if error == 0:
        variableNames = [ _['name'] for _ in task.externalObjects]
        variables = list()                        
        for variableName in variableNames:
            variable = Variable(task, variableName)
            try:
                dataType = variable.dataType
                value = variable.value
                variables.append( { "Name" : variableName, "Type" : dataType, "Value" : value} )
            except PviError as e:
                print(e)

            variable.kill()

        # write content to file
        with open('content.txt', 'w') as f: 
            pprint(variables, stream=f, indent = 4)
        print('content.txt was created !')                      
        pviConnection.stop()
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged

pviConnection.start()





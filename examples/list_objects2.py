# list_objects2.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example lists global and local variables and their content
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


def cpuErrorChanged( error : int):

    if error == 0:
        # read content
        allObjects = cpu.externalObjects
        taskNames = [ _['name'] for _ in allObjects if _['type'] == 'Task'] # read task names

        tasks = dict()
        for taskName in taskNames:
            task = Task( cpu, taskName )
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
            tasks.update({ taskName : variables })
            task.kill
        # write content to file
        with open('content.txt', 'w') as f: 
            pprint(tasks, stream=f, indent = 4)

        globalVariableNames = [ _['name'] for _ in allObjects if _['type'] == 'Pvar'] # read names of global variables
        variables = list()
        for variableName in globalVariableNames:
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
        pviConnection.stop()
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged

pviConnection.start()




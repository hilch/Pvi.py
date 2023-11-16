# list_objects6.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on PP65 with AR 3.x
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example lists all local variables of a specific task and their content
#
# This is similar to list_objects6.py but since we use a control running < AR 4.x
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
task = Task( cpu, 'conveyor' )

# alternative: use 'INA node number' instead of IP address. INA node numbers must be unique in network !
# cpu = Cpu( device, 'myPP65', CD='/DA=32' )


def cpuErrorChanged( error : int):

    if error == 0:
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

        # write content to file
        with open('content.txt', 'w') as f: 
            pprint(variables, stream=f, indent = 4)
        print('content.txt was created !')                      
        pviConnection.stop()
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged

pviConnection.start()






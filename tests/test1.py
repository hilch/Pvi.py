# test against 'coffee machine' in AS 4.1.17.113 SP
import sys
sys.path.append('C:\\projects\\Pvi.py')

from time import sleep
import hashlib
from pvi import *


pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )

run = True

def cpuErrorChanged( error : int):
    global run

     
    if error == 0:
        # read content
        allObjects = cpu.externalObjects

        dataType = None
        tasks = dict()
        for taskName in ['mainlogic', 'feeder', 'conveyor', 'brewing', 'heating', 'visCtrl','visAlarm', 'visTrend' ] :
            task = Task( cpu, taskName )
            variableNames = [ _['name'] for _ in task.externalObjects]
            variables = list()                    
            for variableName in variableNames:
                variable = Variable(task, variableName)

                try:
                    dataType = variable.dataType
                    value = variable.value
                except PviError as e:
                    print(e)
                variables.append( { "Name" : variableName, "Type" : dataType} )
                variable.kill()
            tasks.update({ taskName : variables })
            task.kill

        globalVariableNames = [ _['name'] for _ in allObjects if _['type'] == 'Pvar'] # read names of global variables
        variables = list()
        for variableName in globalVariableNames:
            variable = Variable(cpu, variableName)
            try:
                dataType = variable.dataType
                value = variable.value
            except PviError as e:
                print(e)
            variables.append( { "Name" : variableName, "Type" : dataType } )
            variable.kill()
        
        result = str(tasks) + str(variables)
        h = hashlib.sha256( result.encode() )
        
        if h.hexdigest() == '0ecb1036ba0bc689dc64de86ee1621fc7499da508d038129f258bfadaddf5293':
            print("pass !")
        else:
            print("failed !")

        run = False
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged


while run:
    pviConnection.doEvents() # must be cyclically called
    sleep(0.1)



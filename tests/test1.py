# test against 'coffee machine' in AS 4.1.17.113 SP
from pathlib import Path
import time
import sys
import hashlib

pviPath = str(Path(__file__).parents[1])
cwd = str(Path(__file__).parents[0])

sys.path.append( pviPath )

from pvi import *

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
task1 = Task( cpu, 'mainlogic')
var1 = Variable( task1, 'a-nicer-variable-name', CD ='gHeating.status.actTemp', UT='shows temperature in degree Celsius', RF=200, HY = 10 )

run = True

def cpuErrorChanged( error : int):
    global run

     
    if error == 0:
        print("read variable content.")

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

        print("read cpu info.")

        result = cpu.name + cpu.version + str(cpu.status) + str(cpu.cpuInfo)
        h = hashlib.sha256( result.encode() )

        if h.hexdigest() == 'b39f197f21bcd1c418e6bcc1a62884c9a80ee613e0ffa4b1ef54b040bc9199e4':
            print("pass !")
        else:
            print("failed !")


        print("read variable info.")

        result = var1.name + var1.objectName +  var1.dataType + var1.userName + var1.userTag + str(var1.refresh) + str(var1.hysteresis)
        h = hashlib.sha256( result.encode() )

        if h.hexdigest() == 'd3171541c1362616d825b69e806001cf289fe6765b83eef07e0589974baac1b5':
            print("pass !")
        else:
            print("failed !")

        run = False
    
    elif error:
        raise PviError(error)


cpu.errorChanged = cpuErrorChanged


while run:
    pviConnection.doEvents() # must be cyclically called
    time.sleep(0.1)



# task1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example just reads out some info from a task
# and shows how to use .start() .stop() .cycle() and .resume()
#


from pvi import *
from datetime import datetime, timedelta

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
task1 = Task( cpu, 'brewing')

step = 0

def cpuErrorChanged( cpu : Cpu,  error : int ):
    global step

    if error == 11020:
        print("Unabled to establish connection")
        pviConnection.stop() # exit
    elif error != 0:
        raise PviError(error)
    else:
        step = 1 # CPU is connected


cpu.errorChanged = cpuErrorChanged
t0 = datetime.now()
t = timedelta()


def stateMachine(init : bool ):
    global step, t0, t
    t = datetime.now()-t0
 
    if step == 1:
        print("Task name: " + task1.objectName + ", Version: " + task1.version )
        task1.stop() # stop the task
        task1.cycle(3)          
        t0 = datetime.now()
        step +=1

    elif step == 2 and t > timedelta(seconds=2):
        print( "after stop. current task status: " + str(task1.status) )
        task1.resume() # execute a single cycle
        t0 = datetime.now()
        step +=1

    elif step == 3 and t > timedelta(seconds=2):
        print( "after resume. current task status: " + str(task1.status) )
        task1.stop() # stop cycle mode
        task1.start() # start the task again
        t0 = datetime.now()  
        step +=1

    elif step == 4 and t > timedelta(seconds=2):
        print( "after start. current task status: " + str(task1.status) )
        pviConnection.stop() # exit

    
pviConnection.start(stateMachine)






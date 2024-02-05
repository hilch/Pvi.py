# cpu1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example shows how to use .stopTarget(), .warmStart and diagnostics()
#


from pvi import *
from datetime import datetime, timedelta

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )


step = 0
t0 = datetime.now()
t = timedelta()

def cpuErrorChanged( cpu : Cpu,  error : int ):
    global step

    if error == 0:
        if step == 0:
            print("connection to Cpu established")
            step = 1
        else:
            print("re-connected to Cpu")


cpu.errorChanged = cpuErrorChanged

def stateMachine(init : bool ):
    global step, t0, t
    t = datetime.now()-t0

    try:
        if step == 1:
            print("Cpu status " + str(cpu.status) )
            cpu.stopTarget()
            t0 = datetime.now()
            step +=1

        elif step == 2 and t > timedelta(seconds=10):
            print( "after .stopTarget. Cpu status: " + str(cpu.status) )
            cpu.warmStart()
            t0 = datetime.now()
            step +=1

        elif step == 3 and t > timedelta(seconds=5):
            print( "after .warmStart. Cpu status: " + str(cpu.status) )
            cpu.diagnostics()
            t0 = datetime.now()  
            step +=1

        elif step == 4 and t > timedelta(seconds=5):
            print( "after .diagnostics. Cpu status: " + str(cpu.status) )
            print( "You have to restart ArSim via Control Window now:")
            print( "1. press 'Shut Down' and wait for 'System terminaton done'")
            print( "2. Press 'Restart'")
            t0 = datetime.now()
            step +=1

        elif step == 5:
            print( t, '\r', end='')
            if cpu.status["RunState"] == "RUN" or t > timedelta(seconds=120):
                pviConnection.stop() # exit
    except PviError as e:
        if e.number != 11022:
            raise e
    
pviConnection.start(stateMachine)






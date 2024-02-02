# cpu1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this simple example just reads out some info from CPU
#


from pvi import *

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )

def cpuErrorChanged( cpu : Cpu,  error : int ):

    if error == 11020:
        print("Unabled to establish connection")
        pviConnection.stop() # exit
    elif error != 0:
        raise PviError(error)
    else:
        print( "PVI-Version: " + pviConnection.root.version.replace('\n','/ ') )
        print("connected to CPU " + cpu.name + ", AR-Version: " + cpu.version )
        print( "current CPU status: " + cpu.status.get('RunState','unknown') )
        print( "cpu clock shows " + cpu.time.isoformat() )
        print("cpu type: " + cpu.cpuInfo.get('CT', 'unknown') )
        print( f"there are {len(cpu.tasks)} tasks installed.")
        pviConnection.stop() # exit


cpu.errorChanged = cpuErrorChanged


pviConnection.start()






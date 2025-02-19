# multiple2.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example demonstrates how to connect to two PVI managers simultaneously.
# this is similar to multiple1.py but CPU2 connection now runs in a separate thread
# 

import datetime
import threading
from pvi import *

pviConnection1 = Connection() # start a Pvi connection to local PVI manager
#
line1 = Line( pviConnection1.root, 'LNANSL', CD='LNANSL')
device1 = Device( line1, 'TCP', CD='/IF=TcpIp' )
cpu1 = Cpu( device1, 'myArsim', CD='/IP=127.0.0.1' )

pviConnection2 = Connection(IP='192.168.182.128', PN=20000 ) # start a remote Pvi
#
line2 = Line( pviConnection2.root, 'LNANSL', CD='LNANSL')
device2 = Device( line2, 'TCP', CD='/IF=TcpIp' )
cpu2 = Cpu( device2, 'myArsim', CD='/IP=127.0.0.1' )


startTime = datetime.datetime.now()

# CPU1 actions
def cpu1ErrorChanged( error : int ):
    if error == 0: # CPU connected
        print( "CPU1 time: %s, AR version: %s, status: %s" % (cpu1.time, cpu1.version, cpu1.status))
    else:
        raise PviError(error)

cpu1.errorChanged = cpu1ErrorChanged

def cpu1_loop( init : bool ):
    if datetime.datetime.now() - startTime > datetime.timedelta(seconds = 10):
        print("connection #1 stopped !")
        pviConnection1.stop() # exit loop1


# CPU2 actions
def cpu2ErrorChanged( error : int ):
    if error == 0: # CPU connected
        print( "CPU2 time: %s, AR version: %s, status: %s" % (cpu2.time, cpu2.version, cpu2.status))
    else:
        raise PviError(error)

cpu2.errorChanged = cpu2ErrorChanged

def cpu2_loop( init : bool ):
    if datetime.datetime.now() - startTime > datetime.timedelta(seconds = 8):
        print("connection #2 stopped !")
        pviConnection2.stop() # exit loop2


# CPU2 is handled in a second thread
thread2 = threading.Thread(target= lambda : pviConnection2.start(cpu2_loop))
thread2.start()

# CPU1 runs in main thread
pviConnection1.start( cpu1_loop )




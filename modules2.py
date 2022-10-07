# modules1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this simple example creates a module on CPU by downloading a bytestream and 
# afterwards uploads it again
#


from time import sleep
import datetime
from tkinter import FALSE
from pvi import *

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
# line ANSL is the 'modern' way to access PLC variables
# (compared to the older INA2000 line)
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
module = Module( cpu, 'bigmod' )

startTime = datetime.datetime.now()

step = 0
    
def callback_progress(percent):
    print( f'progress: {percent} %\r', end="")   


def callback_downloaded():
    global step
    modules = cpu.modules
    if 'bigmod' in modules:
        print(" 'bigmod' was sucessfully downloaded !")
        module.upload( uploaded = callback_uploaded, progress = callback_progress )
        print("start uploading...")
        step = 2
    else:
        print("error: 'bigmod' not found !")
        step = 99 #exit


def callback_uploaded( data ):
    global step
    print(f"'bigmod' uploaded, len={len(data)} !")
    step = 99 #exit


while step < 99:
    pviConnection.doEvents() # must be cyclically called
    if step == 0:
        s = cpu.status
        if s == 'RUN' or s == 'SERV':
            step = 1
            cpu.downloadModule( bytes(5000000), MN='bigmod', MT='BRT', progress = callback_progress , downloaded = callback_downloaded )
            print("downloading...")

    elif step == 1: # wait until downloaded
        pass

    elif step == 2: # wait until uploaded
        pass

    elif datetime.datetime.now() - startTime > datetime.timedelta(seconds = 20): # timeout
        print("timeout !")
        step = 99 # exit
    sleep(0.1)





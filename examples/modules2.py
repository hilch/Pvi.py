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


run = True
    
def callback_progress(percent):
    print( f'progress: {percent} %\r', end="")   


def callback_downloaded():
    global run
    modules = cpu.modules
    if 'bigmod' in modules:
        print(" 'bigmod' was sucessfully downloaded !")
        module.upload( uploaded = callback_uploaded, progress = callback_progress )
        print("start uploading...")
        
    else:
        print("error: 'bigmod' not found !")
        run = False #exit


def callback_uploaded( data ):
    global run
    print(f"'bigmod' uploaded, len={len(data)} !")
    run = False #exit


def cpuErrorChanged( error : int ):
    if error == 0:    
        s = cpu.status.get("RunState")
        if s == 'RUN' or s == 'SERV':
            step = 1
            cpu.downloadModule( bytes(5000000), MN='bigmod', MT='BRT', progress = callback_progress , downloaded = callback_downloaded )
            print("downloading...")        
    else:
        raise PviError( error )

cpu.errorChanged = cpuErrorChanged


while run:
    pviConnection.doEvents() # must be cyclically called
    sleep(0.1)





# linknode1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is X20CP3584 with a X20DO6322 running AR G4.09
#
# this simple example just toggles an forced output
# remark: force status must be set with Automation Studio !
#


from time import sleep
import datetime
from pvi import *


class Output( Variable ):
    '''
    convinience class to make code more readable
    '''
    def __init__(self, cpu, linkNode ):
        super().__init__( cpu, linkNode, CD=f'"{linkNode}"' )
        self._state = False

    @property
    def forceable(self) -> bool:
        return True if self.status['FC'] == '1' else False
        
    def set(self):
        self._state = True
        self.value = self._state

    def reset(self):
        self._state = False        
        self.value = self._state

    def toggle(self) -> bool:
        if self._state:
            self.reset()
        else:
            self.set()
        return self._state
 
        
        
pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myCpu', CD='/IP=10.49.40.221' )
# syntax for linknode variables: GUID 3d1b8b36-111a-4f29-ac05-a6f0e6c76a80
output1 = Output( cpu, 'F+%QX.IF6.ST1.DigitalOutput01')


run = True
cpuInRun = False

def cpuErrorChanged( error : int ):
    global run
    global cpuInRun

    if error != 0:
        raise PviError(error)
    cpuInRun = cpu.status['RunState'] == 'RUN'
   

    
cpu.errorChanged = cpuErrorChanged
startTime = datetime.datetime.now()

while run:
    if output1.writable and cpuInRun:
        if datetime.datetime.now() - startTime > datetime.timedelta(seconds=5):
            startTime = datetime.datetime.now()         
            if output1.forceable:
                print( output1.toggle() )
            else:
                print('output cannot be forced !')

    pviConnection.doEvents() # must be cyclically called
    sleep(0.1)






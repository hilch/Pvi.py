## Prerequisites

Of course, you have to install Python first (>= 3.8).
Pip should come with Python so install the wrapper with it:

```
pip install pvipy
```
PVI only makes sense if you also have a B&R PLC available.
In the simplest case, start the 'CoffeeMachine' demo project that comes with the installation of Automation Studio and run it on an ArSim Simulation.
Some examples require a few more variables, so it is easier to use the included 'CoffeeMachine' project from the Github repository (under '/tools/CoffeeMachine').

This project was created with the not-so-new Automation Studio version 4.1.17. This version can be downloaded for free from the B&R homepage and does not require a license. If you prefer a newer version, the project must be converted, which is not always easy.

## Examples in repository

PVI uses a complex interface to define objects and their parameters but it is well documented in its online help system and also in Automation Studio help system. There is no point in repeating this here since most of its parameters still apply in this Python interface. Instead, look at the examples to use parts from this for your programs.

find the following examples on GitHub [github.com/hilch/Pvi.py](https://github.com/hilch/Pvi.py/tree/main/examples)

### simple1.py (ANSL)
this simple example just registers a variable, reads its value and then exit after a few seconds.

Initially, only a simple import of the PVI objects is actually necessary:
```
from pvi import *
```

Then we first need a connection to the PVI Manager:

```
pviConnection = Connection() # start a Pvi connection
```

It should be noted that this does not establish any connection to the CPU, but only to the 'PVI Manager', a Windows task, which in turn manages all PVI objects and takes care of all communication.

We can then set up all PVI objects by instantiating and parameterizing the corresponding Python classes.
Line->Device->Cpu->Task->Variable.

```
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
```
The 'Line' determines the protocol used. The currently most important protocol is ANSL, which is mainly used for communication with PLCs.
An older version is called 'INA2000' and is still required if an older PLC with AR < 4.x is to be used.
The 'SNMP' line, which can be used to read and write network parameters, for example, has a completely different meaning. See the corresponding example.
The term 'CD=xxxx' must be specified in exactly the same way and is passed on to the PVI DLL in the same way. For further options, please refer to the PVI documentation.
```
device = Device( line, 'TCP', CD='/IF=TcpIp' )
```
The 'Device' defines the hardware interface to be used. Only 'TcpIp' is actually possible for ANSL. This is used to establish the connection via Ethernet interface, loop-back adapter or also via Wifi.
INA2000 is also able to communicate via serial interface or CAN interface.
```
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
```
Finally, the 'Cpu' is the object that represents the connection to the correct PLC. Depending on which 'Device' is used, corresponding parameters are required for the CPU. Please refer to the PVI documentation if necessary.

At this point, we could already carry out useful actions with the CPU, e.g. trigger a warm start or read out the status of the CPU or much more.

However, we would like to read out a local variable of the CPU at this point. Global variables should be created hierarchically below the 'CPU' object. 
However, local variables are always part of a task. So we have to take care of this first. The name of the task on the PLC must again be specified.
```
task1 = Task( cpu, 'mainlogic')
```
A 'Task' also has useful options, e.g. it can be stopped and restarted at runtime, which we do not intend to do here.

Now we can finally create a 'Variable' object that allows us to access the properties of the corresponding PLC variables.
```
temperature = Variable( task1, 'gHeating.status.actTemp' )
```
We could now access the '.value' property of the variable object cyclically in order to read the value of the variable. However, this would not be very resource-efficient. PVI is able to work in an event-driven manner. We therefore let it inform us of a value change and pass a callback function that also informs us of the value:
```
temperature.valueChanged = lambda value : print(f'{temperature.name} = {value}')
```
Now we need to breathe some life into the PVI functions in the background. 
A
```
pviConnection.start() # call it once
```
would be absolutely sufficient for this job. As in a classic Windows program, an infinite loop is created internally that cyclically calls the 'doEvents()' function of the 'Connection'.
So

```
while True:
    pviConnection.doEvents() # must be cyclically called
```
would do the same (and could sometimes be the simpler solution).

Since life is not endless, our program should not run indefinitely and end cleanly.
For this we create a monitoring function that calls the '.stop()' member of the Connection after a certain time. This ends the loop and ultimately the entire script.
```
def runtimeMonitor( init : bool ):
    if datetime.datetime.now() - startTime > datetime.timedelta(seconds = 10):
        print("done !")
        pviConnection.stop() # exit
```

Are we finished now ? Not quite yet.
In case the CPU was not available we would not get aware of this. Thus we add another callback function to monitor the connection to CPU.

```
def cpuErrorChanged( error : int ):

    if error != 0:
        raise PviError(error)

cpu.errorChanged = cpuErrorChanged
```
#### open the console (e.g. cmd)
Starting the script by
```
py simple1.py
```
should end in 
```
@Pvi/LNANSL/TCP/myArsim/mainlogic/gHeating.status.actTemp = 20.0
done !
```


### simple2.py (ANSL)
this simple example just registers a variable for reading and another for writing. In fact we switch on the 'coffee machine' and watch its temperature ...

### simple3.py (INA2000)
this simple example just registers a variable for reading and another for writing. In fact we switch on the 'coffee machine' and watch its temperature ...
This is similar to simple2.py but we use a control running AR 3.x. ANSL is not available here and we change to good old INA2000


## Basics
### basics1.py (ANSL)
shows reading and writing of basic data types
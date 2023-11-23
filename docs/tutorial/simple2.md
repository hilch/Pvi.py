## Extend the script

Download [simple2.py](https://github.com/hilch/Pvi.py/tree/main/examples/simple2.py) (ANSL)
This simple example just registers a variable for reading and another for writing. In fact we switch on the 'coffee machine' and watch its temperature ...

Not much different compared to 'simple1.py'.
We add a variable to show how to write into it.
Because it is so beautifully illustrative, we will now switch the coffee machine on and off.

As above we need an associated PVI variable object:
```
switch = Variable( task1, 'gMainLogic.cmd.switchOnOff' )
```

Since we've no HMI (human machine interface) for the coffee client the 'switch' is operated by script watching the actual temperature.
For this we use a state machine running inside a callback function:

```
def checkTemperature( init : bool ):
    global warmUp, coolDown
    if temperature.readable and switch.writable:
        if temperature.value < 25 and not warmUp and not coolDown:
            switch.value = 1 # switch on machine
            warmUp = True
            coolDown = False
            print('warming up...')
        elif temperature.value > 70 and warmUp:
            warmUp = False
            coolDown = True
            switch.value = False # switch off
            print('\ncooling down...')        
        if coolDown and not warmUp and temperature.value < 25:
            print("\nit's cool guys !")
            pviConnection.stop() # exit the loop
```
Then we start the PVI connection by calling .start() with this callback function as argument:

```
pviConnection.start( checkTemperature )
```

## Test
Open the console (e.g. cmd)
Starting the script by
```
py simple2.py
```
lets the script run for a few seconds and will end in a view like this:
```
Temperature = 20.0warming up...
Temperature = 69.704475402832036
cooling down...
Temperature = 25.024797439575195
it's cool guys !
Temperature = 24.99532699584961
```
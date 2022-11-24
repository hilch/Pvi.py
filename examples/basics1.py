# basics1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
# and shows reading and writing of basic data types
#
# PLC counterpart is a simple program running on ArSim 
#
# content of 'myProg.var':
# VAR
#     myUSINT : USINT := 0;
#     myUINT : UINT := 0;
#     mySTRING : STRING[80] := '';
#     myWSTRING : WSTRING[80] := "";
#     myTIME : TIME := T#0S;
#     myTOD : TIME_OF_DAY := TOD#00:00:00;
#     myDT : DATE_AND_TIME := DT#1970-01-01-00:00:00;
#     myDINT : DINT := 0;
#     myUDINT : UDINT := 0;
#     myDATE : DATE := D#1970-01-01;
#     myLREAL : LREAL := 0.0;
#     myREAL : REAL := 0.0;
#     myINT : INT := 0;
#     mySINT : SINT := 0;
#     myBOOL : BOOL := FALSE;
#     myINTArray : ARRAY[0..9] OF INT := [10(0)];
#     mySTRINGArray : ARRAY[0..9] OF STRING[80] := [10('')];
#     myREALArray : ARRAY[0..9] OF REAL := [10(0.0)];
# END_VAR
#
# content of 'myProg.st':
#   PROGRAM _INIT
#  	    myUSINT;
#  	    myUINT;
# 	    mySTRING;
# 	    myWSTRING;
# 	    myTIME;
# 	    myTOD;
# 	    myDT;
# 	    myDINT;
# 	    myINTArray;
# 	    mySTRINGArray;
#       myREALArray;
# 	    myUDINT;
# 	    myDATE;
# 	    myLREAL;
# 	    myREAL;
# 	    myINT;
# 	    mySINT;
# 	    myBOOL;
#   END_PROGRAM
#
#   PROGRAM _CYCLIC
#
#   END_PROGRAM
#
#

from time import sleep
from datetime import time, date, timedelta, datetime
from pvi import *

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
# line ANSL is the 'modern' way to access PLC variables
# (compared to the older INA2000 line)
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
task1 = Task( cpu, 'myProg')

# create a list with variable names and values we want to write into
variableList = (   ('myBOOL', True), 
                ('myUSINT', 123),
                ('mySINT', -123),
                ('myUINT', 1234),
                ('myINT', -1234),
                ('myUDINT', 1234567),
                ('myDINT', -124567),                
                ('myREAL', 1.234e2 ),
                ('myLREAL', -3.1415e100),
                ('mySTRING', b'hello, world'),
                ('myWSTRING', 'hello, world'),
                ('myDT', datetime.fromisoformat('2011-11-04T00:05:23')),
                ('myTIME', timedelta(minutes = 3, seconds = 45, milliseconds= 33)),
                ('myTOD', time(hour=14, minute= 30, second = 13)),
                ('myDATE', date.today()),
                ('myINTArray', (1,2,3,4,5,6,7) ), # write the first seven elements
                ('mySTRINGArray', (b'Huey', b'Dewey', b'Louie') ), # write the first three elements
                ('myREALArray', 100.0) # set all elements to the same value
            )

run = True

def taskErrorChanged( error : int ):
    global run

    if error != 0:
        raise PviError(error)
    else: # connection to task available
        try:
            for name, value in variableList:
                variable = Variable( task1, name )
                variable.value = value # write into
                print( name + ' : ' + str(variable.value) ) # read from
                variable.kill
        except BaseException as e:
            print( e )
        finally:
            run = False


task1.errorChanged = taskErrorChanged


while run:
    pviConnection.doEvents() # must be cyclically called
    sleep(0.1)

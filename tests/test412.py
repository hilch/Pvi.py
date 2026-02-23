# test against 'coffee machine' in AS 4.12.9.18 SP
import unittest
from pathlib import Path
import sys
import string
import random
import datetime
from collections import OrderedDict
import time
from enum import IntEnum

pviPath = str(Path(__file__).parents[1])
cwd = str(Path(__file__).parents[0])

sys.path.append( pviPath )

from pvi import *

class myEnumType(IntEnum):
    eins = 0
    zwei = 1
    drei = 2



def cpuErrorChanged( self, error : int):     
    if error == 0:
        unittest.main(verbosity=1)
        pass
    else:
        raise PviError(error)

pviConnection = Connection() # start a Pvi connection
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=127.0.0.1' )
cpu.errorChanged = cpuErrorChanged


class TestLists( unittest.TestCase):

    def test_module_list(self):
        # read content
        allModules = [e['name'] for e in cpu.externalObjects if e['type'] == 'Module']
        self.assertIn('$$sysconf', allModules )
        self.assertIn('$arlogsys', allModules )
        self.assertIn('$arlogusr', allModules )
        self.assertIn('$fieldbus', allModules )
        self.assertIn('$safety', allModules )
        self.assertIn('Acp10map', allModules )
        self.assertIn('AsArProf', allModules )
        self.assertIn('AsArSdm', allModules )
        self.assertIn('CoffeeLib', allModules )
        self.assertIn('Convert', allModules )
        self.assertIn('DataObj', allModules )
        self.assertIn('FileIO', allModules )
        self.assertIn('LoopConR', allModules )
        self.assertIn('Visu', allModules )
        self.assertIn('Visu01', allModules )
        self.assertIn('Visu02', allModules )
        self.assertIn('Visu03', allModules )
        self.assertIn('acp10_mc', allModules )
        self.assertIn('acp10cfg', allModules )
        self.assertIn('acp10man', allModules )
        self.assertIn('acp10par', allModules )
        self.assertIn('acp10sdc', allModules )
        self.assertIn('acp10sim', allModules )
        self.assertIn('acp_err', allModules )
        self.assertIn('arconfig', allModules )
        self.assertIn('arial', allModules )
        self.assertIn('arialbd', allModules )
        self.assertIn('arialxsr', allModules )
        self.assertIn('asfw', allModules )
        self.assertIn('ashwd', allModules )
        self.assertIn('astime', allModules )
        self.assertIn('brewing', allModules )
        self.assertIn('brsystem', allModules )
        self.assertIn('cappu', allModules )
        self.assertIn('conv_ini', allModules )
        self.assertIn('conveyor', allModules )
        self.assertIn('espres', allModules )
        self.assertIn('feed_ini', allModules )
        self.assertIn('feeder', allModules )
        self.assertIn('heating', allModules )
        self.assertIn('iomap', allModules )
        self.assertIn('mainlogic', allModules )
        self.assertIn('motor_offi', allModules )
        self.assertIn('motor_sim', allModules )
        self.assertIn('ncglobal', allModules )
        self.assertIn('operator', allModules )
        self.assertIn('powerlnk', allModules )

    def test_task_list(self):
        # read content
        allTasks = [e['name'] for e in cpu.externalObjects if e['type'] == 'Task']
        self.assertIn( 'brewing', allTasks)
        self.assertIn( 'conveyor', allTasks)
        self.assertIn( 'feeder', allTasks)
        self.assertIn( 'heating', allTasks)
        self.assertIn( 'mainlogic', allTasks)
        self.assertIn( 'visAlarm', allTasks)
        self.assertIn( 'visCtrl', allTasks)
        self.assertIn( 'visTrend', allTasks)

    def test_globalvars_list(self):
        # read content
        allGlobalVars = [e['name'] for e in cpu.externalObjects if e['type'] == 'Pvar']
        self.assertIn( 'LCRPID_D_MODE_X', allGlobalVars )
        self.assertIn( 'LCRPID_FBK_MODE_INTERN', allGlobalVars )
        self.assertIn( 'LCRPID_MODE_AUTO', allGlobalVars )
        self.assertIn( 'LCRPID_MODE_CLOSE', allGlobalVars )
        self.assertIn( 'aoHeating', allGlobalVars )
        self.assertIn( 'atWaterTemp', allGlobalVars )
        self.assertIn( 'axConveyor', allGlobalVars )
        self.assertIn( 'axFeeder', allGlobalVars )
        self.assertIn( 'diStartCoffee', allGlobalVars )
        self.assertIn( 'doCupPull', allGlobalVars )
        self.assertIn( 'doDoseCoffee', allGlobalVars )
        self.assertIn( 'doDoseMilk', allGlobalVars )
        self.assertIn( 'doDoseSugar', allGlobalVars )
        self.assertIn( 'doPumpWater', allGlobalVars )
        self.assertIn( 'gActConveyorPosition', allGlobalVars )
        self.assertIn( 'gActConveyorVelocity', allGlobalVars )
        self.assertIn( 'gActFeederPosition', allGlobalVars )
        self.assertIn( 'gActFeederVelocity', allGlobalVars )
        self.assertIn( 'gBrewing', allGlobalVars )
        self.assertIn( 'gConveyor', allGlobalVars )
        self.assertIn( 'gFeeder', allGlobalVars )
        self.assertIn( 'gHeating', allGlobalVars )
        self.assertIn( 'gMainLogic', allGlobalVars )
        self.assertIn( 'mcHOME_DEFAULT', allGlobalVars )
        self.assertIn( 'sdmOPTION_VOLATILE', allGlobalVars )
        self.assertIn( 'sdm_APPMODE_ERROR', allGlobalVars )
        self.assertIn( 'sdm_APPMODE_OK', allGlobalVars )
        self.assertIn( 'sdm_APPMODE_WARNING', allGlobalVars )

    def test_localvars1( self ):
        task = Task( cpu, 'brewing' )
        variableNames = [ _['name'] for _ in task.externalObjects]
        self.assertEqual( variableNames, ['Edge0000100000', 'coffeeTP', 'milkTP', 'pBrewingText', 'sBREWING', 'sDOSING', 'sFINISH', 
                                          'sSTANDBY', 'sugarTP', 'waterTP'])
        task.kill()

    def test_localvars2( self ):
        task = Task( cpu, 'conveyor' )
        variableNames = [ _['name'] for _ in task.externalObjects]
        self.assertEqual( variableNames,['MC_ReadActualPosition_0', 'MC_ReadActualVelocity_0', 'conveyorMC_Home', 'conveyorMC_MoveAdditive', 
                                         'conveyorMC_Power', 'conveyorMC_ReadAxisError', 'conveyorMC_ReadStatus', 'conveyorMC_Reset', 
                                         'conveyorTakeoutMC_MoveAdditve', 'zz000600010000', 'zz000700010000', 'zz000700010001', 
                                         'zzBOOL00010000', 'zzBOOL00010001', 'zzRTR000010000', 'zzRTR000010001', 'zzRTR000010002'])
        task.kill()

    def test_localvars3( self ):
        task = Task( cpu, 'feeder' )
        variableNames = [ _['name'] for _ in task.externalObjects]
        self.assertEqual( variableNames,['MC_ReadActualPosition_0', 'MC_ReadActualVelocity_0', 'feederMC_Home', 'feederMC_MoveAdditive', 
                                         'feederMC_Power', 'feederMC_ReadAxisError', 'feederMC_ReadStatus', 'feederMC_Reset', 
                                         'zz000600010000', 'zz000700010000', 'zz000700010001', 'zzBOOL00010000', 'zzBOOL00010001', 
                                         'zzBOOL00010002', 'zzBOOL00010003', 'zzBOOL00010004', 'zzRTR000010000', 'zzRTR000010001'])
        task.kill()


class TestCpuInfo( unittest.TestCase):
    def test_cpuName(self):
        self.assertEqual( cpu.name, '@Pvi/LNANSL/TCP/myArsim' )

    def test_cpuStatus(self):
        status = cpu.status
        self.assertIn( 'ST', status.keys() )
        self.assertIn( 'RunState', status.keys() )  
        self.assertIn( status['ST'] , ['ColdStart', 'WarmStart', 'Reset'])
        self.assertIn( status['RunState'] , ['RUN', 'SERV'])

    def test_cpuInfo(self):
        info = cpu.cpuInfo
        self.assertEqual( info, {'CT': '1A4000.00'} )


class TestTaskInfo( unittest.TestCase ):
    def test_Taskinfo1(self):
        task = Task( cpu, 'mainlogic')
        self.assertEqual( 'Running', task.status['ST'] )
        task.kill

    def test_Taskinfo2(self):
        task = Task( cpu, 'myTask', CD='/RO=::mainlogic')
        self.assertEqual( 'Running', task.status['ST'] )
        task.kill

    def test_applicationModuleTask(self):
        task = Task( cpu, 'myAppTask', CD='/RO=AppMod1::myApptask1')
        self.assertEqual( 'Running', task.status['ST'] )
        self.assertIn( 'i', task.variables)
        task.kill


class TestVariables( unittest.TestCase):
    def test_variableInfo(self):
        task = Task( cpu, 'mainlogic')
        var = Variable( task, 'a-nicer-variable-name', CD ='gHeating.status.actTemp', UT='shows temperature in degree Celsius', RF=200, HY = 10 )
        self.assertEqual( var.name, '@Pvi/LNANSL/TCP/myArsim/mainlogic/a-nicer-variable-name' )
        self.assertEqual( var.objectName, 'a-nicer-variable-name' )
        self.assertEqual( var.dataType, 'f32' )
        self.assertEqual( var.userName, 'a-nicer-variable-name' )
        self.assertEqual( var.userTag, 'shows temperature in degree Celsius' )
        self.assertEqual( var.refresh, 200 ) 
        self.assertEqual( var.hysteresis, 10.0 )
        var.kill()
        task.kill()

    def test_roi(self):
        task = Task( cpu, 'myProg')
        var = Variable(task, 'x', CD='/RO=myComplexStruct.myStruct2[2].member2[2] /ROI=1') 
        self.assertEqual( var.value, 55)
        var.kill()
        task.kill()

    def test_SINT(self):
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myComplexStruct.sint')
        self.assertEqual( var.dataType, 'i8')
        for value in range( -127, 127, 0xf ):
            var.value = value
            self.assertEqual( var.value, value )
        var.value = -11
        def func(var : Variable):
            var.value = "wrong"
        self.assertRaises( TypeError, func)
        del func
        var.kill()
        task.kill()

    def test_INT(self):
        task = Task( cpu, 'myProg')        
        var = Variable(task, 'myComplexStruct.int')
        self.assertEqual( var.dataType, 'i16')        
        for value in range( -32767, 32767, 0xfff):
            var.value = value
            self.assertEqual( var.value, value )
        var.value = -12
        var.kill()
        task.kill()

    def test_INTArray(self):
        task = Task( cpu, 'myProg')      
        for n in range(0,10):
             var = Variable(task, f"myComplexStruct.intvector[{n}]")
             var.value = n
             var.kill()
        var = Variable(task, "myComplexStruct.intvector")
        self.assertEqual( var.dataType, 'i16[0..9]')         
        self.assertEqual( var.value, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        var.kill() 
        for n in range(0,10):
             var = Variable(task, f"myComplexStruct.intvector[{n}]")
             var.value = 300 + n
             var.kill()                
        task.kill()     

    def test_DINT(self):
        task = Task( cpu, 'myProg')    
        var = Variable(task, 'myComplexStruct.dint')
        self.assertEqual( var.dataType, 'i32')         
        for value in range( -2147483647, 2147483647, 0xfffffff):
            var.value = value
            self.assertEqual( var.value, value )
        var.value = -13
        var.kill()
        task.kill()

    def test_BOOL(self):
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myComplexStruct.bool')
        self.assertEqual( var.dataType, 'boolean')         
        var.value = True
        self.assertEqual( var.value, True )
        var.value = False
        self.assertEqual( var.value, False)
        var.value = 99
        self.assertEqual( var.value, True )
        var.value = False                                   
        var.kill()
        task.kill()

    def test_USINT(self):
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myComplexStruct.usint')
        self.assertEqual( var.dataType, 'u8')         
        for value in range( -0xf, 0xff, 0xf):
            var.value = value
            if value >= 0:
                self.assertEqual( var.value, value )
            else:
                self.assertNotEqual( var.value, value ) 
        var.value = 11               
        var.kill()
        task.kill()

    def test_UINT(self):
        task = Task( cpu, 'myProg')        
        var = Variable(task, 'myComplexStruct.uint')
        self.assertEqual( var.dataType, 'u16')         
        for value in range( -0xf, 0xffff, 0xfff):
            var.value = value
            if value >= 0:
                self.assertEqual( var.value, value )
            else:
                self.assertNotEqual( var.value, value ) 
        var.value = 12                 
        var.kill()
        task.kill()

    def test_UDINT(self):
        task = Task( cpu, 'myProg')        
        var = Variable(task, 'myComplexStruct.udint')
        self.assertEqual( var.dataType, 'u32')         
        for value in range( -0xf, 0xffffffff, 0xfffffff):
            var.value = value
            if value >= 0:
                self.assertEqual( var.value, value )
            else:
                self.assertNotEqual( var.value, value ) 
        var.value = 13                 
        var.kill()
        task.kill()


    def test_REAL(self):
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myComplexStruct.real')
        self.assertEqual( var.dataType, 'f32')         
        for value in range( -10,11,1):
            var.value = float(value)
            self.assertEqual(round(var.value, 6), round(value,6) )
        var.value = 3.14
        var.kill()
        task.kill()

    def test_LREAL(self):
        task = Task( cpu, 'myProg')  
        var = Variable(task, 'myComplexStruct.lreal')
        self.assertEqual( var.dataType, 'f64')         
        for value in range( -10,11,1):
            var.value = float(value)
            self.assertEqual(round(var.value, 6), round(value,6) )
        var.value = 6.28
        var.kill()        
        task.kill()

    def test_REALArray(self):
        task = Task( cpu, 'myProg')        
        for n in range(0,10):
             var = Variable(task, f"myComplexStruct.vector[{n}]")
             var.value = float(200 + n)
             var.kill()
        var = Variable(task, "myComplexStruct.vector")
        self.assertEqual( var.dataType, 'f32[1..10]')          
        self.assertEqual( var.value, [200.0, 201.0, 202.0, 203.0, 204.0, 205.0, 206.0, 207.0, 208.0, 209.0])
        var.kill()
        var = Variable(task, 'myReal', CD="myComplexStruct.vector")
        self.assertEqual( var.value, [200.0, 201.0, 202.0, 203.0, 204.0, 205.0, 206.0, 207.0, 208.0, 209.0] )
        var.kill()
        var = Variable( task, 'myComplexStruct.matrix')
        self.assertEqual( var.value, [[1000.0, 1001.0, 1002.0, 1003.0], [1010.0, 1011.0, 1012.0, 1013.0], 
                                      [1020.0, 1021.0, 1022.0, 1023.0], [1030.0, 1031.0, 1032.0, 1033.0], 
                                      [1040.0, 1041.0, 1042.0, 1043.0], [1050.0, 1051.0, 1052.0, 1053.0], 
                                      [1060.0, 1061.0, 1062.0, 1063.0], [1070.0, 1071.0, 1072.0, 1073.0], 
                                      [1080.0, 1081.0, 1082.0, 1083.0], [1090.0, 1091.0, 1092.0, 1093.0]] )
        var.kill
        task.kill()       

    def test_STRING(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myComplexStruct.string')
        self.assertEqual( var.dataType, 'string')            
        for n in range(0,3):
            random_string = bytes(''.join(random.choices(string.printable, k=80)), encoding='ascii')
            var.value = random_string
            pviConnection.sleep(100)
            self.assertEqual(var.value, random_string)
        def func1(var : Variable):
            var.value = "wrong"
        self.assertRaises( TypeError, func1)
        def func2(var : Variable):
            var.value = 1
        self.assertRaises( TypeError, func2)
        var.value = b'The quick brown fox jumps over the lazy dog'            
        var.kill()  

        for n in range(0,10):
             var = Variable(task, f"myComplexStruct.stringlist[{n}]")
             var.value = bytes(string.ascii_uppercase[n], encoding='ascii')
             var.kill()
        var = Variable(task, "myComplexStruct.stringlist")
        self.assertEqual( var.value, [b'A', b'B', b'C', b'D', b'E', b'F', b'G', b'H', b'I', b'J'])
        var.kill()

    def test_WSTRING(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myComplexStruct.wstring')
        self.assertEqual( var.dataType, 'wstring')          
        for n in range(0,3):
            random_string = ''.join(random.choices(string.printable, k=80))
            var.value = random_string
            pviConnection.sleep(100)
            self.assertEqual(var.value, random_string)
        var.value = 'The quick brown fox jumps over the lazy dog'              
        var.kill()       

        for n in range(0,10):
             var = Variable(task, f"myComplexStruct.wstringlist[{n}]")
             var.value = string.ascii_uppercase[n]
             var.kill()
        var = Variable(task, "myComplexStruct.wstringlist")
        self.assertEqual( var.value, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        var.kill()         
        task.kill()

    def test_TIME(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myComplexStruct.time')
        self.assertEqual( var.dataType, 'time')          
        var.value = 0
        self.assertEqual( var.value, datetime.timedelta(0) )
        var.value = 1200
        self.assertEqual( var.value, datetime.timedelta(seconds=1, microseconds=200000) )           
        var.value = 0        
        var.kill()
        task.kill()


    def test_DATE(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myComplexStruct.date')
        self.assertEqual( var.dataType, 'date')          
        var.value = 0
        self.assertEqual( var.value, datetime.date(1970, 1, 1) )
        var.value = datetime.date(1970,1,1)
        self.assertEqual( var.value, datetime.date(1970, 1, 1) )        
        var.value = 10000000
        self.assertEqual( var.value, datetime.date(1970, 4, 26))
        var.value = datetime.date(2021,2,3)
        self.assertEqual( var.value, datetime.date(2021,2,3))  
        var.value = datetime.date(1970,1,1)     
        var.kill()
        task.kill()

    def test_DATETIME(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myComplexStruct.dt')
        self.assertEqual( var.dataType, 'dt')          
        var.value = 0
        self.assertEqual( var.value, datetime.datetime(1970, 1, 1, 0, 0) )
        var.value = 10000000
        self.assertEqual( var.value, datetime.datetime(1970, 4, 26, 17, 46, 40))
        var.value = datetime.datetime(2021,2,3,4,5,6)
        self.assertEqual( var.value, datetime.datetime(2021, 2, 3, 4, 5, 6))    
        var.value = 0              
        var.kill()
        task.kill()


    def test_TIMEOFDAY(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myComplexStruct.tod')
        self.assertEqual( var.dataType, 'tod')          
        var.value = 0
        self.assertEqual( var.value, datetime.time(0, 0) )
        var.value = 10000000
        self.assertEqual( var.value, datetime.time(2, 46, 40))
        var.value = datetime.time(1, 2, 3)
        self.assertEqual( var.value, datetime.time(1, 2, 3)) 
        var.value = 0                 
        var.kill()
        task.kill()


class TestEnums( unittest.TestCase):
    def test_enum(self):
        task = Task( cpu, 'myProg')
        var = Variable( task, 'myComplexStruct.myEnum' )
        var.value = 2
        self.assertEqual( var.value, myEnumType.drei)
        var.value = myEnumType.eins
        self.assertEqual( var.value.value, 0)        
        var.kill
        task.kill
        
    def test_enumlist(self):       
        task = Task( cpu, 'myProg')             
        var = Variable( task, 'myComplexStruct.enumlist')
        var.value = [myEnumType.drei, 0, myEnumType.zwei, 0, myEnumType.eins]
        self.assertEqual( var.value, [myEnumType.drei, myEnumType.eins, myEnumType.zwei, myEnumType.eins, myEnumType.eins])
        var.value = [myEnumType.eins, myEnumType.zwei, myEnumType.drei, myEnumType.eins, myEnumType.zwei]
        task.kill

class TestDerivedDatatypes( unittest.TestCase):
    def test_derived1(self):
        task = Task( cpu, 'myProg')
        var = Variable( task, 'myComplexStruct.derived1' )
        self.assertEqual( var.value, 4)
        self.assertEqual( var.dataType, 'myDerivedType1')
        var.kill
        var = Variable( task, 'myComplexStruct.derived2' )
        self.assertEqual( var.value, [3,4,5,6])
        self.assertEqual( var.dataType, 'myDerivedType2[3..6]')        
        task.kill


class TestStructures( unittest.TestCase):
    def test_simpleStructure(self):
        task = Task( cpu, 'myProg')
        var = Variable( task, 'myComplexStruct.myStruct0' )
        self.assertEqual( var.dataType, 'myStructType')        
        var.kill
        task.kill

    def test_structArray(self):
        task = Task( cpu, 'myProg')
        var = Variable( task, 'myComplexStruct.myStruct1' )
        self.assertEqual( var.dataType, 'myStructType[0..1]')
        self.assertEqual( var.value,[OrderedDict({'.member1': 3, '.member2': [33, 44, 55]}), 
                                     OrderedDict({'.member1': 3, '.member2': [33, 44, 55]})])        
        var.kill
        var = Variable( task, 'myComplexStruct.myStruct2' ) # array with only one element
        self.assertEqual( var.dataType, 'myStructType[2..2]')  
        self.assertEqual( var.value, [OrderedDict({'.member1': 3, '.member2': [33, 44, 55]})])     
        var.kill        
        task.kill

    def test_complexStructure(self):
        task = Task( cpu, 'myProg')
        var = Variable( task, 'myComplexStruct' )
        
        start = time.time()
        while (time.time() - start) < 5: # ensure all writes have been done
            pviConnection.doEvents()
        
        self.assertEqual( var.value['.bool'], False)
        self.assertEqual( var.value['.usint'], 11)
        self.assertEqual( var.value['.uint'], 12)
        self.assertEqual( var.value['.udint'], 13)
        self.assertEqual( var.value['.sint'], -11)
        self.assertEqual( var.value['.int'], -12)
        self.assertEqual( var.value['.dint'], -13)
        self.assertEqual( round(var.value['.real']), 3)
        self.assertEqual( round(var.value['.lreal']), 6)
        self.assertEqual( var.value['.time'], datetime.timedelta(0))
        self.assertEqual( var.value['.tod'], datetime.time(0, 0))
        self.assertEqual( var.value['.date'], datetime.date(1970, 1, 1))
        self.assertEqual( var.value['.dt'], datetime.datetime(1970, 1, 1, 0, 0))
        self.assertEqual( var.value['.string'], b'The quick brown fox jumps over the lazy dog')
        self.assertEqual( var.value['.wstring'], 'The quick brown fox jumps over the lazy dog')
        self.assertEqual( var.value['.stringlist'], [b'A', b'B', b'C', b'D', b'E', b'F', b'G', b'H', b'I', b'J'])
        self.assertEqual( var.value['.wstringlist'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.assertEqual( var.value['.vector'], [200.0, 201.0, 202.0, 203.0, 204.0, 205.0, 206.0, 207.0, 208.0, 209.0])
        self.assertEqual( var.value['.intvector'], [300, 301, 302, 303, 304, 305, 306, 307, 308, 309])
        self.assertEqual( var.value['.matrix'], [[1000.0, 1001.0, 1002.0, 1003.0],
                                                [1010.0, 1011.0, 1012.0, 1013.0],
                                                [1020.0, 1021.0, 1022.0, 1023.0],
                                                [1030.0, 1031.0, 1032.0, 1033.0],
                                                [1040.0, 1041.0, 1042.0, 1043.0],
                                                [1050.0, 1051.0, 1052.0, 1053.0],
                                                [1060.0, 1061.0, 1062.0, 1063.0],
                                                [1070.0, 1071.0, 1072.0, 1073.0],
                                                [1080.0, 1081.0, 1082.0, 1083.0],
                                                [1090.0, 1091.0, 1092.0, 1093.0]] )
        self.assertEqual( var.value['.myStruct0.member1'], 3)
        self.assertEqual( var.value['.myStruct0.member2'], [33, 44, 55])
        self.assertEqual( var.value['.myStruct1[0].member1'], 3)
        self.assertEqual( var.value['.myStruct1[0].member2'], [33, 44, 55])
        self.assertEqual( var.value['.myStruct1[1].member1'], 3)
        self.assertEqual( var.value['.myStruct1[1].member2'], [33, 44, 55])
        self.assertEqual( var.value['.myStruct2[2].member1'], 3)
        self.assertEqual( var.value['.myStruct2[2].member2'], [33, 44, 55])
        self.assertEqual( var.value['.myStruct3[-1].member1'], 4)
        self.assertEqual( var.value['.myStruct3[-1].member2'], [9, 19, 29])
        self.assertEqual( var.value['.myStruct3[0].member1'], 5)
        self.assertEqual( var.value['.myStruct3[0].member2'], [10, 20, 30])
        self.assertEqual( var.value['.myStruct3[1].member1'], 6)
        self.assertEqual( var.value['.myStruct3[1].member2'], [11, 21, 31])
        self.assertEqual( var.value['.myStruct4[0,0].member1'], 0)
        self.assertEqual( var.value['.myStruct4[0,0].member2'], [0, 0, 0])
        self.assertEqual( var.value['.myStruct4[0,1].member1'], 1)
        self.assertEqual( var.value['.myStruct4[0,1].member2'], [1, 1, 1])
        self.assertEqual( var.value['.myStruct4[0,2].member1'], 2)
        self.assertEqual( var.value['.myStruct4[0,2].member2'], [2, 2, 2])
        self.assertEqual( var.value['.myStruct4[0,3].member1'], 3)
        self.assertEqual( var.value['.myStruct4[0,3].member2'], [3, 3, 3])
        self.assertEqual( var.value['.myStruct4[1,0].member1'], 10)
        self.assertEqual( var.value['.myStruct4[1,0].member2'], [20, 30, 40])
        self.assertEqual( var.value['.myStruct4[1,1].member1'], 11)
        self.assertEqual( var.value['.myStruct4[1,1].member2'], [21, 31, 41])
        self.assertEqual( var.value['.myStruct4[1,2].member1'], 12)
        self.assertEqual( var.value['.myStruct4[1,2].member2'], [22, 32, 42])
        self.assertEqual( var.value['.myStruct4[1,3].member1'], 13)
        self.assertEqual( var.value['.myStruct4[1,3].member2'], [23, 33, 43])
        self.assertEqual( var.value['.myStruct4[2,0].member1'], 20)
        self.assertEqual( var.value['.myStruct4[2,0].member2'], [40, 60, 80])
        self.assertEqual( var.value['.myStruct4[2,1].member1'], 21)
        self.assertEqual( var.value['.myStruct4[2,1].member2'], [41, 61, 81])
        self.assertEqual( var.value['.myStruct4[2,2].member1'], 22)
        self.assertEqual( var.value['.myStruct4[2,2].member2'], [42, 62, 82])
        self.assertEqual( var.value['.myStruct4[2,3].member1'], 23)
        self.assertEqual( var.value['.myStruct4[2,3].member2'], [43, 63, 83])
        self.assertEqual( var.value['.myStruct5[0].struct1.member1'], 5)
        self.assertEqual( var.value['.myStruct5[0].struct1.member2'], [2, 3, 4])
        self.assertEqual( var.value['.myStruct5[0].structList[0].member1'], 10)
        self.assertEqual( var.value['.myStruct5[0].structList[0].member2'], [10, 11, 12])
        self.assertEqual( var.value['.myStruct5[0].structList[1].member1'], 11)
        self.assertEqual( var.value['.myStruct5[0].structList[1].member2'], [20, 21, 22])
        self.assertEqual( var.value['.myStruct5[0].structList[2].member1'], 12)
        self.assertEqual( var.value['.myStruct5[0].structList[2].member2'], [30, 31, 32])
        self.assertEqual( var.value['.myStruct5[1].struct1.member1'], 6)
        self.assertEqual( var.value['.myStruct5[1].struct1.member2'], [3, 4, 5])
        self.assertEqual( var.value['.myStruct5[1].structList[0].member1'], 11)
        self.assertEqual( var.value['.myStruct5[1].structList[0].member2'], [10, 11, 12])
        self.assertEqual( var.value['.myStruct5[1].structList[1].member1'], 12)
        self.assertEqual( var.value['.myStruct5[1].structList[1].member2'], [20, 21, 22])
        self.assertEqual( var.value['.myStruct5[1].structList[2].member1'], 13)
        self.assertEqual( var.value['.myStruct5[1].structList[2].member2'], [30, 31, 32])
        self.assertEqual( var.value['.myStruct5[2].struct1.member1'], 7)
        self.assertEqual( var.value['.myStruct5[2].struct1.member2'], [4, 5, 6])
        self.assertEqual( var.value['.myStruct5[2].structList[0].member1'], 12)
        self.assertEqual( var.value['.myStruct5[2].structList[0].member2'], [10, 11, 12])
        self.assertEqual( var.value['.myStruct5[2].structList[1].member1'], 13)
        self.assertEqual( var.value['.myStruct5[2].structList[1].member2'], [20, 21, 22])
        self.assertEqual( var.value['.myStruct5[2].structList[2].member1'], 14)
        self.assertEqual( var.value['.myStruct5[2].structList[2].member2'], [30, 31, 32])
        self.assertEqual( var.value['.myEnum'], myEnumType.eins)
        self.assertEqual( var.value['.subrange1'], -3)
        self.assertEqual( var.value['.derived1'], 4)
        self.assertEqual( var.value['.derived2'], [3, 4, 5, 6])
        self.assertEqual( var.value['.n'], 99 )

        
        var.kill()
        task.kill()

if __name__ == "__main__":
    pviConnection.start()


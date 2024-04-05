# test against 'coffee machine' in AS 4.1.17.113 SP
import unittest
from pathlib import Path
import sys
import string
import random
import datetime
from collections import OrderedDict

pviPath = str(Path(__file__).parents[1])
cwd = str(Path(__file__).parents[0])

sys.path.append( pviPath )

from pvi import *


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


class TestVariables( unittest.TestCase):
    def test_variableInfo(self):
        task = Task( cpu, 'mainlogic')
        var = Variable( task, 'a-nicer-variable-name', CD ='gHeating.status.actTemp', UT='shows temperature in degree Celsius', RF=200, HY = 10 )
        self.assertEqual( var.name, '@Pvi/LNANSL/TCP/myArsim/mainlogic/gHeating.status.actTemp' )
        self.assertEqual( var.objectName, 'gHeating.status.actTemp' )
        self.assertEqual( var.dataType, 'f32' )
        self.assertEqual( var.userName, 'a-nicer-variable-name' )
        self.assertEqual( var.userTag, 'shows temperature in degree Celsius' )
        self.assertEqual( var.refresh, 200 ) 
        self.assertEqual( var.hysteresis, 10.0 )
        var.kill()
        task.kill()

    def test_SINT(self):
        task = Task( cpu, 'myProg')
        var = Variable(task, 'mySINT')
        self.assertEqual( var.dataType, 'i8')
        for value in range( -127, 127, 0xf ):
            var.value = value
            self.assertEqual( var.value, value )
        def func(var : Variable):
            var.value = "wrong"
        self.assertRaises( TypeError, func)
        del func
        var.kill()
        task.kill()

    def test_INT(self):
        task = Task( cpu, 'myProg')        
        var = Variable(task, 'myINT')
        self.assertEqual( var.dataType, 'i16')        
        for value in range( -32767, 32767, 0xfff):
            var.value = value
            self.assertEqual( var.value, value )
        var.kill()
        task.kill()

    def test_INTArray(self):
        task = Task( cpu, 'myProg')      
        for n in range(0,10):
             var = Variable(task, f"myINTArray[{n}]")
             var.value = n
             var.kill()
        var = Variable(task, "myINTArray")
        self.assertEqual( var.dataType, 'i16[0..9]')         
        self.assertEqual( var.value, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        var.kill() 
        task.kill()     

    def test_DINT(self):
        task = Task( cpu, 'myProg')    
        var = Variable(task, 'myDINT')
        self.assertEqual( var.dataType, 'i32')         
        for value in range( -2147483647, 2147483647, 0xfffffff):
            var.value = value
            self.assertEqual( var.value, value )
        var.kill()
        task.kill()

    def test_BOOL(self):
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myBOOL')
        self.assertEqual( var.dataType, 'boolean')         
        var.value = True
        self.assertEqual( var.value, True )
        var.value = False
        self.assertEqual( var.value, False)
        var.value = 99
        self.assertEqual( var.value, True )                                   
        var.kill()
        task.kill()

    def test_USINT(self):
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myUSINT')
        self.assertEqual( var.dataType, 'u8')         
        for value in range( -0xf, 0xff, 0xf):
            var.value = value
            if value >= 0:
                self.assertEqual( var.value, value )
            else:
                self.assertNotEqual( var.value, value )                
        var.kill()
        task.kill()

    def test_UINT(self):
        task = Task( cpu, 'myProg')        
        var = Variable(task, 'myUINT')
        self.assertEqual( var.dataType, 'u16')         
        for value in range( -0xf, 0xffff, 0xfff):
            var.value = value
            if value >= 0:
                self.assertEqual( var.value, value )
            else:
                self.assertNotEqual( var.value, value )                  
        var.kill()
        task.kill()

    def test_UDINT(self):
        task = Task( cpu, 'myProg')        
        var = Variable(task, 'myUDINT')
        self.assertEqual( var.dataType, 'u32')         
        for value in range( -0xf, 0xffffffff, 0xfffffff):
            var.value = value
            if value >= 0:
                self.assertEqual( var.value, value )
            else:
                self.assertNotEqual( var.value, value )                  
        var.kill()
        task.kill()


    def test_REAL(self):
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myREAL')
        self.assertEqual( var.dataType, 'f32')         
        for value in range( -10,11,1):
            var.value = float(value)
            self.assertEqual(round(var.value, 6), round(value,6) )
        var.kill()
        task.kill()

    def test_LREAL(self):
        task = Task( cpu, 'myProg')  
        var = Variable(task, 'myLREAL')
        self.assertEqual( var.dataType, 'f64')         
        for value in range( -10,11,1):
            var.value = float(value)
            self.assertEqual(round(var.value, 6), round(value,6) )
        var.kill()        
        task.kill()

    def test_REALArray(self):
        task = Task( cpu, 'myProg')        
        for n in range(0,10):
             var = Variable(task, f"myREALArray[{n}]")
             var.value = float(n)
             var.kill()
        var = Variable(task, "myREALArray")
        self.assertEqual( var.dataType, 'f32[0..9]')          
        self.assertEqual( var.value, (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0))
        var.kill()
        task.kill()     

    def test_STRING(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'mySTRING')
        self.assertEqual( var.dataType, 'string')            
        for n in range(0,3):
            random_string = bytes(''.join(random.choices(string.printable, k=80)), encoding='ascii')
            var.value = random_string
            pviConnection.sleep(100)
            self.assertEqual(var.value, random_string)
        def func(var : Variable):
            var.value = "wrong"
        self.assertRaises( TypeError, func)
        def func(var : Variable):
            var.value = 1
        self.assertRaises( TypeError, func)            
        del func
        var.kill()  

        for n in range(0,10):
             var = Variable(task, f"mySTRINGArray[{n}]")
             var.value = bytes(string.ascii_uppercase[n], encoding='ascii')
             var.kill()
        var = Variable(task, "mySTRINGArray")
        self.assertEqual( var.value, (b'A', b'B', b'C', b'D', b'E', b'F', b'G', b'H', b'I', b'J'))
        var.kill()

    def test_WSTRING(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myWSTRING')
        self.assertEqual( var.dataType, 'wstring')          
        for n in range(0,3):
            random_string = ''.join(random.choices(string.printable, k=80))
            var.value = random_string
            pviConnection.sleep(100)
            self.assertEqual(var.value, random_string)
        var.kill()       

        for n in range(0,10):
             var = Variable(task, f"myWSTRINGArray[{n}]")
             var.value = string.ascii_uppercase[n]
             var.kill()
        var = Variable(task, "myWSTRINGArray")
        self.assertEqual( var.value, ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'))
        var.kill()         
        task.kill()

    def test_TIME(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myTIME')
        self.assertEqual( var.dataType, 'time')          
        var.value = 0
        self.assertEqual( var.value, datetime.timedelta(0) )
        var.value = 1200
        self.assertEqual( var.value, datetime.timedelta(seconds=1, microseconds=200000) )           
        var.kill()
        task.kill()


    def test_DATE(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myDATE')
        self.assertEqual( var.dataType, 'date')          
        var.value = 0
        self.assertEqual( var.value, datetime.date(1970, 1, 1) )
        var.value = 10000000
        self.assertEqual( var.value, datetime.date(1970, 4, 26))
        var.value = datetime.date(2021,2,3)
        self.assertEqual( var.value, datetime.date(2021,2,3))        
        var.kill()
        task.kill()

    def test_DATETIME(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myDT')
        self.assertEqual( var.dataType, 'dt')          
        var.value = 0
        self.assertEqual( var.value, datetime.datetime(1970, 1, 1, 1, 0) )
        var.value = 10000000
        self.assertEqual( var.value, datetime.datetime(1970, 4, 26, 19, 46, 40))
        var.value = datetime.datetime(2021,2,3,4,5,6)
        self.assertEqual( var.value, datetime.datetime(2021, 2, 3, 4, 5, 6))          
        var.kill()
        task.kill()

    def test_TIMEOFDAY(self):   
        task = Task( cpu, 'myProg')
        var = Variable(task, 'myTOD')
        self.assertEqual( var.dataType, 'tod')          
        var.value = 0
        self.assertEqual( var.value, datetime.time(0, 0) )
        var.value = 10000000
        self.assertEqual( var.value, datetime.time(2, 46, 40))
        var.value = datetime.time(1, 2, 3)
        self.assertEqual( var.value, datetime.time(1, 2, 3))          
        var.kill()
        task.kill()

class TestEnums( unittest.TestCase):
    def test_enum(self):
        task = Task( cpu, 'myProg')
        var = Variable( task, 'myEnumeration' )
        self.assertEqual( var.dataType, 'i32')
        var.value = 2
        self.assertEqual( var.value, 2 )
        var.kill
        task.kill

class TestDerivedDatatypes( unittest.TestCase):
    def test_derived1(self):
        task = Task( cpu, 'myProg')
        var = Variable( task, 'myDerivedDataType' )
        self.assertEqual( var.dataType, 'u8[0..3]')
        var.kill
        task.kill


class TestStructures( unittest.TestCase):
    def test_simpleStructure(self):
        task = Task( cpu, 'myProg')
        var = Variable( task, 'mySimpleStruct' )
        self.assertEqual( var.dataType, 'myStructType')        
        var.kill
        task.kill

    def test_structArray(self):
        task = Task( cpu, 'myProg')
        var = Variable( task, 'myStructArray' )
        self.assertEqual( var.dataType, 'myStructType[0..1]')        
        var.kill
        task.kill

    def test_complexStructure(self):
        task = Task( cpu, 'myProg')
        var = Variable( task, 'myComplexStruct.element' )
        var.value = 11
        var.kill()
        var = Variable( task, 'myComplexStruct.positionDataElements[0].EndlessPositionData[0].MTPhase' )
        var.value = 22
        var.kill()
        var = Variable( task, 'myComplexStruct.positionDataElements[0].EndlessPositionData[1].RefOffset' )
        var.value = 33
        var.kill()
        var = Variable( task, 'myComplexStruct.myStruct2.member' )
        var.value = 44
        var.kill()
        var = Variable( task, 'myComplexStruct.myEnum' )
        var.value = 2
        var.kill()
        var = Variable( task, 'myComplexStruct.myDerived[3]' )
        var.value = 55
        var.kill()
        var = Variable( task, 'myComplexStruct' )
        self.assertEqual( var.value, OrderedDict([('.element', 11), 
                                                  ('.positionDataElements[2].EndlessPositionData[0].MTPhase', 22), 
                                                  ('.positionDataElements[2].EndlessPositionData[0].MTDiffInteger', 0), 
                                                  ('.positionDataElements[2].EndlessPositionData[0].MTDiffFract', 0), 
                                                  ('.positionDataElements[2].EndlessPositionData[0].RefOffset', 0), 
                                                  ('.positionDataElements[2].EndlessPositionData[0].Checksum', 0), 
                                                  ('.positionDataElements[2].EndlessPositionData[1].MTPhase', 0), 
                                                  ('.positionDataElements[2].EndlessPositionData[1].MTDiffInteger', 0), 
                                                  ('.positionDataElements[2].EndlessPositionData[1].MTDiffFract', 0), 
                                                  ('.positionDataElements[2].EndlessPositionData[1].RefOffset', 33), 
                                                  ('.positionDataElements[2].EndlessPositionData[1].Checksum', 0), 
                                                  ('.myStruct1.member', 0), 
                                                  ('.myStruct2.member', 44), 
                                                  ('.myEnum', 2), 
                                                  ('.myDerived', (0, 0, 0, 55))]) )
        var.kill()
        task.kill()

if __name__ == "__main__":
    pviConnection.start()


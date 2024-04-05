# test against 'coffee machine' in AS 4.1.17.113 SP
import unittest
from pathlib import Path
import sys

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
        self.assertIn('$accsec', allModules )
        self.assertIn('$arlogconn', allModules )
        self.assertIn('$arlogsys', allModules )
        self.assertIn('$arlogusr', allModules )
        self.assertIn('$fieldbus', allModules )
        self.assertIn('$firewall', allModules )
        self.assertIn('$motion', allModules )
        self.assertIn('$safety', allModules )
        self.assertIn('$textsys', allModules )
        self.assertIn('$unitsys', allModules )
        self.assertIn('$versinfo', allModules )
        self.assertIn('Acp10map', allModules )
        self.assertIn('AsArProf', allModules )
        self.assertIn('AsArSdm', allModules )
        self.assertIn('CoffeeLib', allModules )
        self.assertIn('Convert', allModules )
        self.assertIn('DataObj', allModules )
        self.assertIn('FileIO', allModules )
        self.assertIn('LoopConR', allModules )
        self.assertIn('Role', allModules )
        self.assertIn('TCData', allModules )
        self.assertIn('User', allModules )
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
        self.assertIn('acp10sys', allModules )
        self.assertIn('acp_err', allModules )
        self.assertIn('arconfig', allModules )
        self.assertIn('arial', allModules )
        self.assertIn('arialbd', allModules )
        self.assertIn('arialxsr', allModules )
        self.assertIn('asfw', allModules )
        self.assertIn('ashwac', allModules )
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
        var.kill
        task.kill

    def test_variableValue1(self):
        task = Task( cpu, 'heating')
        varReal = Variable(task, 'gMainLogic.par.givenMoney')
        varReal.value = 12.34
        value = round(varReal.value, 6)
        self.assertEqual(value, round(varReal.value,6) )
        varReal.kill
        task.kill



if __name__ == "__main__":
    pviConnection.start()




(********************************************************************
 * COPYRIGHT -- Bernecker + Rainer
 ********************************************************************
 * Program: feeder
 * File: feederCyclic.ld
 * Author: paulinw
 * Created: June 13, 2007
 ********************************************************************
 * Implementation of program feeder
 ********************************************************************)

PROGRAM _CYCLIC






















<?xml version="1.0"?>
<?AutomationStudio Version=3.0.71?>
<!-- Automation Studio Generated XML Section -->
<networks maxcolumn="0">
	<network label="" comment="Power management of axis: as soon as machine is switched on, controller of axis becomes active" row="5" column="0">
		<row><empty/><empty/><functionblock position="header" name="feederMC_Power" type="MC_Power"/><empty/></row>
		<row><empty/><contact type="address" name="axFeeder"/><functionblock position="top" type="MC_Power"><input name="Axis"/><output name="Status"/></functionblock><coil type="open" name="gFeeder.status.power"/></row>
		<row><contact type="open" name="TRUE"/><line/><functionblock position="middle" type="MC_Power"><input name="Enable"/><output name="Busy"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_Power"><output name="Error"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="bottom" type="MC_Power"><output name="ErrorID"/></functionblock><empty/></row>
	</network>
	<network label="" comment="Do homing as soon as controller has been switched on
" row="6" column="0">
		<row><empty/><empty/><functionblock position="header" name="feederMC_Home" type="MC_Home"/><empty/></row>
		<row><empty/><contact type="address" name="axFeeder"/><functionblock position="top" type="MC_Home"><input name="Axis"/><output name="Done"/></functionblock><coil type="open" name="gFeeder.status.home"/></row>
		<row><contact type="open" name="gFeeder.status.power"/><line/><functionblock position="middle" type="MC_Home"><input name="Execute"/><output name="Busy"/></functionblock><empty/></row>
		<row><empty/><analog type="input" name="0.0"/><functionblock position="middle" type="MC_Home"><input name="Position"/><output name="CommandAborted"/></functionblock><empty/></row>
		<row><empty/><analog type="input" name="mcHOME_DEFAULT"/><functionblock position="middle" type="MC_Home"><input name="HomingMode"/><output name="Error"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="bottom" type="MC_Home"><output name="ErrorID"/></functionblock><empty/></row>
	</network>
	<network label="" comment="read the actual status of the axis" row="13" column="0">
		<row><empty/><empty/><functionblock position="header" name="feederMC_ReadStatus" type="MC_ReadStatus"/><empty/></row>
		<row><empty/><contact type="address" name="axFeeder"/><functionblock position="top" type="MC_ReadStatus"><input name="Axis"/><output name="Valid"/></functionblock><empty/></row>
		<row><line/><line/><functionblock position="middle" type="MC_ReadStatus"><input name="Enable"/><output name="Busy"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadStatus"><output name="Error"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadStatus"><output name="ErrorID"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadStatus"><output name="Errorstop"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadStatus"><output name="Disabled"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadStatus"><output name="Stopping"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadStatus"><output name="StandStill"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadStatus"><output name="DiscreteMotion"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadStatus"><output name="ContinuousMotion"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadStatus"><output name="SynchronizedMotion"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="bottom" type="MC_ReadStatus"><output name="Homing"/></functionblock><empty/></row>
	</network>
	<network label="" comment="axis error handling
" row="11" column="0">
		<row><empty/><empty/><empty/><empty/><empty/><functionblock position="header" name="feederMC_ReadAxisError" type="MC_ReadAxisError"/><empty/><empty/><empty/><empty/><empty/><empty/><empty/></row>
		<row><empty/><empty/><empty/><empty/><contact type="address" name="axFeeder"/><functionblock position="top" type="MC_ReadAxisError"><input name="Axis"/><output name="Valid"/></functionblock><empty/><empty/><empty/><empty/><empty/><empty/><empty/></row>
		<row><contact type="open" name="TRUE"/><line/><line/><line/><line/><functionblock position="middle" type="MC_ReadAxisError"><input name="Enable"/><output name="Busy"/></functionblock><empty/><empty/><empty/><empty/><empty/><empty/><empty/></row>
		<row><contact type="open" name="gMainLogic.cmd.errorAck"/><line/><line/><line/><line/><functionblock position="middle" type="MC_ReadAxisError"><input name="Acknowledge"/><output name="Error"/></functionblock><empty/><empty/><empty/><empty/><empty/><empty/><empty/></row>
		<row><analog type="input" name="gFeeder.status.axisErrorText"/><function position="topbottom" type="ADR"><input name="in"/><output name="56"/></function><line/><line/><functionblock position="middle" type="MC_ReadAxisError"><input name="DataAddress"/><output name="ErrorID"/></functionblock><empty/><empty/><empty/><empty/><empty/><empty/><empty/></row>
		<row><analog type="input" name="gFeeder.status.axisErrorText"/><function position="topbottom" type="SIZEOF"><input name="in"/><output name="56"/></function><function position="topbottom" type="UDINT_TO_UINT"><input name="IN"/><output name="6"/></function><functionblock position="middle" type="MC_ReadAxisError"><input name="DataLength"/><output name="AxisErrorID"/></functionblock><analog type="output" name="gFeeder.status.axisErrorNumber"/><empty/><empty/><empty/><empty/><empty/><empty/></row>
		<row><empty/><empty/><empty/><empty/><empty/><functionblock position="middle" type="MC_ReadAxisError"/><empty/><empty/><empty/><empty/><functionblock position="header" name="feederMC_Reset" type="MC_Reset"/><empty/></row>
		<row><empty/><empty/><empty/><empty/><analog type="input" name="'acp_err'"/><functionblock position="middle" type="MC_ReadAxisError"><input name="DataObjectName"/></functionblock><empty/><empty/><empty/><contact type="address" name="axFeeder"/><functionblock position="top" type="MC_Reset"><input name="Axis"/><output name="Done"/></functionblock><empty/></row>
		<row><empty/><empty/><empty/><empty/><empty/><functionblock position="bottom" type="MC_ReadAxisError"><output name="AxisErrorCount"/></functionblock><line/><function position="top" type="EQ"><input name="IN1" extensible="true"/><output name="56"/></function><contact type="open" name="feederMC_ReadStatus.Errorstop"/><functionblock position="middle" type="MC_Reset"><input name="Execute"/><output name="Busy"/></functionblock><empty/></row>
		<row><empty/><empty/><empty/><empty/><empty/><empty/><empty/><analog type="input" name="0"/><function position="bottom" type="EQ"><input name="IN2" extensible="true"/></function><empty/><functionblock position="middle" type="MC_Reset"><output name="Error"/></functionblock><empty/></row>
		<row><empty/><empty/><empty/><empty/><empty/><empty/><empty/><empty/><empty/><empty/><empty/><functionblock position="bottom" type="MC_Reset"><output name="ErrorID"/></functionblock><empty/></row>
	</network>
	<network label="" comment="if start pressed and both axes are ready, offer cup to conveyor belt" row="2" column="0">
		<row><contact type="positive transition" name="gMainLogic.cmd.start"/><contact type="open" name="gFeeder.status.home"/><contact type="open" name="gConveyor.status.home"/><coil type="set" name="gFeeder.cmd.requestToPut"/></row>
		<row><empty/><empty/><empty or="true"/><coil type="set" name="gMainLogic.cmd.vis.startFlag"/></row>
	</network>
	<network label="" comment="if conveyor belt ready, reset request, pull cup and turn arm
" row="8" column="0">
		<row><contact type="open" name="gConveyor.status.readyToTake"/><line/><line/><line/><line/><line/><coil type="set" name="doCupPull"/></row>
		<row><empty or="true"/><empty/><empty/><functionblock position="header" name="feederMC_MoveAdditive" type="MC_MoveAdditive"/><empty/><empty/></row>
		<row><empty or="true"/><empty/><contact type="address" name="axFeeder"/><functionblock position="top" type="MC_MoveAdditive"><input name="Axis"/><output name="Done"/></functionblock><contact type="positive transition" name="feederMC_MoveAdditive.Done"/><coil type="reset" name="doCupPull"/></row>
		<row><empty or="true"/><line/><line/><functionblock position="middle" type="MC_MoveAdditive"><input name="Execute"/><output name="Busy"/></functionblock><empty or="true"/><coil type="reset" name="gFeeder.cmd.requestToPut"/></row>
		<row><empty/><empty/><analog type="input" name="45.0"/><functionblock position="middle" type="MC_MoveAdditive"><input name="Distance"/><output name="CommandAborted"/></functionblock><empty/><empty/></row>
		<row><empty/><empty/><analog type="input" name="36.0"/><functionblock position="middle" type="MC_MoveAdditive"><input name="Velocity"/><output name="Error"/></functionblock><empty/><empty/></row>
		<row><empty/><empty/><analog type="input" name="360"/><functionblock position="middle" type="MC_MoveAdditive"><input name="Acceleration"/><output name="ErrorID"/></functionblock><empty/><empty/></row>
		<row><empty/><empty/><analog type="input" name="180.0"/><functionblock position="bottom" type="MC_MoveAdditive"><input name="Deceleration"/></functionblock><empty/><empty/></row>
	</network>
	<network label="" comment="read actual position " row="6" column="0">
		<row><empty/><empty/><functionblock position="header" name="MC_ReadActualPosition_0" type="MC_ReadActualPosition"/><empty/></row>
		<row><empty/><contact type="address" name="axFeeder"/><functionblock position="top" type="MC_ReadActualPosition"><input name="Axis"/><output name="Valid"/></functionblock><empty/></row>
		<row><line/><line/><functionblock position="middle" type="MC_ReadActualPosition"><input name="Enable"/><output name="Busy"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadActualPosition"><output name="Error"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadActualPosition"><output name="ErrorID"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="bottom" type="MC_ReadActualPosition"><output name="Position"/></functionblock><analog type="output" name="gActFeederPosition"/></row>
	</network>
	<network label="" comment="read actual speed" row="6" column="0">
		<row><empty/><empty/><functionblock position="header" name="MC_ReadActualVelocity_0" type="MC_ReadActualVelocity"/><empty/></row>
		<row><empty/><contact type="address" name="axFeeder"/><functionblock position="top" type="MC_ReadActualVelocity"><input name="Axis"/><output name="Valid"/></functionblock><empty/></row>
		<row><line/><line/><functionblock position="middle" type="MC_ReadActualVelocity"><input name="Enable"/><output name="Busy"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadActualVelocity"><output name="Error"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="middle" type="MC_ReadActualVelocity"><output name="ErrorID"/></functionblock><empty/></row>
		<row><empty/><empty/><functionblock position="bottom" type="MC_ReadActualVelocity"><output name="Velocity"/></functionblock><analog type="output" name="gActFeederVelocity"/></row>
	</network>
</networks>
END_PROGRAM























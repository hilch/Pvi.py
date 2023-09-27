(********************************************************************
 * COPYRIGHT -- Bernecker + Rainer
 ********************************************************************
 * Program: visAlarm
 * File: visAlarmCyclic.st
 * Author: B&R
 * Created: November 22, 2007
 ********************************************************************
 * Implementation of program visAlarm
 ********************************************************************)

PROGRAM _CYCLIC

	(* Alarm bit connection *)

        alarmCoffee[0] := NOT gMainLogic.cmd.switchOnOff;
        alarmCoffee[1] := NOT gHeating.status.setTempOK;
        alarmCoffee[2] := NOT gFeeder.status.power;
        alarmCoffee[3] := NOT gFeeder.status.home;
        alarmCoffee[4] := NOT gConveyor.status.power;
        alarmCoffee[5] := NOT gConveyor.status.home;

        
        (* error handling of axis *)
        (* can be acknowledged from the visualization *)
        
        IF (gConveyor.status.axisErrorNumber <> 0) THEN
                alarmCoffee[6] := 1;                    (* set error for conveyor axis *)
        ELSE
                alarmCoffee[6] := 0;
        END_IF
        
        IF (gFeeder.status.axisErrorNumber <> 0) THEN
                alarmCoffee[7] := 1;                    (* set error for feeder axis *)
        ELSE
                alarmCoffee[7] := 0;
        END_IF
              
        (* acknowledge axis error *) 
        IF (EDGENEG(alarmAckCoffee[6]) OR EDGENEG(alarmAckCoffee[7])) THEN
                gMainLogic.cmd.errorAck := 1;
        END_IF
        
        
        (* SDM application status *)
        IF (gMainLogic.cmd.switchOnOff = FALSE) THEN
                sdmAppLink := 'http://localhost/sdm-vga/vga.cgi?menu=logger';              (* warning if machine is switched off *)
                SdmSetAppParam_0(enable := 1, appMode := sdm_APPMODE_WARNING, pLink := ADR(sdmAppLink), Option := sdmOPTION_VOLATILE);
                sdmStatus := SdmSetAppParam_0.status;
        ELSE
                sdmAppLink := 'http://localhost/sdm-vga/vga.cgi?menu=system_general ';     (* ok if machine is switched on *)
                SdmSetAppParam_0(enable := 1, appMode := sdm_APPMODE_OK, pLink := ADR(sdmAppLink), Option := sdmOPTION_VOLATILE);    
                sdmStatus := SdmSetAppParam_0.status;
        END_IF
        IF (gConveyor.status.axisErrorNumber > 0) OR (gFeeder.status.axisErrorNumber > 0) THEN
                sdmAppLink := 'http://localhost/sdm-vga/vga.cgi?menu=?menu=motion';        (* error when feeder or conveyor indicates an error *)
                SdmSetAppParam_0(enable := 1, appMode := sdm_APPMODE_ERROR, pLink := ADR(sdmAppLink), Option := sdmOPTION_VOLATILE);    
                sdmStatus := SdmSetAppParam_0.status;
       END_IF
END_PROGRAM

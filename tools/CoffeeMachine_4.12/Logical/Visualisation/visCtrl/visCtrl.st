(********************************************************************
 * COPYRIGHT -- B&R
 ********************************************************************
 * Program: visCtrl
 * File: visCtrl.st
 * Author: B&R
 * Created: June 20, 2007
 ********************************************************************
 * Implementation of program visCtrl
 ********************************************************************)

PROGRAM _INIT
	       
	gMainLogic.cmd.vis.newPage := 65535;
        atWaterTemp := atWaterTemp;
        statusInsertCoin := 0;
        
	
	#ifdef CONFIG_SIMULATION
		strcpy(ADR(urlSDM), ADR('http://127.0.0.1/sdm-vga/vga.cgi'));
	#else
		strcpy(ADR(urlSDM), ADR('http://localhost/sdm-vga/vga.cgi'));
	#endif
	unitSystem := 0;
    unitMetricLocked := 2;
	unitMetric := 1;
	openLanguage := 1;
END_PROGRAM


PROGRAM _CYCLIC
        
	(* change page from global buttons *)
    IF (gMainLogic.cmd.vis.newPage = 65535) AND (setPage <> setPageOld) THEN
		IF (setPage = 0) THEN
  			setPage := setPageOld;
		ELSE	
			gMainLogic.cmd.vis.newPage := setPage;
			setPageOld := setPage;
		END_IF
	END_IF
	
	(* Display language dialog *)
	IF openLanguage = 0 THEN		(* user selected language dialog *)
		
	
	END_IF
	
	
        (* instead of hard wired start button: link visualization tag variable with diStartCoffee *)
        diStartCoffee := cmdStartCoffee;
	
        (* picture control logic *)
	CASE gMainLogic.status.curPage OF

        	sP00_StartPage:
		        (* check calibration data *)
                        IF (calibrationStatus = 3) THEN
                                calibrateTouch := 1;            (* start calibration *)	
                        ELSE
                             IF (calibrationStatus = 1) THEN
                                calibrateTouch := 0;            (* calibration finished *)
                             END_IF
                        END_IF
			(* Init time = 3 sec *)
			startPageTON(IN := initTimeoutEnable, PT := T#3000ms);
			
			gMainLogic.status.startProgressStep := UDINT_TO_USINT(TIME_TO_UDINT(startPageTON.ET) / 30);
			IF (startPageTON.Q  = 1) THEN
				(* switch to Service page *)
				setPage := sP10_MainPage;
                                initTimeoutEnable := FALSE;
                                statusProgressStep := 1;        (* invisible progress bar on screen saver *)
			END_IF
						
		sP10_MainPage:
			(* change page if brewing process has been started *)
			IF (gMainLogic.cmd.vis.startFlag = TRUE) THEN
				gMainLogic.cmd.vis.startFlag := FALSE;
                                setPage := sP11_TakeoutPage;
                                waterLevel  := 100;
                        END_IF
			cupPosition := 0;
		sP11_TakeoutPage:
		                       
                        (* controlling water level *)
                        IF (gMainLogic.status.progressStep = 1) THEN
                                brewingTON(IN := 1, PT:= T#5000ms);
                                waterLevel := 100 - UDINT_TO_INT(TIME_TO_UDINT(brewingTON.ET) / 50);
                        ELSIF (gMainLogic.status.progressStep = 2) THEN
                                brewingTON(IN := 0, PT:= T#5000ms);
                        END_IF
                        
                        (* cup position *)
                        cupPositionCnt := REAL_TO_INT(gActConveyorPosition ) MOD 50;
                        IF cupPositionCnt <> 0 THEN
                                cupPosition := cupPositionCnt;
                        END_IF
                sP12_InfoPage:                        
                        
                sP20_TrendPage:
		
                sP30_AlarmPage:
		
                sP31_AlarmHistoryPage:

		sP60_Setup:
			(* set date and time *)
		
			IF(systemHMI.cmd.changeDateTime = 0) THEN
				systemGetTime(enable:= 1);

				dateTime:= systemGetTime.DT1;
				DT_TO_DTStructure(dateTime, ADR(systemHMI.par.DateTimeActual));
			ELSE
				systemHMI.cmd.changeDateTime := 0;
				dateTime:= DTStructure_TO_DT(ADR(systemHMI.par.DateTimeActual));

				systemSetTime(enable:= 1, DT1:= dateTime);
			END_IF
			
                        IF EDGEPOS(unitMetric = 1) THEN
                              unitMetricLocked := 2;  
                              unitImperialLocked := 0;
                              unitImperial := 0;
                              unitSystem := 0;
                        END_IF
                        IF EDGEPOS(unitImperial = 1) THEN
                              unitMetricLocked := 0;
                              unitImperialLocked := 2;
                              unitMetric := 0;
                              unitSystem := 1;
                        END_IF
                        
                        
                        
                        
                sP60_SystemDiagnostics:
                        IF (showBusyValue < 100) THEN
                                showBusyValue := showBusyValue + 1;
                        ELSE
                                showBusyValue := 0;
                        END_IF
                        IF (diagIsLoading = 1) THEN
                                showBusyLayer := 0;
                        ELSE
                                showBusyLayer := 1;
                        END_IF
                        
                        
	END_CASE;
	
        (* runtime coloring of water temperature *)
        IF (gMainLogic.cmd.switchOnOff = FALSE) THEN
                gMainLogic.cmd.vis.waterTempColor := 16#070F;	(* gray on white background *)
	ELSIF (gHeating.status.setTempOK = TRUE) THEN
 		gMainLogic.cmd.vis.waterTempColor := 16#020F;	(* green on white background *)
	ELSE
 		gMainLogic.cmd.vis.waterTempColor := 16#330F;	(* red on white background *)
	END_IF	
 	
	(* runtime coloring of start button *)
	IF (gMainLogic.par.givenMoney >= gMainLogic.par.recipe.price) AND (gHeating.status.setTempOK = TRUE) AND (gFeeder.status.home = TRUE) AND (gConveyor.status.home = TRUE)THEN
		gMainLogic.cmd.vis.startButtonColor := 2;	 (* enabled color *)
	ELSE
		gMainLogic.cmd.vis.startButtonColor := 0;        (* disabled color *)
	END_IF
	
	(* instant messages *)
	IF (gMainLogic.cmd.switchOnOff = FALSE) THEN
		gMainLogic.cmd.vis.messageIndex := 0;
 		gMainLogic.cmd.vis.messageColor := 16#070F;	(* gray on white background *)
	ELSIF (gHeating.status.setTempOK = TRUE) THEN
		gMainLogic.cmd.vis.messageIndex := 2;
 		gMainLogic.cmd.vis.messageColor := 16#020F;	(* green on white background *)
	ELSE
		gMainLogic.cmd.vis.messageIndex := 1;
 		gMainLogic.cmd.vis.messageColor := 16#330F;	(* red on white background *)
	END_IF
	IF (gMainLogic.status.curPage <> sP12_InfoPage) THEN
                showInfo := 100;
        END_IF
	(* visibility of coins *)
	gMainLogic.cmd.vis.euro2hidden  := NOT(UDINT_TO_BOOL(gMainLogic.status.money.euro2));
	gMainLogic.cmd.vis.euro1hidden  := NOT(UDINT_TO_BOOL(gMainLogic.status.money.euro1));
	gMainLogic.cmd.vis.cent50hidden := NOT(UDINT_TO_BOOL(gMainLogic.status.money.cent50));
	gMainLogic.cmd.vis.cent20hidden := NOT(UDINT_TO_BOOL(gMainLogic.status.money.cent20));
	gMainLogic.cmd.vis.cent10hidden := NOT(UDINT_TO_BOOL(gMainLogic.status.money.cent10));
	gMainLogic.cmd.vis.cent5hidden  := NOT(UDINT_TO_BOOL(gMainLogic.status.money.cent5));
	gMainLogic.cmd.vis.cent2hidden  := NOT(UDINT_TO_BOOL(gMainLogic.status.money.cent2));
	gMainLogic.cmd.vis.cent1hidden  := NOT(UDINT_TO_BOOL(gMainLogic.status.money.cent1));
	
        
        
END_PROGRAM

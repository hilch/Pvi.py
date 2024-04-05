(********************************************************************
 * COPYRIGHT -- B&R
 ********************************************************************
 * Program: Brewing
 * File: Brewing.st
 * Author: B&R
 * Created: June 12, 2007
 ********************************************************************
 * Implementation of program Brewing
 ********************************************************************)

PROGRAM _CYCLIC
	(* plain text information of current step *)	
	IF (pBrewingText <> 0) THEN
			strcpy(ADR(gBrewing.status.brewingStepText), pBrewingText);
	END_IF

	IF EDGEPOS(diStartCoffee) = TRUE THEN
 		gMainLogic.status.progressStep := 0;			(* transporting cup to brewing station *) 		
	END_IF	

	CASE gBrewing.status.sBrewingStep OF
		(* wait for start signal *)
		sSTANDBY:
			pBrewingText := ADR('sSTANDBY');

			IF (gBrewing.cmd.start = TRUE) THEN
				gMainLogic.status.progressStep := 1;			(* brewing in progress *)				 
   			    gBrewing.cmd.start   := FALSE;				
				gBrewing.status.done := FALSE;
				gBrewing.status.sBrewingStep := sDOSING;				
			END_IF
		 
		(* dose ingredients according to recipe *)	
		sDOSING:
			pBrewingText := ADR('sDOSING');

			milkTP  (IN := 1, PT := REAL_TO_TIME(gMainLogic.par.recipe.milk   * 10));	(* 100ml -> 1s *)
			sugarTP (IN := 1, PT := REAL_TO_TIME(gMainLogic.par.recipe.sugar  * 10));  (* 50g -> 500ms *)
			coffeeTP(IN := 1, PT := REAL_TO_TIME(gMainLogic.par.recipe.coffee * 10));  (* 80g -> 800ms *)

			doDoseMilk   := milkTP.Q;
			doDoseSugar  := sugarTP.Q;
			doDoseCoffee := coffeeTP.Q;

			(* wait until dosing is finished *)
			IF (milkTP.Q = 0) AND (sugarTP.Q = 0) AND (coffeeTP.Q = 0) THEN
				milkTP  (IN := 0, PT := 0);
				sugarTP (IN := 0, PT := 0);
				coffeeTP(IN := 0, PT := 0);
	 			gBrewing.status.sBrewingStep := sBREWING;
	 		END_IF						
 

		(* brew coffee *)	
		sBREWING:
			pBrewingText := ADR('sBREWING');

			(* start brewing if set temperature has been reached *)
			IF (gHeating.status.setTempOK = TRUE) THEN
				waterTP(IN := 1, PT := REAL_TO_TIME(gMainLogic.par.recipe.water * 50));		(* 100ml -> 1s *)

				doPumpWater := waterTP.Q;

				(* wait until dosing is finished *)
				IF (waterTP.Q = 0) THEN
					waterTP(IN := 0, PT := 0);
		 			gBrewing.status.sBrewingStep := sFINISH;
		 		END_IF						
			END_IF			

		(* all done *)	
		sFINISH:
			pBrewingText := ADR('sFINISH');
 		
			gMainLogic.status.progressStep := 2;			(* ready for take out *)			
			
			gBrewing.status.done := TRUE;		
			gBrewing.status.sBrewingStep := sSTANDBY;			
	END_CASE;
END_PROGRAM

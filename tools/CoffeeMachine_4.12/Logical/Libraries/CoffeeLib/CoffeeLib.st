(********************************************************************
 * COPYRIGHT -- B&R
 ********************************************************************
 * Library: CoffeeLib
 * File: CoffeeLib.st
 * Author: B&R
 * Created: June 18, 2007
 ********************************************************************
 * Implementation of library CoffeeLib
 ********************************************************************)

(*tempChanges given money based on euros*)
FUNCTION_BLOCK MoneyChanger
	IF (executeOld <> execute) AND (execute = TRUE) THEN
 		(* plausibility check: *)
		IF (given < price) THEN
			cent1 := 0;
			cent2 := 0;
			cent5 := 0;
			cent10 := 0;
			cent20 := 0;
			cent50 := 0;
			euro1  := 0;
			euro2  := 0;
			RETURN;
		END_IF
		 
		(* calculate change *)				
		change := given - price;
		
		(* trim to two floating point digits -> cents *)
		change := UDINT_TO_REAL(REAL_TO_UDINT(change * 100)) / 100;
		
		(* EURO *)
		euro2 := TRUNC(change) / 2;
		euro1 := TRUNC(change) MOD 2;
		
		(* CENTS *)
		centChange := REAL_TO_USINT((change - TRUNC(change)) * 100.0);	(* get digits after floating point in front of floating point (integer) *)
		cent50     := centChange / 50;
		centChange := centChange MOD 50;
		cent20     := centChange / 20;
		centChange := centChange MOD 20;
		cent10     := centChange / 10;
		centChange := centChange MOD 10;
		cent5      := centChange / 5;
		centChange := centChange MOD 5;
		cent2      := centChange / 2;
		centChange := centChange MOD 2;
		cent1      := centChange;
		
		resetMoney := 0;
	ELSE
		(* do not touch reset if not active *)
		resetMoney := given;
	END_IF
	
	executeOld := execute;
END_FUNCTION_BLOCK



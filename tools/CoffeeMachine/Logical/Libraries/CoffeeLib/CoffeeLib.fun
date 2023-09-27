(********************************************************************
 * COPYRIGHT -- B&R
 ********************************************************************
 * Library: CoffeeLib
 * File: CoffeeLib.fun
 * Author: B&R
 * Created: June 18, 2007
 ********************************************************************
 * Functions and function blocks of library CoffeeLib
 ********************************************************************)

FUNCTION_BLOCK MoneyChanger (*Changes given money based on euros*)
	VAR_INPUT
		execute : BOOL; (*Do change*)
		given : REAL; (*Given money*)
		price : REAL; (*Price*)
	END_VAR
	VAR_OUTPUT
		change : REAL; (*total money to change*)
		cent1 : USINT; (*Number of 1 Cent coins*)
		cent2 : USINT; (*Number of 2 Cent coins*)
		cent5 : USINT; (*Number of 5 Cent coins*)
		cent10 : USINT; (*Number of 10 Cent coins*)
		cent20 : USINT; (*Number of 20 Cent coins*)
		cent50 : USINT; (*Number of 50 Cent coins*)
		euro1 : UDINT; (*Number of 1 Euro coins*)
		euro2 : UDINT; (*Number of 2 Euro coins*)
		resetMoney : REAL; (*Resets given money*)
	END_VAR
	VAR
		centChange : USINT; (*cent change calculation*)
		executeOld : BOOL; (*edge sensitive operation*)
	END_VAR
END_FUNCTION_BLOCK

(********************************************************************
 * COPYRIGHT -- B&R
 ********************************************************************
 * File: Global.typ
 * Author: B&R
 * Created: June 06, 2007
 ********************************************************************
 * Global data types of project coffee
 ********************************************************************)

TYPE
	feeder_status_typ : 	STRUCT 
		power : BOOL;
		home : BOOL;
		axisErrorNumber : UINT;
		axisErrorText : STRING[255];
	END_STRUCT;
	feeder_cmd_typ : 	STRUCT 
		requestToPut : BOOL;
	END_STRUCT;
	feeder_typ : 	STRUCT 
		cmd : feeder_cmd_typ;
		status : feeder_status_typ;
	END_STRUCT;
	main_status_money_typ : 	STRUCT 
		changedMoney : REAL;
		cent1 : USINT;
		cent2 : USINT;
		cent5 : USINT;
		cent10 : USINT;
		cent20 : USINT;
		cent50 : USINT;
		euro1 : UDINT;
		euro2 : UDINT;
	END_STRUCT;
	main_status_progress_typ : 	STRUCT 
		total : REAL;
		current : REAL;
	END_STRUCT;
	main_status_typ : 	STRUCT 
		money : main_status_money_typ;
		progressStep : USINT;
		curPage : UINT;
		curLanguage : UINT;
		startProgressStep : USINT;
	END_STRUCT;
	main_par_recipe_typ : 	STRUCT 
		price : REAL;
		setTemp : REAL;
		milk : REAL;
		sugar : REAL;
		coffee : REAL;
		water : REAL;
	END_STRUCT;
	main_par_typ : 	STRUCT 
		coffeeType : SINT;
		givenMoney : REAL;
		recipe : main_par_recipe_typ;
	END_STRUCT;
	main_cmd_typ : 	STRUCT 
		switchOnOff : BOOL;
		errorAck : BOOL;
		start : BOOL;
		vis : main_cmd_vis_typ;
	END_STRUCT;
	main_cmd_vis_typ : 	STRUCT 
		newPage : UINT;
		startFlag : BOOL;
		startButtonColor : UINT;
		waterTempColor : UINT;
		messageColor : UINT;
		messageIndex : USINT;
		euro2hidden : UINT;
		euro1hidden : UINT;
		cent50hidden : UINT;
		cent20hidden : UINT;
		cent10hidden : UINT;
		cent5hidden : UINT;
		cent2hidden : UINT;
		cent1hidden : UINT;
		newLanguage : UINT;
	END_STRUCT;
	main_typ : 	STRUCT 
		cmd : main_cmd_typ;
		par : main_par_typ;
		status : main_status_typ;
	END_STRUCT;
	conveyor_typ : 	STRUCT 
		status : conveyor_status_typ;
	END_STRUCT;
	conveyor_status_typ : 	STRUCT 
		power : BOOL;
		home : BOOL;
		axisErrorNumber : UINT;
		axisErrorText : STRING[255];
		readyToTake : BOOL;
	END_STRUCT;
	brewing_par_typ : 	STRUCT 
		coffeeType : USINT;
	END_STRUCT;
	brewing_cmd_typ : 	STRUCT 
		start : BOOL;
	END_STRUCT;
	brewing_status_typ : 	STRUCT 
		done : BOOL;
		sBrewingStep : UINT;
		brewingStepText : STRING[64];
	END_STRUCT;
	brewing_typ : 	STRUCT 
		cmd : brewing_cmd_typ;
		par : brewing_par_typ;
		status : brewing_status_typ;
	END_STRUCT;
	heating_status_typ : 	STRUCT 
		setTempOK : BOOL;
		actTemp : REAL;
	END_STRUCT;
	heating_cmd_typ : 	STRUCT 
		start : BOOL;
		updatePIDpar : BOOL;
	END_STRUCT;
	heating_typ : 	STRUCT 
		cmd : heating_cmd_typ;
		status : heating_status_typ;
	END_STRUCT;
END_TYPE

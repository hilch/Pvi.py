(********************************************************************
 * COPYRIGHT -- Bernecker + Rainer
 ********************************************************************
 * Program: visCtrl
 * File: visCtrl.typ
 * Author: B&R
 * Created: November 08, 2007
 ********************************************************************
 * Local data types of program visCtrl
 ********************************************************************)

TYPE
	sysset_typ : 	STRUCT 
		cmd : sysset_cmd_typ;
		par : sysset_par_typ;
	END_STRUCT;
	sysset_cmd_typ : 	STRUCT 
		enable : BOOL;
		changeDateTime : BOOL;
	END_STRUCT;
	sysset_par_typ : 	STRUCT 
		DateTimeActual : DTStructure;
	END_STRUCT;
END_TYPE

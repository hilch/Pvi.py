(********************************************************************
 * COPYRIGHT (C) BERNECKER + RAINER, AUSTRIA, A-5142 EGGELSBERG
 ********************************************************************
 * Library: AsTime
 * File: AsTime.typ
 * Created: 11.11.2003
 ********************************************************************
 * Global data types of library AsTime
 ********************************************************************)
TYPE
	TIMEStructure : STRUCT
		day	: SINT ;
		hour	: USINT ;
		minute	: USINT ;
		second	: USINT ;
		millisec	: UINT ;
		microsec	: UINT ;
	END_STRUCT;
	DTStructure : STRUCT
		year	: UINT ;
		month	: USINT ;
		day	: USINT ;
		wday	: USINT ;
		hour	: USINT ;
		minute	: USINT ;
		second	: USINT ;
		millisec	: UINT ;
		microsec	: UINT ;
	END_STRUCT;
END_TYPE
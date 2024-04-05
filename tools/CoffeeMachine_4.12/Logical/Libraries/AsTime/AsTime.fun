(********************************************************************
 * COPYRIGHT (C) BERNECKER + RAINER, AUSTRIA, A-5142 EGGELSBERG
 ********************************************************************
 * Library: AsTime
 * File: AsTime.fun
 * Created: 11.11.2003
 ********************************************************************
 * Functions and function blocks of library AsTime
 ********************************************************************)
FUNCTION_BLOCK DTExSetTime
	VAR_INPUT
		enable	:BOOL;
		DT1	:DATE_AND_TIME;
		Option	:USINT;
	END_VAR
	VAR_OUTPUT
		status	:UINT;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK DTSetTime
	VAR_INPUT
		enable	:BOOL;
		DT1	:DATE_AND_TIME;
	END_VAR
	VAR_OUTPUT
		status	:UINT;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK DTGetTime
	VAR_INPUT
		enable	:BOOL;
	END_VAR
	VAR_OUTPUT
		status	:UINT;
		DT1	:DATE_AND_TIME;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION clock_ms : TIME
END_FUNCTION
FUNCTION ascTIMEStructure : UDINT
	VAR_INPUT
		pTIMEStructure	:UDINT;
		pStr	:UDINT;
		len	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ascDTStructure : UDINT
	VAR_INPUT
		pDTStructure	:UDINT;
		pStr	:UDINT;
		len	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ascTIME : UDINT
	VAR_INPUT
		TIME1	:TIME;
		pStr	:UDINT;
		len	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ascDT : UDINT
	VAR_INPUT
		DT1	:DATE_AND_TIME;
		pStr	:UDINT;
		len	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION TIMEStructure_TO_TIME : TIME
	VAR_INPUT
		pTIMEStructure	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION TIME_TO_TIMEStructure : UDINT
	VAR_INPUT
		TIME1	:TIME;
		pTIMEStructure	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DTStructure_TO_DT : DATE_AND_TIME
	VAR_INPUT
		pDTStructure	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DT_TO_DTStructure : UDINT
	VAR_INPUT
		DT1	:DATE_AND_TIME;
		pDTStructure	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DiffT : UDINT
	VAR_INPUT
		TIME2	:TIME;
		TIME1	:TIME;
	END_VAR
END_FUNCTION
FUNCTION DiffDT : UDINT
	VAR_INPUT
		DT2	:DATE_AND_TIME;
		DT1	:DATE_AND_TIME;
	END_VAR
END_FUNCTION

(********************************************************************
 * COPYRIGHT (C) BERNECKER + RAINER, AUSTRIA, A-5142 EGGELSBERG
 ********************************************************************
 * Library: DataObj
 * File: DataObj.fun
 * Created: 11.11.2003
 ********************************************************************
 * Functions and function blocks of library DataObj
 ********************************************************************)
FUNCTION_BLOCK DatObjCreate
	VAR_INPUT
		enable	:BOOL;
		grp	:USINT;
		pName	:UDINT;
		len	:UDINT;
		MemType	:USINT;
		Option	:UDINT;
		pCpyData	:UDINT;
	END_VAR
	VAR_OUTPUT
		status	:UINT;
		ident	:UDINT;
		pDatObjMem	:UDINT;
	END_VAR
	VAR
		DatObjInternalStruct	:DatObjCreateInternal;
		byState	:USINT;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK DatObjWrite
	VAR_INPUT
		enable	:BOOL;
		ident	:UDINT;
		Offset	:UDINT;
		pSource	:UDINT;
		len	:UDINT;
	END_VAR
	VAR_OUTPUT
		status	:UINT;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK DatObjRead
	VAR_INPUT
		enable	:BOOL;
		ident	:UDINT;
		Offset	:UDINT;
		pDestination	:UDINT;
		len	:UDINT;
	END_VAR
	VAR_OUTPUT
		status	:UINT;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK DatObjDelete
	VAR_INPUT
		enable	:BOOL;
		ident	:UDINT;
	END_VAR
	VAR_OUTPUT
		status	:UINT;
	END_VAR
	VAR
		DatObjInternalStruct	:DatObjDeleteInternal;
		byState	:USINT;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK DatObjMove
	VAR_INPUT
		enable	:BOOL;
		ident	:UDINT;
		MemType	:USINT;
		Option	:UDINT;
	END_VAR
	VAR_OUTPUT
		status	:UINT;
		identNew	:UDINT;
		pDatObjMem	:UDINT;
	END_VAR
	VAR
		DatObjInternalStruct	:DatObjCopyInternal;
		byState	:USINT;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK DatObjCopy
	VAR_INPUT
		enable	:BOOL;
		ident	:UDINT;
		pNameTarget	:UDINT;
		MemTypeTarget	:USINT;
		OptionTarget	:UDINT;
	END_VAR
	VAR_OUTPUT
		status	:UINT;
		identNew	:UDINT;
		pDatObjMemNew	:UDINT;
	END_VAR
	VAR
		DatObjInternalStruct	:DatObjCopyInternal;
		byState	:USINT;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK DatObjInfo
	VAR_INPUT
		enable	:BOOL;
		pName	:UDINT;
	END_VAR
	VAR_OUTPUT
		status	:UINT;
		ident	:UDINT;
		pDatObjMem	:UDINT;
		len	:UDINT;
		MemType	:USINT;
		Option	:UDINT;
		ChangeDate	:DATE_AND_TIME;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK DatObjChangeDate
	VAR_INPUT
		enable	:BOOL;
		pName	:UDINT;
		SetDate	:DATE_AND_TIME;
	END_VAR
	VAR_OUTPUT
		status	:UINT;
	END_VAR
END_FUNCTION_BLOCK

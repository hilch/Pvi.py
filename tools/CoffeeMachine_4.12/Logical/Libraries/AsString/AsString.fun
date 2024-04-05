(********************************************************************
 * COPYRIGHT (C) BERNECKER + RAINER, AUSTRIA, A-5142 EGGELSBERG
 ********************************************************************
 * Library: AsString
 * File: AsString.fun
 * Created: 11.11.2003
 ********************************************************************
 * Functions and function blocks of library AsString
 ********************************************************************)
FUNCTION ftoa : UINT
	VAR_INPUT
		value	:REAL;
		pString	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION atof : REAL
	VAR_INPUT
		pString	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION itoa : UINT
	VAR_INPUT
		value	:DINT;
		pString	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION atoi : DINT
	VAR_INPUT
		pString	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION memset : UDINT
	VAR_INPUT
		pDest	:UDINT;
		value	:USINT;
		length	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION memcpy : UDINT
	VAR_INPUT
		pDest	:UDINT;
		pSrc	:UDINT;
		length	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION memmove : UDINT
	VAR_INPUT
		pDest	:UDINT;
		pSrc	:UDINT;
		length	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION memcmp : DINT
	VAR_INPUT
		pMem1	:UDINT;
		pMem2	:UDINT;
		length	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION strcat : UDINT
	VAR_INPUT
		pDest	:UDINT;
		pSrc	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION strlen : UINT
	VAR_INPUT
		pString	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION strcpy : UDINT
	VAR_INPUT
		pDest	:UDINT;
		pSrc	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION strcmp : DINT
	VAR_INPUT
		pString1	:UDINT;
		pString2	:UDINT;
	END_VAR
END_FUNCTION

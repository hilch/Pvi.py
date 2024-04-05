(********************************************************************
 * COPYRIGHT (C) BERNECKER + RAINER, AUSTRIA, A-5142 EGGELSBERG
 ********************************************************************
 * Library: Visapi
 * File: Visapi.typ
 * Created: 11.11.2003
 ********************************************************************
 * Global data types of library Visapi
 ********************************************************************)
TYPE
	display_info : STRUCT
		width	: UINT ;
		height	: UINT ;
		func1	: UDINT ;
		func2	: UDINT ;
		bpp	: USINT ;
	END_STRUCT;
	VCHANDLE : STRUCT
	END_STRUCT;
	TouchAction : STRUCT
		status	: UDINT ;
		y	: UDINT ;
		x	: UDINT ;
	END_STRUCT;
	sVCBitmap : STRUCT
		vpInternalData : UDINT;
		vpData : UDINT;
		iBPP : DINT;
		iHeight : DINT;
		iWidth : DINT;
	END_STRUCT;
END_TYPE

(********************************************************************
 * COPYRIGHT (C) BERNECKER + RAINER, AUSTRIA, A-5142 EGGELSBERG
 ********************************************************************
 * Library: DataObj
 * File: DataObj.typ
 * Created: 11.11.2003
 ********************************************************************
 * Global data types of library DataObj
 ********************************************************************)
TYPE
	DatObjDeleteInternal : STRUCT
		byKennung	: USINT ;
		bReadyFlag	: BOOL ;
		wStatus	: UINT ;
		ulIdent	: UDINT ;
	END_STRUCT;
	DatObjCopyInternal : STRUCT
		byKennung	: USINT ;
		bReadyFlag	: BOOL ;
		wStatus	: UINT ;
		szName	: ARRAY[0..32] OF USINT ;
		byMemType	: USINT ;
		pBrmSource	: UDINT ;
		ulOption	: UDINT ;
		pBrmModule	: UDINT ;
		ulIdent	: UDINT ;
	END_STRUCT;
	DatObjCreateInternal : STRUCT
		byKennung	: USINT ;
		bReadyFlag	: BOOL ;
		wStatus	: UINT ;
		szName	: ARRAY[0..32] OF USINT ;
		ModulHeader	: ARRAY[0..31] OF USINT ;
		DaMbSection	: ARRAY[0..35] OF USINT ;
		pDaSection	: UDINT ;
		ulSectionLength	: UDINT ;
		byMemType	: USINT ;
		pBrmModule	: UDINT ;
		ulIdent	: UDINT ;
	END_STRUCT;
END_TYPE
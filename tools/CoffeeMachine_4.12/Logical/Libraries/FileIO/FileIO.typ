(********************************************************************
 * COPYRIGHT -- Bernecker + Rainer
 ********************************************************************
 * Library: FileIO
 * File: FileIO.typ
 * Author: feinerr
 * Created: 09.11.2005
 ********************************************************************
 * Data types of library FileIO
 ********************************************************************)

TYPE
    fiDIR_READ_DATA		: STRUCT						(* directory read structure *)
        Filename		: ARRAY[0..259] OF USINT;		(* file name *)
        Date			: DATE_AND_TIME;				(* date and time *)
        Filelength		: UDINT;						(* file length *)
	END_STRUCT;

    fiDIR_READ_EX_DATA	: STRUCT						(* directory read extended structure *)
        Filename		: ARRAY[0..259] OF USINT;		(* file name *)
        Date			: DATE_AND_TIME;				(* date and time *)
        Filelength		: UDINT;						(* file length *)
        Mode			: UINT;							(* mode *)
	END_STRUCT;
END_TYPE

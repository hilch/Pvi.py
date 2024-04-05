(********************************************************************
 * COPYRIGHT (C) BERNECKER + RAINER, AUSTRIA, A-5142 EGGELSBERG
 ********************************************************************
 * Library: Sys_lib
 * File: Sys_lib.typ
 * Created: 11.11.2003
 ********************************************************************
 * Global data types of library Sys_lib
 ********************************************************************)
TYPE
	MoVerStruc_typ : STRUCT
		version	: ARRAY[0..9] OF USINT ;
		year	: UINT ;
		month	: USINT ;
		day	: USINT ;
		reserve	: USINT ;
		hour	: USINT ;
		minute	: USINT ;
		second	: USINT ;
	END_STRUCT;
	ERR_xtyp : STRUCT
		err_nr	: UINT ;
		err_info	: UDINT ;
		t_name	: ARRAY[0..4] OF SINT ;
		err_type	: USINT ;
		err_year	: UINT ;
		err_month	: USINT ;
		err_day	: USINT ;
		err_reserve	: USINT ;
		err_hour	: USINT ;
		err_minute	: USINT ;
		err_second	: USINT ;
		err_millisec	: UINT ;
		err_microsec	: UINT ;
		err_string	: ARRAY[0..33] OF USINT ;
	END_STRUCT;
	ERR_typ : STRUCT
		err_nr	: UINT ;
		err_info	: UDINT ;
		t_name	: ARRAY[0..4] OF SINT ;
		err_type	: USINT ;
		err_year	: UINT ;
		err_month	: USINT ;
		err_day	: USINT ;
		err_reserve	: USINT ;
		err_hour	: USINT ;
		err_minute	: USINT ;
		err_second	: USINT ;
		err_millisec	: UINT ;
		err_microsec	: UINT ;
	END_STRUCT;
	PV_xList_typ : STRUCT
		name	: ARRAY[0..32] OF SINT ;
		data_typ	: USINT ;
		data_len	: UDINT ;
		dimension	: UDINT ;
		adress	: UDINT ;
	END_STRUCT;
	PV_List_typ : STRUCT
		name	: ARRAY[0..13] OF SINT ;
		tcnr	: USINT ;
		grp	: USINT ;
		ident	: UDINT ;
		adress	: UDINT ;
	END_STRUCT;
	MO_List_typ : STRUCT
		name	: ARRAY[0..13] OF SINT ;
		grp	: USINT ;
		type	: USINT ;
		state	: USINT ;
		reserve	: USINT ;
		adress	: UDINT ;
		memtype	: UDINT ;
	END_STRUCT;
	SYSxinfo_typ : STRUCT
		aws_name	: ARRAY[0..5] OF SINT ;
		aws_type	: ARRAY[0..1] OF SINT ;
		cpu_info	: UDINT ;
		ma_globl_len	: UINT ;
		md_globl_len	: UINT ;
		os_len	: UDINT ;
		user_len	: UDINT ;
		tmp_len	: UDINT ;
		eprom_len	: UDINT ;
		fix_ram_len	: UDINT ;
	END_STRUCT;
	RTCtime_typ : STRUCT
		year	: UINT ;
		month	: USINT ;
		day	: USINT ;
		reserve	: USINT ;
		hour	: USINT ;
		minute	: USINT ;
		second	: USINT ;
		millisec	: UINT ;
		microsec	: UINT ;
	END_STRUCT;
END_TYPE
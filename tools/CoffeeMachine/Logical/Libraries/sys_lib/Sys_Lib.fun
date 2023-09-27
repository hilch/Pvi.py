(********************************************************************
 * COPYRIGHT (C) BERNECKER + RAINER, AUSTRIA, A-5142 EGGELSBERG
 ********************************************************************
 * Library: Sys_lib
 * File: Sys_lib.fun
 * Created: 11.11.2003
 ********************************************************************
 * Functions and function blocks of library Sys_lib
 ********************************************************************)
FUNCTION MO_ver : UINT
	VAR_INPUT
		pName	:UDINT;
		grp	:USINT;
		pMoVerStruc	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ERRxfatal : UINT (* Enter a fatal error in error module and stop plc *)
	VAR_INPUT
		errornr	:UINT;
		errorinfo	:UDINT;
		errorstring	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION PV_xlist : UINT (* List all the (complex) PV of the plc *)
	VAR_INPUT
		prev_index	:UINT;
		index	:UDINT;
		PV_xList_struct	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION_BLOCK Byte2Bit (* Convert/Copy Bytefields to Bitfields *)
	VAR_INPUT
		byteadr	:UDINT;
		length	:UINT;
	END_VAR
	VAR_OUTPUT
		bitadr	:UDINT;
	END_VAR
	VAR
		bmem000	:BOOL;
		static_val	:ARRAY[0..138] OF USINT;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK Bit2Byte (* Convert/Copy Bitfields to Bytefields *)
	VAR_INPUT
		bitadr	:UDINT;
		length	:UINT;
	END_VAR
	VAR_OUTPUT
		byteadr	:UDINT;
	END_VAR
	VAR
		byte_00	:USINT;
		byte_01	:USINT;
		byte_02	:USINT;
		byte_03	:USINT;
		byte_04	:USINT;
		byte_05	:USINT;
		byte_06	:USINT;
		byte_07	:USINT;
		byte_08	:USINT;
		byte_09	:USINT;
		byte_10	:USINT;
		byte_11	:USINT;
		byte_12	:USINT;
		byte_13	:USINT;
		byte_14	:USINT;
		byte_15	:USINT;
		bmem000	:BOOL;
		static_val	:ARRAY[0..138] OF USINT;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION PV_ninfo : UINT (* Get information of a complex PV-name *)
	VAR_INPUT
		pv_name	:UDINT;
		data_typ_p	:UDINT;
		data_len_p	:UDINT;
		dimension_p	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION PV_item : UINT (* Get item-name of a complex PV *)
	VAR_INPUT
		pv_name	:UDINT;
		index	:UINT;
		itemname	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION PV_ident : UINT (* Determine a PV identifier *)
	VAR_INPUT
		pv_name	:UDINT;
		pv_tknr	:USINT;
		pv_grp	:USINT;
		pv_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION KEY_read : UINT (* Read status of all the keys *)
	VAR_INPUT
		keys	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION UT_sleep : UINT (* Suspend an user task for a set time *)
	VAR_INPUT
		tickcount	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION UT_exit : UINT (* Terminate an user task *)
	VAR_INPUT
		exitinfo	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DA_fix : UINT (* Put a data module in the FIX RAM *)
	VAR_INPUT
		mo_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DA_info : UINT (* Retrieve various info about the data module *)
	VAR_INPUT
		mo_ident	:UDINT;
		moduldata_adr	:UDINT;
		moduldata_len	:UDINT;
		memorytype	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DA_copy : UINT (* Copy a data module *)
	VAR_INPUT
		mo_ident	:UDINT;
		new_name	:UDINT;
		mem_typ	:USINT;
		da_ident	:UDINT;
		daten_p	:UDINT;
		daten_len	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DA_store : UINT (* Store a data module *)
	VAR_INPUT
		mo_ident	:UDINT;
		mem_typ	:USINT;
		daten_p	:UDINT;
		daten_len	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DA_burn : UINT (* Burn a data module into the EPROM *)
	VAR_INPUT
		mo_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DA_delete : UINT (* Delete a data module *)
	VAR_INPUT
		mo_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DA_ident : UINT (* Fetch the data module identifier *)
	VAR_INPUT
		name_p	:UDINT;
		grp	:USINT;
		mo_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DA_read : UINT (* Read data of a data module *)
	VAR_INPUT
		mo_ident	:UDINT;
		data_p	:UDINT;
		data_len	:UDINT;
		mo_data_offset	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DA_write : UINT (* Write data to a data module *)
	VAR_INPUT
		mo_ident	:UDINT;
		data_p	:UDINT;
		data_len	:UDINT;
		mo_data_offset	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DA_create : UINT (* Create a data module *)
	VAR_INPUT
		name_p	:UDINT;
		grp	:USINT;
		spooladr	:UINT;
		data_len	:UDINT;
		data_p	:UDINT;
		mo_data_p	:UDINT;
		mo_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION DIS_clr : UINT (* Clear the display *)
	VAR_INPUT
		dummy_input	:USINT;
	END_VAR
END_FUNCTION
FUNCTION DIS_chr : UINT (* Write a character to the display *)
	VAR_INPUT
		row	:UDINT;
		col	:UDINT;
		character	:SINT;
	END_VAR
END_FUNCTION
FUNCTION DIS_str : UINT (* Write a string to the display *)
	VAR_INPUT
		row	:UDINT;
		col	:UDINT;
		string	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ERR_read : UINT (* Read an error module entry *)
	VAR_INPUT
		entry_nr	:UINT;
		ERR_typ_struct	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ERRxread : UINT (* Read an error module entry *)
	VAR_INPUT
		entry_nr	:UINT;
		ERR_xtyp_struct	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ERR_fatal : UINT (* Enter a fatal error in error module and E.STOP *)
	VAR_INPUT
		errornr	:UINT;
		errorinfo	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ERR_warning : UINT (* Enter a warning in the error module *)
	VAR_INPUT
		errornr	:UINT;
		errorinfo	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ERRxwarning : UINT (* Enter a warning (string) in the error module *)
	VAR_INPUT
		errornr	:UINT;
		errorinfo	:UDINT;
		errorstring	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION SM_release : UINT (* Release use of a semaphore *)
	VAR_INPUT
		sm_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION SM_attach : UINT (* Request use of a semaphore *)
	VAR_INPUT
		sm_ident	:UDINT;
		timeout	:UDINT;
		flags	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION SM_delete : UINT (* Delete a semaphore *)
	VAR_INPUT
		sm_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION SM_ident : UINT (* Determine the identifier of a semaphore *)
	VAR_INPUT
		sm_name	:UDINT;
		sm_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION SM_create : UINT (* Create a semaphore *)
	VAR_INPUT
		sm_name	:UDINT;
		sm_count	:USINT;
		sm_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION TIM_ticks : UINT (* Number of ticks in the current second *)
	VAR_INPUT
		dummy_input	:USINT;
	END_VAR
END_FUNCTION
FUNCTION TIM_musec : UINT (* Number of ticks in the current cycle *)
	VAR_INPUT
		dummy_input	:USINT;
	END_VAR
END_FUNCTION
FUNCTION SW_settime : UINT (* Set the Software-Timer *)
	VAR_INPUT
		RTCtime_struct	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION SW_gettime : UINT (* Read the Software-Timer *)
	VAR_INPUT
		RTCtime_struct	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION RTC_settime : UINT (* Set the real time clock *)
	VAR_INPUT
		RTCtime_struct	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION RTC_gettime : UINT (* Read the real time clock *)
	VAR_INPUT
		RTCtime_struct	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION TMP_free : UINT (* De-allocate memory in temporary RAM *)
	VAR_INPUT
		memlng	:UDINT;
		memptr	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION TMP_alloc : UINT (* Allocate memory in temporary RAM *)
	VAR_INPUT
		memlng	:UDINT;
		memptr	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION MEM_free : UINT (* De-allocate memory in user RAM *)
	VAR_INPUT
		memlng	:UDINT;
		memptr	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION MEM_alloc : UINT (* Allocate memory in user RAM *)
	VAR_INPUT
		memlng	:UDINT;
		memptr	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION AVT_info : UINT (* Dynamic Libraries: Get AVT entry information *)
	VAR_INPUT
		av_ident	:UDINT;
		av_linkcount	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION AVT_release : UINT (* Dynamic Libraries: Release AVT entry *)
	VAR_INPUT
		av_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION AVT_attach : UINT (* Dynamic Libraries: Attach AVT entry *)
	VAR_INPUT
		av_ident	:UDINT;
		av_info	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION AVT_ident : UINT (* Dynamic Libraries: Fetch AVT identifier *)
	VAR_INPUT
		av_name	:UDINT;
		av_grp	:USINT;
		av_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION AVT_cancel : UINT (* Dynamic Libraries: Delete an AVT entry *)
	VAR_INPUT
		av_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION AVT_create : UINT (* Dynamic Libraries: Create an AVT entry *)
	VAR_INPUT
		av_name	:UDINT;
		av_grp	:USINT;
		av_info	:UDINT;
		av_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION UT_freemsg : UINT (* Free the memory user for a message *)
	VAR_INPUT
		msglng	:UDINT;
		msg	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION UT_recmsg : UINT (* Receive a message from another user task *)
	VAR_INPUT
		ut_ident	:UDINT;
		msg	:UDINT;
		msglng	:UDINT;
		flags	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION UT_sendmsg : UINT (* Send a message to another user task *)
	VAR_INPUT
		ut_ident	:UDINT;
		msg	:UDINT;
		msglng	:UDINT;
		flags	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION UT_resume : UINT (* Restart a stopped user task *)
	VAR_INPUT
		ut_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION UT_suspend : UINT (* Stop an user task *)
	VAR_INPUT
		ut_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION UT_ident : UINT (* Determine an user task identifier *)
	VAR_INPUT
		ut_name	:UDINT;
		ut_grp	:USINT;
		ut_proc	:USINT;
		ut_sps_p	:UDINT;
		ut_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ST_name : UINT (* Retrieve task name *)
	VAR_INPUT
		st_ident	:UDINT;
		st_name_p	:UDINT;
		st_grp	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ST_info : UINT (* Retrieve task information *)
	VAR_INPUT
		st_ident	:UDINT;
		state	:UDINT;
		tknr	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ST_allsuspend : UINT (*  Stop ALL running task *)
	VAR_INPUT
		dummy_input	:USINT;
	END_VAR
END_FUNCTION
FUNCTION ST_tmp_resume : UINT (* Start a stopped task (temporary) *)
	VAR_INPUT
		st_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ST_tmp_suspend : UINT (* Stop a running task (temporary) *)
	VAR_INPUT
		st_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ST_resume : UINT (* Start a stopped task (permanent) *)
	VAR_INPUT
		st_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ST_suspend : UINT (* Stop a running task (permanent) *)
	VAR_INPUT
		st_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION ST_ident : UINT (* Determine task identifier *)
	VAR_INPUT
		st_name	:UDINT;
		st_grp	:USINT;
		st_ident	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION FORCE_info : UINT (* Check if a task class is beeing forced *)
	VAR_INPUT
		tknr	:USINT;
		force	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION KEY_enadis : UINT (* Set key handling mode *)
	VAR_INPUT
		mode	:BOOL;
	END_VAR
END_FUNCTION
FUNCTION MO_list : UINT (* List all modules of the plc *)
	VAR_INPUT
		prev_index	:UINT;
		index	:UDINT;
		MO_List_struct	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION SYS_battery : USINT (*  Returns the state of the battery and rechargeable *)
	VAR_INPUT
		dummy_input	:USINT;
	END_VAR
END_FUNCTION
FUNCTION SYSreset : UINT (* Reset the PLC *)
	VAR_INPUT
		enable	:BOOL;
		mode	:USINT;
	END_VAR
END_FUNCTION
FUNCTION SYSxinfo : UINT (* Retrieve more system information *)
	VAR_INPUT
		SYSxinfo_struct	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION SYS_info : UINT (* Retrieve various system information *)
	VAR_INPUT
		init_count	:UDINT;
		init_descr	:UDINT;
		tick_count	:UDINT;
		version	:UDINT;
		ov_version	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION PV_list : UINT (* List all the PV of the plc *)
	VAR_INPUT
		prev_index	:UINT;
		index	:UDINT;
		PVList_struct	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION PV_info : UINT (* Get information of a PV *)
	VAR_INPUT
		pv_ident	:UDINT;
		data_typ	:UDINT;
		data_len	:UDINT;
		dimension	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION PV_xgetval : UINT (* Get the value from a complex PV *)
	VAR_INPUT
		pv_ident	:UDINT;
		subindex	:UINT;
		data_p	:UDINT;
		data_len	:USINT;
	END_VAR
END_FUNCTION
FUNCTION PV_xsetval : UINT (* Set a complex PV to a value *)
	VAR_INPUT
		pv_ident	:UDINT;
		subindex	:UINT;
		data_p	:UDINT;
		data_len	:USINT;
	END_VAR
END_FUNCTION
FUNCTION PV_xgetadr : UINT (* Find the address of a complex PV *)
	VAR_INPUT
		pv_name_p	:UDINT;
		pv_adresse	:UDINT;
		data_len	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION PV_getadr : UINT (* Find the address of a process variable *)
	VAR_INPUT
		pv_name_p	:UDINT;
		pv_tknr	:USINT;
		pv_grpnr	:USINT;
		pv_adresse	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION PV_getval : UINT (* Get the value from a PV *)
	VAR_INPUT
		pv_ident	:UDINT;
		value	:UDINT;
	END_VAR
END_FUNCTION
FUNCTION PV_setval : UINT (* Set a PV to a particular value *)
	VAR_INPUT
		pv_ident	:UDINT;
		value	:UDINT;
	END_VAR
END_FUNCTION

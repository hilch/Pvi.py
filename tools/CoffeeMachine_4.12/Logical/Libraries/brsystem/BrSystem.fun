(********************************************************************
 * COPYRIGHT (C) BERNECKER + RAINER, AUSTRIA, A-5142 EGGELSBERG
 ********************************************************************
 * Library: BrSystem
 * File: BrSystem.fun
 * Created: 11.11.2003
 ********************************************************************
 * Functions and function blocks of library BrSystem
 ********************************************************************)

FUNCTION_BLOCK MEMInfo				(* returns information about the memory areas available on the system *)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
		FreeUSR_Ram	:UDINT;			(* SG3: free memory in USER RAM SG4: free memory in SRAM (Userram) *)
		FreeSYSTEM	:UDINT;			(* SG3: free system memory SG4: not used, always 0 *)
		FreeUSR_Prom	:UDINT;		(* SG3: free memory in USER PROM SG4: free memory of HD where RPSHD is located *)
		FreeSYS_Prom	:UDINT;		(* SG3: free memory in system PROM SG4: free memory of HD where RPSHD is located *)
		FreeFIX_Ram	:UDINT;			(* SG3: free memory in FIX RAM SG4: not used, always 0 *)
		FreeTMP_Ram	:UDINT;			(* SG3: free temporary memory in RAM SG4: free memory in DRAM *)
		FreeMEMCARD	:UDINT;			(* SG3: free memory on MEMCARD SG4: not used, always 0*)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK MEMxInfo
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
		mem_typ	:UDINT;
	END_VAR
	VAR
		i_state	:UINT;
		i_result	:UINT;
		i_temp	:UDINT;
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
		MemSize	:UDINT;
		FreeMemSize	:UDINT;
		BiggestFreeBlockSize	:UDINT;
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK SysInfo				(* returns information about the target system *)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
	END_VAR
	VAR_OUTPUT
		init_reason	:USINT;			(* reason for initialization *)
		init_count	:USINT;			(* SG3: the value is increased by every INIT (warm restart) SG4: not used, always 0 *)
		tick_count	:UDINT;			(* tick count *)
		version	:UDINT;				(* operating system version of the target system *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK RTInfo				(* returns runtime information about the software object *)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
		cycle_time	:UDINT;			(* cycle time in microsec. *)
		init_reason	:SINT;			(* reason for initialization *)
		task_class	:SINT;			(* task class (SG3: #1 - #4 SG4: #1 - #8) *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK TARGETInfo			(* returns information about the target *)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
		pOSVersion	:UDINT;			(* pointer to a string ( min. 7 char), where the os version is written *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
		DataFormat	:USINT;			(* wether "big endian" or "little endian" ("TARGET_BIG_ENDIAN"/"TARGET_LITTLE_ENDIAN") *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK HWInfo				(* returns information about hardware configuration *)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
		first	:BOOL;				(* determines the hardware module on which the FUB is used 0/1 next/first *)
		pName	:UDINT;				(* pointer to a string, where the name of the module is written *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
		family	:USINT;				(* family designation *)
		usetype	:USINT;				(* hardware type *)
		module_typ	:UDINT;			(* module type *)
		master_no	:USINT;			(* logical number of the IO master, RIO master, CAN bus with CANIO *)
		slave_no	:USINT;			(* slave number *)
		module_adr	:USINT;			(* hardware module address (decimal) *)
		slot_no	:USINT;				(* slot of the first submodule found (decimal) *)
	END_VAR
	VAR
		next_vw_p	:UDINT;			(* next entry in the control table *)
		last_modul_p	:UDINT;		(* pointer to last control table entry *)
		next_entry_p	:UDINT;		(* pointer to nest control table entry *)
		next_entry_ix	:USINT;		(* index of next control table entry *)	
		next_slot_ix	:USINT;		(* index of next slot *)
		last_rio_master	:USINT;		(* last RIO master *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK SysconfInfo			(* returns the parameters for a sysconf entry; SG4 only*)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
		pEntry	:UDINT;				(* pointer to a string, where the name of the entry is written *)
		pValue	:UDINT;				(* pointer to a string, where the value of the entry is copied *)
		value_len	:UDINT;			(* length of the "value-string" *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK SysconfSet			(* sets the parameters for a sysconf entry; SG4 only*)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
		pEntry	:UDINT;				(* pointer to a string, where the name of the entry is written *)
		pNewValue	:UDINT;			(* pointer to a string, where the new value of the entry is written *)
		option	:USINT;				(* sets the parameter volatile/permanent ("brSYSCONF_SET_VOLATILE"/"brSYSCONF_SET_NON_VOLATILE") *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK BatteryInfo			(* returns the state of the battery; SG3 and CP3xx only *)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
		pDevice	:UDINT;				(* pointer to a string, where the DEVICENAME is written *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
		state	:USINT;				(* state of the battery *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK EXCInfo				(* returns information about the software object that triggered the exception; SG3 only *)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
		task_class	:UDINT;			(* task class in which the exception was triggered *)
		task_ident	:UDINT;			(* ID number of the software object that triggered the exception *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK ZYKVLenable			(* enables/disables the cycle time monitoring of software objects; SG3 only *)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
		mode	:BOOL;				(* 0/1 monitoring off/on *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK PMemGet				(* reads data of len byte from the permanent memeory area beginning at offset; SG3 only *)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
		offset	:UDINT;				(* offset within the permanent memory area *)
		len	 :UDINT;				(* length of data area to be read *)
		adress	:UDINT;				(* address where the read data is copied *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK PMemPut				(* writes len bytes to the permanent memory area beginning at offset; SG3 only *)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
		offset	:UDINT;				(* offset within the permanent memory area *)
		len	 :UDINT;				(* length of data area to be written *)
		adress	:UDINT;				(* address of the data to be written to the permanent memory area *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK PMemSize				(* determines the size of permanent memory area in its existing configuration; SG3 only *)
	VAR_INPUT
		enable	:BOOL;				(* this function block is only executed if enable is <> 0 *)
	END_VAR
	VAR_OUTPUT
		status	:UINT;				(* errornumber *)
		size	:UDINT;				(* size of permanent memory area *)
	END_VAR
END_FUNCTION_BLOCK

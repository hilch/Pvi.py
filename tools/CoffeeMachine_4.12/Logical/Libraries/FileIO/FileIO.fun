(********************************************************************
 * COPYRIGHT -- Bernecker + Rainer
 ********************************************************************
 * Library: FileIO
 * File: FileIO.fun
 * Author: feinerr
 * Created: 09.11.2005
 ********************************************************************
 * Functions and function blocks of library FileIO
 ********************************************************************)

FUNCTION_BLOCK FileCreate				(* file create *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pFile		: UDINT;			(* pointer to file name *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
		ident		: UDINT;			(* file ident *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK FileOpen					(* file open *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pFile		: UDINT;			(* pointer to file name *)
		mode		: USINT;			(* access mode (FILE_R, FILE_W, FILE_RW) *) 
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
		ident		: UDINT;			(* file ident *)
		filelen		: UDINT;			(* file length *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK FileClose				(* file close *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		ident		: UDINT;			(* file ident *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK FileRead					(* file read *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		ident		: UDINT;			(* file ident *)
		offset		: UDINT;			(* offset *)
		pDest		: UDINT;			(* pointer to read buffer *)
		len			: UDINT;			(* number of bytes to read *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK FileReadEx				(* file read extended *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		ident		: UDINT;			(* file ident *)
		offset		: UDINT;			(* offset *)
		pDest		: UDINT;			(* pointer to read buffer *)
		len			: UDINT;			(* number of bytes to read *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
		bytesread	: UDINT;			(* number of bytes read *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK FileWrite				(* file write *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		ident		: UDINT;			(* file ident *)
		offset		: UDINT;			(* offset *)
		pSrc		: UDINT;			(* pointer to write buffer *)
		len			: UDINT;			(* number of bytes to write *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK FileRename				(* file rename *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pName		: UDINT;			(* pointer to file name *)
		pNewName	: UDINT;			(* new file name *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK FileCopy					(* file copy *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pSrcDev		: UDINT;			(* pointer to source file device name *)
		pSrc		: UDINT;			(* pointer to existing file name *)
		pDestDev	: UDINT;			(* pointer to destination file device name *)
		pDest		: UDINT;			(* pointer to copy file name *)
		option		: USINT;			(* copy option *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK FileDelete				(* file delete *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pName		: UDINT;			(* pointer to file name *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DirCreate				(* directory create *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pName		: UDINT;			(* pointer to directory name *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DirOpen					(* directory open *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pName		: UDINT;			(* pointer to directory name *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
		ident		: UDINT;			(* directory ident *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DirClose					(* directory close *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		ident		: UDINT;			(* directory ident *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DirRead					(* directory read *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pPath		: UDINT;
		entry		: UDINT;
		option		: USINT;
		pData		: UDINT;
		data_len	: UDINT;
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DirReadEx				(* directory read extended *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		ident		: UDINT;
		pData		: UDINT;
		data_len	: UDINT;
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DirInfo					(* directory info *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pPath		: UDINT;
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
		dirnum		: UDINT;
		filenum		: UDINT;	
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DirRename				(* directory rename *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pName		: UDINT;			(* pointer to directory name *)
		pNewName	: UDINT;			(* pointer to new directory name *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DirCopy					(* directory copy *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pSrcDev		: UDINT;			(* pointer to source file device name *)
		pSrcDir		: UDINT;			(* pointer to source directory name *)
		pDestDev	: UDINT;			(* pointer to destination file device name *)
		pDestDir	: UDINT;			(* pointer to destination directory name *)
		option		: USINT;			(* copy option *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DirDelete				(* directory delete *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pName		: UDINT;			(* pointer to directory name *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DirDeleteEx				(* directory delete extended *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pName		: UDINT;			(* pointer to directory name *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK SetAttributes			(* attributes set *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pPath		: UDINT;			(* pointer to path name (file or directory) *)
		attributes	: USINT;			(* attributes *)
		option		: USINT;			(* set options *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK GetAttributes			(* attributes get *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
		pPath		: UDINT;			(* pointer to path name (file or directory) *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
		attributes	: USINT;			(* attributes *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DevMemInfo				(* file device memory info *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to file device name *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
		freemem		: UDINT;			(* available disk space *)
		memsize		: UDINT;			(* total disk space *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DevLink					(* file device link *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		pDevice		: UDINT;			(* pointer to new file device name *)
		pParam		: UDINT;			(* pointer to link parameter *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
		handle		: UDINT;			(* file device handle *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION_BLOCK DevUnlink				(* file device unlink *)
	VAR_INPUT
		enable		: BOOL;				(* fub enable *)
		handle		: UDINT;			(* file device handle *)
	END_VAR

	VAR
        i_state		: UINT;				(* internal variable *)
		i_result	: UINT;				(* internal variable *)
        i_tmp		: UDINT;			(* internal variable *)
	END_VAR

	VAR_OUTPUT
		status		: UINT;				(* status *)
	END_VAR
END_FUNCTION_BLOCK

FUNCTION FileIoGetSysError	: UINT		(* get system error info *)
END_FUNCTION

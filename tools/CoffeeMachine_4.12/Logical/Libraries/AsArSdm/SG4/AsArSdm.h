/* Automation Studio generated header file */
/* Do not edit ! */

#ifndef _ASARSDM_
#define _ASARSDM_
#ifdef __cplusplus
extern "C" 
{
#endif

#include <bur/plctypes.h>

#include <runtime.h>

#ifndef _IEC_CONST
#define _IEC_CONST _WEAK const
#endif

/* Constants */
#ifdef _REPLACE_CONST
 #define sdmOPTION_VOLATILE 0U
 #define sdmOPTION_NON_VOLATILE 1U
 #define sdm_APPMODE_ERROR 3U
 #define sdm_APPMODE_WARNING 2U
 #define sdm_APPMODE_OK 1U
 #define sdm_APPMODE_NOTUSED 0U
 #define sdm_SYSTEMDUMP_DATA 1U
 #define sdm_SYSTEMDUMP_PARAM 0U
 #define sdmERR_OPTION_INVALID 34906U
 #define sdmERR_INVALID_VALUE 34905U
 #define sdmERR_INVALID_POINTER 34904U
 #define sdmERR_INVALID_DEVICE 34903U
 #define sdmERR_SYSTEMDUMP 34902U
 #define sdmERR_ARREG 34901U
 #define sdmERR_NOT_EXIST 34900U
#else
 _IEC_CONST unsigned long sdmOPTION_VOLATILE = 0U;
 _IEC_CONST unsigned long sdmOPTION_NON_VOLATILE = 1U;
 _IEC_CONST unsigned short sdm_APPMODE_ERROR = 3U;
 _IEC_CONST unsigned short sdm_APPMODE_WARNING = 2U;
 _IEC_CONST unsigned short sdm_APPMODE_OK = 1U;
 _IEC_CONST unsigned short sdm_APPMODE_NOTUSED = 0U;
 _IEC_CONST unsigned short sdm_SYSTEMDUMP_DATA = 1U;
 _IEC_CONST unsigned short sdm_SYSTEMDUMP_PARAM = 0U;
 _IEC_CONST unsigned short sdmERR_OPTION_INVALID = 34906U;
 _IEC_CONST unsigned short sdmERR_INVALID_VALUE = 34905U;
 _IEC_CONST unsigned short sdmERR_INVALID_POINTER = 34904U;
 _IEC_CONST unsigned short sdmERR_INVALID_DEVICE = 34903U;
 _IEC_CONST unsigned short sdmERR_SYSTEMDUMP = 34902U;
 _IEC_CONST unsigned short sdmERR_ARREG = 34901U;
 _IEC_CONST unsigned short sdmERR_NOT_EXIST = 34900U;
#endif




/* Datatypes and datatypes of function blocks */
typedef struct SdmSystemDump
{
	/* VAR_INPUT (analog) */
	unsigned long configuration;
	unsigned long pDevice;
	unsigned long pFile;
	unsigned long pParam;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	/* VAR (analog) */
	unsigned short i_state;
	unsigned short i_result;
	unsigned long i_tmp;
	/* VAR_INPUT (digital) */
	plcbit enable;
} SdmSystemDump_typ;

typedef struct SdmSetAppParam
{
	/* VAR_INPUT (analog) */
	unsigned long appMode;
	unsigned long pLink;
	unsigned long Option;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	/* VAR (analog) */
	unsigned short i_state;
	unsigned short i_result;
	unsigned long i_tmp;
	/* VAR_INPUT (digital) */
	plcbit enable;
} SdmSetAppParam_typ;



/* Prototyping of functions and function blocks */
void SdmSystemDump(struct SdmSystemDump* inst);
void SdmSetAppParam(struct SdmSetAppParam* inst);


#ifdef __cplusplus
};
#endif
#endif /* _ASARSDM_ */


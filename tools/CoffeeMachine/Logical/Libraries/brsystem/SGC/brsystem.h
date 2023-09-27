/* Automation Studio Generated Header File, Format Version 1.00 */
/* do not change */
#ifndef BRSYSTEM_H_
#define BRSYSTEM_H_
#define _WEAK	__attribute__((__weak__))

#include <bur/plctypes.h>



/* Constants */
_WEAK const signed char INIT_REASON_COLDSTART = 2;
_WEAK const signed char INIT_REASON_DOWNLOAD = 3;
_WEAK const signed char INIT_REASON_UNKNOWN = -1;
_WEAK const signed char INIT_REASON_WARMSTART = 1;
_WEAK const unsigned char TARGET_BIG_ENDIAN = 2;
_WEAK const unsigned char TARGET_LITTLE_ENDIAN = 1;
_WEAK const unsigned char br2003 = 2;
_WEAK const unsigned char br2005 = 1;
_WEAK const unsigned char br2010 = 0;
_WEAK const unsigned char brACOPOS = 7;
_WEAK const unsigned char brADDON = 7;
_WEAK const unsigned char brAUTOMATION_RUNTIME = 4;
_WEAK const unsigned char brBASE_IO = 3;
_WEAK const unsigned char brBATTERY_LOW = 0;
_WEAK const unsigned char brBATTERY_MISSING = 3;
_WEAK const unsigned char brBATTERY_NOTEST = 2;
_WEAK const unsigned char brBATTERY_OK = 1;
_WEAK const unsigned char brC200 = 9;
_WEAK const unsigned char brC300 = 8;
_WEAK const unsigned char brCAN_IO = 5;
_WEAK const unsigned char brCPU = 1;
_WEAK const unsigned short brERR_INVALID_DEVICE = 27250;
_WEAK const unsigned short brERR_INVALID_PARAMETER = 27251;
_WEAK const unsigned char brETHER_IO = 6;
_WEAK const unsigned char brKEY = 8;
_WEAK const unsigned char brLOGICSCANNER = 3;
_WEAK const unsigned char brNO_FAMILY = 255;
_WEAK const unsigned char brPANEL = 6;
_WEAK const unsigned char brPLUGIN_MODULE = 10;
_WEAK const unsigned char brPOWERPANEL = 5;
_WEAK const unsigned char brPP = 255;
_WEAK const unsigned char brPRODUCT = 0;
_WEAK const unsigned char brREMOTE_IO = 4;
_WEAK const unsigned char brSYSTEM_MODULE = 2;


/* Datatypes */


/* Datatypes of function blocks */
typedef struct SysInfo
{
	/* VAR_OUTPUT (analogous) */
	unsigned char init_reason;
	unsigned char init_count;
	unsigned long tick_count;
	unsigned long version;
	/* VAR_INPUT (digital) */
	plcbit enable;
} SysInfo_typ;

typedef struct RTInfo
{
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	unsigned long cycle_time;
	signed char init_reason;
	signed char task_class;
	/* VAR_INPUT (digital) */
	plcbit enable;
} RTInfo_typ;

typedef struct ZYKVLenable
{
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit mode;
} ZYKVLenable_typ;

typedef struct EXCInfo
{
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	unsigned long task_class;
	unsigned long task_ident;
	/* VAR_INPUT (digital) */
	plcbit enable;
} EXCInfo_typ;

typedef struct PMemSize
{
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	unsigned long size;
	/* VAR_INPUT (digital) */
	plcbit enable;
} PMemSize_typ;

typedef struct PMemPut
{
	/* VAR_INPUT (analogous) */
	unsigned long offset;
	unsigned long len;
	unsigned long adress;
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	/* VAR_INPUT (digital) */
	plcbit enable;
} PMemPut_typ;

typedef struct PMemGet
{
	/* VAR_INPUT (analogous) */
	unsigned long offset;
	unsigned long len;
	unsigned long adress;
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	/* VAR_INPUT (digital) */
	plcbit enable;
} PMemGet_typ;

typedef struct MEMInfo
{
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	unsigned long FreeUSR_Ram;
	unsigned long FreeSYSTEM;
	unsigned long FreeUSR_Prom;
	unsigned long FreeSYS_Prom;
	unsigned long FreeFIX_Ram;
	unsigned long FreeTMP_Ram;
	unsigned long FreeMEMCARD;
	/* VAR_INPUT (digital) */
	plcbit enable;
} MEMInfo_typ;

typedef struct TARGETInfo
{
	/* VAR_INPUT (analogous) */
	unsigned long pOSVersion;
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	unsigned char DataFormat;
	/* VAR_INPUT (digital) */
	plcbit enable;
} TARGETInfo_typ;

typedef struct HWInfo
{
	/* VAR_INPUT (analogous) */
	unsigned long pName;
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	unsigned char family;
	unsigned char usetype;
	unsigned long module_typ;
	unsigned char master_no;
	unsigned char slave_no;
	unsigned char module_adr;
	unsigned char slot_no;
	/* VAR (analogous) */
	unsigned long next_vw_p;
	unsigned long last_modul_p;
	unsigned long next_entry_p;
	unsigned char next_entry_ix;
	unsigned char next_slot_ix;
	unsigned char last_rio_master;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit first;
} HWInfo_typ;

typedef struct BatteryInfo
{
	/* VAR_INPUT (analogous) */
	unsigned long pDevice;
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit enable;
} BatteryInfo_typ;



/* Prototyping of functions and function blocks */
void SysInfo(SysInfo_typ* inst);
void RTInfo(RTInfo_typ* inst);
void ZYKVLenable(ZYKVLenable_typ* inst);
void EXCInfo(EXCInfo_typ* inst);
void PMemSize(PMemSize_typ* inst);
void PMemPut(PMemPut_typ* inst);
void PMemGet(PMemGet_typ* inst);
void MEMInfo(MEMInfo_typ* inst);
void TARGETInfo(TARGETInfo_typ* inst);
void HWInfo(HWInfo_typ* inst);
void BatteryInfo(BatteryInfo_typ* inst);



#endif /* BRSYSTEM_H_ */


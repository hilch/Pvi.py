/* Automation Studio generated header file */
/* Do not edit ! */

#ifndef _ACP10SDC_
#define _ACP10SDC_

#include <bur/plctypes.h>

#ifndef _IEC_CONST
#define _IEC_CONST _WEAK const
#endif

/* Constants */
#ifdef _REPLACE_CONST
 #define ncSDC_ENC16 100U
 #define ncSDC_ENC32 101U
 #define ncSDC_DRVSM16 110U
 #define ncSDC_DRVSM32 111U
 #define ncSDC_DRVSM16_CTRL 112U
 #define ncSDC_DRVSM32_CTRL 113U
 #define ncSDC_DRVSERVO16 120U
 #define ncSDC_TRIG 130U
 #define ncSDC_TRIGDIGin 131U
 #define ncSDC_DIDO 140U
#else
 _IEC_CONST unsigned short ncSDC_ENC16 = 100U;
 _IEC_CONST unsigned short ncSDC_ENC32 = 101U;
 _IEC_CONST unsigned short ncSDC_DRVSM16 = 110U;
 _IEC_CONST unsigned short ncSDC_DRVSM32 = 111U;
 _IEC_CONST unsigned short ncSDC_DRVSM16_CTRL = 112U;
 _IEC_CONST unsigned short ncSDC_DRVSM32_CTRL = 113U;
 _IEC_CONST unsigned short ncSDC_DRVSERVO16 = 120U;
 _IEC_CONST unsigned short ncSDC_TRIG = 130U;
 _IEC_CONST unsigned short ncSDC_TRIGDIGin = 131U;
 _IEC_CONST unsigned short ncSDC_DIDO = 140U;
#endif


/* Variables */


/* Datatypes and datatypes of function blocks */
typedef struct SdcHwCfg_typ
{	unsigned short EncIf1_Typ;
	unsigned short EncIf2_Typ;
	unsigned short DrvIf_Typ;
	unsigned short TrigIf1_Typ;
	unsigned short TrigIf2_Typ;
	unsigned short DiDoIf_Typ;
	unsigned char EncIf1_Name[34];
	unsigned char EncIf2_Name[34];
	unsigned char DrvIf_Name[34];
	unsigned char TrigIf1_Name[34];
	unsigned char TrigIf2_Name[34];
	unsigned char DiDoIf_Name[34];
	unsigned long NOT_USE[10];
} SdcHwCfg_typ;

typedef struct SdcEncIf16_typ
{	signed char iLifeCnt;
	plcbit iEncOK;
	signed short iActTime;
	signed short iActPos;
	signed short iRefPulsePos;
	signed char iRefPulseCnt;
	plcbit reserve[3];
} SdcEncIf16_typ;

typedef struct SdcEncIf32_typ
{	signed char iLifeCnt;
	plcbit iEncOK;
	signed short iActTime;
	signed long iActPos;
	signed long iRefPulsePos;
	signed char iRefPulseCnt;
	plcbit reserve[3];
} SdcEncIf32_typ;

typedef struct SdcDrvIf16_typ
{	signed char iLifeCnt;
	plcbit iDrvOK;
	signed short oSetTime;
	signed short oSetPos;
	plcbit oBoostCurrent;
	plcbit oStandStillCurrent;
	plcbit iStatusEnable;
	plcbit oBrake;
	plcbit reserve[2];
} SdcDrvIf16_typ;

typedef struct SdcDrvIf32_typ
{	signed char iLifeCnt;
	plcbit iDrvOK;
	signed short oSetTime;
	signed long oSetPos;
	plcbit oBoostCurrent;
	plcbit oStandStillCurrent;
	plcbit iStatusEnable;
	plcbit oBrake;
} SdcDrvIf32_typ;

typedef struct SdcTrigIf_typ
{	signed char iLifeCnt;
	signed char iTriggerCntRise;
	signed char iTriggerCntFall;
	plcbit iTriggerInput;
	signed short iTriggerTimeRise;
	signed short iTriggerTimeFall;
} SdcTrigIf_typ;

typedef struct SdcTrigIfDIGin_typ
{	signed char iLifeCnt;
	plcbit iTriggerInput;
	plcbit reserve[2];
} SdcTrigIfDIGin_typ;

typedef struct SdcDiDoIf_typ
{	signed char iLifeCntDriveReady;
	signed char iLifeCntPosHwEnd;
	signed char iLifeCntNegHwEnd;
	signed char iLifeCntReference;
	signed char iLifeCntDriveEnable;
	plcbit iDriveReady;
	plcbit iPosHwEnd;
	plcbit iNegHwEnd;
	plcbit iReference;
	plcbit oDriveEnable;
	plcbit reserve[2];
} SdcDiDoIf_typ;



/* Prototyping of functions and function blocks */


__asm__(".section \".plc\"");

__asm__(".previous");


#endif /* _ACP10SDC_ */


/* Automation Studio generated header file */
/* Do not edit ! */

#ifndef _LOOPCONR_
#define _LOOPCONR_

#include <bur/plctypes.h>

#include <sys_lib.h>
#include <brsystem.h>

#ifndef _IEC_CONST
#define _IEC_CONST _WEAK const
#endif

/* Constants */
#ifdef _REPLACE_CONST
 #define LCR_ERROR 12025U
 #define LCRTEMP_PT1 0U
 #define LCRTEMP_PT2 1U
 #define LCRTEMP_COOL 1U
 #define LCRTEMP_HEAT 0U
 #define LCR_ERR_MAXMIN 12037U
 #define LCR_WARN_Tx_DT 12007U
 #define LCRPID_D_MODE_E 2U
 #define LCRPID_D_MODE_X 1U
 #define LCRPID_MODE_MAN 2U
 #define LCRPID_MODE_OFF 0U
 #define LCR_ERR_POINTER 31563U
 #define LCRPID_MODE_AUTO 1U
 #define LCRPID_MODE_OPEN 3U
 #define LCR_ERR_DISABLED 65534U
 #define LCR_ERR_LCRPT1_T 12031U
 #define LCRPID_MODE_CLOSE 4U
 #define LCRSLIMPID_REQU_P 300U
 #define LCRPID_MODE_FREEZE 5U
 #define LCRPID_TUNE_REQU_P 300U
 #define LCRSLIMPID_REQU_PI 200U
 #define LCR_WARN_LCRTT_MEM 12018U
 #define LCRDBLPID_TSTATE_Y1 1U
 #define LCRDBLPID_TSTATE_Y2 2U
 #define LCRPID_TUNE_REQU_PI 200U
 #define LCRSLIMPID_REQU_OFF 0U
 #define LCRSLIMPID_REQU_PID 100U
 #define LCRTEMPPID_MODE_MAN 2U
 #define LCR_ERR_LCRPID_MODE 31553U
 #define LCRDBLPID_TSTATE_OFF 0U
 #define LCRPID_TUNE_REQU_OFF 0U
 #define LCRPID_TUNE_REQU_PID 100U
 #define LCRTEMPPID_MODE_AUTO 1U
 #define LCRTEMPTune_MODE_DEF 0U
 #define LCRTEMPTune_MODE_EXP 1U
 #define LCR_ERR_LCRPID_IDENT 31552U
 #define LCR_ERR_LCRTT_TT_NEG 12048U
 #define LCR_WARN_LCRTT_TT_TS 12016U
 #define LCRDBLPID_MODE_TUNE_4 6U
 #define LCRDBLPID_MODE_TUNE_6 7U
 #define LCRSLIMPID_REQU_OSC_1 10000U
 #define LCRSLIMPID_REQU_OSC_2 20000U
 #define LCRSLIMPID_REQU_OSC_3 30000U
 #define LCRSLIMPID_REQU_PER_3 300000U
 #define LCRSLIMPID_REQU_PER_4 400000U
 #define LCRSLIMPID_REQU_PER_5 500000U
 #define LCR_ERR_LCRPID_PAR_KP 12026U
 #define LCR_ERR_LCRPID_PAR_KW 12027U
 #define LCR_ERR_LCRPID_PAR_TF 12028U
 #define LCR_ERR_LCRPID_PAR_TN 12029U
 #define LCR_ERR_LCRPID_PAR_TV 12030U
 #define LCR_WARN_LCRTT_TT_INT 12017U
 #define LCRDBLPID_MODE_TUNE_Y1 8U
 #define LCRDBLPID_MODE_TUNE_Y2 9U
 #define LCRDBLPID_TSTATE_ERROR 4U
 #define LCRPID_FBK_MODE_EXTERN 2U
 #define LCRPID_FBK_MODE_INTERN 1U
 #define LCRPID_TUNE_REQU_OSC_1 10000U
 #define LCRPID_TUNE_REQU_OSC_2 20000U
 #define LCRPID_TUNE_REQU_OSC_3 30000U
 #define LCRPID_TUNE_REQU_PER_3 300000U
 #define LCRPID_TUNE_REQU_PER_4 400000U
 #define LCRPID_TUNE_REQU_PER_5 500000U
 #define LCR_ERR_LCRPID_PARADAT 31554U
 #define LCR_ERR_LCRPT12_T1_NEG 12046U
 #define LCR_ERR_LCRPT12_T2_NEG 12047U
 #define LCR_ERR_LCRPWM_TPERIOD 12033U
 #define LCR_WARN_LCRPT12_T1_TS 12010U
 #define LCR_WARN_LCRPT12_T2_TS 12013U
 #define LCR_WARN_LCRTT_TT_ZERO 12015U
 #define LCRPID_TUNE_STATE_READY 0U
 #define LCRSLIMPID_REQU_DIR_NEG 20U
 #define LCRSLIMPID_REQU_DIR_POS 10U
 #define LCRSLIMPID_REQU_ZN_DIST 3000U
 #define LCR_ERR_LCRDBLPID_DX_DT 31562U
 #define LCR_ERR_LCRIntegrate_TN 31550U
 #define LCR_ERR_LCRPID_PAR_KFBK 12025U
 #define LCR_WARN_LCRPID_A_LIMIT 12008U
 #define LCR_WARN_LCRPT12_T1_INT 12011U
 #define LCR_WARN_LCRPT12_T2_INT 12014U
 #define LCRPID_MODE_MAN_JOLTFREE 102U
 #define LCRPID_TUNE_REQU_DIR_NEG 20U
 #define LCRPID_TUNE_REQU_DIR_POS 10U
 #define LCRPID_TUNE_REQU_ZN_DIST 3000U
 #define LCR_ERR_LCRDBLPID_WX_LOW 31561U
 #define LCR_ERR_LCRPIDTune_ABORT 12038U
 #define LCR_ERR_LCRPID_PAR_DMODE 31556U
 #define LCR_ERR_LCRPID_PAR_DYMAX 31557U
 #define LCR_ERR_LCRPWM_TMINPULSE 12032U
 #define LCR_WARN_LCRPT12_T1_ZERO 12005U
 #define LCR_WARN_LCRPT12_T2_ZERO 12012U
 #define LCRDBLPID_TSTATE_FINISHED 3U
 #define LCRPID_MODE_OPEN_JOLTFREE 103U
 #define LCRSLIMPID_REQU_OSCILLATE 1U
 #define LCR_ERR_LCRMovAvgFlt_BASE 31551U
 #define LCR_ERR_LCRPIDTune_MAXMIN 31564U
 #define LCR_ERR_LCRTEMPPID_WR_PTR 31568U
 #define LCRPID_MODE_CLOSE_JOLTFREE 104U
 #define LCRPID_TUNE_REQU_OSCILLATE 1U
 #define LCRPID_TUNE_STATE_FINISHED 50U
 #define LCRSLIMPID_REQU_CHR_REF_AP 4000U
 #define LCRSLIMPID_REQU_CHR_REF_OS 5000U
 #define LCRSLIMPID_REQU_READ_PARAS 3U
 #define LCR_ERR_LCRPIDTune_TIMEOUT 12040U
 #define LCR_ERR_LCRPID_PAR_FBKMODE 31558U
 #define LCR_ERR_LCRTEMPPID_WR_PARA 31567U
 #define LCR_ERR_LCRTEMPTune_WR_PTR 31566U
 #define LCR_WARN_LCRPID_I_MAXLIMIT 12001U
 #define LCR_WARN_LCRPID_I_MINLIMIT 12002U
 #define LCR_WARN_LCRPID_YFBK_LIMIT 12003U
 #define LCR_WARN_LCRPID_YMAN_LIMIT 12009U
 #define LCR_WARN_LCRTEMPTune_ASYNC 33101U
 #define LCRPID_MODE_FREEZE_JOLTFREE 105U
 #define LCRPID_TUNE_REQU_CHR_REF_AP 4000U
 #define LCRPID_TUNE_REQU_CHR_REF_OS 5000U
 #define LCRPID_TUNE_STATE_CALC_PARA 45U
 #define LCRPID_TUNE_STATE_OSCILLATE 10U
 #define LCRSLIMPID_REQU_CHR_DIST_AP 1000U
 #define LCRSLIMPID_REQU_CHR_DIST_OS 2000U
 #define LCRSLIMPID_REQU_WRITE_PARAS 4U
 #define LCR_ERR_LCRPID_PAR_DEADBAND 12044U
 #define LCR_ERR_LCRRamp_DYUP_DYDOWN 12034U
 #define LCR_ERR_LCRTEMPTune_WR_TSET 31567U
 #define LCR_WARN_LCRTEMPPID_WR_PARA 12024U
 #define LCRPID_FBK_MODE_EXT_SELECTOR 3U
 #define LCRPID_TUNE_REQU_CHR_DIST_AP 1000U
 #define LCRPID_TUNE_REQU_CHR_DIST_OS 2000U
 #define LCRPID_TUNE_STATE_RESET_CNTL 49U
 #define LCRSLIMPID_REQU_STEPRESPONSE 2U
 #define LCR_ERR_LCRPIDTune_PARAMETER 12039U
 #define LCR_ERR_LCRPIDTune_W_CHANGED 12041U
 #define LCR_ERR_LCRPID_PAR_WX_MAXMIN 12043U
 #define LCR_WARN_LCRPIDTune_OSC_HYST 12020U
 #define LCR_WARN_LCRTEMPTune_DT_HIGH 33100U
 #define LCR_WARN_LCRTEMPTune_HEAT_TP 12021U
 #define LCR_WARN_LCRTEMPTune_WR_BASE 12023U
 #define LCR_WARN_LCRTEMPTune_WR_PARA 12022U
 #define LCRPID_TUNE_REQU_STEPRESPONSE 2U
 #define LCRPID_TUNE_STATE_OSC_CNTLPAR 19U
 #define LCR_WARN_LCRPIDTune_CYCLETIME 12004U
 #define LCRPID_TUNE_ADDINFO_OSC_PERIOD 111U
 #define LCRPID_TUNE_STATE_OSC_SEQ_CNTL 11U
 #define LCRPID_TUNE_STATE_STEP_MAXGRAD 21U
 #define LCRPID_TUNE_STATE_STEP_WAITEQ1 20U
 #define LCRPID_TUNE_STATE_STEP_WAITEQ2 22U
 #define LCR_ERR_LCRContinServo_TCHANGE 12035U
 #define LCR_ERR_LCRCurveByPoints_TABLE 12045U
 #define LCR_ERR_LCRPIDTune_CONTROL_VAR 31560U
 #define LCR_ERR_LCRTEMPPID_ILLEGALMODE 31569U
 #define LCR_ERR_LCRTEMPTune_TASKTIME_0 31570U
 #define LCR_WARN_LCRDBLPID_TUNE_CHANGE 12019U
 #define LCRPID_TUNE_STATE_OSC_PERFORM_1 12U
 #define LCRPID_TUNE_STATE_OSC_PERFORM_2 13U
 #define LCR_ERR_LCRContinServo_TIMPULSE 12036U
 #define LCR_ERR_LCRPIDTune_INVALID_REQU 31559U
 #define LCR_ERR_LCRTEMPPID_INVALID_MODE 33151U
 #define LCR_ERR_LCRTEMPTune_INVALID_MODE 33150U
#else
 _IEC_CONST unsigned short LCR_ERROR = 12025U;
 _IEC_CONST unsigned char LCRTEMP_PT1 = 0U;
 _IEC_CONST unsigned char LCRTEMP_PT2 = 1U;
 _IEC_CONST unsigned char LCRTEMP_COOL = 1U;
 _IEC_CONST unsigned char LCRTEMP_HEAT = 0U;
 _IEC_CONST unsigned short LCR_ERR_MAXMIN = 12037U;
 _IEC_CONST unsigned short LCR_WARN_Tx_DT = 12007U;
 _IEC_CONST unsigned char LCRPID_D_MODE_E = 2U;
 _IEC_CONST unsigned char LCRPID_D_MODE_X = 1U;
 _IEC_CONST unsigned char LCRPID_MODE_MAN = 2U;
 _IEC_CONST unsigned char LCRPID_MODE_OFF = 0U;
 _IEC_CONST unsigned short LCR_ERR_POINTER = 31563U;
 _IEC_CONST unsigned char LCRPID_MODE_AUTO = 1U;
 _IEC_CONST unsigned char LCRPID_MODE_OPEN = 3U;
 _IEC_CONST unsigned short LCR_ERR_DISABLED = 65534U;
 _IEC_CONST unsigned short LCR_ERR_LCRPT1_T = 12031U;
 _IEC_CONST unsigned char LCRPID_MODE_CLOSE = 4U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_P = 300U;
 _IEC_CONST unsigned char LCRPID_MODE_FREEZE = 5U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_P = 300U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_PI = 200U;
 _IEC_CONST unsigned short LCR_WARN_LCRTT_MEM = 12018U;
 _IEC_CONST unsigned char LCRDBLPID_TSTATE_Y1 = 1U;
 _IEC_CONST unsigned char LCRDBLPID_TSTATE_Y2 = 2U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_PI = 200U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_OFF = 0U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_PID = 100U;
 _IEC_CONST unsigned long LCRTEMPPID_MODE_MAN = 2U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_MODE = 31553U;
 _IEC_CONST unsigned char LCRDBLPID_TSTATE_OFF = 0U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_OFF = 0U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_PID = 100U;
 _IEC_CONST unsigned long LCRTEMPPID_MODE_AUTO = 1U;
 _IEC_CONST unsigned long LCRTEMPTune_MODE_DEF = 0U;
 _IEC_CONST unsigned long LCRTEMPTune_MODE_EXP = 1U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_IDENT = 31552U;
 _IEC_CONST unsigned short LCR_ERR_LCRTT_TT_NEG = 12048U;
 _IEC_CONST unsigned short LCR_WARN_LCRTT_TT_TS = 12016U;
 _IEC_CONST unsigned char LCRDBLPID_MODE_TUNE_4 = 6U;
 _IEC_CONST unsigned char LCRDBLPID_MODE_TUNE_6 = 7U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_OSC_1 = 10000U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_OSC_2 = 20000U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_OSC_3 = 30000U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_PER_3 = 300000U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_PER_4 = 400000U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_PER_5 = 500000U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PAR_KP = 12026U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PAR_KW = 12027U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PAR_TF = 12028U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PAR_TN = 12029U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PAR_TV = 12030U;
 _IEC_CONST unsigned short LCR_WARN_LCRTT_TT_INT = 12017U;
 _IEC_CONST unsigned char LCRDBLPID_MODE_TUNE_Y1 = 8U;
 _IEC_CONST unsigned char LCRDBLPID_MODE_TUNE_Y2 = 9U;
 _IEC_CONST unsigned char LCRDBLPID_TSTATE_ERROR = 4U;
 _IEC_CONST unsigned char LCRPID_FBK_MODE_EXTERN = 2U;
 _IEC_CONST unsigned char LCRPID_FBK_MODE_INTERN = 1U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_OSC_1 = 10000U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_OSC_2 = 20000U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_OSC_3 = 30000U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_PER_3 = 300000U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_PER_4 = 400000U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_PER_5 = 500000U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PARADAT = 31554U;
 _IEC_CONST unsigned short LCR_ERR_LCRPT12_T1_NEG = 12046U;
 _IEC_CONST unsigned short LCR_ERR_LCRPT12_T2_NEG = 12047U;
 _IEC_CONST unsigned short LCR_ERR_LCRPWM_TPERIOD = 12033U;
 _IEC_CONST unsigned short LCR_WARN_LCRPT12_T1_TS = 12010U;
 _IEC_CONST unsigned short LCR_WARN_LCRPT12_T2_TS = 12013U;
 _IEC_CONST unsigned short LCR_WARN_LCRTT_TT_ZERO = 12015U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_READY = 0U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_DIR_NEG = 20U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_DIR_POS = 10U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_ZN_DIST = 3000U;
 _IEC_CONST unsigned short LCR_ERR_LCRDBLPID_DX_DT = 31562U;
 _IEC_CONST unsigned short LCR_ERR_LCRIntegrate_TN = 31550U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PAR_KFBK = 12025U;
 _IEC_CONST unsigned short LCR_WARN_LCRPID_A_LIMIT = 12008U;
 _IEC_CONST unsigned short LCR_WARN_LCRPT12_T1_INT = 12011U;
 _IEC_CONST unsigned short LCR_WARN_LCRPT12_T2_INT = 12014U;
 _IEC_CONST unsigned char LCRPID_MODE_MAN_JOLTFREE = 102U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_DIR_NEG = 20U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_DIR_POS = 10U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_ZN_DIST = 3000U;
 _IEC_CONST unsigned short LCR_ERR_LCRDBLPID_WX_LOW = 31561U;
 _IEC_CONST unsigned short LCR_ERR_LCRPIDTune_ABORT = 12038U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PAR_DMODE = 31556U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PAR_DYMAX = 31557U;
 _IEC_CONST unsigned short LCR_ERR_LCRPWM_TMINPULSE = 12032U;
 _IEC_CONST unsigned short LCR_WARN_LCRPT12_T1_ZERO = 12005U;
 _IEC_CONST unsigned short LCR_WARN_LCRPT12_T2_ZERO = 12012U;
 _IEC_CONST unsigned char LCRDBLPID_TSTATE_FINISHED = 3U;
 _IEC_CONST unsigned char LCRPID_MODE_OPEN_JOLTFREE = 103U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_OSCILLATE = 1U;
 _IEC_CONST unsigned short LCR_ERR_LCRMovAvgFlt_BASE = 31551U;
 _IEC_CONST unsigned short LCR_ERR_LCRPIDTune_MAXMIN = 31564U;
 _IEC_CONST unsigned short LCR_ERR_LCRTEMPPID_WR_PTR = 31568U;
 _IEC_CONST unsigned char LCRPID_MODE_CLOSE_JOLTFREE = 104U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_OSCILLATE = 1U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_FINISHED = 50U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_CHR_REF_AP = 4000U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_CHR_REF_OS = 5000U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_READ_PARAS = 3U;
 _IEC_CONST unsigned short LCR_ERR_LCRPIDTune_TIMEOUT = 12040U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PAR_FBKMODE = 31558U;
 _IEC_CONST unsigned short LCR_ERR_LCRTEMPPID_WR_PARA = 31567U;
 _IEC_CONST unsigned short LCR_ERR_LCRTEMPTune_WR_PTR = 31566U;
 _IEC_CONST unsigned short LCR_WARN_LCRPID_I_MAXLIMIT = 12001U;
 _IEC_CONST unsigned short LCR_WARN_LCRPID_I_MINLIMIT = 12002U;
 _IEC_CONST unsigned short LCR_WARN_LCRPID_YFBK_LIMIT = 12003U;
 _IEC_CONST unsigned short LCR_WARN_LCRPID_YMAN_LIMIT = 12009U;
 _IEC_CONST unsigned short LCR_WARN_LCRTEMPTune_ASYNC = 33101U;
 _IEC_CONST unsigned char LCRPID_MODE_FREEZE_JOLTFREE = 105U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_CHR_REF_AP = 4000U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_CHR_REF_OS = 5000U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_CALC_PARA = 45U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_OSCILLATE = 10U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_CHR_DIST_AP = 1000U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_CHR_DIST_OS = 2000U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_WRITE_PARAS = 4U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PAR_DEADBAND = 12044U;
 _IEC_CONST unsigned short LCR_ERR_LCRRamp_DYUP_DYDOWN = 12034U;
 _IEC_CONST unsigned short LCR_ERR_LCRTEMPTune_WR_TSET = 31567U;
 _IEC_CONST unsigned short LCR_WARN_LCRTEMPPID_WR_PARA = 12024U;
 _IEC_CONST unsigned char LCRPID_FBK_MODE_EXT_SELECTOR = 3U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_CHR_DIST_AP = 1000U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_CHR_DIST_OS = 2000U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_RESET_CNTL = 49U;
 _IEC_CONST unsigned long LCRSLIMPID_REQU_STEPRESPONSE = 2U;
 _IEC_CONST unsigned short LCR_ERR_LCRPIDTune_PARAMETER = 12039U;
 _IEC_CONST unsigned short LCR_ERR_LCRPIDTune_W_CHANGED = 12041U;
 _IEC_CONST unsigned short LCR_ERR_LCRPID_PAR_WX_MAXMIN = 12043U;
 _IEC_CONST unsigned short LCR_WARN_LCRPIDTune_OSC_HYST = 12020U;
 _IEC_CONST unsigned short LCR_WARN_LCRTEMPTune_DT_HIGH = 33100U;
 _IEC_CONST unsigned short LCR_WARN_LCRTEMPTune_HEAT_TP = 12021U;
 _IEC_CONST unsigned short LCR_WARN_LCRTEMPTune_WR_BASE = 12023U;
 _IEC_CONST unsigned short LCR_WARN_LCRTEMPTune_WR_PARA = 12022U;
 _IEC_CONST unsigned long LCRPID_TUNE_REQU_STEPRESPONSE = 2U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_OSC_CNTLPAR = 19U;
 _IEC_CONST unsigned short LCR_WARN_LCRPIDTune_CYCLETIME = 12004U;
 _IEC_CONST unsigned short LCRPID_TUNE_ADDINFO_OSC_PERIOD = 111U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_OSC_SEQ_CNTL = 11U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_STEP_MAXGRAD = 21U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_STEP_WAITEQ1 = 20U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_STEP_WAITEQ2 = 22U;
 _IEC_CONST unsigned short LCR_ERR_LCRContinServo_TCHANGE = 12035U;
 _IEC_CONST unsigned short LCR_ERR_LCRCurveByPoints_TABLE = 12045U;
 _IEC_CONST unsigned short LCR_ERR_LCRPIDTune_CONTROL_VAR = 31560U;
 _IEC_CONST unsigned short LCR_ERR_LCRTEMPPID_ILLEGALMODE = 31569U;
 _IEC_CONST unsigned short LCR_ERR_LCRTEMPTune_TASKTIME_0 = 31570U;
 _IEC_CONST unsigned short LCR_WARN_LCRDBLPID_TUNE_CHANGE = 12019U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_OSC_PERFORM_1 = 12U;
 _IEC_CONST unsigned short LCRPID_TUNE_STATE_OSC_PERFORM_2 = 13U;
 _IEC_CONST unsigned short LCR_ERR_LCRContinServo_TIMPULSE = 12036U;
 _IEC_CONST unsigned short LCR_ERR_LCRPIDTune_INVALID_REQU = 31559U;
 _IEC_CONST unsigned short LCR_ERR_LCRTEMPPID_INVALID_MODE = 33151U;
 _IEC_CONST unsigned short LCR_ERR_LCRTEMPTune_INVALID_MODE = 33150U;
#endif


/* Variables */


/* Datatypes and datatypes of function blocks */
typedef struct lcrtemp_tune_internal_typ
{
	plcbit cool_tuning;
	plcbit disable_heating;
	unsigned long mode;
	float Temp_amb;
	float dRatio_heat;
	float cnt_tp_heat;
	float delta_T_heat;
	float dT_min_heat;
	float dRatio_free;
	float cnt_tp_free;
	float delta_T_free;
	float dT_min_free;
	float dRatio_cool;
	float cnt_tp_cool;
	float delta_T_cool;
	float dT_min_cool;
	float delta_T_sync_heat;
	float delta_dT_sync_heat;
	float cnt_wait_heat;
	float delta_T_sync_free;
	float delta_dT_sync_free;
	float cnt_wait_free;
	float delta_T_sync_cool;
	float delta_dT_sync_cool;
	float cnt_wait_cool;
	float filter_base_T;
	float delta_T_sync_stop;
} lcrtemp_tune_internal_typ;

typedef struct lcrtemp_pid_internal_typ
{
	plcbit enable_cooling;
	plcbit disable_heating;
	float hyst;
	float delay;
	float Kw;
	float Kfbk;
	float Kp_h;
	float Tn_h;
	float Tv_h;
	float Kp_c;
	float Tn_c;
	float Tv_c;
	float dynGeneral;
	float dynHeat;
	float dynCool;
	float mem01;
	float mem02;
	float mem10;
	float mem20;
	float exp_mem;
} lcrtemp_pid_internal_typ;

typedef struct lcrtemp_pid_opt_typ
{
	float Kp_h;
	float Tn_h;
	float Tv_h;
	float Kp_c;
	float Tn_c;
	float Tv_c;
	float dynGeneral;
	float dynHeat;
	float dynCool;
} lcrtemp_pid_opt_typ;

typedef struct lcrtemp_tune_set_typ
{
	unsigned long mode;
	float Temp_amb;
	float dRatio_heat;
	float cnt_tp_heat;
	float delta_T_heat;
	float dT_min_heat;
	float dRatio_free;
	float cnt_tp_free;
	float delta_T_free;
	float dT_min_free;
	float dRatio_cool;
	float cnt_tp_cool;
	float delta_T_cool;
	float dT_min_cool;
	float delta_T_sync_heat;
	float delta_dT_sync_heat;
	float cnt_wait_heat;
	float delta_T_sync_free;
	float delta_dT_sync_free;
	float cnt_wait_free;
	float delta_T_sync_cool;
	float delta_dT_sync_cool;
	float cnt_wait_cool;
	float filter_base_T;
	float delta_T_sync_stop;
} lcrtemp_tune_set_typ;

typedef struct lcrtemp_pid_set_typ
{
	float hyst;
	float delay;
	float Kw;
	float Kfbk;
} lcrtemp_pid_set_typ;

typedef struct lcrtemp_add_typ
{
	float mem01;
	float mem02;
	float mem10;
	float mem20;
	float exp_mem;
	float cnt01;
	float cnt02;
	float cnt10;
	float cnt20;
	float cnt03;
	float cnt30;
	float cnt00;
	float reserved1;
	float reserved2;
	unsigned long reserved3;
	unsigned long reserved4;
	plcbit reserved5;
	plcbit reserved6;
} lcrtemp_add_typ;

typedef struct lcrtemp_set_typ
{
	plcbit enable_cooling;
	plcbit disable_heating;
	struct lcrtemp_pid_opt_typ PIDpara;
	struct lcrtemp_tune_set_typ TuneSet;
	struct lcrtemp_pid_set_typ PIDSet;
	struct lcrtemp_add_typ Internal;
} lcrtemp_set_typ;

typedef struct lcrslimpid_par_typ
{
	float Y_max;
	float Y_min;
	float Kp;
	float Tn;
	float Tv;
	float Kfbk;
} lcrslimpid_par_typ;

typedef struct lcrdblpid_par_typ
{
	float Y_max;
	float Y_min;
	signed short K_fact;
	float Kp;
	float Tn;
	float Tv;
} lcrdblpid_par_typ;

typedef struct lcrpid_tune_osc_options_typ
{
	float osc_minAmplitude;
	float Q_min;
} lcrpid_tune_osc_options_typ;

typedef struct lcrpid_tune_step_options_typ
{
	float eqDeltaX;
	float eqDeltaWX;
	float eqDeltat;
	float evalDeltaX;
	unsigned short evalNfilter;
	unsigned short exitNotMaxdXCount;
	float exitdXRatio;
} lcrpid_tune_step_options_typ;

typedef struct lcrdblpid_tune_typ
{
	signed short P1_manualAdjust;
	signed short I1_manualAdjust;
	signed short D1_manualAdjust;
	signed short P2_manualAdjust;
	signed short I2_manualAdjust;
	signed short D2_manualAdjust;
	float X_min;
	float X_max;
	float X0;
	float de_min;
	float Y0;
	float Y1step;
	float Y2step;
	unsigned long tuneY1_opt;
	unsigned long tuneY2_opt;
	unsigned char tune_first;
	float hyst;
	float measDelta;
	struct lcrpid_tune_osc_options_typ osc_opt;
	struct lcrpid_tune_step_options_typ step_opt;
} lcrdblpid_tune_typ;

typedef struct lcrpid_tune_addpar_typ
{
	float t_max_tune;
	float WX_min;
	float WX_max;
	float dY_max;
	float Tf_Tv;
	float Kw;
	float Kfbk;
	unsigned char fbk_mode;
	unsigned char d_mode;
	float deadband;
	plcbit invert;
} lcrpid_tune_addpar_typ;

typedef struct lcrpid_procPar_typ
{
	unsigned short size;
	plcbit valid;
	plcbit stepResp_valid;
	float stepResp_v;
	float stepResp_t_u;
	float stepResp_t_g;
	plcbit osc_valid;
	float osc_amplitudeRatio;
	float osc_tPeriod;
	plcbit force_params;
	float Kp;
	float Kp_tune;
	float Tn;
	float Tn_tune;
	float Tv;
	float Tv_tune;
} lcrpid_procPar_typ;

typedef struct lcrpid_old_typ
{
	struct lcrpid_procPar_typ processPar;
	signed short P_manualAdjust;
	signed short I_manualAdjust;
	signed short D_manualAdjust;
	float Y_min;
	float Y_max;
	float dY_max;
	float Tf_Tv;
	float Kw;
	float Kfbk;
	float deadband;
	float W;
	unsigned long request;
	unsigned char fbk_mode;
	unsigned char d_mode;
	plcbit invert;
	plcbit enable;
} lcrpid_old_typ;

typedef struct lcrpid_tune_step_typ
{
	struct lcrpid_tune_step_options_typ options;
	float Y0;
	float Y1;
	float t_jump;
	float W;
	float X0;
	float Xmax;
	float Xmin;
	float Xfiltered;
	plcbit deltaXok;
	plcbit deltaWXok;
	float eqTime;
	signed char dir;
	float deltaX;
	float X1;
	float t1;
	plcbit t1set;
	float dX_dt;
	float dX_dt_max;
	float XmaxGrad;
	float maxX1;
	float maxX2;
	float maxt1;
	float maxt2;
	float tmaxGrad;
	float gainFactor;
	float deadTime;
	float riseTime;
	unsigned short notMaxCount;
	float gradientRatio;
} lcrpid_tune_step_typ;

typedef struct lcrpid_osc_val_typ
{
	float X;
	float t;
} lcrpid_osc_val_typ;

typedef struct lcrpid_osc_per_typ
{
	struct lcrpid_osc_val_typ max;
	struct lcrpid_osc_val_typ min;
} lcrpid_osc_per_typ;

typedef struct lcrpid_tune_osc_typ
{
	struct lcrpid_tune_osc_options_typ options;
	unsigned short oscPhase;
	signed char dir;
	plcbit enHi;
	plcbit enLo;
	float Y_hi;
	float Y_lo;
	unsigned short i_maxPeriod;
	unsigned short i_period;
	float X_ampl;
	float X_avg;
	float X_min_avg;
	float X_max_avg;
	float Y_avg;
	float deltaY;
	float t_Ylohi[5];
	float t_Yhilo[5];
	float Q_act;
	float a_wx;
	float amplitudeRatio;
	float Ku;
	float tPeriod;
	struct lcrpid_osc_per_typ period[5];
} lcrpid_tune_osc_typ;

typedef struct lcrCurveByPoints_TabEntry_type
{
	float x;
	float y;
} lcrCurveByPoints_TabEntry_type;

typedef struct lcrpid_internal_typ
{
	unsigned short size;
	plcbit valid;
	float WX_max;
	float WX_min;
	plcbit invert;
	float deadband;
	float dY_max;
	float Kp;
	float Kp_Tn;
	float Tv_Tf;
	float Tf_reciproc;
	float Kw;
	float Kfbk_Kp;
	unsigned char fbk_mode;
	unsigned char d_mode;
	unsigned char force_mode;
	float Y_force;
	float W;
	float X;
	unsigned char pid_init;
	signed long Yp1;
	signed long Yp2;
	signed long dYi1;
	signed long dYi2;
	signed long Yi1;
	signed long Yi2;
	float dt_Tf;
	signed long a11;
	signed long a12;
	signed long a21;
	signed long a22;
	signed long Yd1;
	signed long Yd2;
	signed long Ytotal1;
	signed long Ytotal2;
	signed long Ylim1;
	signed long Ylim2;
	signed long Y1;
	signed long Y2;
	float e_fbk;
} lcrpid_internal_typ;

typedef struct LCRScal
{
	/* VAR_INPUT (analog) */
	float x;
	float x1;
	float y1;
	float x2;
	float y2;
	/* VAR_OUTPUT (analog) */
	float y;
} LCRScal_typ;

typedef struct LCRPID
{
	/* VAR_INPUT (analog) */
	unsigned long ident;
	float W;
	float X;
	float Y_max;
	float Y_min;
	float A;
	float Y_man;
	float Y_fbk;
	unsigned char mode;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	float e;
	float Y;
	float Yp;
	float Yi;
	float Yd;
	/* VAR (analog) */
	float Tv_Tf_old;
	float e_old;
	unsigned short deadband_state;
	struct SysInfo sysinfo_inst;
	struct LCRScal scal_inst;
	unsigned short counter_state;
	unsigned long bootkey_old;
	unsigned long systicks_old;
	unsigned short musecs_old;
	float Yi_min;
	float Yi_max;
	float Yi_minInternal;
	float Yi_maxInternal;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit hold_I;
	/* VAR (digital) */
	plcbit enable_old;
} LCRPID_typ;

typedef struct LCRCurveByPoints
{
	/* VAR_INPUT (analog) */
	float x;
	unsigned short NoOfPoints;
	struct lcrCurveByPoints_TabEntry_type* ptr_table;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	float y;
	/* VAR (analog) */
	signed short i_tab;
	unsigned short iterations;
	struct LCRScal scal1;
} LCRCurveByPoints_typ;

typedef struct LCRPIDpara
{
	/* VAR_INPUT (analog) */
	float WX_max;
	float WX_min;
	float deadband;
	float dY_max;
	float Kp;
	float Tn;
	float Tv;
	float Tf;
	float Kw;
	float Kfbk;
	unsigned char fbk_mode;
	unsigned char d_mode;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	unsigned long ident;
	/* VAR (analog) */
	struct lcrpid_internal_typ internal_data;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit enter;
	plcbit invert;
} LCRPIDpara_typ;

typedef struct LCRContinServo
{
	/* VAR_INPUT (analog) */
	float x;
	float max_value;
	float min_value;
	float t_impulse;
	float t_change_up;
	float t_change_down;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	float hysteresis_up;
	float hysteresis_down;
	/* VAR (analog) */
	unsigned short counter_state;
	unsigned long bootkey_old;
	unsigned long systicks_old;
	unsigned short musecs_old;
	signed long t_cnt_1;
	signed long t_cnt_2;
	signed long y_dbl_1;
	signed long y_dbl_2;
	struct SysInfo sysInfo_inst;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit ref;
	/* VAR_OUTPUT (digital) */
	plcbit up;
	plcbit down;
	plcbit refOk;
	/* VAR (digital) */
	plcbit enable_old;
	plcbit ref_old;
} LCRContinServo_typ;

typedef struct LCRPT1
{
	/* VAR_INPUT (analog) */
	float x;
	float t;
	float y_set;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	float y;
	/* VAR (analog) */
	unsigned short counter_state;
	unsigned long bootkey_old;
	unsigned long systicks_old;
	unsigned short musecs_old;
	signed long y_dbl_1;
	signed long y_dbl_2;
	struct SysInfo sysinfo_inst;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit set;
} LCRPT1_typ;

typedef struct LCRRamp
{
	/* VAR_INPUT (analog) */
	float x;
	float dy_up;
	float dy_down;
	float y_max;
	float y_min;
	float y_set;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	float y;
	/* VAR (analog) */
	unsigned short counter_state;
	unsigned long bootkey_old;
	unsigned long systicks_old;
	unsigned short musecs_old;
	signed long y_dbl_1;
	signed long y_dbl_2;
	struct SysInfo sysinfo_inst;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit set;
	/* VAR_OUTPUT (digital) */
	plcbit x_reached;
	plcbit max_limit;
	plcbit min_limit;
} LCRRamp_typ;

typedef struct LCRIntegrate
{
	/* VAR_INPUT (analog) */
	float x;
	float tn;
	float y_max;
	float y_min;
	float y_set;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	float y;
	/* VAR (analog) */
	unsigned short counter_state;
	unsigned long bootkey_old;
	unsigned long systicks_old;
	unsigned short musecs_old;
	signed long y_dbl_1;
	signed long y_dbl_2;
	struct SysInfo sysinfo_inst;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit set;
	/* VAR_OUTPUT (digital) */
	plcbit max_limit;
	plcbit min_limit;
} LCRIntegrate_typ;

typedef struct LCRLimit
{
	/* VAR_INPUT (analog) */
	float in;
	signed long max_value;
	signed long min_value;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	signed long out;
	/* VAR_OUTPUT (digital) */
	plcbit max_limit;
	plcbit min_limit;
} LCRLimit_typ;

typedef struct LCRLimScal
{
	/* VAR_INPUT (analog) */
	float x;
	float x1;
	float y1;
	float x2;
	float y2;
	/* VAR_OUTPUT (analog) */
	float y;
} LCRLimScal_typ;

typedef struct LCRMovAvgFlt
{
	/* VAR_INPUT (analog) */
	float x;
	unsigned short base;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	float y;
	/* VAR (analog) */
	signed long sum_old_dbl_1;
	signed long sum_old_dbl_2;
	float x_old[32];
	unsigned long p_xold;
	unsigned short i_xold;
	unsigned short base_old;
	unsigned long bootkey_old;
	/* VAR_INPUT (digital) */
	plcbit enable;
	/* VAR (digital) */
	plcbit enable_old;
} LCRMovAvgFlt_typ;

typedef struct LCRPWM
{
	/* VAR_INPUT (analog) */
	float x;
	float max_value;
	float min_value;
	float t_min_pulse;
	float t_period;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	float t_on;
	float t_off;
	/* VAR (analog) */
	unsigned short counter_state;
	unsigned long bootkey_old;
	unsigned long systicks_old;
	unsigned short musecs_old;
	signed long cnt_terron_1;
	signed long cnt_terron_2;
	signed long cnt_terroff_1;
	signed long cnt_terroff_2;
	signed long cnt_t_pulse_1;
	signed long cnt_t_pulse_2;
	struct SysInfo sysinfo_inst;
	/* VAR_INPUT (digital) */
	plcbit enable;
	/* VAR_OUTPUT (digital) */
	plcbit pulse;
	/* VAR (digital) */
	plcbit corr;
} LCRPWM_typ;

typedef struct LCRTimeBasedOnOff
{
	/* VAR_INPUT (analog) */
	float x;
	float max_value;
	float min_value;
	float timpulse;
	float tchange_up;
	float tchange_down;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	float hysteresis_up;
	float hysteresis_down;
	/* VAR (analog) */
	unsigned short counter_state;
	unsigned long bootkey_old;
	unsigned long systicks_old;
	unsigned short musecs_old;
	signed long t_cnt_1;
	signed long t_cnt_2;
	signed long y_dbl_1;
	signed long y_dbl_2;
	struct SysInfo sysInfo_inst;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit ref;
	/* VAR_OUTPUT (digital) */
	plcbit up;
	plcbit down;
	plcbit refOk;
	/* VAR (digital) */
	plcbit enable_old;
	plcbit ref_old;
} LCRTimeBasedOnOff_typ;

typedef struct LCRDifferentiate
{
	/* VAR_INPUT (analog) */
	float x;
	float tv;
	float tf;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	float y;
	/* VAR (analog) */
	unsigned short counter_state;
	unsigned long bootkey_old;
	unsigned long systicks_old;
	unsigned short musecs_old;
	struct SysInfo sysinfo_inst;
	signed long a11;
	signed long a12;
	signed long a21;
	signed long a22;
	/* VAR_INPUT (digital) */
	plcbit enable;
} LCRDifferentiate_typ;

typedef struct LCRPIDTune
{
	/* VAR_INPUT (analog) */
	float Y_min;
	float Y_max;
	float Y0;
	float Y1;
	float X0;
	float X_min;
	float X_max;
	signed short P_manualAdjust;
	signed short I_manualAdjust;
	signed short D_manualAdjust;
	unsigned long request;
	struct lcrpid_tune_addpar_typ* pAddPar;
	struct lcrpid_tune_osc_options_typ* pOptions_osc;
	struct lcrpid_tune_step_options_typ* pOptions_step;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	unsigned short addInfo;
	unsigned long ident;
	unsigned short state;
	/* VAR (analog) */
	float t_autotune;
	unsigned short status_tmp;
	unsigned short counter_state;
	unsigned long bootkey_old;
	unsigned long systicks_old;
	unsigned short musecs_old;
	struct SysInfo sysinfo_inst;
	struct LCRMovAvgFlt MovAvgFlt_inst;
	struct lcrpid_old_typ old;
	struct lcrpid_procPar_typ processPar;
	struct lcrpid_internal_typ internal_data;
	struct lcrpid_tune_addpar_typ addPar;
	struct lcrpid_tune_osc_typ oscillation;
	struct lcrpid_tune_step_typ stepresponse;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit okToStep;
	/* VAR_OUTPUT (digital) */
	plcbit rdyToStep;
} LCRPIDTune_typ;

typedef struct LCRSlimPID
{
	/* VAR_INPUT (analog) */
	float W;
	float X;
	unsigned long request;
	struct lcrslimpid_par_typ* pPar;
	/* VAR_OUTPUT (analog) */
	float e;
	float Y;
	unsigned short status;
	unsigned short addInfo;
	/* VAR (analog) */
	struct LCRMovAvgFlt MovAvgFlt_inst;
	struct LCRPIDTune PIDTune_inst;
	struct LCRPID PID_inst;
	unsigned long requ_old;
	/* VAR_INPUT (digital) */
	plcbit enable;
	/* VAR (digital) */
	plcbit enable_old;
} LCRSlimPID_typ;

typedef struct LCRPFM
{
	/* VAR_INPUT (analog) */
	float x;
	float max_value;
	float min_value;
	float t_pulse;
	float t_pause;
	/* VAR_OUTPUT (analog) */
	unsigned short status;
	/* VAR (analog) */
	float area;
	float area_c;
	float range;
	float last;
	float tpls;
	unsigned short counter_state;
	unsigned long bootkey_old;
	unsigned long systicks_old;
	unsigned short musecs_old;
	struct SysInfo sysinfo_inst;
	/* VAR_INPUT (digital) */
	plcbit enable;
	/* VAR_OUTPUT (digital) */
	plcbit pulse;
	/* VAR (digital) */
	plcbit enable_old;
} LCRPFM_typ;

typedef struct LCRTt
{
	/* VAR_INPUT (analog) */
	signed long Tt;
	float x;
	float y_set;
	/* VAR_OUTPUT (analog) */
	float y;
	unsigned short status;
	/* VAR (analog) */
	signed long Ts;
	signed long Tt_Max;
	float* pRingBuf;
	float* pBuf_OutIn;
	unsigned char set_old;
	unsigned char Set_y;
	unsigned long Bootkey;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit set;
	/* VAR (digital) */
	plcbit enable_old;
} LCRTt_typ;

typedef struct LCRPT2
{
	/* VAR_INPUT (analog) */
	float V;
	float T1;
	float T2;
	float x;
	float y_set;
	unsigned char set;
	/* VAR_OUTPUT (analog) */
	float y;
	unsigned short status;
	/* VAR (analog) */
	unsigned long x1_dbl_1;
	unsigned long x1_dbl_2;
	unsigned long x2_dbl_1;
	unsigned long x2_dbl_2;
	signed long Ts;
	unsigned long Ts_dbl_1;
	unsigned long Ts_dbl_2;
	unsigned char set_old;
	unsigned char Set_y;
	unsigned long Bootkey;
	/* VAR_INPUT (digital) */
	plcbit enable;
} LCRPT2_typ;

typedef struct LCRSimModExt
{
	/* VAR_INPUT (analog) */
	signed long Tt_h;
	signed long Tt_c;
	float k_h;
	float k_c;
	float PT2_T1;
	float PT2_T2;
	float Temp_amb;
	float Temp_c;
	float Alpha_h;
	float Alpha_c;
	/* VAR_OUTPUT (analog) */
	float y;
	unsigned short status;
	/* VAR (analog) */
	struct LCRTt Tt_heat;
	struct LCRTt Tt_cool;
	float k_h_intern;
	float k_c_intern;
	struct LCRPT2 PT2;
	float y_c;
	float y_end;
	float y_h;
	unsigned long Bootkey;
	/* VAR_INPUT (digital) */
	plcbit enable;
	/* VAR (digital) */
	plcbit enable_old;
} LCRSimModExt_typ;

typedef struct LCRPT1e
{
	/* VAR_INPUT (analog) */
	float V;
	float T1;
	float x;
	float y_set;
	unsigned char set;
	/* VAR_OUTPUT (analog) */
	float y;
	unsigned short status;
	/* VAR (analog) */
	unsigned long x1_dbl_1;
	unsigned long x1_dbl_2;
	signed long Ts;
	unsigned long Ts_dbl_1;
	unsigned long Ts_dbl_2;
	unsigned char set_old;
	unsigned char Set_y;
	unsigned long Bootkey;
	/* VAR_INPUT (digital) */
	plcbit enable;
} LCRPT1e_typ;

typedef struct LCRDblActPID
{
	/* VAR_INPUT (analog) */
	float W;
	float X;
	float Y_man;
	unsigned char mode;
	struct lcrdblpid_par_typ* pPar1;
	struct lcrdblpid_par_typ* pPar2;
	struct lcrpid_tune_addpar_typ* pAddPar;
	struct lcrdblpid_tune_typ* pOpt;
	/* VAR_OUTPUT (analog) */
	float e;
	float Y1;
	float Y2;
	unsigned short status;
	unsigned char tuneState;
	/* VAR (analog) */
	struct LCRPID pid;
	struct LCRPIDTune tune;
	struct SysInfo sysinfo_inst;
	float gradient;
	float Y_avg;
	unsigned long tcnt_1;
	unsigned long tcnt_2;
	float Tmeas;
	float y_lim_old;
	float p_fact;
	unsigned long bootkey_old;
	unsigned long systicks_old;
	unsigned short musecs_old;
	unsigned char use_par;
	unsigned char meas;
	unsigned char mode_old;
	unsigned char tune_step;
	unsigned char tune_grad;
	unsigned char tune_2nd;
	unsigned char invert;
	unsigned char counter_state;
	unsigned char mode_int;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit hold_I;
	plcbit okToStep;
	/* VAR_OUTPUT (digital) */
	plcbit rdyToStep;
	/* VAR (digital) */
	plcbit enable_old;
} LCRDblActPID_typ;

typedef struct LCRMinMax
{
	/* VAR_INPUT (analog) */
	float in;
	/* VAR_OUTPUT (analog) */
	float out_min;
	float out_max;
	/* VAR_INPUT (digital) */
	plcbit reset;
} LCRMinMax_typ;

typedef struct LCRTempPID
{
	/* VAR_INPUT (analog) */
	float Temp_set;
	float Temp;
	float Y_man;
	unsigned long mode;
	struct lcrtemp_set_typ* pSettings;
	/* VAR_OUTPUT (analog) */
	float y_heat;
	float y_cool;
	unsigned short status;
	/* VAR (analog) */
	struct LCRPID pid;
	struct LCRPIDpara pid_para;
	float Temp_set_delay;
	float Temp_set_int;
	float t;
	signed char state;
	float a;
	struct SysInfo sysinfo_inst;
	unsigned char para_check_done;
	struct lcrtemp_pid_internal_typ internal_para;
	float dbl_dt;
	float a_internal;
	float Temp_set_int_old1;
	float Temp_set_int_old2;
	float Temp_set_int_old3;
	unsigned long mode_old;
	unsigned long timestore1;
	unsigned long timestore2;
	unsigned long timeCnt;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit update;
	/* VAR (digital) */
	plcbit new_Temp_set;
	plcbit enable_old;
	plcbit err_flag;
} LCRTempPID_typ;

typedef struct LCRTempTune
{
	/* VAR_INPUT (analog) */
	float Temp_set;
	float Temp;
	struct lcrtemp_set_typ* pSettings;
	/* VAR_OUTPUT (analog) */
	float y_heat;
	float y_cool;
	unsigned short status;
	/* VAR (analog) */
	struct LCRPID pid;
	struct LCRPIDpara pid_para;
	struct LCRMovAvgFlt MovAvgFltTemp;
	unsigned short step;
	float t;
	float Temp_start;
	float mem00;
	float cnt02;
	float cnt33;
	float cnt20;
	float pem01;
	float pem33;
	float pem10;
	float pem02;
	float pem44;
	float pem20;
	float tol01;
	float tol10;
	float tol02;
	float tol20;
	float tol22;
	float Temp_old;
	float delta_Temp;
	unsigned long tcnt_1;
	unsigned long tcnt_2;
	unsigned long tcnt_dT_1;
	unsigned long tcnt_dT_2;
	struct SysInfo sysinfo_inst;
	float Temp_set_internal;
	struct RTInfo rt_info;
	float tasktime;
	float timecounter;
	struct lcrtemp_tune_internal_typ internal_para;
	float dbl_dt;
	unsigned long call_counter;
	unsigned long store1;
	unsigned long store2;
	unsigned long timeCnt;
	unsigned short waitCounter;
	/* VAR_INPUT (digital) */
	plcbit enable;
	plcbit start;
	plcbit okToHeat;
	plcbit okToFree;
	plcbit okToFreeEnd;
	plcbit okToCool;
	plcbit okToCoolEnd;
	/* VAR_OUTPUT (digital) */
	plcbit rdyToHeat;
	plcbit rdyToFree;
	plcbit rdyToFreeEnd;
	plcbit rdyToCool;
	plcbit rdyToCoolEnd;
	plcbit done;
	plcbit busy;
	/* VAR (digital) */
	plcbit enable_old;
} LCRTempTune_typ;



/* Prototyping of functions and function blocks */
void LCRPID(struct LCRPID* inst);
void LCRScal(struct LCRScal* inst);
void LCRCurveByPoints(struct LCRCurveByPoints* inst);
void LCRPIDpara(struct LCRPIDpara* inst);
void LCRContinServo(struct LCRContinServo* inst);
void LCRPT1(struct LCRPT1* inst);
void LCRRamp(struct LCRRamp* inst);
void LCRIntegrate(struct LCRIntegrate* inst);
void LCRLimit(struct LCRLimit* inst);
void LCRLimScal(struct LCRLimScal* inst);
void LCRMovAvgFlt(struct LCRMovAvgFlt* inst);
void LCRPWM(struct LCRPWM* inst);
void LCRTimeBasedOnOff(struct LCRTimeBasedOnOff* inst);
void LCRDifferentiate(struct LCRDifferentiate* inst);
void LCRSlimPID(struct LCRSlimPID* inst);
void LCRPIDTune(struct LCRPIDTune* inst);
void LCRPFM(struct LCRPFM* inst);
void LCRSimModExt(struct LCRSimModExt* inst);
void LCRTt(struct LCRTt* inst);
void LCRPT2(struct LCRPT2* inst);
void LCRPT1e(struct LCRPT1e* inst);
void LCRDblActPID(struct LCRDblActPID* inst);
void LCRMinMax(struct LCRMinMax* inst);
void LCRTempPID(struct LCRTempPID* inst);
void LCRTempTune(struct LCRTempTune* inst);



#endif /* _LOOPCONR_ */


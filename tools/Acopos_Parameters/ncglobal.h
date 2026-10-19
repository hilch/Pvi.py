/* ncglobal.h V5.31.3 */ 
/* COPYRIGHT (C) B&R Industrial Automation GmbH */ 

/* Automation Studio generated header file */
/* Do not edit ! */

#ifndef _NCGLOBAL_
#define _NCGLOBAL_
#ifdef __cplusplus
extern "C" 
{
#endif

#include <bur/plctypes.h>

#ifndef _BUR_PUBLIC
#define _BUR_PUBLIC
#endif
/* Constants */
#ifdef _REPLACE_CONST
 #define SafeMC_action_READ_SAFEOUT_DATA3 6U
 #define SafeMC_action_READ_SAFEOUT_DATA2 4U
 #define SafeMC_action_READ_SAFEOUT_DATA 2U
 #define SafeMC_action_READ_SAFEIN_DATA3 7U
 #define SafeMC_action_READ_SAFEIN_DATA2 5U
 #define SafeMC_action_READ_SAFEIN_DATA 3U
 #define SafeMC_action_GET_CFG_PTR 1U
 #define RIO4_2005 4480U
 #define RIO3_2005 3456U
 #define RIO2_2005 2432U
 #define RIO1_2005 1408U
 #define ncZX 1U
 #define ncZEROPMON 216U
 #define ncZERO_TAB 208U
 #define ncZERO_DAT 21U
 #define ncZERO 1U
 #define ncZ_TRANS 3U
 #define ncYZ 2U
 #define ncXY 0U
 #define ncWRITE_HPRIO 290U
 #define ncWRITE_COB 320U
 #define ncWITHOUT_INDEX 1U
 #define ncWITH_INDEX 0U
 #define ncWITH_CAM 31U
 #define ncWINDOW 1U
 #define ncVIRTUAL_IF 128U
 #define ncVERTICAL 1U
 #define ncVARIABLE 377U
 #define ncV_TRAJ 20U
 #define ncV_STOP 70U
 #define ncV_SET_COMP 17U
 #define ncV_SET 12U
 #define ncV_JUMP_T 4U
 #define ncV_JUMP 1U
 #define ncV_CONST 2U
 #define ncV_COMP_S_SL 38U
 #define ncV_COMP_S_MA 37U
 #define ncV_COMP_A_SL 36U
 #define ncV_COMP_A_CYC 39U
 #define ncV_AXIS 4U
 #define ncV_ACT 14U
 #define ncUSERROM 2U
 #define ncUSER 1U
 #define ncUSE_TN 8U
 #define ncUSE_FILTER_PAR 4U
 #define ncUPLOAD 338U
 #define ncUNLINK 344U
 #define ncUF 7U
 #define ncU_SET 13U
 #define ncU_LIMIT 40U
 #define ncTUNE_V_CONSTANT 1U
 #define ncTUNE_TN 16U
 #define ncTUNE_STANDSTILL 0U
 #define ncTUNE_MODEL_FRICTION 8192U
 #define ncTUNE_MODEL_2MASS 32768U
 #define ncTUNE_FBCTRL_MODEL_2MASS 8192U
 #define ncTUNE_FBCTRL_MODEL_1MASS 12288U
 #define ncTRUE 1U
 #define ncTRQ_LIMIT 30U
 #define ncTRIGGPOS 112U
 #define ncTRIGGER8 34U
 #define ncTRIGGER7 32U
 #define ncTRIGGER6 30U
 #define ncTRIGGER5 28U
 #define ncTRIGGER4 26U
 #define ncTRIGGER3 24U
 #define ncTRIGGER2 22U
 #define ncTRIGGER1 20U
 #define ncTRIGGER_2 6U
 #define ncTRIGGER 0U
 #define ncTRGPOS_S 118U
 #define ncTRG_STOP_S_REST 2U
 #define ncTRG_STOP_NORMAL 1U
 #define ncTRG_STOP 8192U
 #define ncTRACE_PAR_SEC_REC 2048U
 #define ncTRACE_DAT_WR 2050U
 #define ncTRACE 304U
 #define ncTR_TRIGG 3U
 #define ncTR_TRACE 2U
 #define ncTR_START 20U
 #define ncTR_SDM 21U
 #define ncTR_SAVE 7U
 #define ncTR_RING 4U
 #define ncTR_REST 5U
 #define ncTR_END 1U
 #define ncTR_DELAY 6U
 #define ncTOOLDAT 2U
 #define ncTOOL_TAB 209U
 #define ncTOOL 22U
 #define ncTHRESHLD 0U
 #define ncTEXT 271U
 #define ncTEST_SPEED 16385U
 #define ncTEST_POSITION 16386U
 #define ncTEST 31U
 #define ncTANGENT 2U
 #define ncT_TOTAL 128U
 #define ncT_JOLT 1U
 #define ncT_FORMAT 15U
 #define ncT_FILTER_2 65U
 #define ncT_FILTER 64U
 #define ncSYSROM 0U
 #define ncSYNC 266U
 #define ncSWITCH_ON 258U
 #define ncSWITCH_OFF 259U
 #define ncSWITCH_GATE 1U
 #define ncSWITCH 2U
 #define ncSW_ON 258U
 #define ncSW_OFF 259U
 #define ncSW_END 1U
 #define ncSTOP_HOMING 255U
 #define ncSTOP 261U
 #define ncSTEP_OVER 220U
 #define ncSTEP_INTO 221U
 #define ncSTATE 128U
 #define ncSTARTDIR 267U
 #define ncSTARTABS 272U
 #define ncSTART_T 275U
 #define ncSTART_NETWORK_REQU_PARCMD 280U
 #define ncSTART_IV 270U
 #define ncSTART_CYC_TRACE_CTRL_BITS 289U
 #define ncSTART_CG 269U
 #define ncSTART 260U
 #define ncSTANDARD 0U
 #define ncST_END 12U
 #define ncST_COMP 4U
 #define ncST_CAMPR 2U
 #define ncSSI_SEND 3U
 #define ncSSI_PARITY_CHK_ODD 7U
 #define ncSSI_PARITY_CHK_EVEN 6U
 #define ncSSI_CONT_TYP_WRN_INV 5U
 #define ncSSI_CONT_TYP_WRN 4U
 #define ncSSI_CONT_TYP_POS 1U
 #define ncSSI_CONT_TYP_FILL 6U
 #define ncSSI_CONT_TYP_ERR_INV 3U
 #define ncSSI_CONT_TYP_ERR 2U
 #define ncSSI_CONT_TYP_END 0U
 #define ncSSI 6U
 #define ncSSE 2U
 #define ncSPOSSTDZ 160U
 #define ncSPEED 2U
 #define ncSL_LATCHPOS 34U
 #define ncSL_ABS 33U
 #define ncSKIP_PARSE 10U
 #define ncSKIP_FCN 205U
 #define ncSINGLE 204U
 #define ncSIMULATION 150U
 #define ncSIMULAT 150U
 #define ncSIM_START 127U
 #define ncSIM_2MASS_GEAR 4U
 #define ncSIM_2MASS 2U
 #define ncSIM_1MASS_GEAR 3U
 #define ncSIM_1MASS_AUTO 0U
 #define ncSIM_1MASS 1U
 #define ncSIGNAL4 94U
 #define ncSIGNAL3 93U
 #define ncSIGNAL2 92U
 #define ncSIGNAL1 91U
 #define ncSIGNAL_PRBS 0U
 #define ncSIGNAL_CHIRP_TRAPEZOID 2U
 #define ncSIGNAL_CHIRP 1U
 #define ncSIGNAL 4U
 #define ncSIG_LINE 110U
 #define ncSHORT_PATH 1U
 #define ncSETUP_MOVE_T_JOLT 16U
 #define ncSETUP 16384U
 #define ncSET_GEN_ONLY 1024U
 #define ncSET 264U
 #define ncSERVICE 165U
 #define ncSERCOSIF 310U
 #define ncSERCOS_LIN 128U
 #define ncSERCOS 2U
 #define ncSEND 368U
 #define ncSDC_IF 129U
 #define ncSCALE 180U
 #define ncSBL_CONTROL 2U
 #define ncSAVE 341U
 #define ncS_START_IV4 44U
 #define ncS_START_IV3 43U
 #define ncS_START_IV2 42U
 #define ncS_START_IV1 41U
 #define ncS_START 10U
 #define ncS_SET_COMP 16U
 #define ncS_SET 10U
 #define ncS_REST 4096U
 #define ncS_NCPROG 21U
 #define ncS_NCBLOCK_TOT 24U
 #define ncS_NCBLOCK_N1 25U
 #define ncS_NCBLOCK 23U
 #define ncS_MOTOR 1U
 #define ncS_JUMP_T 8U
 #define ncS_ACT_TO_S_SET 279U
 #define ncS_ACT 11U
 #define ncROTARY 32U
 #define ncRING_STARTIDX 4096U
 #define ncRIGHT 3U
 #define ncRESTORE_POS 8U
 #define ncRESTART 273U
 #define ncRESOLVER 5U
 #define ncRESET 320U
 #define ncREPLACE 1U
 #define ncRELEASE 387U
 #define ncRELATIVE 1U
 #define ncREL_POS 119U
 #define ncREL_MOVE 131U
 #define ncRECORD 202U
 #define ncREAD_COB 321U
 #define ncREAD 265U
 #define ncRAM 1U
 #define ncR_PULSE 2U
 #define ncR_PARTAB 210U
 #define ncR_PARAM 211U
 #define ncR_PAR 23U
 #define ncQUICKSTOP_T_JOLT 2U
 #define ncQUICKSTOP 2U
 #define ncQUADRATIC_NO_OVERSHOOT 4U
 #define ncQUADRATIC 2U
 #define ncPUSHPULL 0U
 #define ncPUSH 1U
 #define ncPULL 2U
 #define ncPROGRAM 201U
 #define ncPRELOAD 4U
 #define ncPOWERLINK_IF 1U
 #define ncPOSMON 216U
 #define ncPOSITIVE 0U
 #define ncPOSITION 1U
 #define ncPOS_THRESH 1U
 #define ncPOS_MOVE 134U
 #define ncPOS_ERR 4U
 #define ncPOLAR_RAD 4U
 #define ncPOLAR_PHI 8U
 #define ncPN_EDGE 10U
 #define ncPLC_ITR 302U
 #define ncPI_PRED 0U
 #define ncPATHDISTANCE 0U
 #define ncPATH 386U
 #define ncPASSIVE 4U
 #define ncPARID_TRACE 10U
 #define ncPAR_TYP_VOID_NO_NET_TRACE 65534U
 #define ncPAR_TYP_VOID 65535U
 #define ncPAR_TYP_USINT 5U
 #define ncPAR_TYP_UINT 6U
 #define ncPAR_TYP_UDINT 7U
 #define ncPAR_TYP_T5 9U
 #define ncPAR_TYP_STR32 8202U
 #define ncPAR_TYP_STR16 4106U
 #define ncPAR_TYP_SINT 2U
 #define ncPAR_TYP_REAL 8U
 #define ncPAR_TYP_NIL 0U
 #define ncPAR_TYP_LREAL 17U
 #define ncPAR_TYP_INT 3U
 #define ncPAR_TYP_GRP 12U
 #define ncPAR_TYP_DINT 4U
 #define ncPAR_TYP_DATA 13U
 #define ncPAR_TYP_BYTES 11U
 #define ncPAR_TYP_BRMOD 14U
 #define ncPAR_TYP_BOOL 1U
 #define ncPAR_SEQU 400U
 #define ncPAR_LIST_MOVE 16384U
 #define ncPAR_LIST 402U
 #define ncPAR_ID4 19U
 #define ncPAR_ID3 18U
 #define ncPAR_ID2 17U
 #define ncPAR_ID1 16U
 #define ncPAR_ID 16U
 #define ncPACSI 1U
 #define ncP_THRESH 3U
 #define ncP_LATCH2 2U
 #define ncP_LATCH1 1U
 #define ncP_EDGE 0U
 #define ncOUT_WINDOW 30U
 #define ncOPEN 0U
 #define ncONTHEFLY 3U
 #define ncONLYCOMP_DIRECT 35U
 #define ncONLYCOMP 30U
 #define ncONL_V 113U
 #define ncONL_POS 107U
 #define ncON 1U
 #define ncOK 0U
 #define ncOFF 0U
 #define ncODD 2U
 #define ncOBJ_PTR 64U
 #define ncNP_EDGE 11U
 #define ncNOTCH 2U
 #define ncNOSTOP 16U
 #define ncNOFEED 64U
 #define ncNO_NET_TRACE 32768U
 #define ncNO_CHECK 30U
 #define ncNETWORK 403U
 #define ncNET_TRACE 404U
 #define ncNET_GLOBAL 12U
 #define ncNEGATIVE 1U
 #define ncNEG_THRESH 2U
 #define ncNEG_MOVE 133U
 #define ncNCRECNO 22U
 #define ncNCPR_POS 218U
 #define ncNCGLOBAL 384U
 #define ncNCBLOCKNO 22U
 #define ncNC_SYS_RESTART 32768U
 #define ncN_THRESH 4U
 #define ncN_PERIOD 1U
 #define ncN_EDGE 1U
 #define ncMULTI_AX_TRACE 11U
 #define ncMTC 305U
 #define ncMP_LOG 221U
 #define ncMOVE_END 2U
 #define ncMOVE_CMD 5U
 #define ncMOVE_BEG 1U
 #define ncMOVE 3U
 #define ncMOTPH_STEPPER 31U
 #define ncMOTPH_SET_OFFSET 34U
 #define ncMOTPH_SATURATION 30U
 #define ncMOTPH_DITHER2 35U
 #define ncMOTPH_DITHER 32U
 #define ncMOTOR_SYNCHRON 142U
 #define ncMOTOR_PHASING 143U
 #define ncMOTOR_PAR 1U
 #define ncMOTOR_INDUCTION 141U
 #define ncMOTOR 140U
 #define ncMODULE 3U
 #define ncMODEL_2MASS 3U
 #define ncMODEL_1MASS 4U
 #define ncMOD_SYNC 303U
 #define ncMOD_DIR 128U
 #define ncMM 0U
 #define ncMESSAGE 1U
 #define ncMEMCARD 4U
 #define ncMC_STATE_SYNCHRONIZED_MOTION 8U
 #define ncMC_STATE_STOPPING 5U
 #define ncMC_STATE_STANDSTILL 2U
 #define ncMC_STATE_NET_INIT 0U
 #define ncMC_STATE_MOTION 9U
 #define ncMC_STATE_HOMING 3U
 #define ncMC_STATE_GroupStopping 5U
 #define ncMC_STATE_GroupStandby 4U
 #define ncMC_STATE_GroupMoving 1U
 #define ncMC_STATE_GroupHoming 2U
 #define ncMC_STATE_GroupErrorstop 3U
 #define ncMC_STATE_GroupDisabled 6U
 #define ncMC_STATE_ERRORSTOP 4U
 #define ncMC_STATE_ERROR 10U
 #define ncMC_STATE_DISCRETE_MOTION 6U
 #define ncMC_STATE_DISABLED 1U
 #define ncMC_STATE_CONTINUOUS_MOTION 7U
 #define ncMAINPROG (-1)
 #define ncMAGNESCALE 12U
 #define ncMA_V_COMP 32768U
 #define ncMA_TO_SL 16384U
 #define ncMA_SL_ABS 40U
 #define ncMA_S_START_I32 2048U
 #define ncMA_LATCHPOS 32U
 #define ncMA_IV_SL_ABS 41U
 #define ncM1_STOP 203U
 #define ncM_GRP_TAB 126U
 #define ncLOW_PASS 1U
 #define ncLOW 0U
 #define ncLOAD_ABORT 278U
 #define ncLOAD 276U
 #define ncLINMOT 11U
 #define ncLINK 343U
 #define ncLINENUMBER 4U
 #define ncLINEAR2 3U
 #define ncLINEAR 1U
 #define ncLINE 372U
 #define ncLIMITS 2U
 #define ncLIMITER 114U
 #define ncLEFT 2U
 #define ncLATCHPOS 32U
 #define ncLATCH2 109U
 #define ncLATCH1 108U
 #define ncLAG_ERR 2U
 #define ncISQR_REF_SYSTEM_FLUX 1U
 #define ncISQR_REF_SYSTEM_ENCODER 0U
 #define ncISQR_MODE_A_PHI 20U
 #define ncISQF_TRQ_ADDLIM 8U
 #define ncISQF_LIM3 4U
 #define ncISQF_LIM2 7U
 #define ncISQF_LIM 5U
 #define ncISQF_COMP 6U
 #define ncISQ_RIPPLE 144U
 #define ncISQ_F3_NOTCH 512U
 #define ncISQ_F3_LOW_PASS 4096U
 #define ncISQ_F2_NOTCH 256U
 #define ncISQ_F2_LOW_PASS 2048U
 #define ncISQ_F1_NOTCH 128U
 #define ncISQ_F1_LOW_PASS 1024U
 #define ncIPGLOBAL 385U
 #define ncIP_INFO_AS_WARNING 222U
 #define ncINVERSE 255U
 #define ncINTERPRETER 41U
 #define ncINIT_SET_POS 6U
 #define ncINIT 512U
 #define ncINFO 268U
 #define ncINDUCTION 40U
 #define ncINDRAMAT 0U
 #define ncINDIRECT 255U
 #define ncINCLUDE 2U
 #define ncINCH 1U
 #define ncINC_SSI 10U
 #define ncINC_OUTPUT 7U
 #define ncINC_COMP 252U
 #define ncINC 2U
 #define ncIN_WINDOW 20U
 #define ncIDENTIFICATION 10U
 #define ncI_LIMIT 30U
 #define ncHW_END 4096U
 #define ncHORIZONTAL 0U
 #define ncHOMING 106U
 #define ncHOME_OFFSET_INTERNAL 11U
 #define ncHOME_OFFSET 5U
 #define ncHIPERFACE_DSL 13U
 #define ncHIPERFACE 8U
 #define ncHIGH 1U
 #define ncHALT_SST 1U
 #define ncHALT_RST 16U
 #define ncHALT_PRG 2U
 #define ncHALT_POS 8U
 #define ncHALT_PLC 4U
 #define ncHALT_OK 135U
 #define ncHALT_EXEC_ERR 64U
 #define ncHALT_ERR 32U
 #define ncHALT 219U
 #define ncGRAY 0U
 #define ncGO_HOME 106U
 #define ncglobal_action_NCDA_WRITE 3U
 #define ncglobal_action_NCDA_INFO 2U
 #define ncglobal_action_NCDA_DIR 4U
 #define ncglobal_action_NCDA_CREATE 1U
 #define ncglobal_action_ACP10MSG_TEXT 5U
 #define ncGLOBAL 4U
 #define ncGETINFO 376U
 #define ncGERMAN 0U
 #define ncGEARSABS 124U
 #define ncGEARS_V 116U
 #define ncGEARS 111U
 #define ncGATE 1U
 #define ncGANTRY 1U
 #define ncG03 3U
 #define ncG02 2U
 #define ncG01 1U
 #define ncG00 0U
 #define ncFORMAT_T14 3U
 #define ncFORMAT_T10 1U
 #define ncFORMAT_B06 2U
 #define ncFORMAT_ADR 0U
 #define ncFORCE 288U
 #define ncFIXRAM 5U
 #define ncFINISH 282U
 #define ncFILEOFFSET 0U
 #define ncFILE_XL 1U
 #define ncFILE 3U
 #define ncFF_POS_MOVE 33U
 #define ncFF_NEG_MOVE 34U
 #define ncFF 32U
 #define ncFC 1U
 #define ncFALSE 0U
 #define ncEXTERN 128U
 #define ncEXTENCOD 8U
 #define ncEXPRESSION 375U
 #define ncEXECUTE 374U
 #define ncEX_PARAM 214U
 #define ncEVENT 136U
 #define ncEVEN 3U
 #define ncETEL 2U
 #define ncERROR 1U
 #define ncERR_CL0 215U
 #define ncERR_A2 60U
 #define ncEPROM 2U
 #define ncENTRY 4U
 #define ncENGLISH 1U
 #define ncENDAT3 16U
 #define ncENDAT_SafeMOTION 14U
 #define ncENDAT 4U
 #define ncEND_SWITCH 4U
 #define ncENCODER_IF 103U
 #define ncENCOD_IF 103U
 #define ncENABLE 170U
 #define ncEMPTY 0U
 #define ncEDGE2 12U
 #define ncE_STOP 262U
 #define ncDV_STOP_INIT 1U
 #define ncDV_STOP_AUTO2 3U
 #define ncDV_STOP_AUTO1 2U
 #define ncDRIVE_READY 255U
 #define ncDRIVE_IF 104U
 #define ncDRIVE_ID 123U
 #define ncDRIVE 166U
 #define ncDRAM 65U
 #define ncDPR_TRACE 306U
 #define ncDPR_OVR 217U
 #define ncDOWNLOAD 339U
 #define ncDNC 2U
 #define ncDM16BIT 8192U
 #define ncDIRECT 0U
 #define ncDIG_IN 102U
 #define ncDIAGNOSE 321U
 #define ncDELETE 342U
 #define ncDEFINE 369U
 #define ncDECODER 206U
 #define ncDECEL 4U
 #define ncDCM 7U
 #define ncDATOBJ_FORMAT_TXT 2U
 #define ncDATOBJ_FORMAT_CSV 1U
 #define ncDATOBJ_FORMAT_BIN 0U
 #define ncDATOBJ_FILE 1U
 #define ncDATOBJ_BRMOD_DEFAULT 65535U
 #define ncDATOBJ_BRMOD 0U
 #define ncDATMOD_ZERO_P_OFF 21U
 #define ncDATMOD_NET_TRACE 30U
 #define ncDATMOD_NC_MAPPING 28U
 #define ncDATMOD_DATBLOCK 33U
 #define ncDATMOD_CNC_TOOL 22U
 #define ncDATMOD_CNC_R_PAR 23U
 #define ncDATMOD_CNC_PROG 20U
 #define ncDATMOD_CNC_CAM_TAB 24U
 #define ncDATMOD_CNC_CAM_POLY 25U
 #define ncDATMOD_ACP_PAR_TRACE 31U
 #define ncDATMOD_ACP_PAR 16U
 #define ncDATMOD_ACP_CAM_POLY 27U
 #define ncDATBLOCK 162U
 #define ncDATA_TEXT 1024U
 #define ncDATA 0U
 #define ncDAT_MOD 301U
 #define ncD_SINGLE 207U
 #define ncD_POS 13U
 #define ncCYCLIC 8U
 #define ncCYCL_USER_TODRV_AT_STARTUP 258U
 #define ncCYCL_USER_TODRV 256U
 #define ncCYCL_USER_FRDRV_AT_STARTUP 259U
 #define ncCYCL_USER_FRDRV 257U
 #define ncCTRL_OFF 50U
 #define ncCSTRF 1U
 #define ncCOUPLING 274U
 #define ncCOUNT 11U
 #define ncCORRECTION 128U
 #define ncCONTROLLER 105U
 #define ncCONTROL 105U
 #define ncCONTINUE_ 263U
 #define ncCONTINUE 263U
 #define ncCOMPAR 115U
 #define ncCOMP_ERR 14U
 #define ncCOMP 125U
 #define ncCNCSYS 2U
 #define ncCNC_PROG 20U
 #define ncCNC_PLC 212U
 #define ncCNC_C_AX 199U
 #define ncCNC 0U
 #define ncCMD_WARNING_ONLY 0U
 #define ncCMD_ERROR_V_STOP_CTRL_OFF 4U
 #define ncCMD_ERROR_TRQLIM_T_JOLT_STOP 13U
 #define ncCMD_ERROR_TRQLIM_STOP 12U
 #define ncCMD_ERROR_STOP_CTRL_OFF 3U
 #define ncCMD_ERROR_STOP 2U
 #define ncCMD_ERROR_ONLY 1U
 #define ncCMD_ERROR_INDUCTION_HALT 6U
 #define ncCMD_ERROR_COAST_TO_STANDSTILL 5U
 #define ncCMD_ERROR_A2_V_STOP_CTRL_OFF 9U
 #define ncCMD_ERROR_A2_STOP_CTRL_OFF 8U
 #define ncCMD_ERROR_A2_STOP 7U
 #define ncCMD_ERROR 281U
 #define ncCLOSED 1U
 #define ncCAN_IF 0U
 #define ncCAMPRPOL_ACOPOS 27U
 #define ncCAMPRPOL 25U
 #define ncCAMPRDAT 24U
 #define ncCAM_PROF 117U
 #define ncCAM_BEG 6U
 #define ncCALCULATION 11U
 #define ncBYTEOFFSET 3U
 #define ncBURN 340U
 #define ncBREAKPOINT 370U
 #define ncBREAK 2U
 #define ncBRAKE 171U
 #define ncBLOCKSEARCH 277U
 #define ncBLOCKNUMBER 1U
 #define ncBLOCKMONITOR 4U
 #define ncBLOCKMON 371U
 #define ncBLOCK_TORQUE 9U
 #define ncBLOCK_DS 10U
 #define ncBLOCK 202U
 #define ncBL 1U
 #define ncBISS 9U
 #define ncBIQUAD 9U
 #define ncBINARY 1U
 #define ncBIDIR 4U
 #define ncBELOW_WINDOW 50U
 #define ncBASIS_TRG_STOP 137U
 #define ncBASIS_MOVE 130U
 #define ncBASIS 1U
 #define ncAXIS 1U
 #define ncAXES 213U
 #define ncAUTOSAVE 64U
 #define ncAUTOMAT 122U
 #define ncAUTO 1U
 #define ncAUT_END 10U
 #define ncAT_ONCE 0U
 #define ncARNC0MAN 36864U
 #define ncAND_N2E 15U
 #define ncANALOG 0U
 #define ncALL 373U
 #define ncAIL_DUMP 220U
 #define ncADD_DATE_TIME 1U
 #define ncACTIVE 1U
 #define ncACTIV_LO 0U
 #define ncACTIV_HI 1U
 #define ncACT_POS 120U
 #define ncACP10USCOB 255U
 #define ncACP10MAN 32768U
 #define ncACP_TYP_SIM 129U
 #define ncACP_TYP_SDC 128U
 #define ncACP_TYP_PS 0U
 #define ncACP_TYP_PPS 2U
 #define ncACP_TYP_INV 1U
 #define ncACP_SIM_STANDARD 1U
 #define ncACP_SIM_COMPLETE 2U
 #define ncACP_PAR_SEND 352U
 #define ncACP_PAR_RECEIVE 353U
 #define ncACP_PAR_INIT_BRC_DP64 354U
 #define ncACP_PAR_INIT_BRC_DP 355U
 #define ncACP_PAR 401U
 #define ncACOPOSremote 8U
 #define ncACOPOSmulti65m 4U
 #define ncACOPOSmulti65 8U
 #define ncACOPOSmulti3 9U
 #define ncACOPOSmulti_PPS 6U
 #define ncACOPOSmulti 5U
 #define ncACOPOSmotor_C 18U
 #define ncACOPOSmotor 4U
 #define ncACOPOSmicro 7U
 #define ncACOPOS_SIM 129U
 #define ncACOPOS_SDC 128U
 #define ncACOPOS_P3 12U
 #define ncACOPOS_INFO 322U
 #define ncACOPOS_2 1U
 #define ncACOPOS_1 0U
 #define ncACKNOWLEDGE 257U
 #define ncACK 257U
 #define ncACCEL 1U
 #define ncABSOLUTE 0U
 #define ncABS_SWITCH 2U
 #define ncABS_MOVE 132U
 #define ncABS 1U
 #define ncABOVE_WINDOW 40U
 #define ncABORT_LINE 4U
 #define ncABORT_DATA 8U
 #define ncA_MOVE 10U
 #define ncA_LIMIT 20U
 #define nc2ENCOD_SPEED 5U
 #define nc20KHZ 0U
 #define nc158CAN 7U
 #define nc157CAN 9U
 #define nc156CAN 6U
 #define nc154CAN 5U
 #define nc100KHZ 1U
 #define MOD_UPDATE 32768U
 #define MC_InitFunction 1U
 #define IO_2010 1024U
 #define IO_2005 1152U
 #define FB_MC_WriteParameter 53U
 #define FB_MC_WriteDigitalOutput 52U
 #define FB_MC_WriteBoolParameter 51U
 #define FB_MC_TouchProbe 50U
 #define FB_MC_TorqueControl 96U
 #define FB_MC_Stop 49U
 #define FB_MC_SetOverride 48U
 #define FB_MC_Reset 47U
 #define FB_MC_ReadStatus 46U
 #define FB_MC_ReadParameter 45U
 #define FB_MC_ReadDigitalOutput 44U
 #define FB_MC_ReadDigitalInput 43U
 #define FB_MC_ReadBoolParameter 42U
 #define FB_MC_ReadAxisError 41U
 #define FB_MC_ReadActualVelocity 40U
 #define FB_MC_ReadActualTorque 38U
 #define FB_MC_ReadActualPosition 39U
 #define FB_MC_Power 37U
 #define FB_MC_Phasing 36U
 #define FB_MC_MoveVelocity 35U
 #define FB_MC_MoveRelative 34U
 #define FB_MC_MoveAdditive 33U
 #define FB_MC_MoveAbsolute 32U
 #define FB_MC_LimitLoad 133U
 #define FB_MC_Home 31U
 #define FB_MC_Halt 30U
 #define FB_MC_GearOut 29U
 #define FB_MC_GearInPos 28U
 #define FB_MC_GearIn 27U
 #define FB_MC_DigitalCamSwitch 26U
 #define FB_MC_CamTableSelect 25U
 #define FB_MC_CamOut 24U
 #define FB_MC_CamIn 23U
 #define FB_MC_BR_WriteParIDText 91U
 #define FB_MC_BR_WriteParID 22U
 #define FB_MC_BR_WriteLoadSimTwoEncPos 149U
 #define FB_MC_BR_WriteLoadSimTorque 144U
 #define FB_MC_BR_WriteLoadSimPosition 143U
 #define FB_MC_BR_WriteLoadSimOutputData 132U
 #define FB_MC_BR_VelocityControl 95U
 #define FB_MC_BR_TouchProbe 60U
 #define FB_MC_BR_TorqueControl 100U
 #define FB_MC_BR_Simulation 71U
 #define FB_MC_BR_SetupSynchronMotor 129U
 #define FB_MC_BR_SetupMotorPhasing 97U
 #define FB_MC_BR_SetupIsqRipple 101U
 #define FB_MC_BR_SetupInductionMotor 87U
 #define FB_MC_BR_SetupFromParTabObj 145U
 #define FB_MC_BR_SetupController 88U
 #define FB_MC_BR_SetHardwareInputs 108U
 #define FB_MC_BR_SaveCamProfileObj 116U
 #define FB_MC_BR_SaveAxisPar 55U
 #define FB_MC_BR_ResetAutPar 136U
 #define FB_MC_BR_RegMarkCapture002 117U
 #define FB_MC_BR_RegMarkCapture001 66U
 #define FB_MC_BR_RegMarkCalc001 67U
 #define FB_MC_BR_ReceiveParIDOnPLC 113U
 #define FB_MC_BR_ReadParTraceStatus 81U
 #define FB_MC_BR_ReadParList 148U
 #define FB_MC_BR_ReadParIDText 90U
 #define FB_MC_BR_ReadParID 21U
 #define FB_MC_BR_ReadNetTraceStatus 79U
 #define FB_MC_BR_ReadLoadSimTorque 142U
 #define FB_MC_BR_ReadLoadSimInputData 131U
 #define FB_MC_BR_ReadDriveStatus 72U
 #define FB_MC_BR_ReadCyclicPosition 83U
 #define FB_MC_BR_ReadAxisError 105U
 #define FB_MC_BR_ReadAutPosition 75U
 #define FB_MC_BR_PowerMeter 89U
 #define FB_MC_BR_Phasing 59U
 #define FB_MC_BR_ParTraceConfig 102U
 #define FB_MC_BR_ParTrace 80U
 #define FB_MC_BR_OffsetZone 128U
 #define FB_MC_BR_OffsetVelocity 127U
 #define FB_MC_BR_Offset 58U
 #define FB_MC_BR_NetworkInit 139U
 #define FB_MC_BR_NetTrace 78U
 #define FB_MC_BR_MoveVelocityTriggStop 20U
 #define FB_MC_BR_MoveCyclicVelocityExt 125U
 #define FB_MC_BR_MoveCyclicVelocity 92U
 #define FB_MC_BR_MoveCyclicPositionExt 124U
 #define FB_MC_BR_MoveCyclicPosition 84U
 #define FB_MC_BR_MoveAdditiveTriggStop 19U
 #define FB_MC_BR_MoveAbsoluteTriggStop 18U
 #define FB_MC_BR_MechPosDeviationComp 147U
 #define FB_MC_BR_LoadAxisPar 56U
 #define FB_MC_BR_LimitLoadCam 135U
 #define FB_MC_BR_LimitLoad 134U
 #define FB_MC_BR_JogVelocity 118U
 #define FB_MC_BR_JogTargetPosition 120U
 #define FB_MC_BR_JogLimitPosition 119U
 #define FB_MC_BR_InitSendParID 111U
 #define FB_MC_BR_InitReceiveParID 112U
 #define FB_MC_BR_InitReceiveNetworkEnc 141U
 #define FB_MC_BR_InitReceiveNetworkData 115U
 #define FB_MC_BR_InitParTabObj 17U
 #define FB_MC_BR_InitParSequ 16U
 #define FB_MC_BR_InitParList 15U
 #define FB_MC_BR_InitModPos 14U
 #define FB_MC_BR_InitMasterParIDTransfer 13U
 #define FB_MC_BR_InitEndlessPosition 82U
 #define FB_MC_BR_InitEndlessPosAcpEnc 138U
 #define FB_MC_BR_InitCyclicWrite 12U
 #define FB_MC_BR_InitCyclicRead 11U
 #define FB_MC_BR_InitAxisSubjectPar 57U
 #define FB_MC_BR_InitAxisPar 54U
 #define FB_MC_BR_InitAutState 10U
 #define FB_MC_BR_InitAutPar 9U
 #define FB_MC_BR_InitAutEvent 8U
 #define FB_MC_BR_InitAutData 76U
 #define FB_MC_BR_HomeAcpEncoder 68U
 #define FB_MC_BR_GetParIDTransferInfo 121U
 #define FB_MC_BR_GetParIDInfo 107U
 #define FB_MC_BR_GetHardwareInfo 109U
 #define FB_MC_BR_GetErrorText 77U
 #define FB_MC_BR_GetCamSlavePosition 85U
 #define FB_MC_BR_GetCamMasterPosition 86U
 #define FB_MC_BR_GearIn 126U
 #define FB_MC_BR_EventMoveVelocity 63U
 #define FB_MC_BR_EventMoveAdditive 62U
 #define FB_MC_BR_EventMoveAbsolute 61U
 #define FB_MC_BR_DownloadParSequ 7U
 #define FB_MC_BR_DownloadCamProfileObj 6U
 #define FB_MC_BR_DownloadCamProfileData 5U
 #define FB_MC_BR_DigitalCamSwitch 106U
 #define FB_MC_BR_CyclicWrite 70U
 #define FB_MC_BR_CyclicReadDataInfo 98U
 #define FB_MC_BR_CyclicRead 69U
 #define FB_MC_BR_CrossCutterControl 114U
 #define FB_MC_BR_CreateCamProfileObj 74U
 #define FB_MC_BR_ConfigPowerStageCheck 137U
 #define FB_MC_BR_CommandError 140U
 #define FB_MC_BR_CheckEndlessPosition 130U
 #define FB_MC_BR_CheckAutCompensation 103U
 #define FB_MC_BR_CamTransition 94U
 #define FB_MC_BR_CamIn 146U
 #define FB_MC_BR_CamDwell 64U
 #define FB_MC_BR_CalcSectionsFromCam 122U
 #define FB_MC_BR_CalcPointsFromCam 123U
 #define FB_MC_BR_CalcCamFromSections 73U
 #define FB_MC_BR_CalcCamFromPoints 93U
 #define FB_MC_BR_BrakeOperation 4U
 #define FB_MC_BR_BrakeControl 110U
 #define FB_MC_BR_AxisErrorCollector 104U
 #define FB_MC_BR_AutoCamDwell 65U
 #define FB_MC_BR_AutControl 3U
 #define FB_MC_BR_AutCommand 99U
 #define FB_MC_AbortTrigger 2U
 #define FAST_BOOT 16384U
 #define BASIS2005 1U
#else
 #ifndef _GLOBAL_CONST
   #define _GLOBAL_CONST _WEAK const
 #endif
 _GLOBAL_CONST unsigned long SafeMC_action_READ_SAFEOUT_DATA3;
 _GLOBAL_CONST unsigned long SafeMC_action_READ_SAFEOUT_DATA2;
 _GLOBAL_CONST unsigned long SafeMC_action_READ_SAFEOUT_DATA;
 _GLOBAL_CONST unsigned long SafeMC_action_READ_SAFEIN_DATA3;
 _GLOBAL_CONST unsigned long SafeMC_action_READ_SAFEIN_DATA2;
 _GLOBAL_CONST unsigned long SafeMC_action_READ_SAFEIN_DATA;
 _GLOBAL_CONST unsigned long SafeMC_action_GET_CFG_PTR;
 _GLOBAL_CONST unsigned short RIO4_2005;
 _GLOBAL_CONST unsigned short RIO3_2005;
 _GLOBAL_CONST unsigned short RIO2_2005;
 _GLOBAL_CONST unsigned short RIO1_2005;
 _GLOBAL_CONST unsigned char ncZX;
 _GLOBAL_CONST unsigned short ncZEROPMON;
 _GLOBAL_CONST unsigned short ncZERO_TAB;
 _GLOBAL_CONST unsigned char ncZERO_DAT;
 _GLOBAL_CONST unsigned short ncZERO;
 _GLOBAL_CONST unsigned short ncZ_TRANS;
 _GLOBAL_CONST unsigned char ncYZ;
 _GLOBAL_CONST unsigned char ncXY;
 _GLOBAL_CONST unsigned short ncWRITE_HPRIO;
 _GLOBAL_CONST unsigned short ncWRITE_COB;
 _GLOBAL_CONST unsigned short ncWITHOUT_INDEX;
 _GLOBAL_CONST unsigned short ncWITH_INDEX;
 _GLOBAL_CONST unsigned char ncWITH_CAM;
 _GLOBAL_CONST unsigned char ncWINDOW;
 _GLOBAL_CONST unsigned short ncVIRTUAL_IF;
 _GLOBAL_CONST unsigned char ncVERTICAL;
 _GLOBAL_CONST unsigned short ncVARIABLE;
 _GLOBAL_CONST unsigned char ncV_TRAJ;
 _GLOBAL_CONST unsigned char ncV_STOP;
 _GLOBAL_CONST unsigned char ncV_SET_COMP;
 _GLOBAL_CONST unsigned char ncV_SET;
 _GLOBAL_CONST unsigned char ncV_JUMP_T;
 _GLOBAL_CONST unsigned char ncV_JUMP;
 _GLOBAL_CONST unsigned char ncV_CONST;
 _GLOBAL_CONST unsigned char ncV_COMP_S_SL;
 _GLOBAL_CONST unsigned char ncV_COMP_S_MA;
 _GLOBAL_CONST unsigned char ncV_COMP_A_SL;
 _GLOBAL_CONST unsigned char ncV_COMP_A_CYC;
 _GLOBAL_CONST unsigned short ncV_AXIS;
 _GLOBAL_CONST unsigned char ncV_ACT;
 _GLOBAL_CONST unsigned char ncUSERROM;
 _GLOBAL_CONST unsigned char ncUSER;
 _GLOBAL_CONST unsigned short ncUSE_TN;
 _GLOBAL_CONST unsigned short ncUSE_FILTER_PAR;
 _GLOBAL_CONST unsigned short ncUPLOAD;
 _GLOBAL_CONST unsigned short ncUNLINK;
 _GLOBAL_CONST unsigned char ncUF;
 _GLOBAL_CONST unsigned char ncU_SET;
 _GLOBAL_CONST unsigned char ncU_LIMIT;
 _GLOBAL_CONST unsigned char ncTUNE_V_CONSTANT;
 _GLOBAL_CONST unsigned short ncTUNE_TN;
 _GLOBAL_CONST unsigned char ncTUNE_STANDSTILL;
 _GLOBAL_CONST unsigned short ncTUNE_MODEL_FRICTION;
 _GLOBAL_CONST unsigned short ncTUNE_MODEL_2MASS;
 _GLOBAL_CONST unsigned short ncTUNE_FBCTRL_MODEL_2MASS;
 _GLOBAL_CONST unsigned short ncTUNE_FBCTRL_MODEL_1MASS;
 _GLOBAL_CONST unsigned char ncTRUE;
 _GLOBAL_CONST unsigned char ncTRQ_LIMIT;
 _GLOBAL_CONST unsigned short ncTRIGGPOS;
 _GLOBAL_CONST unsigned char ncTRIGGER8;
 _GLOBAL_CONST unsigned char ncTRIGGER7;
 _GLOBAL_CONST unsigned char ncTRIGGER6;
 _GLOBAL_CONST unsigned char ncTRIGGER5;
 _GLOBAL_CONST unsigned char ncTRIGGER4;
 _GLOBAL_CONST unsigned char ncTRIGGER3;
 _GLOBAL_CONST unsigned char ncTRIGGER2;
 _GLOBAL_CONST unsigned char ncTRIGGER1;
 _GLOBAL_CONST unsigned char ncTRIGGER_2;
 _GLOBAL_CONST unsigned char ncTRIGGER;
 _GLOBAL_CONST unsigned short ncTRGPOS_S;
 _GLOBAL_CONST unsigned char ncTRG_STOP_S_REST;
 _GLOBAL_CONST unsigned char ncTRG_STOP_NORMAL;
 _GLOBAL_CONST unsigned short ncTRG_STOP;
 _GLOBAL_CONST unsigned short ncTRACE_PAR_SEC_REC;
 _GLOBAL_CONST unsigned short ncTRACE_DAT_WR;
 _GLOBAL_CONST unsigned short ncTRACE;
 _GLOBAL_CONST unsigned char ncTR_TRIGG;
 _GLOBAL_CONST unsigned char ncTR_TRACE;
 _GLOBAL_CONST unsigned char ncTR_START;
 _GLOBAL_CONST unsigned char ncTR_SDM;
 _GLOBAL_CONST unsigned char ncTR_SAVE;
 _GLOBAL_CONST unsigned char ncTR_RING;
 _GLOBAL_CONST unsigned char ncTR_REST;
 _GLOBAL_CONST unsigned char ncTR_END;
 _GLOBAL_CONST unsigned char ncTR_DELAY;
 _GLOBAL_CONST unsigned char ncTOOLDAT;
 _GLOBAL_CONST unsigned short ncTOOL_TAB;
 _GLOBAL_CONST unsigned char ncTOOL;
 _GLOBAL_CONST unsigned char ncTHRESHLD;
 _GLOBAL_CONST unsigned short ncTEXT;
 _GLOBAL_CONST unsigned short ncTEST_SPEED;
 _GLOBAL_CONST unsigned short ncTEST_POSITION;
 _GLOBAL_CONST unsigned short ncTEST;
 _GLOBAL_CONST unsigned char ncTANGENT;
 _GLOBAL_CONST unsigned char ncT_TOTAL;
 _GLOBAL_CONST unsigned char ncT_JOLT;
 _GLOBAL_CONST unsigned char ncT_FORMAT;
 _GLOBAL_CONST unsigned short ncT_FILTER_2;
 _GLOBAL_CONST unsigned short ncT_FILTER;
 _GLOBAL_CONST unsigned char ncSYSROM;
 _GLOBAL_CONST unsigned short ncSYNC;
 _GLOBAL_CONST unsigned short ncSWITCH_ON;
 _GLOBAL_CONST unsigned short ncSWITCH_OFF;
 _GLOBAL_CONST unsigned char ncSWITCH_GATE;
 _GLOBAL_CONST unsigned char ncSWITCH;
 _GLOBAL_CONST unsigned short ncSW_ON;
 _GLOBAL_CONST unsigned short ncSW_OFF;
 _GLOBAL_CONST unsigned char ncSW_END;
 _GLOBAL_CONST unsigned char ncSTOP_HOMING;
 _GLOBAL_CONST unsigned short ncSTOP;
 _GLOBAL_CONST unsigned char ncSTEP_OVER;
 _GLOBAL_CONST unsigned char ncSTEP_INTO;
 _GLOBAL_CONST unsigned char ncSTATE;
 _GLOBAL_CONST unsigned short ncSTARTDIR;
 _GLOBAL_CONST unsigned short ncSTARTABS;
 _GLOBAL_CONST unsigned short ncSTART_T;
 _GLOBAL_CONST unsigned short ncSTART_NETWORK_REQU_PARCMD;
 _GLOBAL_CONST unsigned short ncSTART_IV;
 _GLOBAL_CONST unsigned short ncSTART_CYC_TRACE_CTRL_BITS;
 _GLOBAL_CONST unsigned short ncSTART_CG;
 _GLOBAL_CONST unsigned short ncSTART;
 _GLOBAL_CONST unsigned char ncSTANDARD;
 _GLOBAL_CONST unsigned char ncST_END;
 _GLOBAL_CONST unsigned char ncST_COMP;
 _GLOBAL_CONST unsigned char ncST_CAMPR;
 _GLOBAL_CONST unsigned char ncSSI_SEND;
 _GLOBAL_CONST unsigned char ncSSI_PARITY_CHK_ODD;
 _GLOBAL_CONST unsigned char ncSSI_PARITY_CHK_EVEN;
 _GLOBAL_CONST unsigned char ncSSI_CONT_TYP_WRN_INV;
 _GLOBAL_CONST unsigned char ncSSI_CONT_TYP_WRN;
 _GLOBAL_CONST unsigned char ncSSI_CONT_TYP_POS;
 _GLOBAL_CONST unsigned char ncSSI_CONT_TYP_FILL;
 _GLOBAL_CONST unsigned char ncSSI_CONT_TYP_ERR_INV;
 _GLOBAL_CONST unsigned char ncSSI_CONT_TYP_ERR;
 _GLOBAL_CONST unsigned char ncSSI_CONT_TYP_END;
 _GLOBAL_CONST unsigned char ncSSI;
 _GLOBAL_CONST unsigned char ncSSE;
 _GLOBAL_CONST unsigned short ncSPOSSTDZ;
 _GLOBAL_CONST unsigned char ncSPEED;
 _GLOBAL_CONST unsigned char ncSL_LATCHPOS;
 _GLOBAL_CONST unsigned char ncSL_ABS;
 _GLOBAL_CONST unsigned char ncSKIP_PARSE;
 _GLOBAL_CONST unsigned short ncSKIP_FCN;
 _GLOBAL_CONST unsigned short ncSINGLE;
 _GLOBAL_CONST unsigned short ncSIMULATION;
 _GLOBAL_CONST unsigned short ncSIMULAT;
 _GLOBAL_CONST unsigned char ncSIM_START;
 _GLOBAL_CONST unsigned short ncSIM_2MASS_GEAR;
 _GLOBAL_CONST unsigned short ncSIM_2MASS;
 _GLOBAL_CONST unsigned short ncSIM_1MASS_GEAR;
 _GLOBAL_CONST unsigned short ncSIM_1MASS_AUTO;
 _GLOBAL_CONST unsigned short ncSIM_1MASS;
 _GLOBAL_CONST unsigned char ncSIGNAL4;
 _GLOBAL_CONST unsigned char ncSIGNAL3;
 _GLOBAL_CONST unsigned char ncSIGNAL2;
 _GLOBAL_CONST unsigned char ncSIGNAL1;
 _GLOBAL_CONST unsigned short ncSIGNAL_PRBS;
 _GLOBAL_CONST unsigned short ncSIGNAL_CHIRP_TRAPEZOID;
 _GLOBAL_CONST unsigned short ncSIGNAL_CHIRP;
 _GLOBAL_CONST unsigned char ncSIGNAL;
 _GLOBAL_CONST unsigned short ncSIG_LINE;
 _GLOBAL_CONST unsigned char ncSHORT_PATH;
 _GLOBAL_CONST unsigned short ncSETUP_MOVE_T_JOLT;
 _GLOBAL_CONST unsigned short ncSETUP;
 _GLOBAL_CONST unsigned short ncSET_GEN_ONLY;
 _GLOBAL_CONST unsigned short ncSET;
 _GLOBAL_CONST unsigned short ncSERVICE;
 _GLOBAL_CONST unsigned short ncSERCOSIF;
 _GLOBAL_CONST unsigned char ncSERCOS_LIN;
 _GLOBAL_CONST unsigned char ncSERCOS;
 _GLOBAL_CONST unsigned short ncSEND;
 _GLOBAL_CONST unsigned short ncSDC_IF;
 _GLOBAL_CONST unsigned short ncSCALE;
 _GLOBAL_CONST unsigned char ncSBL_CONTROL;
 _GLOBAL_CONST unsigned short ncSAVE;
 _GLOBAL_CONST unsigned char ncS_START_IV4;
 _GLOBAL_CONST unsigned char ncS_START_IV3;
 _GLOBAL_CONST unsigned char ncS_START_IV2;
 _GLOBAL_CONST unsigned char ncS_START_IV1;
 _GLOBAL_CONST unsigned char ncS_START;
 _GLOBAL_CONST unsigned char ncS_SET_COMP;
 _GLOBAL_CONST unsigned char ncS_SET;
 _GLOBAL_CONST unsigned short ncS_REST;
 _GLOBAL_CONST unsigned char ncS_NCPROG;
 _GLOBAL_CONST unsigned char ncS_NCBLOCK_TOT;
 _GLOBAL_CONST unsigned char ncS_NCBLOCK_N1;
 _GLOBAL_CONST unsigned char ncS_NCBLOCK;
 _GLOBAL_CONST unsigned char ncS_MOTOR;
 _GLOBAL_CONST unsigned char ncS_JUMP_T;
 _GLOBAL_CONST unsigned short ncS_ACT_TO_S_SET;
 _GLOBAL_CONST unsigned char ncS_ACT;
 _GLOBAL_CONST unsigned char ncROTARY;
 _GLOBAL_CONST unsigned short ncRING_STARTIDX;
 _GLOBAL_CONST unsigned char ncRIGHT;
 _GLOBAL_CONST unsigned char ncRESTORE_POS;
 _GLOBAL_CONST unsigned short ncRESTART;
 _GLOBAL_CONST unsigned char ncRESOLVER;
 _GLOBAL_CONST unsigned short ncRESET;
 _GLOBAL_CONST unsigned char ncREPLACE;
 _GLOBAL_CONST unsigned short ncRELEASE;
 _GLOBAL_CONST unsigned char ncRELATIVE;
 _GLOBAL_CONST unsigned short ncREL_POS;
 _GLOBAL_CONST unsigned short ncREL_MOVE;
 _GLOBAL_CONST unsigned short ncRECORD;
 _GLOBAL_CONST unsigned short ncREAD_COB;
 _GLOBAL_CONST unsigned short ncREAD;
 _GLOBAL_CONST unsigned char ncRAM;
 _GLOBAL_CONST unsigned char ncR_PULSE;
 _GLOBAL_CONST unsigned short ncR_PARTAB;
 _GLOBAL_CONST unsigned short ncR_PARAM;
 _GLOBAL_CONST unsigned char ncR_PAR;
 _GLOBAL_CONST unsigned char ncQUICKSTOP_T_JOLT;
 _GLOBAL_CONST unsigned char ncQUICKSTOP;
 _GLOBAL_CONST unsigned char ncQUADRATIC_NO_OVERSHOOT;
 _GLOBAL_CONST unsigned char ncQUADRATIC;
 _GLOBAL_CONST unsigned char ncPUSHPULL;
 _GLOBAL_CONST unsigned char ncPUSH;
 _GLOBAL_CONST unsigned char ncPULL;
 _GLOBAL_CONST unsigned short ncPROGRAM;
 _GLOBAL_CONST unsigned char ncPRELOAD;
 _GLOBAL_CONST unsigned short ncPOWERLINK_IF;
 _GLOBAL_CONST unsigned short ncPOSMON;
 _GLOBAL_CONST unsigned char ncPOSITIVE;
 _GLOBAL_CONST unsigned char ncPOSITION;
 _GLOBAL_CONST unsigned char ncPOS_THRESH;
 _GLOBAL_CONST unsigned short ncPOS_MOVE;
 _GLOBAL_CONST unsigned char ncPOS_ERR;
 _GLOBAL_CONST unsigned char ncPOLAR_RAD;
 _GLOBAL_CONST unsigned char ncPOLAR_PHI;
 _GLOBAL_CONST unsigned char ncPN_EDGE;
 _GLOBAL_CONST unsigned short ncPLC_ITR;
 _GLOBAL_CONST unsigned char ncPI_PRED;
 _GLOBAL_CONST unsigned char ncPATHDISTANCE;
 _GLOBAL_CONST unsigned short ncPATH;
 _GLOBAL_CONST unsigned short ncPASSIVE;
 _GLOBAL_CONST unsigned short ncPARID_TRACE;
 _GLOBAL_CONST unsigned short ncPAR_TYP_VOID_NO_NET_TRACE;
 _GLOBAL_CONST unsigned short ncPAR_TYP_VOID;
 _GLOBAL_CONST unsigned short ncPAR_TYP_USINT;
 _GLOBAL_CONST unsigned short ncPAR_TYP_UINT;
 _GLOBAL_CONST unsigned short ncPAR_TYP_UDINT;
 _GLOBAL_CONST unsigned short ncPAR_TYP_T5;
 _GLOBAL_CONST unsigned short ncPAR_TYP_STR32;
 _GLOBAL_CONST unsigned short ncPAR_TYP_STR16;
 _GLOBAL_CONST unsigned short ncPAR_TYP_SINT;
 _GLOBAL_CONST unsigned short ncPAR_TYP_REAL;
 _GLOBAL_CONST unsigned short ncPAR_TYP_NIL;
 _GLOBAL_CONST unsigned short ncPAR_TYP_LREAL;
 _GLOBAL_CONST unsigned short ncPAR_TYP_INT;
 _GLOBAL_CONST unsigned short ncPAR_TYP_GRP;
 _GLOBAL_CONST unsigned short ncPAR_TYP_DINT;
 _GLOBAL_CONST unsigned short ncPAR_TYP_DATA;
 _GLOBAL_CONST unsigned short ncPAR_TYP_BYTES;
 _GLOBAL_CONST unsigned short ncPAR_TYP_BRMOD;
 _GLOBAL_CONST unsigned short ncPAR_TYP_BOOL;
 _GLOBAL_CONST unsigned short ncPAR_SEQU;
 _GLOBAL_CONST unsigned short ncPAR_LIST_MOVE;
 _GLOBAL_CONST unsigned short ncPAR_LIST;
 _GLOBAL_CONST unsigned char ncPAR_ID4;
 _GLOBAL_CONST unsigned char ncPAR_ID3;
 _GLOBAL_CONST unsigned char ncPAR_ID2;
 _GLOBAL_CONST unsigned char ncPAR_ID1;
 _GLOBAL_CONST unsigned char ncPAR_ID;
 _GLOBAL_CONST unsigned char ncPACSI;
 _GLOBAL_CONST unsigned char ncP_THRESH;
 _GLOBAL_CONST unsigned char ncP_LATCH2;
 _GLOBAL_CONST unsigned char ncP_LATCH1;
 _GLOBAL_CONST unsigned char ncP_EDGE;
 _GLOBAL_CONST unsigned char ncOUT_WINDOW;
 _GLOBAL_CONST unsigned char ncOPEN;
 _GLOBAL_CONST unsigned char ncONTHEFLY;
 _GLOBAL_CONST unsigned char ncONLYCOMP_DIRECT;
 _GLOBAL_CONST unsigned char ncONLYCOMP;
 _GLOBAL_CONST unsigned short ncONL_V;
 _GLOBAL_CONST unsigned short ncONL_POS;
 _GLOBAL_CONST unsigned char ncON;
 _GLOBAL_CONST unsigned short ncOK;
 _GLOBAL_CONST unsigned char ncOFF;
 _GLOBAL_CONST unsigned char ncODD;
 _GLOBAL_CONST unsigned short ncOBJ_PTR;
 _GLOBAL_CONST unsigned char ncNP_EDGE;
 _GLOBAL_CONST unsigned short ncNOTCH;
 _GLOBAL_CONST unsigned char ncNOSTOP;
 _GLOBAL_CONST unsigned char ncNOFEED;
 _GLOBAL_CONST unsigned short ncNO_NET_TRACE;
 _GLOBAL_CONST unsigned char ncNO_CHECK;
 _GLOBAL_CONST unsigned short ncNETWORK;
 _GLOBAL_CONST unsigned short ncNET_TRACE;
 _GLOBAL_CONST unsigned short ncNET_GLOBAL;
 _GLOBAL_CONST unsigned char ncNEGATIVE;
 _GLOBAL_CONST unsigned char ncNEG_THRESH;
 _GLOBAL_CONST unsigned short ncNEG_MOVE;
 _GLOBAL_CONST unsigned char ncNCRECNO;
 _GLOBAL_CONST unsigned short ncNCPR_POS;
 _GLOBAL_CONST unsigned short ncNCGLOBAL;
 _GLOBAL_CONST unsigned char ncNCBLOCKNO;
 _GLOBAL_CONST unsigned short ncNC_SYS_RESTART;
 _GLOBAL_CONST unsigned char ncN_THRESH;
 _GLOBAL_CONST unsigned char ncN_PERIOD;
 _GLOBAL_CONST unsigned char ncN_EDGE;
 _GLOBAL_CONST unsigned short ncMULTI_AX_TRACE;
 _GLOBAL_CONST unsigned short ncMTC;
 _GLOBAL_CONST unsigned short ncMP_LOG;
 _GLOBAL_CONST unsigned char ncMOVE_END;
 _GLOBAL_CONST unsigned char ncMOVE_CMD;
 _GLOBAL_CONST unsigned char ncMOVE_BEG;
 _GLOBAL_CONST unsigned short ncMOVE;
 _GLOBAL_CONST unsigned short ncMOTPH_STEPPER;
 _GLOBAL_CONST unsigned short ncMOTPH_SET_OFFSET;
 _GLOBAL_CONST unsigned short ncMOTPH_SATURATION;
 _GLOBAL_CONST unsigned short ncMOTPH_DITHER2;
 _GLOBAL_CONST unsigned short ncMOTPH_DITHER;
 _GLOBAL_CONST unsigned short ncMOTOR_SYNCHRON;
 _GLOBAL_CONST unsigned short ncMOTOR_PHASING;
 _GLOBAL_CONST unsigned char ncMOTOR_PAR;
 _GLOBAL_CONST unsigned short ncMOTOR_INDUCTION;
 _GLOBAL_CONST unsigned short ncMOTOR;
 _GLOBAL_CONST unsigned short ncMODULE;
 _GLOBAL_CONST unsigned short ncMODEL_2MASS;
 _GLOBAL_CONST unsigned short ncMODEL_1MASS;
 _GLOBAL_CONST unsigned short ncMOD_SYNC;
 _GLOBAL_CONST unsigned char ncMOD_DIR;
 _GLOBAL_CONST unsigned char ncMM;
 _GLOBAL_CONST unsigned short ncMESSAGE;
 _GLOBAL_CONST unsigned char ncMEMCARD;
 _GLOBAL_CONST unsigned char ncMC_STATE_SYNCHRONIZED_MOTION;
 _GLOBAL_CONST unsigned char ncMC_STATE_STOPPING;
 _GLOBAL_CONST unsigned char ncMC_STATE_STANDSTILL;
 _GLOBAL_CONST unsigned char ncMC_STATE_NET_INIT;
 _GLOBAL_CONST unsigned char ncMC_STATE_MOTION;
 _GLOBAL_CONST unsigned char ncMC_STATE_HOMING;
 _GLOBAL_CONST unsigned char ncMC_STATE_GroupStopping;
 _GLOBAL_CONST unsigned char ncMC_STATE_GroupStandby;
 _GLOBAL_CONST unsigned char ncMC_STATE_GroupMoving;
 _GLOBAL_CONST unsigned char ncMC_STATE_GroupHoming;
 _GLOBAL_CONST unsigned char ncMC_STATE_GroupErrorstop;
 _GLOBAL_CONST unsigned char ncMC_STATE_GroupDisabled;
 _GLOBAL_CONST unsigned char ncMC_STATE_ERRORSTOP;
 _GLOBAL_CONST unsigned char ncMC_STATE_ERROR;
 _GLOBAL_CONST unsigned char ncMC_STATE_DISCRETE_MOTION;
 _GLOBAL_CONST unsigned char ncMC_STATE_DISABLED;
 _GLOBAL_CONST unsigned char ncMC_STATE_CONTINUOUS_MOTION;
 _GLOBAL_CONST signed long ncMAINPROG;
 _GLOBAL_CONST unsigned char ncMAGNESCALE;
 _GLOBAL_CONST unsigned short ncMA_V_COMP;
 _GLOBAL_CONST unsigned short ncMA_TO_SL;
 _GLOBAL_CONST unsigned char ncMA_SL_ABS;
 _GLOBAL_CONST unsigned short ncMA_S_START_I32;
 _GLOBAL_CONST unsigned char ncMA_LATCHPOS;
 _GLOBAL_CONST unsigned char ncMA_IV_SL_ABS;
 _GLOBAL_CONST unsigned short ncM1_STOP;
 _GLOBAL_CONST unsigned short ncM_GRP_TAB;
 _GLOBAL_CONST unsigned short ncLOW_PASS;
 _GLOBAL_CONST unsigned char ncLOW;
 _GLOBAL_CONST unsigned short ncLOAD_ABORT;
 _GLOBAL_CONST unsigned short ncLOAD;
 _GLOBAL_CONST unsigned char ncLINMOT;
 _GLOBAL_CONST unsigned short ncLINK;
 _GLOBAL_CONST unsigned char ncLINENUMBER;
 _GLOBAL_CONST unsigned char ncLINEAR2;
 _GLOBAL_CONST unsigned char ncLINEAR;
 _GLOBAL_CONST unsigned short ncLINE;
 _GLOBAL_CONST unsigned short ncLIMITS;
 _GLOBAL_CONST unsigned short ncLIMITER;
 _GLOBAL_CONST unsigned char ncLEFT;
 _GLOBAL_CONST unsigned char ncLATCHPOS;
 _GLOBAL_CONST unsigned short ncLATCH2;
 _GLOBAL_CONST unsigned short ncLATCH1;
 _GLOBAL_CONST unsigned char ncLAG_ERR;
 _GLOBAL_CONST unsigned char ncISQR_REF_SYSTEM_FLUX;
 _GLOBAL_CONST unsigned char ncISQR_REF_SYSTEM_ENCODER;
 _GLOBAL_CONST unsigned short ncISQR_MODE_A_PHI;
 _GLOBAL_CONST unsigned short ncISQF_TRQ_ADDLIM;
 _GLOBAL_CONST unsigned short ncISQF_LIM3;
 _GLOBAL_CONST unsigned short ncISQF_LIM2;
 _GLOBAL_CONST unsigned short ncISQF_LIM;
 _GLOBAL_CONST unsigned short ncISQF_COMP;
 _GLOBAL_CONST unsigned short ncISQ_RIPPLE;
 _GLOBAL_CONST unsigned short ncISQ_F3_NOTCH;
 _GLOBAL_CONST unsigned short ncISQ_F3_LOW_PASS;
 _GLOBAL_CONST unsigned short ncISQ_F2_NOTCH;
 _GLOBAL_CONST unsigned short ncISQ_F2_LOW_PASS;
 _GLOBAL_CONST unsigned short ncISQ_F1_NOTCH;
 _GLOBAL_CONST unsigned short ncISQ_F1_LOW_PASS;
 _GLOBAL_CONST unsigned short ncIPGLOBAL;
 _GLOBAL_CONST unsigned short ncIP_INFO_AS_WARNING;
 _GLOBAL_CONST unsigned char ncINVERSE;
 _GLOBAL_CONST unsigned char ncINTERPRETER;
 _GLOBAL_CONST unsigned char ncINIT_SET_POS;
 _GLOBAL_CONST unsigned short ncINIT;
 _GLOBAL_CONST unsigned short ncINFO;
 _GLOBAL_CONST unsigned char ncINDUCTION;
 _GLOBAL_CONST unsigned char ncINDRAMAT;
 _GLOBAL_CONST unsigned char ncINDIRECT;
 _GLOBAL_CONST unsigned char ncINCLUDE;
 _GLOBAL_CONST unsigned char ncINCH;
 _GLOBAL_CONST unsigned char ncINC_SSI;
 _GLOBAL_CONST unsigned char ncINC_OUTPUT;
 _GLOBAL_CONST unsigned char ncINC_COMP;
 _GLOBAL_CONST unsigned char ncINC;
 _GLOBAL_CONST unsigned char ncIN_WINDOW;
 _GLOBAL_CONST unsigned short ncIDENTIFICATION;
 _GLOBAL_CONST unsigned char ncI_LIMIT;
 _GLOBAL_CONST unsigned short ncHW_END;
 _GLOBAL_CONST unsigned char ncHORIZONTAL;
 _GLOBAL_CONST unsigned short ncHOMING;
 _GLOBAL_CONST unsigned char ncHOME_OFFSET_INTERNAL;
 _GLOBAL_CONST unsigned char ncHOME_OFFSET;
 _GLOBAL_CONST unsigned char ncHIPERFACE_DSL;
 _GLOBAL_CONST unsigned char ncHIPERFACE;
 _GLOBAL_CONST unsigned char ncHIGH;
 _GLOBAL_CONST unsigned char ncHALT_SST;
 _GLOBAL_CONST unsigned char ncHALT_RST;
 _GLOBAL_CONST unsigned char ncHALT_PRG;
 _GLOBAL_CONST unsigned char ncHALT_POS;
 _GLOBAL_CONST unsigned char ncHALT_PLC;
 _GLOBAL_CONST unsigned short ncHALT_OK;
 _GLOBAL_CONST unsigned char ncHALT_EXEC_ERR;
 _GLOBAL_CONST unsigned char ncHALT_ERR;
 _GLOBAL_CONST unsigned short ncHALT;
 _GLOBAL_CONST unsigned char ncGRAY;
 _GLOBAL_CONST unsigned short ncGO_HOME;
 _GLOBAL_CONST unsigned long ncglobal_action_NCDA_WRITE;
 _GLOBAL_CONST unsigned long ncglobal_action_NCDA_INFO;
 _GLOBAL_CONST unsigned long ncglobal_action_NCDA_DIR;
 _GLOBAL_CONST unsigned long ncglobal_action_NCDA_CREATE;
 _GLOBAL_CONST unsigned long ncglobal_action_ACP10MSG_TEXT;
 _GLOBAL_CONST unsigned short ncGLOBAL;
 _GLOBAL_CONST unsigned short ncGETINFO;
 _GLOBAL_CONST unsigned short ncGERMAN;
 _GLOBAL_CONST unsigned short ncGEARSABS;
 _GLOBAL_CONST unsigned short ncGEARS_V;
 _GLOBAL_CONST unsigned short ncGEARS;
 _GLOBAL_CONST unsigned char ncGATE;
 _GLOBAL_CONST unsigned char ncGANTRY;
 _GLOBAL_CONST unsigned char ncG03;
 _GLOBAL_CONST unsigned char ncG02;
 _GLOBAL_CONST unsigned char ncG01;
 _GLOBAL_CONST unsigned char ncG00;
 _GLOBAL_CONST unsigned short ncFORMAT_T14;
 _GLOBAL_CONST unsigned short ncFORMAT_T10;
 _GLOBAL_CONST unsigned short ncFORMAT_B06;
 _GLOBAL_CONST unsigned short ncFORMAT_ADR;
 _GLOBAL_CONST unsigned short ncFORCE;
 _GLOBAL_CONST unsigned char ncFIXRAM;
 _GLOBAL_CONST unsigned short ncFINISH;
 _GLOBAL_CONST unsigned char ncFILEOFFSET;
 _GLOBAL_CONST unsigned char ncFILE_XL;
 _GLOBAL_CONST unsigned char ncFILE;
 _GLOBAL_CONST unsigned short ncFF_POS_MOVE;
 _GLOBAL_CONST unsigned short ncFF_NEG_MOVE;
 _GLOBAL_CONST unsigned char ncFF;
 _GLOBAL_CONST unsigned char ncFC;
 _GLOBAL_CONST unsigned char ncFALSE;
 _GLOBAL_CONST unsigned char ncEXTERN;
 _GLOBAL_CONST unsigned short ncEXTENCOD;
 _GLOBAL_CONST unsigned short ncEXPRESSION;
 _GLOBAL_CONST unsigned short ncEXECUTE;
 _GLOBAL_CONST unsigned short ncEX_PARAM;
 _GLOBAL_CONST unsigned short ncEVENT;
 _GLOBAL_CONST unsigned char ncEVEN;
 _GLOBAL_CONST unsigned char ncETEL;
 _GLOBAL_CONST unsigned short ncERROR;
 _GLOBAL_CONST unsigned short ncERR_CL0;
 _GLOBAL_CONST unsigned char ncERR_A2;
 _GLOBAL_CONST unsigned char ncEPROM;
 _GLOBAL_CONST unsigned char ncENTRY;
 _GLOBAL_CONST unsigned short ncENGLISH;
 _GLOBAL_CONST unsigned char ncENDAT3;
 _GLOBAL_CONST unsigned char ncENDAT_SafeMOTION;
 _GLOBAL_CONST unsigned char ncENDAT;
 _GLOBAL_CONST unsigned char ncEND_SWITCH;
 _GLOBAL_CONST unsigned short ncENCODER_IF;
 _GLOBAL_CONST unsigned short ncENCOD_IF;
 _GLOBAL_CONST unsigned short ncENABLE;
 _GLOBAL_CONST unsigned short ncEMPTY;
 _GLOBAL_CONST unsigned char ncEDGE2;
 _GLOBAL_CONST unsigned short ncE_STOP;
 _GLOBAL_CONST unsigned long ncDV_STOP_INIT;
 _GLOBAL_CONST unsigned long ncDV_STOP_AUTO2;
 _GLOBAL_CONST unsigned long ncDV_STOP_AUTO1;
 _GLOBAL_CONST unsigned char ncDRIVE_READY;
 _GLOBAL_CONST unsigned short ncDRIVE_IF;
 _GLOBAL_CONST unsigned short ncDRIVE_ID;
 _GLOBAL_CONST unsigned short ncDRIVE;
 _GLOBAL_CONST unsigned char ncDRAM;
 _GLOBAL_CONST unsigned short ncDPR_TRACE;
 _GLOBAL_CONST unsigned short ncDPR_OVR;
 _GLOBAL_CONST unsigned short ncDOWNLOAD;
 _GLOBAL_CONST unsigned char ncDNC;
 _GLOBAL_CONST unsigned short ncDM16BIT;
 _GLOBAL_CONST unsigned char ncDIRECT;
 _GLOBAL_CONST unsigned short ncDIG_IN;
 _GLOBAL_CONST unsigned short ncDIAGNOSE;
 _GLOBAL_CONST unsigned short ncDELETE;
 _GLOBAL_CONST unsigned short ncDEFINE;
 _GLOBAL_CONST unsigned short ncDECODER;
 _GLOBAL_CONST unsigned char ncDECEL;
 _GLOBAL_CONST unsigned char ncDCM;
 _GLOBAL_CONST unsigned short ncDATOBJ_FORMAT_TXT;
 _GLOBAL_CONST unsigned short ncDATOBJ_FORMAT_CSV;
 _GLOBAL_CONST unsigned short ncDATOBJ_FORMAT_BIN;
 _GLOBAL_CONST unsigned short ncDATOBJ_FILE;
 _GLOBAL_CONST unsigned short ncDATOBJ_BRMOD_DEFAULT;
 _GLOBAL_CONST unsigned short ncDATOBJ_BRMOD;
 _GLOBAL_CONST unsigned char ncDATMOD_ZERO_P_OFF;
 _GLOBAL_CONST unsigned char ncDATMOD_NET_TRACE;
 _GLOBAL_CONST unsigned char ncDATMOD_NC_MAPPING;
 _GLOBAL_CONST unsigned char ncDATMOD_DATBLOCK;
 _GLOBAL_CONST unsigned char ncDATMOD_CNC_TOOL;
 _GLOBAL_CONST unsigned char ncDATMOD_CNC_R_PAR;
 _GLOBAL_CONST unsigned char ncDATMOD_CNC_PROG;
 _GLOBAL_CONST unsigned char ncDATMOD_CNC_CAM_TAB;
 _GLOBAL_CONST unsigned char ncDATMOD_CNC_CAM_POLY;
 _GLOBAL_CONST unsigned char ncDATMOD_ACP_PAR_TRACE;
 _GLOBAL_CONST unsigned char ncDATMOD_ACP_PAR;
 _GLOBAL_CONST unsigned char ncDATMOD_ACP_CAM_POLY;
 _GLOBAL_CONST unsigned short ncDATBLOCK;
 _GLOBAL_CONST unsigned short ncDATA_TEXT;
 _GLOBAL_CONST unsigned char ncDATA;
 _GLOBAL_CONST unsigned short ncDAT_MOD;
 _GLOBAL_CONST unsigned short ncD_SINGLE;
 _GLOBAL_CONST unsigned char ncD_POS;
 _GLOBAL_CONST unsigned char ncCYCLIC;
 _GLOBAL_CONST unsigned short ncCYCL_USER_TODRV_AT_STARTUP;
 _GLOBAL_CONST unsigned short ncCYCL_USER_TODRV;
 _GLOBAL_CONST unsigned short ncCYCL_USER_FRDRV_AT_STARTUP;
 _GLOBAL_CONST unsigned short ncCYCL_USER_FRDRV;
 _GLOBAL_CONST unsigned char ncCTRL_OFF;
 _GLOBAL_CONST unsigned char ncCSTRF;
 _GLOBAL_CONST unsigned short ncCOUPLING;
 _GLOBAL_CONST unsigned char ncCOUNT;
 _GLOBAL_CONST unsigned char ncCORRECTION;
 _GLOBAL_CONST unsigned short ncCONTROLLER;
 _GLOBAL_CONST unsigned short ncCONTROL;
 _GLOBAL_CONST unsigned short ncCONTINUE_;
 _GLOBAL_CONST unsigned short ncCONTINUE;
 _GLOBAL_CONST unsigned short ncCOMPAR;
 _GLOBAL_CONST unsigned char ncCOMP_ERR;
 _GLOBAL_CONST unsigned short ncCOMP;
 _GLOBAL_CONST unsigned short ncCNCSYS;
 _GLOBAL_CONST unsigned char ncCNC_PROG;
 _GLOBAL_CONST unsigned short ncCNC_PLC;
 _GLOBAL_CONST unsigned short ncCNC_C_AX;
 _GLOBAL_CONST unsigned char ncCNC;
 _GLOBAL_CONST unsigned short ncCMD_WARNING_ONLY;
 _GLOBAL_CONST unsigned short ncCMD_ERROR_V_STOP_CTRL_OFF;
 _GLOBAL_CONST unsigned short ncCMD_ERROR_TRQLIM_T_JOLT_STOP;
 _GLOBAL_CONST unsigned short ncCMD_ERROR_TRQLIM_STOP;
 _GLOBAL_CONST unsigned short ncCMD_ERROR_STOP_CTRL_OFF;
 _GLOBAL_CONST unsigned short ncCMD_ERROR_STOP;
 _GLOBAL_CONST unsigned short ncCMD_ERROR_ONLY;
 _GLOBAL_CONST unsigned short ncCMD_ERROR_INDUCTION_HALT;
 _GLOBAL_CONST unsigned short ncCMD_ERROR_COAST_TO_STANDSTILL;
 _GLOBAL_CONST unsigned short ncCMD_ERROR_A2_V_STOP_CTRL_OFF;
 _GLOBAL_CONST unsigned short ncCMD_ERROR_A2_STOP_CTRL_OFF;
 _GLOBAL_CONST unsigned short ncCMD_ERROR_A2_STOP;
 _GLOBAL_CONST unsigned short ncCMD_ERROR;
 _GLOBAL_CONST unsigned char ncCLOSED;
 _GLOBAL_CONST unsigned short ncCAN_IF;
 _GLOBAL_CONST unsigned char ncCAMPRPOL_ACOPOS;
 _GLOBAL_CONST unsigned char ncCAMPRPOL;
 _GLOBAL_CONST unsigned char ncCAMPRDAT;
 _GLOBAL_CONST unsigned short ncCAM_PROF;
 _GLOBAL_CONST unsigned char ncCAM_BEG;
 _GLOBAL_CONST unsigned short ncCALCULATION;
 _GLOBAL_CONST unsigned char ncBYTEOFFSET;
 _GLOBAL_CONST unsigned short ncBURN;
 _GLOBAL_CONST unsigned short ncBREAKPOINT;
 _GLOBAL_CONST unsigned short ncBREAK;
 _GLOBAL_CONST unsigned short ncBRAKE;
 _GLOBAL_CONST unsigned short ncBLOCKSEARCH;
 _GLOBAL_CONST unsigned char ncBLOCKNUMBER;
 _GLOBAL_CONST unsigned char ncBLOCKMONITOR;
 _GLOBAL_CONST unsigned short ncBLOCKMON;
 _GLOBAL_CONST unsigned char ncBLOCK_TORQUE;
 _GLOBAL_CONST unsigned char ncBLOCK_DS;
 _GLOBAL_CONST unsigned short ncBLOCK;
 _GLOBAL_CONST unsigned char ncBL;
 _GLOBAL_CONST unsigned char ncBISS;
 _GLOBAL_CONST unsigned short ncBIQUAD;
 _GLOBAL_CONST unsigned char ncBINARY;
 _GLOBAL_CONST unsigned char ncBIDIR;
 _GLOBAL_CONST unsigned char ncBELOW_WINDOW;
 _GLOBAL_CONST unsigned short ncBASIS_TRG_STOP;
 _GLOBAL_CONST unsigned short ncBASIS_MOVE;
 _GLOBAL_CONST unsigned char ncBASIS;
 _GLOBAL_CONST unsigned short ncAXIS;
 _GLOBAL_CONST unsigned short ncAXES;
 _GLOBAL_CONST unsigned char ncAUTOSAVE;
 _GLOBAL_CONST unsigned short ncAUTOMAT;
 _GLOBAL_CONST unsigned char ncAUTO;
 _GLOBAL_CONST unsigned char ncAUT_END;
 _GLOBAL_CONST unsigned char ncAT_ONCE;
 _GLOBAL_CONST unsigned short ncARNC0MAN;
 _GLOBAL_CONST unsigned char ncAND_N2E;
 _GLOBAL_CONST unsigned char ncANALOG;
 _GLOBAL_CONST unsigned short ncALL;
 _GLOBAL_CONST unsigned short ncAIL_DUMP;
 _GLOBAL_CONST unsigned short ncADD_DATE_TIME;
 _GLOBAL_CONST unsigned short ncACTIVE;
 _GLOBAL_CONST unsigned char ncACTIV_LO;
 _GLOBAL_CONST unsigned char ncACTIV_HI;
 _GLOBAL_CONST unsigned short ncACT_POS;
 _GLOBAL_CONST unsigned short ncACP10USCOB;
 _GLOBAL_CONST unsigned short ncACP10MAN;
 _GLOBAL_CONST unsigned char ncACP_TYP_SIM;
 _GLOBAL_CONST unsigned char ncACP_TYP_SDC;
 _GLOBAL_CONST unsigned char ncACP_TYP_PS;
 _GLOBAL_CONST unsigned char ncACP_TYP_PPS;
 _GLOBAL_CONST unsigned char ncACP_TYP_INV;
 _GLOBAL_CONST unsigned char ncACP_SIM_STANDARD;
 _GLOBAL_CONST unsigned char ncACP_SIM_COMPLETE;
 _GLOBAL_CONST unsigned short ncACP_PAR_SEND;
 _GLOBAL_CONST unsigned short ncACP_PAR_RECEIVE;
 _GLOBAL_CONST unsigned short ncACP_PAR_INIT_BRC_DP64;
 _GLOBAL_CONST unsigned short ncACP_PAR_INIT_BRC_DP;
 _GLOBAL_CONST unsigned short ncACP_PAR;
 _GLOBAL_CONST unsigned char ncACOPOSremote;
 _GLOBAL_CONST unsigned char ncACOPOSmulti65m;
 _GLOBAL_CONST unsigned char ncACOPOSmulti65;
 _GLOBAL_CONST unsigned char ncACOPOSmulti3;
 _GLOBAL_CONST unsigned char ncACOPOSmulti_PPS;
 _GLOBAL_CONST unsigned char ncACOPOSmulti;
 _GLOBAL_CONST unsigned char ncACOPOSmotor_C;
 _GLOBAL_CONST unsigned char ncACOPOSmotor;
 _GLOBAL_CONST unsigned char ncACOPOSmicro;
 _GLOBAL_CONST unsigned char ncACOPOS_SIM;
 _GLOBAL_CONST unsigned char ncACOPOS_SDC;
 _GLOBAL_CONST unsigned char ncACOPOS_P3;
 _GLOBAL_CONST unsigned short ncACOPOS_INFO;
 _GLOBAL_CONST unsigned char ncACOPOS_2;
 _GLOBAL_CONST unsigned char ncACOPOS_1;
 _GLOBAL_CONST unsigned short ncACKNOWLEDGE;
 _GLOBAL_CONST unsigned short ncACK;
 _GLOBAL_CONST unsigned char ncACCEL;
 _GLOBAL_CONST unsigned char ncABSOLUTE;
 _GLOBAL_CONST unsigned char ncABS_SWITCH;
 _GLOBAL_CONST unsigned short ncABS_MOVE;
 _GLOBAL_CONST unsigned char ncABS;
 _GLOBAL_CONST unsigned char ncABOVE_WINDOW;
 _GLOBAL_CONST unsigned char ncABORT_LINE;
 _GLOBAL_CONST unsigned char ncABORT_DATA;
 _GLOBAL_CONST unsigned char ncA_MOVE;
 _GLOBAL_CONST unsigned char ncA_LIMIT;
 _GLOBAL_CONST unsigned short nc2ENCOD_SPEED;
 _GLOBAL_CONST unsigned char nc20KHZ;
 _GLOBAL_CONST unsigned short nc158CAN;
 _GLOBAL_CONST unsigned short nc157CAN;
 _GLOBAL_CONST unsigned short nc156CAN;
 _GLOBAL_CONST unsigned short nc154CAN;
 _GLOBAL_CONST unsigned char nc100KHZ;
 _GLOBAL_CONST unsigned short MOD_UPDATE;
 _GLOBAL_CONST unsigned short MC_InitFunction;
 _GLOBAL_CONST unsigned short IO_2010;
 _GLOBAL_CONST unsigned short IO_2005;
 _GLOBAL_CONST unsigned short FB_MC_WriteParameter;
 _GLOBAL_CONST unsigned short FB_MC_WriteDigitalOutput;
 _GLOBAL_CONST unsigned short FB_MC_WriteBoolParameter;
 _GLOBAL_CONST unsigned short FB_MC_TouchProbe;
 _GLOBAL_CONST unsigned short FB_MC_TorqueControl;
 _GLOBAL_CONST unsigned short FB_MC_Stop;
 _GLOBAL_CONST unsigned short FB_MC_SetOverride;
 _GLOBAL_CONST unsigned short FB_MC_Reset;
 _GLOBAL_CONST unsigned short FB_MC_ReadStatus;
 _GLOBAL_CONST unsigned short FB_MC_ReadParameter;
 _GLOBAL_CONST unsigned short FB_MC_ReadDigitalOutput;
 _GLOBAL_CONST unsigned short FB_MC_ReadDigitalInput;
 _GLOBAL_CONST unsigned short FB_MC_ReadBoolParameter;
 _GLOBAL_CONST unsigned short FB_MC_ReadAxisError;
 _GLOBAL_CONST unsigned short FB_MC_ReadActualVelocity;
 _GLOBAL_CONST unsigned short FB_MC_ReadActualTorque;
 _GLOBAL_CONST unsigned short FB_MC_ReadActualPosition;
 _GLOBAL_CONST unsigned short FB_MC_Power;
 _GLOBAL_CONST unsigned short FB_MC_Phasing;
 _GLOBAL_CONST unsigned short FB_MC_MoveVelocity;
 _GLOBAL_CONST unsigned short FB_MC_MoveRelative;
 _GLOBAL_CONST unsigned short FB_MC_MoveAdditive;
 _GLOBAL_CONST unsigned short FB_MC_MoveAbsolute;
 _GLOBAL_CONST unsigned short FB_MC_LimitLoad;
 _GLOBAL_CONST unsigned short FB_MC_Home;
 _GLOBAL_CONST unsigned short FB_MC_Halt;
 _GLOBAL_CONST unsigned short FB_MC_GearOut;
 _GLOBAL_CONST unsigned short FB_MC_GearInPos;
 _GLOBAL_CONST unsigned short FB_MC_GearIn;
 _GLOBAL_CONST unsigned short FB_MC_DigitalCamSwitch;
 _GLOBAL_CONST unsigned short FB_MC_CamTableSelect;
 _GLOBAL_CONST unsigned short FB_MC_CamOut;
 _GLOBAL_CONST unsigned short FB_MC_CamIn;
 _GLOBAL_CONST unsigned short FB_MC_BR_WriteParIDText;
 _GLOBAL_CONST unsigned short FB_MC_BR_WriteParID;
 _GLOBAL_CONST unsigned short FB_MC_BR_WriteLoadSimTwoEncPos;
 _GLOBAL_CONST unsigned short FB_MC_BR_WriteLoadSimTorque;
 _GLOBAL_CONST unsigned short FB_MC_BR_WriteLoadSimPosition;
 _GLOBAL_CONST unsigned short FB_MC_BR_WriteLoadSimOutputData;
 _GLOBAL_CONST unsigned short FB_MC_BR_VelocityControl;
 _GLOBAL_CONST unsigned short FB_MC_BR_TouchProbe;
 _GLOBAL_CONST unsigned short FB_MC_BR_TorqueControl;
 _GLOBAL_CONST unsigned short FB_MC_BR_Simulation;
 _GLOBAL_CONST unsigned short FB_MC_BR_SetupSynchronMotor;
 _GLOBAL_CONST unsigned short FB_MC_BR_SetupMotorPhasing;
 _GLOBAL_CONST unsigned short FB_MC_BR_SetupIsqRipple;
 _GLOBAL_CONST unsigned short FB_MC_BR_SetupInductionMotor;
 _GLOBAL_CONST unsigned short FB_MC_BR_SetupFromParTabObj;
 _GLOBAL_CONST unsigned short FB_MC_BR_SetupController;
 _GLOBAL_CONST unsigned short FB_MC_BR_SetHardwareInputs;
 _GLOBAL_CONST unsigned short FB_MC_BR_SaveCamProfileObj;
 _GLOBAL_CONST unsigned short FB_MC_BR_SaveAxisPar;
 _GLOBAL_CONST unsigned short FB_MC_BR_ResetAutPar;
 _GLOBAL_CONST unsigned short FB_MC_BR_RegMarkCapture002;
 _GLOBAL_CONST unsigned short FB_MC_BR_RegMarkCapture001;
 _GLOBAL_CONST unsigned short FB_MC_BR_RegMarkCalc001;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReceiveParIDOnPLC;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReadParTraceStatus;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReadParList;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReadParIDText;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReadParID;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReadNetTraceStatus;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReadLoadSimTorque;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReadLoadSimInputData;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReadDriveStatus;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReadCyclicPosition;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReadAxisError;
 _GLOBAL_CONST unsigned short FB_MC_BR_ReadAutPosition;
 _GLOBAL_CONST unsigned short FB_MC_BR_PowerMeter;
 _GLOBAL_CONST unsigned short FB_MC_BR_Phasing;
 _GLOBAL_CONST unsigned short FB_MC_BR_ParTraceConfig;
 _GLOBAL_CONST unsigned short FB_MC_BR_ParTrace;
 _GLOBAL_CONST unsigned short FB_MC_BR_OffsetZone;
 _GLOBAL_CONST unsigned short FB_MC_BR_OffsetVelocity;
 _GLOBAL_CONST unsigned short FB_MC_BR_Offset;
 _GLOBAL_CONST unsigned short FB_MC_BR_NetworkInit;
 _GLOBAL_CONST unsigned short FB_MC_BR_NetTrace;
 _GLOBAL_CONST unsigned short FB_MC_BR_MoveVelocityTriggStop;
 _GLOBAL_CONST unsigned short FB_MC_BR_MoveCyclicVelocityExt;
 _GLOBAL_CONST unsigned short FB_MC_BR_MoveCyclicVelocity;
 _GLOBAL_CONST unsigned short FB_MC_BR_MoveCyclicPositionExt;
 _GLOBAL_CONST unsigned short FB_MC_BR_MoveCyclicPosition;
 _GLOBAL_CONST unsigned short FB_MC_BR_MoveAdditiveTriggStop;
 _GLOBAL_CONST unsigned short FB_MC_BR_MoveAbsoluteTriggStop;
 _GLOBAL_CONST unsigned short FB_MC_BR_MechPosDeviationComp;
 _GLOBAL_CONST unsigned short FB_MC_BR_LoadAxisPar;
 _GLOBAL_CONST unsigned short FB_MC_BR_LimitLoadCam;
 _GLOBAL_CONST unsigned short FB_MC_BR_LimitLoad;
 _GLOBAL_CONST unsigned short FB_MC_BR_JogVelocity;
 _GLOBAL_CONST unsigned short FB_MC_BR_JogTargetPosition;
 _GLOBAL_CONST unsigned short FB_MC_BR_JogLimitPosition;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitSendParID;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitReceiveParID;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitReceiveNetworkEnc;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitReceiveNetworkData;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitParTabObj;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitParSequ;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitParList;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitModPos;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitMasterParIDTransfer;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitEndlessPosition;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitEndlessPosAcpEnc;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitCyclicWrite;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitCyclicRead;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitAxisSubjectPar;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitAxisPar;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitAutState;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitAutPar;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitAutEvent;
 _GLOBAL_CONST unsigned short FB_MC_BR_InitAutData;
 _GLOBAL_CONST unsigned short FB_MC_BR_HomeAcpEncoder;
 _GLOBAL_CONST unsigned short FB_MC_BR_GetParIDTransferInfo;
 _GLOBAL_CONST unsigned short FB_MC_BR_GetParIDInfo;
 _GLOBAL_CONST unsigned short FB_MC_BR_GetHardwareInfo;
 _GLOBAL_CONST unsigned short FB_MC_BR_GetErrorText;
 _GLOBAL_CONST unsigned short FB_MC_BR_GetCamSlavePosition;
 _GLOBAL_CONST unsigned short FB_MC_BR_GetCamMasterPosition;
 _GLOBAL_CONST unsigned short FB_MC_BR_GearIn;
 _GLOBAL_CONST unsigned short FB_MC_BR_EventMoveVelocity;
 _GLOBAL_CONST unsigned short FB_MC_BR_EventMoveAdditive;
 _GLOBAL_CONST unsigned short FB_MC_BR_EventMoveAbsolute;
 _GLOBAL_CONST unsigned short FB_MC_BR_DownloadParSequ;
 _GLOBAL_CONST unsigned short FB_MC_BR_DownloadCamProfileObj;
 _GLOBAL_CONST unsigned short FB_MC_BR_DownloadCamProfileData;
 _GLOBAL_CONST unsigned short FB_MC_BR_DigitalCamSwitch;
 _GLOBAL_CONST unsigned short FB_MC_BR_CyclicWrite;
 _GLOBAL_CONST unsigned short FB_MC_BR_CyclicReadDataInfo;
 _GLOBAL_CONST unsigned short FB_MC_BR_CyclicRead;
 _GLOBAL_CONST unsigned short FB_MC_BR_CrossCutterControl;
 _GLOBAL_CONST unsigned short FB_MC_BR_CreateCamProfileObj;
 _GLOBAL_CONST unsigned short FB_MC_BR_ConfigPowerStageCheck;
 _GLOBAL_CONST unsigned short FB_MC_BR_CommandError;
 _GLOBAL_CONST unsigned short FB_MC_BR_CheckEndlessPosition;
 _GLOBAL_CONST unsigned short FB_MC_BR_CheckAutCompensation;
 _GLOBAL_CONST unsigned short FB_MC_BR_CamTransition;
 _GLOBAL_CONST unsigned short FB_MC_BR_CamIn;
 _GLOBAL_CONST unsigned short FB_MC_BR_CamDwell;
 _GLOBAL_CONST unsigned short FB_MC_BR_CalcSectionsFromCam;
 _GLOBAL_CONST unsigned short FB_MC_BR_CalcPointsFromCam;
 _GLOBAL_CONST unsigned short FB_MC_BR_CalcCamFromSections;
 _GLOBAL_CONST unsigned short FB_MC_BR_CalcCamFromPoints;
 _GLOBAL_CONST unsigned short FB_MC_BR_BrakeOperation;
 _GLOBAL_CONST unsigned short FB_MC_BR_BrakeControl;
 _GLOBAL_CONST unsigned short FB_MC_BR_AxisErrorCollector;
 _GLOBAL_CONST unsigned short FB_MC_BR_AutoCamDwell;
 _GLOBAL_CONST unsigned short FB_MC_BR_AutControl;
 _GLOBAL_CONST unsigned short FB_MC_BR_AutCommand;
 _GLOBAL_CONST unsigned short FB_MC_AbortTrigger;
 _GLOBAL_CONST unsigned short FAST_BOOT;
 _GLOBAL_CONST unsigned short BASIS2005;
#endif




/* Datatypes and datatypes of function blocks */
typedef struct NCDA_DATMO_typ
{	unsigned char name[12];
	unsigned char type;
	unsigned char mem_type;
} NCDA_DATMO_typ;

typedef struct NCDA_MDDIR_typ
{	unsigned short count;
	unsigned long free_ram;
	unsigned long free_prom;
	struct NCDA_DATMO_typ data_modul[100];
} NCDA_MDDIR_typ;

typedef struct NCDA_TPREC_typ
{	float length;
	float radius;
	float offset[3];
} NCDA_TPREC_typ;

typedef struct NCDA_TPTAB_typ
{	unsigned short record_cnt;
	unsigned short startindex;
	struct NCDA_TPREC_typ record[255];
} NCDA_TPTAB_typ;

typedef struct NCDA_RPTAB_typ
{	unsigned short r_par_cnt;
	unsigned short startindex;
	float r_par[1000];
} NCDA_RPTAB_typ;

typedef struct NCDA_ZPREC_typ
{	float offset[3];
} NCDA_ZPREC_typ;

typedef struct NCDA_ZPTAB_typ
{	unsigned short record_cnt;
	unsigned short startindex;
	struct NCDA_ZPREC_typ record[200];
} NCDA_ZPTAB_typ;

typedef struct NCGLACT_NCDA_CR_STA_typ
{	unsigned char ok;
	unsigned char error;
	unsigned char reserved1;
	unsigned char reserved2;
	unsigned long error_number;
	unsigned long ident;
	unsigned long data_adr;
} NCGLACT_NCDA_CR_STA_typ;

typedef struct NCGLACT_NCDA_CR_PAR_typ
{	unsigned char name[32];
	unsigned short version;
	unsigned short reserved;
	unsigned short type;
	unsigned short nc_sw_id;
	unsigned long data_len;
	unsigned long data_adr;
} NCGLACT_NCDA_CR_PAR_typ;

typedef struct NCGLACT_NCDA_CREATE_typ
{	struct NCGLACT_NCDA_CR_STA_typ status;
	struct NCGLACT_NCDA_CR_PAR_typ parameter;
} NCGLACT_NCDA_CREATE_typ;

typedef struct NCGLACT_NCDA_INF_STA_typ
{	unsigned char ok;
	unsigned char error;
	unsigned char reserved1;
	unsigned char reserved2;
	unsigned long error_number;
	unsigned long ident;
	unsigned long data_len;
	unsigned long data_adr;
	unsigned short version;
	unsigned short mem_type;
	unsigned short type;
	unsigned short nc_sw_id;
	unsigned short data_sections;
	unsigned short reserved;
} NCGLACT_NCDA_INF_STA_typ;

typedef struct NCGLACT_NCDA_INF_PAR_typ
{	unsigned char name[32];
	unsigned short data_section_idx;
	unsigned short reserved;
} NCGLACT_NCDA_INF_PAR_typ;

typedef struct NCGLACT_NCDA_INFO_typ
{	struct NCGLACT_NCDA_INF_STA_typ status;
	struct NCGLACT_NCDA_INF_PAR_typ parameter;
} NCGLACT_NCDA_INFO_typ;

typedef struct NCGLACT_NCDA_WR_STA_typ
{	unsigned char ok;
	unsigned char error;
	unsigned char reserved1;
	unsigned char reserved2;
	unsigned long error_number;
} NCGLACT_NCDA_WR_STA_typ;

typedef struct NCGLACT_NCDA_WR_PAR_typ
{	unsigned long ident;
	unsigned long data_len;
	unsigned long data_adr;
	unsigned long data_offset;
} NCGLACT_NCDA_WR_PAR_typ;

typedef struct NCGLACT_NCDA_WRITE_typ
{	struct NCGLACT_NCDA_WR_STA_typ status;
	struct NCGLACT_NCDA_WR_PAR_typ parameter;
} NCGLACT_NCDA_WRITE_typ;

typedef struct NCGLACT_NCDA_DIR_STA_typ
{	unsigned char ok;
	unsigned char error;
	unsigned char reserved1;
	unsigned char reserved2;
	unsigned long error_number;
	unsigned long ident;
	unsigned long data_adr;
} NCGLACT_NCDA_DIR_STA_typ;

typedef struct NCGLACT_NCDA_DIR_PAR_typ
{	unsigned char name[32];
	unsigned short type;
	unsigned short reserved;
} NCGLACT_NCDA_DIR_PAR_typ;

typedef struct NCGLACT_NCDA_DIR_typ
{	struct NCGLACT_NCDA_DIR_STA_typ status;
	struct NCGLACT_NCDA_DIR_PAR_typ parameter;
} NCGLACT_NCDA_DIR_typ;



/* Prototyping of functions and function blocks */
_BUR_PUBLIC unsigned short nccnccom(unsigned long nc_object);
_BUR_PUBLIC unsigned short ncda_dir(unsigned char mo_typ, unsigned char *name_p, void **mo_dat_p_p, void *mo_ident_p);
_BUR_PUBLIC unsigned short ncda_inf(unsigned long mo_ident, void **mo_dat_p_p, void *dat_len_p, void *mem_typ_p);
_BUR_PUBLIC unsigned short ncda_id(unsigned char mo_typ, unsigned char *name_p, void *mo_ident_p);
_BUR_PUBLIC unsigned short ncda_wr(unsigned long mo_ident, void *dat_p, unsigned long dat_len, unsigned long mo_dat_off);
_BUR_PUBLIC unsigned short ncda_cr(unsigned char mo_typ, unsigned char *name_p, unsigned long dat_len, void *dat_p, void **mo_dat_p_p, void *mo_ident_p);
_BUR_PUBLIC unsigned short ncaccess(unsigned short nc_sw_id, char *nc_obj_name, unsigned long *p_nc_object);
_BUR_PUBLIC unsigned short ncalloc(unsigned short bus_typ, unsigned short modul_adr, unsigned short object_typ, unsigned short channel, unsigned long object_adr);
_BUR_PUBLIC unsigned short ncaction(unsigned long nc_object, unsigned short subject, unsigned short action);
_BUR_PUBLIC unsigned short ncglobal_action(unsigned long action_id, void *par_struct_adr, unsigned long par_struct_size);


#ifdef __cplusplus
};
#endif
#endif /* _NCGLOBAL_ */


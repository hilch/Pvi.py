#ifdef __cplusplus
extern "C" {
#endif

/* Automation Studio generated header file */
/* Do not edit ! */

#ifndef _ACP10_MC_
#define _ACP10_MC_

#include <bur/plctypes.h>

#ifndef _IEC_CONST
#define _IEC_CONST _WEAK const
#endif

/* Constants */
#ifdef _REPLACE_CONST
 #define mcWRAP 2U
 #define mcWITHOUT_FF 1U
 #define mcWITH_FF 0U
 #define mcWITHOUT_PERIOD 4U
 #define mcWITHIN_PERIOD 6U
 #define mcWITH_PARAM 2U
 #define mcVERTICAL 1U
 #define mcVELOCITY_CONTROL 4U
 #define mcV_LIMIT_OFF 2U
 #define mcV_LIMIT_CALC 4U
 #define mcUSE_TN 8U
 #define mcUSE_STOP_COMP 4U
 #define mcUSE_FIRST_TRIGGER_POS 64U
 #define mcUSE_FILTER_PAR 4U
 #define mcUSE_AXIS_PERIOD 16384U
 #define mcUPDATE_PERIOD 32768U
 #define mcUNEQUAL 5U
 #define mcTUNE_V_CONSTANT 1U
 #define mcTUNE_STANDSTILL 0U
 #define mcTRANSITION_ON 1U
 #define mcTRANSITION_OFF 0U
 #define mcTRACE_TRIGGER 3U
 #define mcTRACE_TIME 2U
 #define mcTRACE_STARTED 20U
 #define mcTRACE_RING 4U
 #define mcTRACE_REST 5U
 #define mcTRACE_FINISHED 1U
 #define mcTRACE_DELAY 6U
 #define mcTIME_LIMIT 8U
 #define mcTIME_BASED 1U
 #define mcTEXT 1U
 #define mcTEST 31U
 #define mcT_FILTER_2 65U
 #define mcT_FILTER 64U
 #define mcSWITCH_ON 258U
 #define mcSWITCH_OFF 259U
 #define mcSW_LIMIT_POS 2
 #define mcSW_LIMIT_NEG 3
 #define mcSW_END_SPF 2
 #define mcSW_END_MONITORING 1014
 #define mcSW_END_IGNORE 1
 #define mcSW_END_ACTIVE 0
 #define mcSTRAIGHT_LINE 1U
 #define mcSTOP_INDEX 1013
 #define mcSTOP 261U
 #define mcSTEPPER 31U
 #define mcSTART_ONLY 3U
 #define mcSTART 260U
 #define mcSTANDARD 0U
 #define mcSPEED 2U
 #define mcSMALLER 1U
 #define mcSLOW_DOWN 5U
 #define mcSLAVE_POSITION 0U
 #define mcSIMULATION_READ 265U
 #define mcSIMULATION_ON 258U
 #define mcSIMULATION_OFF 259U
 #define mcSIMULATION_INIT_ON 256U
 #define mcSIMULATION_INIT 512U
 #define mcSIMPLE_SINE_CURVE 3U
 #define mcSHORTEST_WAY 3U
 #define mcSHIFT_FROM_RESULT 49U
 #define mcSHIFT_FROM_EXPECTED 50U
 #define mcSET_OFFSET 34U
 #define mcSE 3U
 #define mcSAVE_RING_STARTIDX 4437U
 #define mcSAVE 341U
 #define mcSATURATION 30U
 #define mcREVERSE 8U
 #define mcRESTART 273U
 #define mcRESET_RING_STARTIDX 4416U
 #define mcRESET 320U
 #define mcRELATIVE_NO_RESET 3U
 #define mcRELATIVE 1U
 #define mcQUEUED 1U
 #define mcQUADRATIC_PARABOLA 2U
 #define mcPOSITIVE_DIR 0U
 #define mcPOSITION 1U
 #define mcPERIODIC 1
 #define mcP_EDGE 0U
 #define mcOVERRIDE 1000
 #define mcOUT_WINDOW 30U
 #define mcOPTIMIZED_VELOCITY 512U
 #define mcOPTIMIZED_ACCELERATION 768U
 #define mcOPEN 1U
 #define mcONLY_PSM 1U
 #define mcONLY_EVENTS 254U
 #define mcONE_RECORD 0U
 #define mcONCE 1U
 #define mcON 1
 #define mcOFF 0
 #define mcNULL 1U
 #define mcNOT_AXIS_RELATED 4294967295U
 #define mcNON_PERIODIC 0
 #define mcNO_TEXT 0U
 #define mcNO_START_COMP 1U
 #define mcNO_POSITION 0U
 #define mcNO_PARAMS 253U
 #define mcNO_STATES 253U
 #define mcNO_EVENTS 253U
 #define mcNO_CHANGE_COMP 2U
 #define mcNET_TRACE_GLOBAL 0U
 #define mcNEGATIVE_DIR 1U
 #define mcN_EDGE 1U
 #define mcMULTI_AXIS_TRACE 0U
 #define mcMOVE_VELOCITY_POS 1001
 #define mcMOVE_VELOCITY_NEG 1002
 #define mcMOVE_DECELERATION_POS 1004
 #define mcMOVE_DECELERATION_NEG 1006
 #define mcMOVE_CYCL_VEL_IPL_MODE 1011
 #define mcMOVE_CYCL_POS_IPL_MODE 1010
 #define mcMOVE_ACCELERATION_POS 1003
 #define mcMOVE_ACCELERATION_NEG 1005
 #define mcMOTOR 258U
 #define mcMODIFIED_SINE_CURVE 7U
 #define mcMODIFIED_ACCEL_TRAPEZOID 6U
 #define mcMIN_MASTER_COMP_DISTANCE 2U
 #define mcMIDDLE 5U
 #define mcMAX_VELOCITY_SYSTEM 8
 #define mcMAX_VELOCITY_APPL 9
 #define mcMAX_SLAVE_COMP_DISTANCE_POS 3U
 #define mcMAX_SLAVE_COMP_DISTANCE_NEG 4U
 #define mcMAX_POSITION_LAG 7
 #define mcMAX_POSITION_CHANGE 1016
 #define mcMAX_LOAD_SYSTEM 1015
 #define mcMAX_JERK 16
 #define mcMAX_IV_TIME 8U
 #define mcMAX_DECELERATION_SYSTEM 14
 #define mcMAX_DECELERATION_APPL 15
 #define mcMAX_ACCELERATION_SYSTEM 12
 #define mcMAX_ACCELERATION_APPL 13
 #define mcMASTER_POSITION_BASED 2U
 #define mcMASTER_POSITION 256U
 #define mcMASTER_DISTANCE_BASED 3U
 #define mcMANUAL_SEARCH 64U
 #define mcLOAD 276U
 #define mcLINEAR_CAM_PERIODIC 255U
 #define mcLINEAR_CAM_NON_PERIODIC 254U
 #define mcLINEAR_CAM 253U
 #define mcLIMIT_PARAMETERS 1
 #define mcLIMIT 40U
 #define mcLENGTH_ONLY 32U
 #define mcLEAD_OUT 4U
 #define mcLEAD_IN 2U
 #define mcLAST_POINT 0U
 #define mcISQ_RIPPLE 20U
 #define mcISQ_F3_NOTCH 512U
 #define mcISQ_F2_NOTCH 256U
 #define mcISQ_F1_NOTCH 128U
 #define mcIPL_QUADRATIC_NO_OVERSHOOT 4U
 #define mcIPL_QUADRATIC 2U
 #define mcIPL_OFF 0U
 #define mcIPL_LINEAR 1U
 #define mcINVERSE 255U
 #define mcINTERVAL_EVENT 16U
 #define mcINCLINED_SINE_CURVE 5U
 #define mcINC_REF 3U
 #define mcINC_ABS 4U
 #define mcINC 2U
 #define mcIN_WINDOW 20U
 #define mcIMMEDIATE 0U
 #define mcIDENTIFICATION 10U
 #define mcHORIZONTAL 0U
 #define mcHOME_SWITCH_GATE 8U
 #define mcHOME_SET_PHASE 7U
 #define mcHOME_RESTORE_POS 11U
 #define mcHOME_REF_PULSE 5U
 #define mcHOME_LIMIT_SWITCH 3U
 #define mcHOME_DIRECT 1U
 #define mcHOME_DEFAULT 0U
 #define mcHOME_DCM_CORR 10U
 #define mcHOME_DCM 9U
 #define mcHOME_BLOCK_TORQUE 13U
 #define mcHOME_BLOCK_DS 14U
 #define mcHOME_AXIS_REF 12U
 #define mcHOME_ABSOLUTE_CORR 6U
 #define mcHOME_ABSOLUTE 4U
 #define mcHOME_ABS_SWITCH 2U
 #define mcHOLDOFF_DISTANCE 16384U
 #define mcHARMONIC_COMBINATION 8U
 #define mcGREATER 4U
 #define mcGET_BRAKE_STATUS 16U
 #define mcGE 6U
 #define mcFLUX 1U
 #define mcFIRST_TRIGGER 2U
 #define mcFIRST_RM 0U
 #define mcFILE_TXT 2U
 #define mcFILE_CSV 1U
 #define mcFILE_BIN 0U
 #define mcFILE 1U
 #define mcFF_POS_MOVE 33U
 #define mcFF_NEG_MOVE 34U
 #define mcFF 32U
 #define mcFB_INPUTS 255
 #define mcFB_ERROR 2U
 #define mcEXCEED_PERIOD 8U
 #define mcEVERY_RECORD 1U
 #define mcEQUAL 2U
 #define mcENCODER 0U
 #define mcENABLE_POS_LAG_MONITORING 6
 #define mcENABLE_LIMIT_POS 4
 #define mcENABLE_LIMIT_NEG 5
 #define mcENABLE 2U
 #define mcEDGE_SENSITIVE 4U
 #define mcDITHER 32U
 #define mcDISTANCE_BASED 0U
 #define mcDIRECT 7U
 #define mcDEFAULT_MOVE_PARAMETERS 1012
 #define mcDATOBJ 0U
 #define mcCYCLIC_ALL_EVENTS 3U
 #define mcCYCLIC 2U
 #define mcCURRENT_DIR 2U
 #define mcCUBIC_SPLINE 256U
 #define mcCORRECT_CURRENT_CYCLE 32768U
 #define mcCONTINUE_CONTROLLER_OFF 128U
 #define mcCOMMANDED_VELOCITY 11
 #define mcCOMMANDED_POSITION 1
 #define mcCMD_WARNING 0U
 #define mcCMD_ERROR_V_STOP_CTRL_OFF 4U
 #define mcCMD_ERROR_STOP_CTRL_OFF 3U
 #define mcCMD_ERROR_STOP 2U
 #define mcCMD_ERROR 1U
 #define mcCLOSE 0U
 #define mcCHECK_HOMING_OFF 1U
 #define mcCHECK 1U
 #define mcCATCH_UP 4U
 #define mcCALCULATION 11U
 #define mcBRAKE_TEST_START 4U
 #define mcBRAKE_TEST_INIT 2U
 #define mcBRAKE_CONTROL_INIT 8U
 #define mcBLANK 0U
 #define mcBESTFIT_6TH_ORDER 1280U
 #define mcBESTFIT_5TH_ORDER 1024U
 #define mcBELOW_WINDOW 50U
 #define mcBASIS_PARAMETERS 2
 #define mcAXIS_WARNING 1U
 #define mcAXIS_PERIOD 1008
 #define mcAXIS_FACTOR 1007
 #define mcAXIS_ERROR 0U
 #define mcAVERAGE_WEIGHTED 4U
 #define mcAVERAGE 2U
 #define mcAUTOMAT_POS 100U
 #define mcAUT_POS_TOLERANCE 1009
 #define mcALL_STATES 255U
 #define mcALL_PARAMS 0U
 #define mcALL_EVENTS 255U
 #define mcALL_AXES 4294967295U
 #define mcADD_DATE_TIME 1U
 #define mcACTUAL_VELOCITY 10
 #define mcACT_CFG 1U
 #define mcACKNOWLEDGE_ALL 2U
 #define mcABSOLUTE_NO_RESET 2U
 #define mcABSOLUTE 0U
 #define mcABS 1U
 #define mcABOVE_WINDOW 40U
 #define mc5TH_ORDER_POLYNOMIAL 4U
#else
 _IEC_CONST unsigned short mcWRAP = 2U;
 _IEC_CONST unsigned char mcWITHOUT_FF = 1U;
 _IEC_CONST unsigned char mcWITH_FF = 0U;
 _IEC_CONST unsigned short mcWITHOUT_PERIOD = 4U;
 _IEC_CONST unsigned char mcWITHIN_PERIOD = 6U;
 _IEC_CONST unsigned char mcWITH_PARAM = 2U;
 _IEC_CONST unsigned char mcVERTICAL = 1U;
 _IEC_CONST unsigned short mcVELOCITY_CONTROL = 4U;
 _IEC_CONST unsigned char mcV_LIMIT_OFF = 2U;
 _IEC_CONST unsigned char mcV_LIMIT_CALC = 4U;
 _IEC_CONST unsigned short mcUSE_TN = 8U;
 _IEC_CONST unsigned char mcUSE_STOP_COMP = 4U;
 _IEC_CONST unsigned short mcUSE_FIRST_TRIGGER_POS = 64U;
 _IEC_CONST unsigned short mcUSE_FILTER_PAR = 4U;
 _IEC_CONST unsigned short mcUSE_AXIS_PERIOD = 16384U;
 _IEC_CONST unsigned short mcUPDATE_PERIOD = 32768U;
 _IEC_CONST unsigned short mcUNEQUAL = 5U;
 _IEC_CONST unsigned char mcTUNE_V_CONSTANT = 1U;
 _IEC_CONST unsigned char mcTUNE_STANDSTILL = 0U;
 _IEC_CONST unsigned short mcTRANSITION_ON = 1U;
 _IEC_CONST unsigned short mcTRANSITION_OFF = 0U;
 _IEC_CONST unsigned char mcTRACE_TRIGGER = 3U;
 _IEC_CONST unsigned char mcTRACE_TIME = 2U;
 _IEC_CONST unsigned char mcTRACE_STARTED = 20U;
 _IEC_CONST unsigned char mcTRACE_RING = 4U;
 _IEC_CONST unsigned char mcTRACE_REST = 5U;
 _IEC_CONST unsigned char mcTRACE_FINISHED = 1U;
 _IEC_CONST unsigned char mcTRACE_DELAY = 6U;
 _IEC_CONST unsigned char mcTIME_LIMIT = 8U;
 _IEC_CONST unsigned short mcTIME_BASED = 1U;
 _IEC_CONST unsigned short mcTEXT = 1U;
 _IEC_CONST unsigned short mcTEST = 31U;
 _IEC_CONST unsigned short mcT_FILTER_2 = 65U;
 _IEC_CONST unsigned short mcT_FILTER = 64U;
 _IEC_CONST unsigned short mcSWITCH_ON = 258U;
 _IEC_CONST unsigned short mcSWITCH_OFF = 259U;
 _IEC_CONST signed short mcSW_LIMIT_POS = 2;
 _IEC_CONST signed short mcSW_LIMIT_NEG = 3;
 _IEC_CONST float mcSW_END_SPF = 2;
 _IEC_CONST signed short mcSW_END_MONITORING = 1014;
 _IEC_CONST float mcSW_END_IGNORE = 1;
 _IEC_CONST float mcSW_END_ACTIVE = 0;
 _IEC_CONST unsigned short mcSTRAIGHT_LINE = 1U;
 _IEC_CONST signed short mcSTOP_INDEX = 1013;
 _IEC_CONST unsigned short mcSTOP = 261U;
 _IEC_CONST unsigned char mcSTEPPER = 31U;
 _IEC_CONST unsigned char mcSTART_ONLY = 3U;
 _IEC_CONST unsigned short mcSTART = 260U;
 _IEC_CONST unsigned char mcSTANDARD = 0U;
 _IEC_CONST unsigned char mcSPEED = 2U;
 _IEC_CONST unsigned short mcSMALLER = 1U;
 _IEC_CONST unsigned char mcSLOW_DOWN = 5U;
 _IEC_CONST unsigned short mcSLAVE_POSITION = 0U;
 _IEC_CONST unsigned short mcSIMULATION_READ = 265U;
 _IEC_CONST unsigned short mcSIMULATION_ON = 258U;
 _IEC_CONST unsigned short mcSIMULATION_OFF = 259U;
 _IEC_CONST unsigned short mcSIMULATION_INIT_ON = 256U;
 _IEC_CONST unsigned short mcSIMULATION_INIT = 512U;
 _IEC_CONST unsigned short mcSIMPLE_SINE_CURVE = 3U;
 _IEC_CONST unsigned char mcSHORTEST_WAY = 3U;
 _IEC_CONST unsigned short mcSHIFT_FROM_RESULT = 49U;
 _IEC_CONST unsigned short mcSHIFT_FROM_EXPECTED = 50U;
 _IEC_CONST unsigned char mcSET_OFFSET = 34U;
 _IEC_CONST unsigned short mcSE = 3U;
 _IEC_CONST unsigned short mcSAVE_RING_STARTIDX = 4437U;
 _IEC_CONST unsigned short mcSAVE = 341U;
 _IEC_CONST unsigned char mcSATURATION = 30U;
 _IEC_CONST unsigned short mcREVERSE = 8U;
 _IEC_CONST unsigned short mcRESTART = 273U;
 _IEC_CONST unsigned short mcRESET_RING_STARTIDX = 4416U;
 _IEC_CONST unsigned short mcRESET = 320U;
 _IEC_CONST unsigned char mcRELATIVE_NO_RESET = 3U;
 _IEC_CONST unsigned char mcRELATIVE = 1U;
 _IEC_CONST unsigned short mcQUEUED = 1U;
 _IEC_CONST unsigned short mcQUADRATIC_PARABOLA = 2U;
 _IEC_CONST unsigned char mcPOSITIVE_DIR = 0U;
 _IEC_CONST unsigned char mcPOSITION = 1U;
 _IEC_CONST plcbit mcPERIODIC = 1;
 _IEC_CONST unsigned char mcP_EDGE = 0U;
 _IEC_CONST signed short mcOVERRIDE = 1000;
 _IEC_CONST unsigned char mcOUT_WINDOW = 30U;
 _IEC_CONST unsigned short mcOPTIMIZED_VELOCITY = 512U;
 _IEC_CONST unsigned short mcOPTIMIZED_ACCELERATION = 768U;
 _IEC_CONST unsigned char mcOPEN = 1U;
 _IEC_CONST unsigned char mcONLY_PSM = 1U;
 _IEC_CONST unsigned char mcONLY_EVENTS = 254U;
 _IEC_CONST unsigned short mcONE_RECORD = 0U;
 _IEC_CONST unsigned short mcONCE = 1U;
 _IEC_CONST plcbit mcON = 1;
 _IEC_CONST plcbit mcOFF = 0;
 _IEC_CONST unsigned short mcNULL = 1U;
 _IEC_CONST unsigned long mcNOT_AXIS_RELATED = 4294967295U;
 _IEC_CONST plcbit mcNON_PERIODIC = 0;
 _IEC_CONST unsigned short mcNO_TEXT = 0U;
 _IEC_CONST unsigned char mcNO_START_COMP = 1U;
 _IEC_CONST unsigned char mcNO_POSITION = 0U;
 _IEC_CONST unsigned char mcNO_PARAMS = 253U;
 _IEC_CONST unsigned char mcNO_STATES = 253U;
 _IEC_CONST unsigned char mcNO_EVENTS = 253U;
 _IEC_CONST unsigned char mcNO_CHANGE_COMP = 2U;
 _IEC_CONST unsigned long mcNET_TRACE_GLOBAL = 0U;
 _IEC_CONST unsigned char mcNEGATIVE_DIR = 1U;
 _IEC_CONST unsigned char mcN_EDGE = 1U;
 _IEC_CONST unsigned long mcMULTI_AXIS_TRACE = 0U;
 _IEC_CONST signed short mcMOVE_VELOCITY_POS = 1001;
 _IEC_CONST signed short mcMOVE_VELOCITY_NEG = 1002;
 _IEC_CONST signed short mcMOVE_DECELERATION_POS = 1004;
 _IEC_CONST signed short mcMOVE_DECELERATION_NEG = 1006;
 _IEC_CONST signed short mcMOVE_CYCL_VEL_IPL_MODE = 1011;
 _IEC_CONST signed short mcMOVE_CYCL_POS_IPL_MODE = 1010;
 _IEC_CONST signed short mcMOVE_ACCELERATION_POS = 1003;
 _IEC_CONST signed short mcMOVE_ACCELERATION_NEG = 1005;
 _IEC_CONST unsigned short mcMOTOR = 258U;
 _IEC_CONST unsigned short mcMODIFIED_SINE_CURVE = 7U;
 _IEC_CONST unsigned short mcMODIFIED_ACCEL_TRAPEZOID = 6U;
 _IEC_CONST unsigned short mcMIN_MASTER_COMP_DISTANCE = 2U;
 _IEC_CONST unsigned char mcMIDDLE = 5U;
 _IEC_CONST signed short mcMAX_VELOCITY_SYSTEM = 8;
 _IEC_CONST signed short mcMAX_VELOCITY_APPL = 9;
 _IEC_CONST unsigned short mcMAX_SLAVE_COMP_DISTANCE_POS = 3U;
 _IEC_CONST unsigned short mcMAX_SLAVE_COMP_DISTANCE_NEG = 4U;
 _IEC_CONST signed short mcMAX_POSITION_LAG = 7;
 _IEC_CONST signed short mcMAX_POSITION_CHANGE = 1016;
 _IEC_CONST signed short mcMAX_LOAD_SYSTEM = 1015;
 _IEC_CONST signed short mcMAX_JERK = 16;
 _IEC_CONST unsigned char mcMAX_IV_TIME = 8U;
 _IEC_CONST signed short mcMAX_DECELERATION_SYSTEM = 14;
 _IEC_CONST signed short mcMAX_DECELERATION_APPL = 15;
 _IEC_CONST signed short mcMAX_ACCELERATION_SYSTEM = 12;
 _IEC_CONST signed short mcMAX_ACCELERATION_APPL = 13;
 _IEC_CONST unsigned short mcMASTER_POSITION_BASED = 2U;
 _IEC_CONST unsigned short mcMASTER_POSITION = 256U;
 _IEC_CONST unsigned short mcMASTER_DISTANCE_BASED = 3U;
 _IEC_CONST unsigned short mcMANUAL_SEARCH = 64U;
 _IEC_CONST unsigned short mcLOAD = 276U;
 _IEC_CONST unsigned char mcLINEAR_CAM_PERIODIC = 255U;
 _IEC_CONST unsigned char mcLINEAR_CAM_NON_PERIODIC = 254U;
 _IEC_CONST unsigned char mcLINEAR_CAM = 253U;
 _IEC_CONST float mcLIMIT_PARAMETERS = 1;
 _IEC_CONST unsigned char mcLIMIT = 40U;
 _IEC_CONST unsigned short mcLENGTH_ONLY = 32U;
 _IEC_CONST unsigned short mcLEAD_OUT = 4U;
 _IEC_CONST unsigned short mcLEAD_IN = 2U;
 _IEC_CONST unsigned short mcLAST_POINT = 0U;
 _IEC_CONST unsigned short mcISQ_RIPPLE = 20U;
 _IEC_CONST unsigned short mcISQ_F3_NOTCH = 512U;
 _IEC_CONST unsigned short mcISQ_F2_NOTCH = 256U;
 _IEC_CONST unsigned short mcISQ_F1_NOTCH = 128U;
 _IEC_CONST unsigned char mcIPL_QUADRATIC_NO_OVERSHOOT = 4U;
 _IEC_CONST unsigned char mcIPL_QUADRATIC = 2U;
 _IEC_CONST unsigned char mcIPL_OFF = 0U;
 _IEC_CONST unsigned char mcIPL_LINEAR = 1U;
 _IEC_CONST unsigned char mcINVERSE = 255U;
 _IEC_CONST unsigned short mcINTERVAL_EVENT = 16U;
 _IEC_CONST unsigned short mcINCLINED_SINE_CURVE = 5U;
 _IEC_CONST unsigned char mcINC_REF = 3U;
 _IEC_CONST unsigned char mcINC_ABS = 4U;
 _IEC_CONST unsigned char mcINC = 2U;
 _IEC_CONST unsigned char mcIN_WINDOW = 20U;
 _IEC_CONST unsigned short mcIMMEDIATE = 0U;
 _IEC_CONST unsigned short mcIDENTIFICATION = 10U;
 _IEC_CONST unsigned char mcHORIZONTAL = 0U;
 _IEC_CONST unsigned char mcHOME_SWITCH_GATE = 8U;
 _IEC_CONST unsigned char mcHOME_SET_PHASE = 7U;
 _IEC_CONST unsigned char mcHOME_RESTORE_POS = 11U;
 _IEC_CONST unsigned char mcHOME_REF_PULSE = 5U;
 _IEC_CONST unsigned char mcHOME_LIMIT_SWITCH = 3U;
 _IEC_CONST unsigned char mcHOME_DIRECT = 1U;
 _IEC_CONST unsigned char mcHOME_DEFAULT = 0U;
 _IEC_CONST unsigned char mcHOME_DCM_CORR = 10U;
 _IEC_CONST unsigned char mcHOME_DCM = 9U;
 _IEC_CONST unsigned char mcHOME_BLOCK_TORQUE = 13U;
 _IEC_CONST unsigned char mcHOME_BLOCK_DS = 14U;
 _IEC_CONST unsigned char mcHOME_AXIS_REF = 12U;
 _IEC_CONST unsigned char mcHOME_ABSOLUTE_CORR = 6U;
 _IEC_CONST unsigned char mcHOME_ABSOLUTE = 4U;
 _IEC_CONST unsigned char mcHOME_ABS_SWITCH = 2U;
 _IEC_CONST unsigned short mcHOLDOFF_DISTANCE = 16384U;
 _IEC_CONST unsigned short mcHARMONIC_COMBINATION = 8U;
 _IEC_CONST unsigned short mcGREATER = 4U;
 _IEC_CONST unsigned char mcGET_BRAKE_STATUS = 16U;
 _IEC_CONST unsigned short mcGE = 6U;
 _IEC_CONST unsigned char mcFLUX = 1U;
 _IEC_CONST unsigned short mcFIRST_TRIGGER = 2U;
 _IEC_CONST unsigned short mcFIRST_RM = 0U;
 _IEC_CONST unsigned short mcFILE_TXT = 2U;
 _IEC_CONST unsigned short mcFILE_CSV = 1U;
 _IEC_CONST unsigned short mcFILE_BIN = 0U;
 _IEC_CONST unsigned short mcFILE = 1U;
 _IEC_CONST unsigned short mcFF_POS_MOVE = 33U;
 _IEC_CONST unsigned short mcFF_NEG_MOVE = 34U;
 _IEC_CONST unsigned char mcFF = 32U;
 _IEC_CONST float mcFB_INPUTS = 255;
 _IEC_CONST unsigned char mcFB_ERROR = 2U;
 _IEC_CONST unsigned char mcEXCEED_PERIOD = 8U;
 _IEC_CONST unsigned short mcEVERY_RECORD = 1U;
 _IEC_CONST unsigned short mcEQUAL = 2U;
 _IEC_CONST unsigned char mcENCODER = 0U;
 _IEC_CONST signed short mcENABLE_POS_LAG_MONITORING = 6;
 _IEC_CONST signed short mcENABLE_LIMIT_POS = 4;
 _IEC_CONST signed short mcENABLE_LIMIT_NEG = 5;
 _IEC_CONST unsigned short mcENABLE = 2U;
 _IEC_CONST unsigned char mcEDGE_SENSITIVE = 4U;
 _IEC_CONST unsigned char mcDITHER = 32U;
 _IEC_CONST unsigned short mcDISTANCE_BASED = 0U;
 _IEC_CONST unsigned char mcDIRECT = 7U;
 _IEC_CONST signed short mcDEFAULT_MOVE_PARAMETERS = 1012;
 _IEC_CONST unsigned short mcDATOBJ = 0U;
 _IEC_CONST unsigned short mcCYCLIC_ALL_EVENTS = 3U;
 _IEC_CONST unsigned short mcCYCLIC = 2U;
 _IEC_CONST unsigned char mcCURRENT_DIR = 2U;
 _IEC_CONST unsigned short mcCUBIC_SPLINE = 256U;
 _IEC_CONST unsigned short mcCORRECT_CURRENT_CYCLE = 32768U;
 _IEC_CONST unsigned short mcCONTINUE_CONTROLLER_OFF = 128U;
 _IEC_CONST signed short mcCOMMANDED_VELOCITY = 11;
 _IEC_CONST signed short mcCOMMANDED_POSITION = 1;
 _IEC_CONST unsigned short mcCMD_WARNING = 0U;
 _IEC_CONST unsigned short mcCMD_ERROR_V_STOP_CTRL_OFF = 4U;
 _IEC_CONST unsigned short mcCMD_ERROR_STOP_CTRL_OFF = 3U;
 _IEC_CONST unsigned short mcCMD_ERROR_STOP = 2U;
 _IEC_CONST unsigned short mcCMD_ERROR = 1U;
 _IEC_CONST unsigned char mcCLOSE = 0U;
 _IEC_CONST unsigned char mcCHECK_HOMING_OFF = 1U;
 _IEC_CONST unsigned short mcCHECK = 1U;
 _IEC_CONST unsigned char mcCATCH_UP = 4U;
 _IEC_CONST unsigned short mcCALCULATION = 11U;
 _IEC_CONST unsigned char mcBRAKE_TEST_START = 4U;
 _IEC_CONST unsigned char mcBRAKE_TEST_INIT = 2U;
 _IEC_CONST unsigned char mcBRAKE_CONTROL_INIT = 8U;
 _IEC_CONST unsigned short mcBLANK = 0U;
 _IEC_CONST unsigned short mcBESTFIT_6TH_ORDER = 1280U;
 _IEC_CONST unsigned short mcBESTFIT_5TH_ORDER = 1024U;
 _IEC_CONST unsigned char mcBELOW_WINDOW = 50U;
 _IEC_CONST float mcBASIS_PARAMETERS = 2;
 _IEC_CONST unsigned char mcAXIS_WARNING = 1U;
 _IEC_CONST signed short mcAXIS_PERIOD = 1008;
 _IEC_CONST signed short mcAXIS_FACTOR = 1007;
 _IEC_CONST unsigned char mcAXIS_ERROR = 0U;
 _IEC_CONST unsigned short mcAVERAGE_WEIGHTED = 4U;
 _IEC_CONST unsigned short mcAVERAGE = 2U;
 _IEC_CONST unsigned char mcAUTOMAT_POS = 100U;
 _IEC_CONST signed short mcAUT_POS_TOLERANCE = 1009;
 _IEC_CONST unsigned char mcALL_STATES = 255U;
 _IEC_CONST unsigned char mcALL_PARAMS = 0U;
 _IEC_CONST unsigned char mcALL_EVENTS = 255U;
 _IEC_CONST unsigned long mcALL_AXES = 4294967295U;
 _IEC_CONST unsigned short mcADD_DATE_TIME = 1U;
 _IEC_CONST signed short mcACTUAL_VELOCITY = 10;
 _IEC_CONST unsigned short mcACT_CFG = 1U;
 _IEC_CONST unsigned short mcACKNOWLEDGE_ALL = 2U;
 _IEC_CONST unsigned char mcABSOLUTE_NO_RESET = 2U;
 _IEC_CONST unsigned char mcABSOLUTE = 0U;
 _IEC_CONST unsigned char mcABS = 1U;
 _IEC_CONST unsigned char mcABOVE_WINDOW = 40U;
 _IEC_CONST unsigned short mc5TH_ORDER_POLYNOMIAL = 4U;
#endif


/* Variables */


/* Datatypes and datatypes of function blocks */
typedef struct MC_ACP_ENCOD_REF
{
	unsigned long Axis;
	unsigned char Slot;
} MC_ACP_ENCOD_REF;

typedef struct MC_ACP_ENCOD_PARAM_REF
{
	unsigned char HomingMode;
	plcbit ReadOffset;
	float Position;
	signed long Offset;
} MC_ACP_ENCOD_PARAM_REF;

typedef struct MC_ADV_LIMITLOAD_REF
{
	unsigned short LoadPosAccelParID;
	unsigned short LoadPosDecelParID;
	unsigned short LoadNegAccelParID;
	unsigned short LoadNegDecelParID;
} MC_ADV_LIMITLOAD_REF;

typedef struct MC_ADV_OFFSETVELOCITY_REF
{
	unsigned short VelocityParID;
	unsigned short PosVelocityTriggerParID;
	unsigned short NegVelocityTriggerParID;
} MC_ADV_OFFSETVELOCITY_REF;

typedef struct MC_ADVANCED_CUT_PAR_REF
{
	signed short CutOverspeed;
	float CutterRadius;
	unsigned char NumberOfKnives;
	unsigned short StartMode;
	float CutPosition;
	float FirstCutPosition;
	float StartInterval;
	float MasterStartDistance;
	unsigned char CamTableID;
	unsigned short MasterParID;
	float MasterMaxVelocity;
} MC_ADVANCED_CUT_PAR_REF;

typedef struct MC_ADVANCED_GEAR_PAR_REF
{
	float Acceleration;
	float Deceleration;
	float JoltTime;
	unsigned char CompensationSelector;
	unsigned short MasterParID;
	float MasterMaxVelocity;
} MC_ADVANCED_GEAR_PAR_REF;

typedef struct MC_ADVANCEDSHIFTPAR_REF
{
	unsigned short ShiftParID;
	float MasterMaxVelocity;
} MC_ADVANCEDSHIFTPAR_REF;

typedef struct MC_ADV_OFFSETZONE_REF
{
	unsigned short ShiftParID;
	float MasterMaxVelocity;
	float Period;
	unsigned short ProfileBasis;
	unsigned short ShiftMode;
} MC_ADV_OFFSETZONE_REF;

typedef struct MC_AUT_COMP_DATA_REF
{
	float MaxMasterVelocity;
	float MasterCompDistance;
	float SlaveCompDistance;
	float StartSlope;
	float EndSlope;
	float MaxSlaveCompVelocity;
	float MinSlaveCompVelocity;
	float MaxSlaveAccelComp1;
	float MaxSlaveAccelComp2;
} MC_AUT_COMP_DATA_REF;

typedef struct MC_AUTDATA_EVENT_TYP
{
	unsigned char Type;
	unsigned char Attribute;
	unsigned long Action;
	unsigned char NextState;
} MC_AUTDATA_EVENT_TYP;

typedef struct MC_AUTDATA_STATE_TYP
{
	unsigned char DisableStateInit;
	unsigned short CamProfileIndex;
	signed long MasterFactor;
	signed long SlaveFactor;
	unsigned char CompMode;
	float MasterCompDistance;
	float SlaveCompDistance;
	unsigned short RepeatCounterInit;
	unsigned short RepeatCounterSet;
	float MasterCamLeadIn;
	unsigned short ExtendedCompLimits;
	float MinMasterCompDistance;
	float MinSlaveCompDistance;
	float MaxSlaveCompDistance;
	float MinSlaveCompVelocity;
	float MaxSlaveCompVelocity;
	float MaxSlaveAccelComp1;
	float MaxSlaveAccelComp2;
	float SlaveCompJoltTime;
	unsigned short MasterParID;
	struct MC_AUTDATA_EVENT_TYP Event[5];
} MC_AUTDATA_STATE_TYP;

typedef struct MC_AUTDATA_TYP
{
	unsigned long Master;
	float StartPosition;
	signed long StartPositionDINT;
	float StartInterval;
	float EventStartPositionInInterval[5];
	unsigned char StartState;
	float StartMaRelPos;
	unsigned char MasterStartPosMode;
	float MaxMasterVelocity;
	unsigned short MasterParID;
	unsigned short AddMasterParID;
	unsigned short AddSlaveParID;
	unsigned short SlaveFactorParID;
	unsigned short EventParID;
	unsigned short EventParID2;
	unsigned short EventParID3;
	unsigned short EventParID4;
	unsigned short SlaveLatchParID;
	struct MC_AUTDATA_STATE_TYP State[15];
} MC_AUTDATA_TYP;

typedef struct MC_AUTINITOPTIONS_REF
{
	unsigned char GlobalParams;
	unsigned char StateIndex;
	unsigned char EventIndex;
	unsigned char MaxStatesPerCycle;
	unsigned char ParLock;
	plcbit Force;
} MC_AUTINITOPTIONS_REF;

typedef struct MC_BRAKE_TEST_REF
{
	float TestTorque;
	float TestDuration;
	float PositionLimit;
	plcbit TestMode;
} MC_BRAKE_TEST_REF;

typedef struct MC_BRAKE_MODE_REF
{
	plcbit AutomaticControl;
	plcbit RestrictBrakeControl;
	plcbit ControlMonitoring;
	plcbit MovementMonitoring;
	plcbit VoltageMonitoring;
	plcbit TestAtPowerOn;
	plcbit TestAtPowerOff;
	plcbit AutomaticInductionStop;
	float ControlMonitoringFilterTime;
	plcbit EnableSBTRequestBySMC;
} MC_BRAKE_MODE_REF;

typedef struct MC_BRAKE_CONFIG_REF
{
	struct MC_BRAKE_TEST_REF BrakeTest;
	struct MC_BRAKE_MODE_REF BrakeMode;
} MC_BRAKE_CONFIG_REF;

typedef struct MC_BR_EVINPUT_REF
{
	unsigned short EventSourceParID;
	unsigned char Edge;
} MC_BR_EVINPUT_REF;

typedef struct MC_BR_TRIGGER_REF
{
	unsigned short EventSourceParID;
	unsigned short ProbeParID;
	unsigned char Edge;
	float MinWidth;
	float MaxWidth;
	signed long SensorDelay;
} MC_BR_TRIGGER_REF;

typedef struct MC_CALC_CAM_CONFIG_REF
{
	unsigned short Mode;
	plcbit CamType;
	unsigned char NumberOfPolynomials;
	signed long MasterPeriod;
	float StartSlope;
	float StartCurvature;
	float EndSlope;
	float EndCurvature;
} MC_CALC_CAM_CONFIG_REF;

typedef struct MC_POLYNOMIAL_DATA
{
	float a;
	float b;
	float c;
	float d;
	float e;
	float f;
	float g;
	float x;
	unsigned long Reserve;
} MC_POLYNOMIAL_DATA;

typedef struct MC_CAMPROFILE_TYP
{
	signed long MasterPeriod;
	signed long SlavePeriod;
	unsigned long PolynomialNumber;
	struct MC_POLYNOMIAL_DATA PolynomialData[64];
} MC_CAMPROFILE_TYP;

typedef struct MC_CAMSWITCH_REF
{
	signed short TrackNumber;
	float FirstOnPosition[16];
	float LastOnPosition[16];
	float Period;
} MC_CAMSWITCH_REF;

typedef struct MC_CAM_SECTION_TYP
{
	float MasterPosition;
	float SlavePosition;
	float FirstDerivative;
	float SecondDerivative;
	unsigned char Mode;
	unsigned short Type;
	float InflectionPoint;
} MC_CAM_SECTION_TYP;

typedef struct MC_CAM_SECTIONS_TYP
{
	struct MC_CAM_SECTION_TYP Section[65];
} MC_CAM_SECTIONS_TYP;

typedef struct MC_CYCLIC_POSITION
{
	signed long Integer;
	float Real;
} MC_CYCLIC_POSITION;

typedef struct MC_CYCLIC_POSITION_REF
{
	signed long Integer;
	float Real;
} MC_CYCLIC_POSITION_REF;

typedef struct MC_CYCLIC_VALUE_REF
{
	signed long Integer;
	float Real;
} MC_CYCLIC_VALUE_REF;

typedef struct MC_DATOBJ_REF
{
	plcstring Name[33];
	unsigned short Type;
	unsigned short Format;
	plcstring Device[33];
} MC_DATOBJ_REF;

typedef struct MC_DRIVESTATUS_TYP
{
	plcbit Simulation;
	plcbit NetworkInit;
	plcbit HomeSwitch;
	plcbit PosHWSwitch;
	plcbit NegHWSwitch;
	plcbit Trigger1;
	plcbit Trigger2;
	plcbit DriveEnable;
	plcbit ControllerReady;
	plcbit ControllerStatus;
	plcbit HomingOk;
	plcbit AxisError;
	plcbit LagWarning;
	plcbit ResetDone;
} MC_DRIVESTATUS_TYP;

typedef struct MC_ENDLESS_POSITION_DATA
{
	signed long MTPhase;
	signed long MTDiffInteger;
	signed long MTDiffFract;
	signed long RefOffset;
	unsigned long Checksum;
} MC_ENDLESS_POSITION_DATA;

typedef struct MC_ENDLESS_POSITION
{
	struct MC_ENDLESS_POSITION_DATA EndlessPositionData[2];
} MC_ENDLESS_POSITION;

typedef struct MC_ENDLESS_POSITION_ACP_ENC_TYP
{
	signed long EndlessPositionDataAcpEnc[16];
} MC_ENDLESS_POSITION_ACP_ENC_TYP;

typedef struct MC_ERRORRECORD_REF
{
	unsigned short ParID;
	unsigned short Number;
	unsigned long Info;
	unsigned char Type;
} MC_ERRORRECORD_REF;

typedef struct MC_ERRORTEXTCONFIG_REF
{
	unsigned short Format;
	unsigned short LineLength;
	unsigned short DataLength;
	unsigned long DataAddress;
	plcstring DataObjectName[13];
} MC_ERRORTEXTCONFIG_REF;

typedef struct MC_INPUT_REF
{
	unsigned long Axis;
	unsigned char Slot;
	unsigned char Channel;
} MC_INPUT_REF;

typedef struct MC_SWITCHES_REF
{
	float FirstOnPosition[64];
	float LastOnPosition[64];
} MC_SWITCHES_REF;

typedef struct MC_MASTER_SWITCHES_REF
{
	unsigned long Master;
	float Period;
	float MasterStartPosition;
	struct MC_SWITCHES_REF Switches[5];
	unsigned short MasterParID;
} MC_MASTER_SWITCHES_REF;

typedef struct MC_ADVANCED_MOVE_CYC_REF
{
	float Velocity;
	float Acceleration;
	float Deceleration;
	unsigned short SetValueParID;
	unsigned short AdditiveParID;
	plcbit DisableJoltTime;
	plcbit CoordinatedMovement;
} MC_ADVANCED_MOVE_CYC_REF;

typedef struct MC_NETTRACE_REF
{
	unsigned long Type;
	unsigned long Reserve;
} MC_NETTRACE_REF;

typedef struct MC_NETTRACECONFIG_REF
{
	struct MC_DATOBJ_REF DatObj;
	struct MC_NETTRACE_REF NetTrace;
} MC_NETTRACECONFIG_REF;

typedef struct MC_OUTPUT_REF
{
	unsigned long Axis;
	unsigned char Slot;
	unsigned char Channel;
} MC_OUTPUT_REF;

typedef struct MC_OUTPUT_OPTIONS_REF
{
	unsigned long Axis;
	unsigned short DestinationParID;
	unsigned char Slot;
	unsigned char Channel;
} MC_OUTPUT_OPTIONS_REF;

typedef struct MC_TRACETRIGGER_REF
{
	unsigned long Axis;
	unsigned short ParID;
	unsigned char Event;
	unsigned char Reserve;
	float Threshold;
	float Window;
} MC_TRACETRIGGER_REF;

typedef struct MC_TRACEPARAM_REF
{
	unsigned long Axis;
	unsigned short ParID;
	unsigned short Reserve;
} MC_TRACEPARAM_REF;

typedef struct MC_PARTRACE_REF
{
	unsigned long Type;
	unsigned long Reserve;
	float TracingTime;
	float SamplingTime;
	float Delay;
	float NetTriggerDelay;
	struct MC_TRACETRIGGER_REF Trigger;
	struct MC_TRACEPARAM_REF Parameter[30];
} MC_PARTRACE_REF;

typedef struct MC_PARTRACECONFIG_REF
{
	struct MC_DATOBJ_REF DatObj;
	struct MC_PARTRACE_REF ParTrace;
} MC_PARTRACECONFIG_REF;

typedef struct MC_POWERDATA_REF
{
	unsigned long IntervalNumber;
	signed long IntervalDuration;
	float AverageActivePower;
	float AverageReactivePower;
	float MaximumActivePower;
	float MinimalActivePower;
	float ConsumedEnergy;
	float RegeneratedEnergy;
	float EnergyBalance;
	float Reserve1;
	float Reserve2;
	float Reserve3;
	float Reserve4;
	float Reserve5;
} MC_POWERDATA_REF;

typedef struct MC_POWER_STAGE_CHECK_REF
{
	plcbit CurrentFlowTestPhase1Off;
	plcbit CurrentFlowTestPhase2Off;
	plcbit CurrentFlowTestPhase3Off;
	plcbit OffsetCurrentWarningOff;
	plcbit MotorSpeedWarningOff;
	plcbit OffsetCurrentMeasurementOff;
	plcbit CurrentFlowTestExtBleederOff;
	plcbit CurrentFlowTestIntBleederOn;
	plcbit OCMonitoringExtBleederOff;
	plcbit SumCurrentMonitoringOff;
} MC_POWER_STAGE_CHECK_REF;

typedef struct MC_RECORD_REF
{
	unsigned short Size;
	unsigned short Reserve1;
	unsigned char OneByteCount;
	unsigned char TwoByteCount;
	unsigned char FourByteCount;
	unsigned char Reserve2;
	unsigned short ParID[12];
	unsigned short Reserve3[4];
} MC_RECORD_REF;

typedef struct MC_RECORD_INFO_REF
{
	struct MC_RECORD_REF Record[8];
} MC_RECORD_INFO_REF;

typedef struct MC_SETUP_CONTROLLER_PAR_REF
{
	unsigned short Mode;
	unsigned char Orientation;
	unsigned char OperatingPoint;
	float MaxCurrentPercent;
	float MaxSpeedPercent;
	float MaxDistance;
	float MaxLagError;
	float PropAmplificationPercent;
	unsigned long SignalOrder;
} MC_SETUP_CONTROLLER_PAR_REF;

typedef struct MC_SETUP_CONTROLLER_CFG_REF
{
	struct MC_DATOBJ_REF DatObj;
	struct MC_SETUP_CONTROLLER_PAR_REF SetupControllerPar;
} MC_SETUP_CONTROLLER_CFG_REF;

typedef struct MC_SETUP_IND_MOTOR_PAR_OPT_REF
{
	unsigned char Phase;
	unsigned char PolePairs;
	float VoltageConstant;
	float MaxSpeed;
	float StallTorque;
	float RatedTorque;
	float PeakTorque;
	float TorqueConstant;
	float StallCurrent;
	float PeakCurrent;
	float MagnetizingCurrent;
	float PhaseCrossSection;
	float InvCharacteristicGain;
	float InvCharacteristicExponent;
} MC_SETUP_IND_MOTOR_PAR_OPT_REF;

typedef struct MC_SETUP_IND_MOTOR_PAR_REF
{
	unsigned short Mode;
	float RatedVoltage;
	float RatedCurrent;
	float RatedSpeed;
	float RatedFrequency;
	float PowerFactor;
	float ThermalTrippingTime;
	struct MC_SETUP_IND_MOTOR_PAR_OPT_REF OptionalData;
} MC_SETUP_IND_MOTOR_PAR_REF;

typedef struct MC_SETUP_IND_MOTOR_CFG_REF
{
	struct MC_DATOBJ_REF DatObj;
	struct MC_SETUP_IND_MOTOR_PAR_REF SetupInductionMotorPar;
} MC_SETUP_IND_MOTOR_CFG_REF;

typedef struct MC_SETUP_ISQ_RIPPLE_PAR_REF
{
	unsigned short Mode;
	unsigned short RefSystem;
	float PositionOffset;
	float Velocity;
} MC_SETUP_ISQ_RIPPLE_PAR_REF;

typedef struct MC_SETUP_ISQ_RIPPLE_CFG_REF
{
	struct MC_DATOBJ_REF DatObj;
	struct MC_SETUP_ISQ_RIPPLE_PAR_REF SetupIsqRipplePar;
} MC_SETUP_ISQ_RIPPLE_CFG_REF;

typedef struct MC_SETUP_MOTOR_PHA_PAR_REF
{
	unsigned short Mode;
	float Current;
	float Time;
} MC_SETUP_MOTOR_PHA_PAR_REF;

typedef struct MC_SETUP_MOTOR_PHA_CFG_REF
{
	struct MC_DATOBJ_REF DatObj;
	struct MC_SETUP_MOTOR_PHA_PAR_REF SetupMotorPhasingPar;
} MC_SETUP_MOTOR_PHA_CFG_REF;

typedef struct MC_SETUP_OUTPUT_REF
{
	float Quality;
	unsigned long DataObjectIdent;
} MC_SETUP_OUTPUT_REF;

typedef struct MC_SETUP_PHASING_RESULT_REF
{
	unsigned char PolePairs;
	float CommutationOffset;
} MC_SETUP_PHASING_RESULT_REF;

typedef struct MC_SETUP_SYNC_MOTOR_PAR_OPT_REF
{
	unsigned char Phase;
	float VoltageConstant;
	float MaxSpeed;
	float StallTorque;
	float TorqueConstant;
	float StallCurrent;
	float PhaseCrossSection;
	float InvCharacteristicGain;
	float InvCharacteristicExponent;
} MC_SETUP_SYNC_MOTOR_PAR_OPT_REF;

typedef struct MC_SETUP_SYNC_MOTOR_PAR_REF
{
	unsigned short Mode;
	float RatedVoltage;
	float RatedCurrent;
	float RatedSpeed;
	float RatedTorque;
	unsigned char PolePairs;
	float PeakCurrent;
	float PeakTorque;
	float ThermalTrippingTime;
	struct MC_SETUP_SYNC_MOTOR_PAR_OPT_REF OptionalData;
} MC_SETUP_SYNC_MOTOR_PAR_REF;

typedef struct MC_SETUP_SYNC_MOTOR_CFG_REF
{
	struct MC_DATOBJ_REF DatObj;
	struct MC_SETUP_SYNC_MOTOR_PAR_REF SetupSynchronMotorPar;
} MC_SETUP_SYNC_MOTOR_CFG_REF;

typedef struct MC_TRACK_OPTIONS_REF
{
	float OnCompensation;
	float OffCompensation;
	float Filter;
	float Hysteresis;
	plcbit DisableNegativeDirection;
} MC_TRACK_OPTIONS_REF;

typedef struct MC_TRACK_REF
{
	plctime OnCompensation;
	plctime OffCompensation;
	float Hysteresis;
} MC_TRACK_REF;

typedef struct MC_TRIGGER_REF
{
	unsigned char InputSource;
	unsigned char Edge;
	unsigned char PosSource;
	unsigned char TouchProbeID;
} MC_TRIGGER_REF;

typedef struct MC_PARID_INFO_REF
{
	unsigned short DataType;
	unsigned short DataLength;
} MC_PARID_INFO_REF;

typedef struct MC_HW_INFO_DRIVE_REF
{
	plcstring ModelNumber[20];
	plcstring SerialNumber[20];
	plcstring Revision[4];
	unsigned long MissionTimeEndDate;
} MC_HW_INFO_DRIVE_REF;

typedef struct MC_HW_INFO_CARD_REF
{
	plcstring ModelNumber[20];
	plcstring SerialNumber[20];
	plcstring Revision[4];
} MC_HW_INFO_CARD_REF;

typedef struct MC_HW_INFO_MOTOR_REF
{
	plcstring ModelNumber[20];
	plcstring SerialNumber[20];
	plcstring Revision[4];
} MC_HW_INFO_MOTOR_REF;

typedef struct MC_HARDWARE_INFO_REF
{
	struct MC_HW_INFO_DRIVE_REF Drive;
	struct MC_HW_INFO_CARD_REF Card[4];
	struct MC_HW_INFO_MOTOR_REF Motor[2];
} MC_HARDWARE_INFO_REF;

typedef struct MC_SEND_INFO_REF
{
	plcbit InUse;
	unsigned short ParID;
	plcbit ChangeAllowed;
} MC_SEND_INFO_REF;

typedef struct MC_RECEIVE_INFO_REF
{
	plcbit InUse;
	unsigned short ParID;
	plcbit ChangeAllowed;
	unsigned char SendNodeNumber;
	unsigned long SendAxisRef;
	plcstring SendAxisObjectName[49];
	unsigned char SendAxisDriveChannel;
	unsigned short SendAxisNetworkType;
	unsigned short SendAxisNetworkIndex;
	unsigned char InterpolationMode;
	unsigned short DataOffset;
	unsigned short DataType;
} MC_RECEIVE_INFO_REF;

typedef struct MC_TRANSFER_INFO_REF
{
	struct MC_SEND_INFO_REF SendChannel[4];
	struct MC_RECEIVE_INFO_REF ReceiveChannel[6];
} MC_TRANSFER_INFO_REF;

typedef struct MC_NET_ENC_INFO_REF
{
	unsigned char Type;
	unsigned long AdrDeviceString;
	unsigned long AdrPosition;
	unsigned long AdrPositionHW;
	unsigned long AdrReferencePosition;
	unsigned long AdrReferenceCount;
	unsigned long AdrPositionTime;
	unsigned long AdrEncoderStatus;
} MC_NET_ENC_INFO_REF;

typedef struct MC_NET_ENC_PARAM_REF
{
	unsigned long ScaleIncrements;
	unsigned long IncValueRangeHW;
	unsigned long IncValueRangeLW;
	unsigned long ScaleUnits;
	unsigned long ScaleRevolutions;
	unsigned char CountDirection;
} MC_NET_ENC_PARAM_REF;

typedef struct MC_NET_ENC_CONFIG_REF
{
	float Timeout;
	plcbit Interpolation;
	plcbit Extrapolation;
	float FilterTime;
	float NetworkCompensation;
} MC_NET_ENC_CONFIG_REF;

typedef struct MC_0068_IS_TYP
{
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	unsigned char LockID;
	unsigned short C_ErrorID;
	signed long C_EncoderOffset;
	unsigned char C_HomingMode;
	unsigned char C_HomingModeBits;
	plcbit C_ReadOffset;
	unsigned char C_Slot;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned short BitIndex;
	signed long C_Position;
	signed long C_Offset;
	unsigned short HomingStatusOffset;
	unsigned char HomingStatusRecIndex;
	unsigned char FbID;
	unsigned long startTick;
	unsigned char C_NCHomingMode;
	unsigned char Reserve1;
	unsigned short Reserve2;
} MC_0068_IS_TYP;

typedef struct MC_0069_IS_TYP
{
	plcbit C_Valid;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned short C_ParID;
	unsigned long C_DataAddress;
	unsigned short C_DataType;
	unsigned short C_Mode;
	unsigned short Offset;
	unsigned char RecIndex;
	unsigned char ParIndex;
	unsigned char state;
	unsigned char LockID;
} MC_0069_IS_TYP;

typedef struct MC_0070_IS_TYP
{
	plcbit C_Valid;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned short C_ParID;
	unsigned long C_DataAddress;
	unsigned short C_DataType;
	unsigned short C_Mode;
	unsigned char ParIndex;
	unsigned char state;
	unsigned char DataLength;
	unsigned char LockID;
	unsigned short Reserve;
} MC_0070_IS_TYP;

typedef struct MC_0071_IS_TYP
{
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned short C_SimulationCommand;
} MC_0071_IS_TYP;

typedef struct MC_0076_IS_TYP
{
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned short C_ErrorID;
	unsigned char C_GlobalParams;
	unsigned char C_StateIndex;
	unsigned char C_EventIndex;
	unsigned char C_MaxStatesPerCycle;
	unsigned char C_ParLock;
	struct MC_AUTDATA_TYP C_AutData;
	unsigned char LockIDMa;
	unsigned char LockIDPar;
	unsigned char C_Force;
	unsigned char readSlot;
	unsigned char sendSlot;
	unsigned short paramCount;
	plcbit lockActive;
	unsigned char actStatesInCycle;
	unsigned char stateCount;
	unsigned char eventCount;
	unsigned char stateParInImg;
	plcbit resetStates;
	plcbit setStateIndex;
	unsigned char lastState;
	unsigned char nextState;
	unsigned char state;
	unsigned char LockIDSend;
	unsigned char LockIDReceive;
	unsigned short Reserve2;
} MC_0076_IS_TYP;

typedef struct MC_0077_IS_TYP
{
	plcbit C_Execute;
	unsigned char LockID;
	struct MC_ERRORRECORD_REF C_ErrorRecord;
	struct MC_ERRORTEXTCONFIG_REF C_Configuration;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned short C_ErrorID;
	unsigned char state;
} MC_0077_IS_TYP;

typedef struct MC_0078_IS_TYP
{
	plcbit C_Execute;
	unsigned short C_Command;
	struct MC_NETTRACECONFIG_REF C_Configuration;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned short C_ErrorID;
	struct MC_ERRORRECORD_REF C_ErrorRecord;
	unsigned char state;
} MC_0078_IS_TYP;

typedef struct MC_0080_IS_TYP
{
	plcbit C_Execute;
	unsigned short C_Command;
	struct MC_PARTRACECONFIG_REF C_Configuration;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned short C_ErrorID;
	struct MC_ERRORRECORD_REF C_ErrorRecord;
	plcbit StartSaveStarted;
	unsigned char state;
} MC_0080_IS_TYP;

typedef struct MC_0081_IS_TYP
{
	struct MC_CYCLIC_POSITION C_CyclicPosition;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	unsigned short C_PositionParID;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	plcbit C_Valid;
	unsigned short C_ErrorID;
	unsigned short C_ReceiveParID;
	unsigned short readSlot;
	unsigned short Reserve1;
	unsigned char LockIDSend;
	unsigned char LockIDReceive;
	unsigned char LockIDPar;
	unsigned char MoveID;
	unsigned char state;
} MC_0081_IS_TYP;

typedef struct MC_0082_IS_TYP
{
	unsigned short C_ParID;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned short C_ErrorID;
	plcbit C_Valid;
	unsigned char LockIDSend;
	struct MC_CYCLIC_POSITION C_CyclicPosition;
	signed long C_Offset;
	unsigned short sendSlot;
	unsigned short MnPResParIndex;
	unsigned char LockIDMa;
	unsigned char state;
	unsigned char Reserve1;
	unsigned char Reserve2;
} MC_0082_IS_TYP;

typedef struct MC_0083_IS_TYP
{
	plcbit C_Execute;
	unsigned long C_DataAddress;
	float C_MasterPosition;
	unsigned long C_MasterFactor;
	signed long C_SlaveFactor;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned short C_ErrorID;
	float C_SlavePosition;
	unsigned char state;
} MC_0083_IS_TYP;

typedef struct MC_0084_IS_TYP
{
	plcbit C_Execute;
	unsigned long C_DataAddress;
	float C_MasterStartPosition;
	float C_SlavePosition;
	unsigned long C_MasterFactor;
	signed long C_SlaveFactor;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned short C_ErrorID;
	float C_MasterPosition;
	unsigned char state;
} MC_0084_IS_TYP;

typedef struct MC_0088_IS_TYP
{
	plcbit C_Execute;
	unsigned short C_Command;
	struct MC_SETUP_IND_MOTOR_CFG_REF C_Configuration;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	unsigned short C_ErrorID;
	struct MC_SETUP_OUTPUT_REF C_SetupOutput;
	unsigned char LockIDPar;
	unsigned char Reserve;
	unsigned char state;
} MC_0088_IS_TYP;

typedef struct MC_0089_IS_TYP
{
	unsigned char C_Mode;
	unsigned short C_IntervalTime;
	plcbit C_RestartInterval;
	struct MC_BR_EVINPUT_REF C_EventInput;
	plcbit C_Valid;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned short C_ErrorID;
	unsigned short CC_ErrorID;
	struct MC_POWERDATA_REF C_PowerData;
	unsigned short C_MissedIntervals;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned short IntervalDurationOffset;
	unsigned char IntervalDurationRecIndex;
	unsigned short AverageActivePowerOffset;
	unsigned char AverageActivePowerRecIndex;
	unsigned short AverageReactivePowerOffset;
	unsigned char AverageReactivePowerRecIndex;
	unsigned short MaximumActivePowerOffset;
	unsigned char MaximumActivePowerRecIndex;
	unsigned short MinimalActivePowerOffset;
	unsigned char MinimalActivePowerRecIndex;
	unsigned short ConsumedEnergyOffset;
	unsigned char ConsumedEnergyRecIndex;
	unsigned short RegEnergyOffset;
	unsigned char RegEnergyRecIndex;
	unsigned char LockIDPmet;
	unsigned char CDLockID;
	unsigned short Reserve1;
	unsigned short Reserve2;
	signed long IntervalTimeMin;
	unsigned char ParamCnt;
	unsigned char CountCnt;
	unsigned short ParamArrayCount;
	unsigned short CountOffset[8];
	unsigned char CountRecIndex[8];
	unsigned char saveParamCnt;
	unsigned char firstFreeParam;
	unsigned char lastFreeParam;
	plcbit dataConfigDone;
	unsigned char SptID;
	unsigned short VarIndex;
	unsigned short CompIndex;
	unsigned char NextState;
	unsigned short ReserveOffset01;
	unsigned char ReserveRecIndex01;
	unsigned short ReserveOffset02;
	unsigned char ReserveRecIndex02;
	unsigned short ReserveOffset03;
	unsigned char ReserveRecIndex03;
	unsigned short ReserveOffset04;
	unsigned char ReserveRecIndex04;
	unsigned short ReserveOffset05;
	unsigned char ReserveRecIndex05;
	unsigned long Reserve3;
	unsigned long Reserve4;
	unsigned long CyclicDataTaskClassCycleTime;
	unsigned char Reserve5;
	unsigned short Reserve6;
	unsigned char state;
} MC_0089_IS_TYP;

typedef struct MC_0090_IS_TYP
{
	plcbit C_Execute;
	unsigned short C_Command;
	struct MC_SETUP_CONTROLLER_CFG_REF C_Configuration;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	unsigned short C_ErrorID;
	struct MC_SETUP_OUTPUT_REF C_SetupOutput;
	unsigned char LockIDPar;
	unsigned char Reserve;
	unsigned char state;
} MC_0090_IS_TYP;

typedef struct MC_0092_IS_TYP
{
	float C_CyclicVelocity;
	unsigned char C_Direction;
	float C_Acceleration;
	float C_Deceleration;
	unsigned short C_VelocityParID;
	plcbit C_Valid;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	unsigned short C_ErrorID;
	unsigned short C_ReceiveParID;
	unsigned char LockIDPar;
	unsigned char MoveID;
	unsigned short VarIndex;
	unsigned char SptID;
	unsigned short readSlot;
	unsigned short Reserve1;
	unsigned char LockIDSend;
	unsigned char LockIDReceive;
	unsigned short ArithIndex;
	unsigned char state;
} MC_0092_IS_TYP;

typedef struct MC_0093_IS_TYP
{
	struct MC_CALC_CAM_CONFIG_REF C_Configuration;
	unsigned char state;
	unsigned char LockID;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned short C_ErrorID;
} MC_0093_IS_TYP;

typedef struct MC_0095_IS_TYP
{
	plcbit Enable;
	unsigned char Reserve1;
	unsigned char Reserve2;
	unsigned char Reserve3;
	float CyclicVelocity;
	float CyclicVelocityCorrection;
	float CyclicVelCorrPerRev;
	float CyclicTorque;
	unsigned char TorqueMode;
	unsigned char Reserve4;
	unsigned char Reserve5;
	unsigned char Reserve6;
	float Acceleration;
	float Deceleration;
	float SctrlKv;
	float SctrlTn;
	plcbit InitSctrl;
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	unsigned char Reserve;
	unsigned short ErrorID;
	plcbit SctrlInitialized;
	plcbit DisableFBactive;
	unsigned short state;
	unsigned short LastState;
	unsigned short NextState;
	unsigned short VarID;
	unsigned char SptID;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned char MoveID;
	unsigned char LockIDFb;
	unsigned char CyclicVelParIndex;
	unsigned char CyclicVelCorrParIndex;
	unsigned char CyclicTorqueParIndex;
	unsigned short ArithID;
	float InitValue_SctrlKv;
	float InitValue_SctrlTn;
	float InitValue_tpredict;
	unsigned short InitValue_S_ACT_PARID;
	unsigned short prev_S_ACT_PARID_value;
	unsigned short C_ErrorID;
	unsigned char Reserve9;
	unsigned char Reserve10;
	float AxisScaleFactor;
} MC_0095_IS_TYP;

typedef struct MC_0096_IS_TYP
{
	plcbit Execute;
	unsigned char Reserve1;
	unsigned char Reserve2;
	unsigned char Reserve3;
	float Torque;
	float TorqueRamp;
	float Velocity;
	float Acceleration;
	plcbit InTorque;
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	unsigned char Reserve4;
	unsigned short ErrorID;
	plcbit AxisLimitActive;
	unsigned char state;
	unsigned short Reserve5;
	unsigned short LastState;
	unsigned short NextState;
	unsigned char MoveID;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned char Reserve6;
	unsigned short TctrlStatusOffset;
	unsigned short TctrlStatusValue;
	unsigned char TctrlStatusRecIdx;
	unsigned char stateInTorque;
	unsigned char SavedFrDrvCnt;
	unsigned char WaitForTelegrams;
} MC_0096_IS_TYP;

typedef struct MC_0097_IS_TYP
{
	plcbit C_Execute;
	unsigned short C_Command;
	struct MC_SETUP_MOTOR_PHA_CFG_REF C_Configuration;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	unsigned short C_ErrorID;
	struct MC_SETUP_OUTPUT_REF C_SetupOutput;
	struct MC_SETUP_PHASING_RESULT_REF C_SetupResult;
	unsigned long Reserve1;
	unsigned long Reserve2;
	unsigned long Reserve3;
	unsigned char LockIDPar;
	unsigned char state;
} MC_0097_IS_TYP;

typedef struct MC_0098_IS_TYP
{
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	signed char tkNo;
	unsigned short ErrorID;
	unsigned short state;
	unsigned char LockID;
	unsigned char Reserve1;
	unsigned short Reserve2;
	unsigned long cycleTime;
} MC_0098_IS_TYP;

typedef struct MC_0099_IS_TYP
{
	plcbit Enable;
	plcbit Start;
	plcbit Stop;
	plcbit Restart;
	float Deceleration;
	plcbit EndAutomat;
	plcbit SetSignal1;
	plcbit SetSignal2;
	plcbit SetSignal3;
	plcbit SetSignal4;
	plcbit ResetSignal1;
	plcbit ResetSignal2;
	plcbit ResetSignal3;
	plcbit ResetSignal4;
	plcbit TransferParLock;
	unsigned char SelectParLock;
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit Running;
	unsigned short ErrorID;
	plcbit StandBy;
	plcbit ParLockTransferred;
	unsigned char ActualStateIndex;
	plcbit InCam;
	unsigned short ActualStateCamIndex;
	plcbit InCompensation;
	unsigned char state;
	plcbit cmdStart;
	plcbit cmdStop;
	plcbit cmdSetSignal[4];
	plcbit cmdResetSignal[4];
	plcbit cmdRestart;
	plcbit cmdEndAutomat;
	plcbit cmdParLock;
	unsigned char SptID;
	unsigned short BitIndex;
	unsigned char LockIDPar;
	unsigned char LockID;
	unsigned long BitValue;
	unsigned short BitValueOffset;
	unsigned char BitValueRecIndex;
	unsigned char StateDataIdxRecIndex;
	unsigned short StateDataIdxOffset;
	unsigned char SignalSet;
	unsigned char SignalReset;
	plcbit ParLockPending;
	unsigned char AutStatus;
	unsigned char AutActCamType;
	unsigned char MoveID;
	plcbit ChangeAxisState;
	plcbit expectRunning;
	unsigned short C_ErrorID;
} MC_0099_IS_TYP;

typedef struct MC_0100_IS_TYP
{
	plcbit Enable;
	plcbit InitData;
	plcbit StartSignal;
	unsigned char Reserve1;
	float Torque;
	float TorqueRamp;
	float PosMaxVelocity;
	float NegMaxVelocity;
	float Acceleration;
	unsigned short Mode;
	unsigned short Reserve2;
	unsigned long TimeLimit;
	unsigned short StartParID;
	unsigned short TorqueParID;
	plcbit InTorque;
	plcbit Busy;
	plcbit Active;
	plcbit CommandAborted;
	plcbit Error;
	unsigned char StatEV_Move;
	unsigned short ErrorID;
	unsigned short C_ErrorID;
	plcbit DataInitialized;
	plcbit WaitingForStart;
	plcbit AxisLimitActive;
	unsigned char stateInTorque;
	unsigned char state;
	unsigned char Reserve3;
	unsigned short LastState;
	unsigned short NextState;
	unsigned char MoveID;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned char BitRecIdx;
	unsigned short BitOffset;
	unsigned short BitValue;
	unsigned short BitIndex;
	unsigned char SavedFrDrvCnt;
	unsigned char WaitForTelegrams;
	unsigned long startTick;
	float MotorTorqueConst;
} MC_0100_IS_TYP;

typedef struct MC_0101_IS_TYP
{
	plcbit Execute;
	plcbit Done;
	unsigned short Command;
	struct MC_SETUP_ISQ_RIPPLE_CFG_REF Configuration;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	unsigned char state;
	unsigned short ErrorID;
	unsigned char LockIDPar;
	struct MC_SETUP_OUTPUT_REF SetupOutput;
} MC_0101_IS_TYP;

typedef struct MC_0102_IS_TYP
{
	plcbit C_Execute;
	unsigned short C_Command;
	unsigned long C_AdrTraceConfig;
	struct MC_PARTRACE_REF C_TraceConfig;
	struct MC_DATOBJ_REF C_DataObject;
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_Error;
	unsigned short C_ErrorID;
	struct MC_ERRORRECORD_REF C_ErrorRecord;
	unsigned char state;
} MC_0102_IS_TYP;

typedef struct MC_0103_IS_TYP
{
	plcbit Execute;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	struct MC_AUT_COMP_DATA_REF CompensationData;
	unsigned short Mode;
	unsigned short ErrorID;
	float Result;
	unsigned char LockIDPar;
	unsigned char LockIDFb;
	unsigned short CurveIndex;
	float compResult;
	signed long C_MasterCompDistance;
	signed long C_SlaveCompDistance;
	unsigned char state;
	unsigned char compStatus;
	unsigned short Reserve;
} MC_0103_IS_TYP;

typedef struct MC_0104_IS_TYP
{
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	unsigned char Reserve;
	unsigned short ErrorID;
	unsigned short state;
} MC_0104_IS_TYP;

typedef struct MC_0105_IS_TYP
{
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	plcbit Reserve1;
	unsigned short ErrorID;
	unsigned short state;
	unsigned long pMessage;
	unsigned short Mode;
	plcbit Acknowledge;
	plcbit ErrorRecordAvailable;
	plcbit AcknowledgeAll;
	unsigned char Reserve2;
	unsigned short Reserve3;
	struct MC_ERRORTEXTCONFIG_REF Configuration;
	struct MC_ERRORRECORD_REF ErrorRecord;
} MC_0105_IS_TYP;

typedef struct MC_0106_IS_TYP
{
	plcbit Execute;
	unsigned short ParID;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned short ErrorID;
	struct MC_PARID_INFO_REF ParIDInfo;
	unsigned char state;
} MC_0106_IS_TYP;

typedef struct MC_0107_IS_TYP
{
	plcbit Enable;
	struct MC_MASTER_SWITCHES_REF Switches;
	unsigned char SwitchSelector;
	unsigned char Reserve1;
	struct MC_OUTPUT_OPTIONS_REF OutputOptions;
	struct MC_TRACK_OPTIONS_REF TrackOptions;
	unsigned char Reserve2;
	unsigned short camConInParID;
	plcbit EnableValue;
	plcbit EnableParID;
	plcbit EnableDigOut;
	plcbit ChangeSwitches;
	plcbit InitSwitches;
	plcbit InitTrackOptions;
	plcbit InOperation;
	plcbit Busy;
	plcbit SwitchesChanged;
	plcbit SwitchesInitialized;
	plcbit TrackOptionsInitialized;
	plcbit Error;
	unsigned short ErrorID;
	unsigned short C_ErrorID;
	plcbit Value;
	unsigned char ActualSwitches;
	unsigned char SptID;
	unsigned char state;
	unsigned char nextState;
	unsigned char readSlot;
	unsigned char sendSlot;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned char LockIDMa;
	unsigned char LockIDSend;
	unsigned char CamConActRecRecIndex;
	unsigned short CamConActRecOffset;
	unsigned short BitValueOffset;
	unsigned short BitIndex;
	unsigned short BitIndex1;
	unsigned short BitIndex2;
	unsigned short BitIndex3;
	unsigned char BitValueRecIndex;
	unsigned char BitInput[3];
	unsigned char neededBit;
	unsigned char cntBit;
	unsigned char BitValue;
	unsigned char selectRecMode;
	unsigned short CamConIndex;
	unsigned short cntCam;
	unsigned char cntTrack;
	unsigned char CamConIndexAdmin;
	unsigned short paramCount;
	plcbit bitFbMade;
	plcbit edgeInitSwitches;
	plcbit edgeChangeSwitches;
	plcbit edgeInitTrackOptions;
	plcbit edgeEnableParID;
	plcbit edgeEnableDigOut;
	unsigned char LockIDReceive;
} MC_0107_IS_TYP;

typedef struct MC_0108_IS_TYP
{
	plcbit Enable;
	plcbit Active;
	plcbit Error;
	plcbit Busy;
	unsigned short ErrorID;
	plcbit InputsSet;
	unsigned char cmdDigInForce;
	unsigned char state;
	unsigned char LockIDPar;
	plcbit oldHomeSwitch;
	plcbit oldPosHWSwitch;
	plcbit oldNegHWSwitch;
	plcbit oldTrigger1;
	plcbit oldTrigger2;
	unsigned char Reserve1;
} MC_0108_IS_TYP;

typedef struct MC_0109_IS_TYP
{
	plcbit Execute;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned short ErrorID;
	unsigned char state;
} MC_0109_IS_TYP;

typedef struct MC_0110_IS_TYP
{
	plcbit Execute;
	unsigned char Command;
	plcbit Done;
	plcbit Busy;
	struct MC_BRAKE_CONFIG_REF Configuration;
	plcbit Error;
	unsigned char LockIDPar;
	unsigned short ErrorID;
	float PositionError;
	unsigned short BrakeMode;
	unsigned short BrakeStatusParID;
	unsigned short Reserve1;
	plcbit BrakeStatus;
	unsigned char state;
	unsigned long startTick;
} MC_0110_IS_TYP;

typedef struct MC_0111_IS_TYP
{
	plcbit Execute;
	unsigned char SendChannel;
	unsigned short ParID;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned char AssignedSendChannel;
	unsigned short ErrorID;
	unsigned char state;
	unsigned char sendSlot;
	unsigned char LockIDPar;
	unsigned char LockIDSend;
} MC_0111_IS_TYP;

typedef struct MC_0112_IS_TYP
{
	plcbit Execute;
	unsigned char InterpolationMode;
	unsigned short ParID;
	unsigned char SendChannel;
	unsigned char ReceiveChannel;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned char state;
	unsigned short ErrorID;
	unsigned short ReceiveParID;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char LockIDPar;
	unsigned char LockIDReceive;
} MC_0112_IS_TYP;

typedef struct MC_0113_IS_TYP
{
	unsigned short ParID;
	unsigned char sendSlot;
	unsigned char Mode;
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	unsigned char state;
	unsigned short ErrorID;
	struct MC_CYCLIC_VALUE_REF CyclicValue;
	signed long Offset;
} MC_0113_IS_TYP;

typedef struct MC_0114_IS_TYP
{
	plcbit InitData;
	plcbit EnableCut;
	unsigned char EnableCutStateSet;
	unsigned char Reserve1;
	signed long MaFactor;
	signed long CutRangeMaster;
	signed long CutRangeSlave;
	signed long ProductLength;
	signed long ProductLengthCorrection;
	signed long MasterDistance;
	signed long SlaveFirstDistance;
	signed long SlaveLastDistance;
	signed long SlaveFullDistance;
	signed long MaStartPos;
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	unsigned short C_ErrorID;
	unsigned short ErrorID;
	plcbit DataInitialized;
	plcbit StandBy;
	plcbit CamAutActive;
	plcbit InCompensation;
	plcbit InCut;
	plcbit InCutPrevCycle;
	unsigned char Reserve2;
	unsigned char cntResetCorrection;
	unsigned long CutCount;
	signed long CutMasterPosition;
	signed short CutOverspeed;
	unsigned short StartMode;
	signed long CutPosition;
	signed long FirstCutPosition;
	signed long StartInterval;
	signed long MasterStartDistance;
	unsigned char CamTableID;
	unsigned char Reserve3;
	unsigned short MasterParID;
	float MasterMaxVelocity;
	unsigned char state;
	unsigned char LastState;
	unsigned char NextState;
	unsigned char MoveID;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char LockIDMa;
	unsigned char LockIDSend;
	unsigned char LockIDReceive;
	unsigned char AutMaOffsetRecIdx;
	unsigned char CompBitInfoRecIdx;
	unsigned char oldCamTypeValue;
	unsigned char CamTypeValue;
	unsigned char AutStatus;
	unsigned short AutMaOffsetOffset;
	unsigned short CompBitInfoOffset;
	signed long oldMasterOffsetValue;
	unsigned short ArithIndex;
	unsigned short BitIndex;
	unsigned char AutActStIdx;
	unsigned char Reserve4;
	unsigned short LatchIndex;
	signed long newCutPositionDiff;
	signed long DownloadedCutPosition;
	signed long ActualUsedCutPosition;
	signed long IMG_Var_I4_2;
	unsigned short VarIndex;
	unsigned short VarParIndex;
	unsigned short DelayIndex;
	unsigned short CountIndex;
	unsigned short EvwrIndex;
	unsigned short MuxIndex;
	unsigned short LogicIndex;
	unsigned short Reserve7;
	float CutterRadius;
	unsigned char NumberOfKnives;
	plcbit correctCurrentCycle;
	unsigned short Reserve8;
	signed long IMG_State1_addDistance;
} MC_0114_IS_TYP;

typedef struct MC_0115_IS_TYP
{
	plcbit Execute;
	unsigned char NodeNumber;
	unsigned short BitOffset;
	unsigned short DataType;
	unsigned char InterpolationMode;
	unsigned char ReceiveChannel;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned char state;
	unsigned short ErrorID;
	unsigned short ReceiveParID;
	unsigned char LockIDPar;
	unsigned char LockIDReceive;
	unsigned char readSlot;
} MC_0115_IS_TYP;

typedef struct MC_0116_IS_TYP
{
	plcbit Execute;
	plcbit Done;
	unsigned short DataObjectVersion;
	plcstring DataObjectName[13];
	unsigned long DataAddress;
	unsigned long DataLength;
	plcbit Busy;
	plcbit Error;
	unsigned short ErrorID;
	struct MC_ERRORRECORD_REF ErrorRecord;
	unsigned long DataObjectIdent;
	unsigned char state;
	unsigned char LockID;
	unsigned short hexVersion;
} MC_0116_IS_TYP;

typedef struct MC_0118_IS_TYP
{
	float Velocity;
	float Acceleration;
	float Deceleration;
	plcbit Enable;
	plcbit JogPositive;
	plcbit JogNegative;
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit Jogging;
	unsigned short ErrorID;
	unsigned char Direction;
	unsigned char state;
	unsigned char NextState;
	plcbit moveActive;
	unsigned char MoveID;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned short Reserve;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
} MC_0118_IS_TYP;

typedef struct MC_0119_IS_TYP
{
	float Velocity;
	float Acceleration;
	float Deceleration;
	signed long FirstPosition;
	signed long LastPosition;
	plcbit Enable;
	plcbit JogPositive;
	plcbit JogNegative;
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit Jogging;
	unsigned short ErrorID;
	plcbit LimitReached;
	unsigned char Direction;
	unsigned char state;
	unsigned char NextState;
	unsigned char MoveID;
	unsigned char LockIDPar;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	signed long targetPosition;
	signed long startOffset;
	signed long CommandedOffset;
	unsigned short C_ErrorID;
	plcbit moveActive;
	unsigned char Reserve;
} MC_0119_IS_TYP;

typedef struct MC_0120_IS_TYP
{
	float Velocity;
	float Acceleration;
	float Deceleration;
	signed long TargetPosition;
	plcbit Enable;
	plcbit JogToTarget;
	plcbit JogPositive;
	plcbit JogNegative;
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	unsigned short ErrorID;
	plcbit Jogging;
	plcbit MovingToTarget;
	plcbit TargetReached;
	unsigned char state;
	unsigned char NextState;
	unsigned char Direction;
	unsigned char MoveID;
	unsigned char LockIDPar;
	plcbit moveActive;
	unsigned char Reserve;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	signed long startOffset;
	signed long CommandedOffset;
	signed long targetPosition;
	unsigned short C_ErrorID;
	unsigned short Reserve1;
} MC_0120_IS_TYP;

typedef struct MC_0121_IS_TYP
{
	plcbit Execute;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned short ErrorID;
	unsigned char state;
	unsigned char LockIDSend;
	unsigned char LockIDReceive;
} MC_0121_IS_TYP;

typedef struct MC_0122_IS_TYP
{
	plcbit Execute;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned short ErrorID;
	unsigned short Reserve1;
	unsigned long DataAddress;
	unsigned long CamDataAddress;
	plcstring DataObjectName[13];
	unsigned char state;
	unsigned short Reserve2;
} MC_0122_IS_TYP;

typedef struct MC_0123_IS_TYP
{
	plcbit Execute;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned long MasterPointsAddress;
	unsigned long SlavePointsAddress;
	unsigned short NumberOfPoints;
	unsigned short ErrorID;
	struct MC_CALC_CAM_CONFIG_REF AdditionalInfo;
	plcstring DataObjectName[13];
	unsigned char state;
	unsigned short Reserve;
	unsigned long DataAddress;
} MC_0123_IS_TYP;

typedef struct MC_0124_IS_TYP
{
	struct MC_CYCLIC_POSITION_REF CyclicPosition;
	struct MC_ADVANCED_MOVE_CYC_REF AdvancedParameters;
	unsigned char InterpolationMode;
	plcbit Valid;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	unsigned char MoveID;
	unsigned short ErrorID;
	unsigned short ReceiveParID;
	unsigned short readSlot;
	unsigned char LockIDSend;
	unsigned char LockIDReceive;
	unsigned short ArithIndex;
	unsigned char LockIDPar;
	unsigned char state;
	unsigned short Reserve;
} MC_0124_IS_TYP;

typedef struct MC_0125_IS_TYP
{
	float CyclicVelocity;
	struct MC_ADVANCED_MOVE_CYC_REF AdvancedParameters;
	unsigned char Direction;
	unsigned char InterpolationMode;
	plcbit Valid;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	unsigned short ErrorID;
	unsigned short ReceiveParID;
	unsigned char LockIDPar;
	unsigned char MoveID;
	unsigned short readSlot;
	unsigned char LockIDSend;
	unsigned char LockIDReceive;
	unsigned short ArithIndex;
	unsigned char state;
	unsigned char Reserve1;
} MC_0125_IS_TYP;

typedef struct MC_0126_IS_TYP
{
	signed long RatioNumerator;
	signed long RatioDenominator;
	struct MC_ADVANCED_GEAR_PAR_REF AdvancedParameters;
	plcbit InitData;
	unsigned char state;
	plcbit Active;
	plcbit InGear;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit DataInitialized;
	unsigned short ErrorID;
	unsigned char LockIDSend;
	unsigned char LockIDReceive;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char MoveID;
	unsigned char LockIDMa;
	unsigned char LockIDPar;
	unsigned char AutActStateIndexRecIndex;
	unsigned short AutActStateIndexOffset;
	unsigned char LockID;
	plcbit flagInitData;
	unsigned short MasterParID;
	unsigned short C_ErrorID;
	plcbit gearRatioChanged;
	plcbit maxMasterVelChanged;
	float usedAccel;
	unsigned char SavedFrDrvCnt;
	plcbit WaitForTelegrams;
} MC_0126_IS_TYP;

typedef struct MC_0127_IS_TYP
{
	float CyclicVelocity;
	float Acceleration;
	struct MC_ADV_OFFSETVELOCITY_REF AdvancedParameters;
	plcbit Active;
	plcbit Busy;
	plcbit Error;
	plcbit C_Error;
	unsigned short ErrorID;
	unsigned short C_ErrorID;
	unsigned char LockIDPar;
	unsigned char LockID;
	float ActualShiftValue;
	unsigned short VarIndex;
	unsigned short MpgenIndex;
	unsigned short MuxIndex;
	unsigned short BitIndex;
	unsigned short CmpIndex;
	unsigned short ArithIndex;
	unsigned char state;
	unsigned char NextState;
	unsigned short AxisState;
	unsigned char MpgenStatus;
	unsigned char FbID;
	plcbit VelocityAttained;
	unsigned char MpgenStatusRecIndex;
	unsigned short MpgenStatusOffset;
	unsigned short MpgenValueOffset;
	unsigned char MpgenValueRecIndex;
	unsigned char SavedToDrvCnt;
	unsigned short VarParIndex;
	plcbit WaitForTelegrams;
	float OldCyclicVelocity;
} MC_0127_IS_TYP;

typedef struct MC_0128_IS_TYP
{
	float Shift;
	float Velocity;
	float Acceleration;
	float ZoneStartPosition;
	float ZoneEndPosition;
	struct MC_ADV_OFFSETZONE_REF AdvancedParameters;
	plcbit InitData;
	plcbit Active;
	plcbit Busy;
	plcbit Error;
	unsigned short ErrorID;
	unsigned short C_ErrorID;
	plcbit C_Error;
	plcbit ShiftAttained;
	plcbit DataInitialized;
	unsigned char LockIDPar;
	unsigned char LockID;
	unsigned char state;
	unsigned char MpgenStatus;
	unsigned char FbID;
	float ActualShiftValue;
	unsigned short VarIndex;
	unsigned short MpgenIndex;
	unsigned short CamConIndex;
	unsigned short EvwrIndex;
	unsigned short AxisState;
	unsigned char NextState;
	unsigned char MpgenStatusRecIndex;
	unsigned short MpgenStatusOffset;
	unsigned short MpgenValueOffset;
	unsigned char MpgenValueRecIndex;
	plcbit InitDataActive;
	unsigned short VarParIndex;
	unsigned long SlaveFactor;
	float SlaveRtN;
	unsigned long ProfileBasisFactor;
	float ProfileBasisRtN;
} MC_0128_IS_TYP;

typedef struct MC_0129_IS_TYP
{
	plcbit Execute;
	unsigned short Command;
	struct MC_SETUP_SYNC_MOTOR_CFG_REF Configuration;
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	unsigned short ErrorID;
	struct MC_SETUP_OUTPUT_REF SetupOutput;
	unsigned char LockIDPar;
	unsigned char state;
} MC_0129_IS_TYP;

typedef struct MC_0130_IS_TYP
{
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	plcbit EndlessPositionInitialized;
	unsigned short ErrorID;
	plcbit DataValid;
	unsigned char state;
} MC_0130_IS_TYP;

typedef struct MC_0133_IS_TYP
{
	unsigned char Direction;
	plcbit Busy;
	plcbit Ready;
	plcbit Active;
	unsigned short ErrorID;
	plcbit Error;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned char LockID;
	unsigned char SptID;
	unsigned char TlimStatusRecIndex;
	unsigned short TlimStatusOffset;
	unsigned short VarIndex;
	unsigned short C_ErrorID;
	unsigned char ParIndex;
	unsigned char VarParIDOffset;
} MC_0133_IS_TYP;

typedef struct MC_0134_IS_TYP
{
	unsigned char Mode;
	plcbit InitData;
	plcbit Busy;
	plcbit Ready;
	plcbit Active;
	plcbit Error;
	unsigned short ErrorID;
	plcbit DataInitialized;
	unsigned char state;
	unsigned char NextState;
	unsigned char LockIDPar;
	unsigned char LockID;
	unsigned char SptID;
	unsigned char TlimStatusRecIndex;
	unsigned short TlimStatusOffset;
	unsigned short VarIndex;
	unsigned short C_ErrorID;
	unsigned char ParIndex;
	unsigned char ParameterInitFlags;
	float OldLoadPosAccel;
	float OldLoadPosDecel;
	float OldLoadNegAccel;
	float OldLoadNegDecel;
	struct MC_ADV_LIMITLOAD_REF AdvancedParameters;
} MC_0134_IS_TYP;

typedef struct MC_0135_IS_TYP
{
	unsigned char Mode;
	plcbit InitData;
	plcbit DataInitialized;
	unsigned char state;
	unsigned short CamProfileIndexPos;
	unsigned short CamProfileIndexNeg;
	signed long PositionFactorPos;
	signed long LoadFactorPos;
	signed long PositionFactorNeg;
	signed long LoadFactorNeg;
	plcbit Busy;
	plcbit Ready;
	plcbit Active;
	plcbit Error;
	unsigned short ErrorID;
	unsigned char NextState;
	unsigned char LockIDPar;
	unsigned char LockID;
	unsigned char SptID;
	unsigned char TlimStatusRecIndex;
	unsigned char ParIndex;
	unsigned short TlimStatusOffset;
	unsigned short CurveIndex;
	unsigned short C_ErrorID;
	unsigned char ParameterInitFlags;
	unsigned char Reserve1;
} MC_0135_IS_TYP;

typedef struct MC_0137_IS_TYP
{
	plcbit Execute;
	struct MC_POWER_STAGE_CHECK_REF Configuration;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned short ErrorID;
	unsigned long MotorTestMode;
	unsigned char state;
	unsigned char LockIDPar;
} MC_0137_IS_TYP;

typedef struct MC_0136_IS_TYP
{
	plcbit Execute;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned short ErrorID;
	unsigned char GlobalParams;
	unsigned char StateIndex;
	unsigned char state;
	unsigned char LockIDPar;
} MC_0136_IS_TYP;

typedef struct MC_0138_IS_TYP
{
	unsigned short ErrorID;
	plcbit Error;
	unsigned char slot;
	unsigned char state;
	plcbit DataValid;
	plcbit Busy;
	plcbit Done;
} MC_0138_IS_TYP;

typedef struct MC_0139_IS_TYP
{
	plcbit Execute;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned short ErrorID;
	unsigned short Command;
	unsigned char state;
} MC_0139_IS_TYP;

typedef struct MC_0140_IS_TYP
{
	plcbit Execute;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned short ErrorID;
	unsigned short Command;
	unsigned char state;
} MC_0140_IS_TYP;

typedef struct MC_NET_ENC_INTERN_TYP
{
	unsigned long AdrChannelName;
	unsigned short DataType;
	unsigned short BitOffset;
	unsigned char readSlot;
	unsigned char Reserve1;
	unsigned short Reserve2;
} MC_NET_ENC_INTERN_TYP;

typedef struct MC_0141_IS_TYP
{
	plcbit Execute;
	struct MC_NET_ENC_INFO_REF EncoderInformation;
	struct MC_NET_ENC_PARAM_REF EncoderParameters;
	struct MC_NET_ENC_CONFIG_REF ReceiveConfiguration;
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	unsigned char state;
	unsigned short ErrorID;
	unsigned short PositionParID;
	unsigned char LockIDPar;
	unsigned char LockIDReceive;
	unsigned char EncoderNodeNumber;
	unsigned char Reserve1;
	struct MC_NET_ENC_INTERN_TYP EncoderInternal[6];
} MC_0141_IS_TYP;

typedef struct MC_0145_IS_TYP
{
	plcbit Execute;
	plcbit Done;
	unsigned short Command;
	struct MC_SETUP_OUTPUT_REF SetupOutput;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	unsigned short ErrorID;
	unsigned char LockIDPar;
	unsigned char state;
	plcstring DataObjectName[13];
} MC_0145_IS_TYP;

typedef struct MC_AbortTrigger
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_TRIGGER_REF TriggerInput;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned char state;
	unsigned short C_ErrorID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Done;
	plcbit C_Error;
} MC_AbortTrigger_typ;

typedef struct MC_BR_AutCommand
{
	/* VAR_INPUT (analog) */
	unsigned long Slave;
	float Deceleration;
	unsigned char SelectParLock;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned char ActualStateIndex;
	unsigned short ActualStateCamIndex;
	/* VAR (analog) */
	unsigned long C_Slave;
	struct MC_0099_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit Start;
	plcbit Stop;
	plcbit Restart;
	plcbit EndAutomat;
	plcbit SetSignal1;
	plcbit SetSignal2;
	plcbit SetSignal3;
	plcbit SetSignal4;
	plcbit ResetSignal1;
	plcbit ResetSignal2;
	plcbit ResetSignal3;
	plcbit ResetSignal4;
	plcbit TransferParLock;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit Running;
	plcbit StandBy;
	plcbit ParLockTransferred;
	plcbit InCam;
	plcbit InCompensation;
} MC_BR_AutCommand_typ;

typedef struct MC_BR_AutControl
{
	/* VAR_INPUT (analog) */
	unsigned long Slave;
	unsigned char ParLock;
	float Deceleration;
	unsigned long AdrAutData;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned char ActualStateIndex;
	unsigned char ActualCamType;
	/* VAR (analog) */
	unsigned long C_Slave;
	unsigned char ParLockOld;
	unsigned char LockID;
	float C_Deceleration;
	struct MC_AUTDATA_TYP C_AutData;
	unsigned long C_Master;
	unsigned short C_ErrorID;
	unsigned short CC_ErrorID;
	unsigned char SignalSet;
	unsigned char SignalReset;
	unsigned short CmdAutStart;
	unsigned char AutStateDld;
	unsigned short AutStatusOffset;
	unsigned char AutStatusRecIndex;
	unsigned char LockIDSend;
	unsigned short AutActualStateIndexOffset;
	unsigned char AutActualStateIndexRecIndex;
	unsigned short AutActualCamTypeOffset;
	unsigned char AutActualCamTypeRecIndex;
	unsigned char LockIDMa;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned char MoveID;
	unsigned char LockIDReceive;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit Signal1;
	plcbit Signal2;
	plcbit Signal3;
	plcbit Signal4;
	plcbit Start;
	plcbit Stop;
	plcbit Restart;
	plcbit InitAutData;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit Error;
	plcbit AutDataInitialized;
	plcbit Running;
	/* VAR (digital) */
	plcbit CmdParLock;
	plcbit EdgeSignal1;
	plcbit EdgeSignal2;
	plcbit EdgeSignal3;
	plcbit EdgeSignal4;
	plcbit EdgeStart;
	plcbit CmdStart;
	plcbit EdgeStop;
	plcbit CmdStop;
	plcbit EdgeRestart;
	plcbit CmdRestart;
	plcbit EdgeInitAutData;
	plcbit CmdInitAutData;
	plcbit C_Error;
	plcbit AutStatusValid;
	plcbit C_Busy;
} MC_BR_AutControl_typ;

typedef struct MC_BR_AutoCamDwell
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	float LeadInMasterDistance;
	float LeadInSlaveDistance;
	float LeadOutMasterDistance;
	float LeadOutSlaveDistance;
	float MasterStartPosition;
	float MasterDwellDistance;
	float MasterLength;
	float SlaveLength;
	unsigned short MasterParID;
	float MasterParIDMaxVelocity;
	unsigned short LeadInParID;
	unsigned short LeadOutParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	signed long C_LeadInMasterDistance;
	signed long C_LeadInSlaveDistance;
	signed long C_LeadOutMasterDistance;
	signed long C_LeadOutSlaveDistance;
	signed long C_MasterStartPosition;
	signed long C_MasterDwellDistance;
	signed long C_MasterLength;
	signed long C_SlaveLength;
	unsigned short C_MasterParID;
	float C_MasterParIDMaxVelocity;
	unsigned short C_LeadInParID;
	unsigned short C_LeadOutParID;
	unsigned short C_ErrorID;
	unsigned short CC_ErrorID;
	signed long RunningMasterDwellDistance;
	unsigned short ArithIndex;
	unsigned short CmpIndex;
	unsigned short MuxIndex;
	unsigned short EvWrIndex;
	unsigned short VarIndex;
	unsigned short LogicIndex;
	unsigned short AutActualStateIndexOffset;
	unsigned char AutActualStateIndexRecIndex;
	unsigned char LockIDMa;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char state;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned char LockIDSend;
	unsigned char MoveID;
	unsigned char LockIDReceive;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitData;
	plcbit LeadInSignal;
	plcbit LeadOutSignal;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit DataInitialized;
	plcbit InSync;
	plcbit InCam;
	plcbit InDwell;
	/* VAR (digital) */
	plcbit EdgeInitData;
	plcbit EdgeLeadInSignal;
	plcbit EdgeLeadOutSignal;
	plcbit LeadInSignalUsed;
	plcbit LeadOutSignalUsed;
	plcbit C_Active;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	plcbit C_InSync;
	plcbit C_InCam;
	plcbit C_InDwell;
	plcbit AutStatusValid;
} MC_BR_AutoCamDwell_typ;

typedef struct MC_BR_AxisErrorCollector
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0104_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	plcbit FunctionBlockError;
	plcbit AxisError;
	plcbit AxisWarning;
	plcbit Errorstop;
} MC_BR_AxisErrorCollector_typ;

typedef struct MC_BR_BrakeControl
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned char Command;
	struct MC_BRAKE_CONFIG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float PositionError;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0110_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	plcbit BrakeStatus;
} MC_BR_BrakeControl_typ;

typedef struct MC_BR_BrakeOperation
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned char BrakeCommand;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned char C_BrakeCommand;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_BrakeOperation_typ;

typedef struct MC_BR_CalcCamFromPoints
{
	/* VAR_INPUT (analog) */
	unsigned long MasterPointsAddress;
	unsigned long SlavePointsAddress;
	unsigned short NumberOfPoints;
	unsigned long CamProfileAddress;
	struct MC_CALC_CAM_CONFIG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	struct MC_0093_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_CalcCamFromPoints_typ;

typedef struct MC_BR_CalcCamFromSections
{
	/* VAR_INPUT (analog) */
	unsigned long DataAddress;
	unsigned long CamProfileAddress;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short ErrorInSection;
	/* VAR (analog) */
	unsigned short C_ErrorID;
	unsigned short C_ErrorInSection;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_BR_CalcCamFromSections_typ;

typedef struct MC_BR_CalcPointsFromCam
{
	/* VAR_INPUT (analog) */
	plcstring DataObjectName[13];
	unsigned long MasterPointsAddress;
	unsigned long SlavePointsAddress;
	unsigned short NumberOfPoints;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_CALC_CAM_CONFIG_REF AdditionalInfo;
	/* VAR (analog) */
	struct MC_0123_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_CalcPointsFromCam_typ;

typedef struct MC_BR_CalcSectionsFromCam
{
	/* VAR_INPUT (analog) */
	plcstring DataObjectName[13];
	unsigned long DataAddress;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	struct MC_0122_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_CalcSectionsFromCam_typ;

typedef struct MC_BR_CamDwell
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	float LeadInMasterDistance;
	float LeadInSlaveDistance;
	float LeadInMasterOffset;
	float LeadOutMasterDistance;
	float LeadOutSlaveDistance;
	float LeadOutMasterOffset;
	float MasterStartPosition;
	float MasterDwellDistance;
	float MasterScaling;
	float SlaveScaling;
	unsigned char CamTableID;
	unsigned short MasterParID;
	float MasterParIDMaxVelocity;
	unsigned short LeadInParID;
	unsigned short LeadOutParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	signed long C_LeadInMasterDistance;
	signed long C_LeadInSlaveDistance;
	signed long C_LeadInMasterOffset;
	signed long C_LeadOutMasterDistance;
	signed long C_LeadOutSlaveDistance;
	signed long C_LeadOutMasterOffset;
	signed long C_MasterStartPosition;
	signed long C_MasterDwellDistance;
	signed long C_MasterScaling;
	signed long C_SlaveScaling;
	unsigned short C_CamTableID;
	unsigned short C_MasterParID;
	float C_MasterParIDMaxVelocity;
	unsigned short C_LeadInParID;
	unsigned short C_LeadOutParID;
	unsigned short C_ErrorID;
	unsigned short CC_ErrorID;
	signed long RunningMasterDwellDistance;
	unsigned short ArithIndex;
	unsigned short CmpIndex;
	unsigned short MuxIndex;
	unsigned short EvWrIndex;
	unsigned short VarIndex;
	unsigned short LogicIndex;
	unsigned short AutActualStateIndexOffset;
	unsigned char AutActualStateIndexRecIndex;
	unsigned char LockIDMa;
	unsigned short AutActualCamTypeOffset;
	unsigned char AutActualCamTypeRecIndex;
	unsigned char LockIDSend;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char state;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned char LockIDReceive;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitData;
	plcbit LeadInSignal;
	plcbit LeadOutSignal;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit DataInitialized;
	plcbit InSync;
	plcbit InCam;
	plcbit InDwell;
	/* VAR (digital) */
	plcbit EdgeInitData;
	plcbit EdgeLeadInSignal;
	plcbit EdgeLeadOutSignal;
	plcbit LeadInSignalUsed;
	plcbit LeadOutSignalUsed;
	plcbit C_Active;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	plcbit C_InSync;
	plcbit C_InCam;
	plcbit C_InDwell;
	plcbit AutStatusValid;
} MC_BR_CamDwell_typ;

typedef struct MC_BR_CamTransition
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	float LeadInMasterDistance;
	float LeadInSlaveDistance;
	float LeadInMasterOffset;
	float LeadOutMasterDistance;
	float LeadOutSlaveDistance;
	float LeadOutMasterOffset;
	float ReverseSlaveDistance;
	float MasterInterval;
	float SlaveInterval;
	float MasterStartPosition;
	float MasterScaling;
	float SlaveScaling;
	unsigned char CamTableID;
	unsigned short MasterParID;
	float MasterParIDMaxVelocity;
	unsigned short LeadInParID;
	unsigned short LeadOutParID;
	unsigned short TransitionMode;
	unsigned short CamMode;
	float CamTime;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	signed long C_LeadInMasterDistance;
	signed long C_LeadInSlaveDistance;
	signed long C_LeadInMasterOffset;
	signed long C_LeadOutMasterDistance;
	signed long C_LeadOutSlaveDistance;
	signed long C_LeadOutMasterOffset;
	signed long C_ReverseSlaveDistance;
	signed long C_MasterInterval;
	signed long C_SlaveInterval;
	signed long C_MasterStartPosition;
	signed long C_MasterScaling;
	signed long C_SlaveScaling;
	unsigned short C_CamTableID;
	unsigned short C_MasterParID;
	float C_MasterParIDMaxVelocity;
	unsigned short C_LeadInParID;
	unsigned short C_LeadOutParID;
	unsigned short C_TransitionMode;
	unsigned short C_CamMode;
	float C_CamTime;
	unsigned short C_ErrorID;
	unsigned short CC_ErrorID;
	signed long C_MasterCompDistance;
	signed long C_SlaveCompDistance;
	signed long C_OldMasterCompDistance;
	signed long C_OldSlaveCompDistance;
	signed long C_CamMasterPeriod;
	signed long C_CamSlavePeriod;
	unsigned short ArithIndex;
	unsigned short CmpIndex;
	unsigned short MuxIndex;
	unsigned short EvWrIndex;
	unsigned short VarIndex;
	unsigned short LogicIndex;
	unsigned short PidIndex;
	unsigned short AutActualStateIndexOffset;
	unsigned char AutActualStateIndexRecIndex;
	unsigned char oldAutomatState;
	unsigned short MasterVelocityOffset;
	unsigned char MasterVelocityRecIndex;
	unsigned char LockIDMa;
	unsigned short AutActualCamTypeOffset;
	unsigned char AutActualCamTypeRecIndex;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char state;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned char MoveID;
	unsigned char LockIDSend;
	unsigned long Reserve3;
	unsigned char nextState;
	unsigned char Reserve4;
	unsigned char LockIDReceive;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitData;
	plcbit LeadInSignal;
	plcbit LeadOutSignal;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit DataInitialized;
	plcbit InSync;
	plcbit InLeadIn;
	plcbit InCam;
	plcbit InTransition;
	plcbit InReverse;
	plcbit InLeadOut;
	/* VAR (digital) */
	plcbit EdgeInitData;
	plcbit EdgeLeadInSignal;
	plcbit EdgeLeadOutSignal;
	plcbit LeadInSignalUsed;
	plcbit LeadOutSignalUsed;
	plcbit C_Active;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	plcbit C_InSync;
	plcbit C_InCam;
	plcbit C_InTransition;
	plcbit C_InReverse;
	plcbit C_InLeadIn;
	plcbit C_InLeadOut;
	plcbit AutStatusValid;
	plcbit InitDataUsed;
	plcbit MasterVelChangePending;
	plcbit Reserve6;
} MC_BR_CamTransition_typ;

typedef struct MC_BR_CheckAutCompensation
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	unsigned short Mode;
	struct MC_AUT_COMP_DATA_REF CompensationData;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float Result;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	struct MC_0103_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_CheckAutCompensation_typ;

typedef struct MC_BR_CheckEndlessPosition
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned long DataAddress;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0130_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	plcbit EndlessPositionInitialized;
	plcbit DataValid;
} MC_BR_CheckEndlessPosition_typ;

typedef struct MC_BR_CommandError
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short Command;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0140_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_CommandError_typ;

typedef struct MC_BR_ConfigPowerStageCheck
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_POWER_STAGE_CHECK_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0137_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_ConfigPowerStageCheck_typ;

typedef struct MC_BR_CrossCutterControl
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	float CutRangeMaster;
	float CutRangeSlave;
	float ProductLength;
	float ProductLengthCorrection;
	struct MC_ADVANCED_CUT_PAR_REF AdvancedParameters;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned long CutCount;
	signed long CutMasterPosition;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	struct MC_0114_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitData;
	plcbit EnableCut;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit DataInitialized;
	plcbit StandBy;
	plcbit InCompensation;
	plcbit InCut;
} MC_BR_CrossCutterControl_typ;

typedef struct MC_BR_CyclicRead
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short ParID;
	unsigned long DataAddress;
	unsigned short DataType;
	unsigned short Mode;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0069_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
} MC_BR_CyclicRead_typ;

typedef struct MC_BR_CyclicReadDataInfo
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short RecordCount;
	unsigned short ParIDCount;
	signed long RecordUpdateTime;
	signed long TotalUpdateTime;
	unsigned short RecordIndex;
	struct MC_RECORD_INFO_REF RecordInfo;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0098_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
} MC_BR_CyclicReadDataInfo_typ;

typedef struct MC_BR_CyclicWrite
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short ParID;
	unsigned long DataAddress;
	unsigned short DataType;
	unsigned short Mode;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0070_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
} MC_BR_CyclicWrite_typ;

typedef struct MC_BR_DigitalCamSwitch
{
	/* VAR_INPUT (analog) */
	struct MC_MASTER_SWITCHES_REF Switches;
	struct MC_OUTPUT_OPTIONS_REF OutputOptions;
	struct MC_TRACK_OPTIONS_REF TrackOptions;
	unsigned char SwitchSelector;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned char ActualSwitches;
	/* VAR (analog) */
	struct MC_0107_IS_TYP IS;
	unsigned long C_Master;
	unsigned long C_Slave;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit EnableValue;
	plcbit EnableParID;
	plcbit EnableDigOut;
	plcbit ChangeSwitches;
	plcbit InitSwitches;
	plcbit InitTrackOptions;
	/* VAR_OUTPUT (digital) */
	plcbit InOperation;
	plcbit Busy;
	plcbit Error;
	plcbit SwitchesChanged;
	plcbit SwitchesInitialized;
	plcbit TrackOptionsInitialized;
	plcbit Value;
} MC_BR_DigitalCamSwitch_typ;

typedef struct MC_BR_DownloadCamProfileObj
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	plcstring DataObjectName[13];
	unsigned short Index;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	plcstring C_DataObjectName[13];
	unsigned char LockIDPar;
	unsigned short C_Index;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	plcbit Periodic;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
	plcbit C_Periodic;
	plcbit C_Done;
} MC_BR_DownloadCamProfileObj_typ;

typedef struct MC_BR_DownloadCamProfileData
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned long DataAddress;
	unsigned short Index;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned long C_DataAddress;
	unsigned short C_Index;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	plcbit Periodic;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
	plcbit C_Periodic;
	plcbit C_Done;
} MC_BR_DownloadCamProfileData_typ;

typedef struct MC_BR_DownloadParSequ
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned long DataAddress;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned short Reserve1;
	unsigned long C_Axis;
	unsigned long C_DataAddress;
	unsigned short C_ErrorID;
	unsigned char LockIDPar;
	unsigned char Reserve2;
	unsigned long SizeOfFormat;
	unsigned long Reserve3;
	unsigned char index;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_DownloadParSequ_typ;

typedef struct MC_BR_EventMoveAbsolute
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_BR_EVINPUT_REF EventInput;
	float Position;
	float Velocity;
	float Acceleration;
	float Deceleration;
	unsigned char Direction;
	unsigned short Mode;
	unsigned short PositionParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_BR_EVINPUT_REF C_EventInput;
	signed long C_Position;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	unsigned char C_Direction;
	unsigned short C_Mode;
	unsigned short C_PositionParID;
	unsigned short C_ErrorID;
	signed long C_CommandedOffset;
	unsigned short CmpIndex;
	unsigned short VarIndex;
	unsigned short EvMoveStatusOffset;
	unsigned char EvMoveStatusRecIndex;
	unsigned char SavedFrDrvCnt;
	unsigned char state;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit InPosition;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit WaitingForEvent;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_InPosition;
	plcbit C_WaitingForEvent;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	plcbit WaitEvMoveStatusValid;
	plcbit C_MoveActive;
	plcbit WaitForTelegrams;
} MC_BR_EventMoveAbsolute_typ;

typedef struct MC_BR_EventMoveAdditive
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_BR_EVINPUT_REF EventInput;
	float Distance;
	float Velocity;
	float Acceleration;
	float Deceleration;
	unsigned short Mode;
	unsigned short DistanceParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_BR_EVINPUT_REF C_EventInput;
	signed long C_Distance;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	unsigned short C_Mode;
	unsigned short C_DistanceParID;
	unsigned short C_ErrorID;
	signed long C_CommandedOffset;
	signed long C_CommandedPosition;
	unsigned short CmpIndex;
	unsigned short VarIndex;
	unsigned short EvMoveStatusOffset;
	unsigned char EvMoveStatusRecIndex;
	unsigned char SavedFrDrvCnt;
	unsigned char state;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit InPosition;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit WaitingForEvent;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_InPosition;
	plcbit C_WaitingForEvent;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	plcbit WaitEvMoveStatusValid;
	plcbit C_MoveActive;
	plcbit WaitForTelegrams;
} MC_BR_EventMoveAdditive_typ;

typedef struct MC_BR_EventMoveVelocity
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_BR_EVINPUT_REF EventInput;
	float Velocity;
	float Acceleration;
	float Deceleration;
	unsigned char Direction;
	unsigned short Mode;
	unsigned short VelocityParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_BR_EVINPUT_REF C_EventInput;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	unsigned char C_Direction;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned short C_Mode;
	unsigned short C_VelocityParID;
	unsigned short C_ErrorID;
	unsigned short CmpIndex;
	unsigned short VarIndex;
	unsigned short EvMoveStatusOffset;
	unsigned char EvMoveStatusRecIndex;
	unsigned char Reserve1;
	unsigned short VelocityOffset;
	unsigned char VelocityRecIndex;
	unsigned char SavedFrDrvCnt;
	unsigned char state;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit InVelocity;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit WaitingForEvent;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_InVelocity;
	plcbit C_WaitingForEvent;
	plcbit C_Busy;
	plcbit C_CommandAborted;
	plcbit C_Error;
	plcbit WaitEvMoveStatusValid;
	plcbit C_MoveActive;
	plcbit WaitForTelegrams;
} MC_BR_EventMoveVelocity_typ;

typedef struct MC_BR_GearIn
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	signed long RatioNumerator;
	signed long RatioDenominator;
	struct MC_ADVANCED_GEAR_PAR_REF AdvancedParameters;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	struct MC_0126_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitData;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit DataInitialized;
	plcbit InGear;
} MC_BR_GearIn_typ;

typedef struct MC_BR_GetCamMasterPosition
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	plcstring DataObjectName[13];
	unsigned long DataAddress;
	float MasterStartPosition;
	float SlavePosition;
	unsigned long MasterFactor;
	signed long SlaveFactor;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float MasterPosition;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	struct MC_0084_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_GetCamMasterPosition_typ;

typedef struct MC_BR_GetCamSlavePosition
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	plcstring DataObjectName[13];
	unsigned long DataAddress;
	float MasterPosition;
	unsigned long MasterFactor;
	signed long SlaveFactor;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float SlavePosition;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	struct MC_0083_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_GetCamSlavePosition_typ;

typedef struct MC_BR_GetErrorText
{
	/* VAR_INPUT (analog) */
	struct MC_ERRORTEXTCONFIG_REF Configuration;
	struct MC_ERRORRECORD_REF ErrorRecord;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	struct MC_0077_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_GetErrorText_typ;

typedef struct MC_BR_GetHardwareInfo
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_HARDWARE_INFO_REF HardwareInfo;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0109_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_GetHardwareInfo_typ;

typedef struct MC_BR_GetParIDTransferInfo
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned char FreeSendChannels;
	unsigned char FreeReceiveChannels;
	struct MC_TRANSFER_INFO_REF ParIDTransferInfo;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0121_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_GetParIDTransferInfo_typ;

typedef struct MC_BR_HomeAcpEncoder
{
	/* VAR_INPUT (analog) */
	struct MC_ACP_ENCOD_REF AcpEncoder;
	struct MC_ACP_ENCOD_PARAM_REF HomingParameters;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	signed long EncoderOffset;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0068_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
} MC_BR_HomeAcpEncoder_typ;

typedef struct MC_BR_InitAutData
{
	/* VAR_INPUT (analog) */
	unsigned long Slave;
	struct MC_AUTINITOPTIONS_REF InitOptions;
	unsigned long AdrAutData;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	struct MC_0076_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_InitAutData_typ;

typedef struct MC_BR_InitAutEvent
{
	/* VAR_INPUT (analog) */
	unsigned long Slave;
	unsigned char StateIndex;
	unsigned char EventIndex;
	unsigned char Type;
	unsigned char Attribute;
	unsigned long Action;
	unsigned char NextState;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Slave;
	unsigned char C_StateIndex;
	unsigned char C_EventIndex;
	unsigned char C_Type;
	unsigned char C_Attribute;
	unsigned long C_Action;
	unsigned char C_NextState;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned long Reserve;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_InitAutEvent_typ;

typedef struct MC_BR_InitAutPar
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	float StartPosition;
	float StartInterval;
	unsigned char StartState;
	float StartMaRelPos;
	float MaxMasterVelocity;
	unsigned short MasterParID;
	unsigned short AddMasterParID;
	unsigned short AddSlaveParID;
	unsigned short SlaveFactorParID;
	unsigned short EventParID;
	unsigned short SlaveLatchParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned char Reserve1;
	unsigned char LockIDReceive;
	unsigned long C_Master;
	unsigned long C_Slave;
	signed long C_StartPosition;
	signed long C_StartInterval;
	unsigned char C_StartState;
	unsigned char LockIDMa;
	unsigned char LockIDPar;
	unsigned char LockIDSend;
	signed long C_StartMaRelPos;
	float C_MaxMasterVelocity;
	unsigned long Reserve2;
	unsigned short C_MasterParID;
	unsigned short C_AddMasterParID;
	unsigned short C_AddSlaveParID;
	unsigned short C_SlaveFactorParID;
	unsigned short C_EventParID;
	unsigned short C_SlaveLatchParID;
	unsigned short C_ErrorID;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_InitAutPar_typ;

typedef struct MC_BR_InitAutState
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	unsigned char StateIndex;
	unsigned short CamProfileIndex;
	unsigned long MasterFactor;
	signed long SlaveFactor;
	unsigned short RepeatCounterInit;
	unsigned short RepeatCounterSet;
	unsigned char CompMode;
	float MasterCompDistance;
	float SlaveCompDistance;
	unsigned char ExtendedCompLimits;
	float MinMasterCompDistance;
	float MinSlaveCompDistance;
	float MaxSlaveCompDistance;
	float MinSlaveCompVelocity;
	float MaxSlaveCompVelocity;
	float MaxSlaveAccelComp1;
	float MaxSlaveAccelComp2;
	float SlaveCompJoltTime;
	unsigned short MasterParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	unsigned char C_StateIndex;
	unsigned char Reserve1;
	unsigned short C_CamProfileIndex;
	signed long C_MasterFactor;
	signed long C_SlaveFactor;
	unsigned short C_RepeatCounterInit;
	unsigned short Reserve2;
	unsigned short C_RepeatCounterSet;
	unsigned char C_CompMode;
	unsigned char LockIDPar;
	signed long C_MasterCompDistance;
	signed long C_SlaveCompDistance;
	unsigned char C_ExtendedCompLimits;
	unsigned char Reserve3;
	unsigned short Reserve4;
	signed long C_MinMasterCompDistance;
	signed long C_MinSlaveCompDistance;
	signed long C_MaxSlaveCompDistance;
	float C_MinSlaveCompVelocity;
	float C_MaxSlaveCompVelocity;
	float C_MaxSlaveAccelComp1;
	float C_MaxSlaveAccelComp2;
	float C_SlaveCompJoltTime;
	unsigned short C_MasterParID;
	unsigned short C_ErrorID;
	unsigned long Reserve5;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_InitAutState_typ;

typedef struct MC_BR_InitAxisPar
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned char* pInit;
	unsigned char* pError;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_BR_InitAxisPar_typ;

typedef struct MC_BR_InitAxisSubjectPar
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short Subject;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_Subject;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned char* pInit;
	unsigned char* pError;
	unsigned long CheckModeBits;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_BR_InitAxisSubjectPar_typ;

typedef struct MC_BR_InitCyclicRead
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short ParID;
	unsigned long DataAddress;
	unsigned short DataType;
	unsigned short Mode;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned long C_Axis;
	unsigned short C_ParID;
	unsigned short Reserve1;
	unsigned long C_DataAddress;
	unsigned short C_DataType;
	unsigned short C_Mode;
	unsigned short C_ErrorID;
	unsigned short ParIDOffset;
	unsigned long Reserve2;
	unsigned char Reserve3;
	unsigned char ParIDRecIndex;
	unsigned char Reserve4;
	unsigned char DataLength;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_InitCyclicRead_typ;

typedef struct MC_BR_InitCyclicWrite
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short ParID;
	unsigned long DataAddress;
	unsigned short DataType;
	unsigned short Mode;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned long C_Axis;
	unsigned short C_ParID;
	unsigned short Reserve1;
	unsigned long C_DataAddress;
	unsigned short C_DataType;
	unsigned short C_Mode;
	unsigned long Reserve2;
	unsigned short C_ErrorID;
	unsigned char ParIDParIndex;
	unsigned char DataLength;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_InitCyclicWrite_typ;

typedef struct MC_BR_InitEndlessPosition
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned long DataAddress;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_BR_InitEndlessPosition_typ;

typedef struct MC_BR_InitEndlessPosAcpEnc
{
	/* VAR_INPUT (analog) */
	struct MC_ACP_ENCOD_REF AcpEncoder;
	unsigned long DataAddress;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0138_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	plcbit DataValid;
} MC_BR_InitEndlessPosAcpEnc_typ;

typedef struct MC_BR_InitMasterParIDTransfer
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	unsigned short MasterParID;
	unsigned char SlaveChannel;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short ReceiveParID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	unsigned short Reserve1;
	unsigned char Reserve2;
	unsigned char LockIDReceive;
	unsigned short C_MasterParID;
	unsigned char C_SlaveChannel;
	unsigned char LockIDSend;
	unsigned short C_ErrorID;
	unsigned short C_ReceiveParID;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char state;
	unsigned char LockIDMa;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_InitMasterParIDTransfer_typ;

typedef struct MC_BR_InitModPos
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned long Period;
	unsigned long Factor;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned long C_Period;
	unsigned long C_Factor;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
	plcbit C_Execute;
} MC_BR_InitModPos_typ;

typedef struct MC_BR_InitParList
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned long DataAddress;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned long C_Axis;
	unsigned long C_DataAddress;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
	plcbit C_Done;
} MC_BR_InitParList_typ;

typedef struct MC_BR_InitParSequ
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned long DataAddress;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned long C_DataAddress;
	unsigned short Reserve1;
	unsigned long Reserve2;
	unsigned short C_ErrorID;
	unsigned long Reserve3;
	unsigned char index;
	unsigned short Reserve4;
	unsigned char state;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_BR_InitParSequ_typ;

typedef struct MC_BR_InitParTabObj
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	plcstring DataObjectName[13];
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	plcstring C_DataObjectName[13];
	unsigned short C_ErrorID;
	unsigned char LockIDPar;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
	plcbit C_Done;
} MC_BR_InitParTabObj_typ;

typedef struct MC_BR_InitReceiveNetworkData
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned char NodeNumber;
	unsigned short BitOffset;
	unsigned short DataType;
	unsigned char InterpolationMode;
	unsigned char ReceiveChannel;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short ReceiveParID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0115_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_InitReceiveNetworkData_typ;

typedef struct MC_BR_InitReceiveNetworkEnc
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_NET_ENC_INFO_REF EncoderInformation;
	struct MC_NET_ENC_PARAM_REF EncoderParameters;
	struct MC_NET_ENC_CONFIG_REF ReceiveConfiguration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short PositionParID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0141_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_InitReceiveNetworkEnc_typ;

typedef struct MC_BR_InitReceiveParID
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	unsigned short ParID;
	unsigned char InterpolationMode;
	unsigned char SendChannel;
	unsigned char ReceiveChannel;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short ReceiveParID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	struct MC_0112_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_InitReceiveParID_typ;

typedef struct MC_BR_InitSendParID
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short ParID;
	unsigned char SendChannel;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned char AssignedSendChannel;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0111_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_InitSendParID_typ;

typedef struct MC_BR_JogVelocity
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Velocity;
	float Acceleration;
	float Deceleration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0118_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit JogPositive;
	plcbit JogNegative;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit Jogging;
} MC_BR_JogVelocity_typ;

typedef struct MC_BR_JogLimitPosition
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Velocity;
	float Acceleration;
	float Deceleration;
	float FirstPosition;
	float LastPosition;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0119_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit JogPositive;
	plcbit JogNegative;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit Jogging;
	plcbit LimitReached;
} MC_BR_JogLimitPosition_typ;

typedef struct MC_BR_JogTargetPosition
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Velocity;
	float Acceleration;
	float Deceleration;
	float TargetPosition;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0120_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit JogToTarget;
	plcbit JogPositive;
	plcbit JogNegative;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit Jogging;
	plcbit MovingToTarget;
	plcbit TargetReached;
} MC_BR_JogTargetPosition_typ;

typedef struct MC_BR_LimitLoad
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float LoadPosAccel;
	float LoadPosDecel;
	float LoadNegAccel;
	float LoadNegDecel;
	unsigned char Mode;
	struct MC_ADV_LIMITLOAD_REF AdvancedParameters;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0134_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitData;
	/* VAR_OUTPUT (digital) */
	plcbit Busy;
	plcbit Ready;
	plcbit Active;
	plcbit Error;
	plcbit DataInitialized;
} MC_BR_LimitLoad_typ;

typedef struct MC_BR_LimitLoadCam
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short CamProfileIndexPos;
	signed long PositionFactorPos;
	signed long LoadFactorPos;
	unsigned short CamProfileIndexNeg;
	signed long PositionFactorNeg;
	signed long LoadFactorNeg;
	unsigned char Mode;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0135_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitData;
	/* VAR_OUTPUT (digital) */
	plcbit Busy;
	plcbit Ready;
	plcbit Active;
	plcbit Error;
	plcbit DataInitialized;
} MC_BR_LimitLoadCam_typ;

typedef struct MC_BR_LoadAxisPar
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	plcstring DataObjectName[13];
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	plcstring C_DataObjectName[13];
	unsigned char state;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned char* pInit;
	unsigned char* pError;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_BR_LoadAxisPar_typ;

typedef struct MC_BR_MoveAbsoluteTriggStop
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_TRIGGER_REF TriggerInput;
	float Position;
	float Velocity;
	float Acceleration;
	float Deceleration;
	unsigned char Direction;
	float TriggerDistance;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	signed long C_Position;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	unsigned char C_Direction;
	signed long C_TriggerDistance;
	struct MC_TRIGGER_REF C_TriggerInput;
	unsigned short C_ErrorID;
	signed long C_CommandedOffset;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	plcbit ForceTriggerDistance;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit cmdExecute;
	plcbit C_ForceTriggerDistance;
	plcbit C_Done;
	plcbit C_CommandAborted;
	plcbit C_Error;
} MC_BR_MoveAbsoluteTriggStop_typ;

typedef struct MC_BR_MoveAdditiveTriggStop
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_TRIGGER_REF TriggerInput;
	float Distance;
	float Velocity;
	float Acceleration;
	float Deceleration;
	float TriggerDistance;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	signed long C_Distance;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	signed long C_TriggerDistance;
	struct MC_TRIGGER_REF C_TriggerInput;
	unsigned short C_ErrorID;
	signed long C_CommandedOffset;
	float C_CommandedPosition;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	plcbit ForceTriggerDistance;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit cmdExecute;
	plcbit C_ForceTriggerDistance;
	plcbit C_Done;
	plcbit C_CommandAborted;
	plcbit C_Error;
} MC_BR_MoveAdditiveTriggStop_typ;

typedef struct MC_BR_MoveCyclicPosition
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_CYCLIC_POSITION CyclicPosition;
	float Velocity;
	float Acceleration;
	float Deceleration;
	unsigned short PositionParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short ReceiveParID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned char Reserve;
	struct MC_0081_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
} MC_BR_MoveCyclicPosition_typ;

typedef struct MC_BR_MoveCyclicPositionExt
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_CYCLIC_POSITION_REF CyclicPosition;
	unsigned char InterpolationMode;
	struct MC_ADVANCED_MOVE_CYC_REF AdvancedParameters;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short ReceiveParID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0124_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
} MC_BR_MoveCyclicPositionExt_typ;

typedef struct MC_BR_MoveCyclicVelocity
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float CyclicVelocity;
	unsigned char Direction;
	float Acceleration;
	float Deceleration;
	unsigned short VelocityParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short ReceiveParID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0092_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
} MC_BR_MoveCyclicVelocity_typ;

typedef struct MC_BR_MoveCyclicVelocityExt
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float CyclicVelocity;
	unsigned char Direction;
	unsigned char InterpolationMode;
	struct MC_ADVANCED_MOVE_CYC_REF AdvancedParameters;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short ReceiveParID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0125_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
} MC_BR_MoveCyclicVelocityExt_typ;

typedef struct MC_BR_MoveVelocityTriggStop
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_TRIGGER_REF TriggerInput;
	float Velocity;
	float Acceleration;
	float Deceleration;
	unsigned char Direction;
	float TriggerDistance;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	unsigned char C_Direction;
	unsigned short C_ErrorID;
	struct MC_TRIGGER_REF C_TriggerInput;
	signed long C_TriggerDistance;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit cmdExecute;
	plcbit C_Done;
	plcbit C_CommandAborted;
	plcbit C_Error;
} MC_BR_MoveVelocityTriggStop_typ;

typedef struct MC_BR_NetTrace
{
	/* VAR_INPUT (analog) */
	unsigned short Command;
	struct MC_NETTRACECONFIG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_ERRORRECORD_REF ErrorRecord;
	/* VAR (analog) */
	struct MC_0078_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_NetTrace_typ;

typedef struct MC_BR_NetworkInit
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short Command;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Object;
	struct MC_0139_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_NetworkInit_typ;

typedef struct MC_BR_Offset
{
	/* VAR_INPUT (analog) */
	unsigned long Slave;
	float Shift;
	float Velocity;
	float Acceleration;
	float ApplicationDistance;
	unsigned short ApplicationMode;
	unsigned short ShiftMode;
	struct MC_ADVANCEDSHIFTPAR_REF AdvancedParameters;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float ActualShiftValue;
	/* VAR (analog) */
	unsigned long C_Slave;
	signed long C_Shift;
	float C_Velocity;
	float C_Acceleration;
	signed long C_ApplicationDistance;
	unsigned short C_ApplicationMode;
	unsigned short C_SelectedMaster;
	unsigned short C_ShiftMode;
	struct MC_ADVANCEDSHIFTPAR_REF C_AdvancedParameters;
	unsigned short C_ErrorID;
	unsigned short CC_ErrorID;
	unsigned short C_AxisState;
	unsigned char NextState;
	unsigned char state;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned long Factor;
	float RtN;
	unsigned short VarIndex;
	unsigned short MpgenIndex;
	unsigned char C_MpgenStatus;
	unsigned short MpgenStatusOffset;
	unsigned char MpgenStatusRecIndex;
	unsigned char Reserve;
	unsigned short MpgenValueOffset;
	unsigned char MpgenValueRecIndex;
	unsigned char FbID;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitData;
	plcbit PerformVelocityControl;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit Error;
	plcbit ShiftAttained;
	plcbit DataInitialized;
	/* VAR (digital) */
	plcbit C_InitData;
	plcbit C_PerformVelocityControl;
	plcbit C_Active;
	plcbit C_Busy;
	plcbit C_Error;
	plcbit C_ShiftAttained;
	plcbit C_DataInitialized;
	plcbit InitDataActive;
} MC_BR_Offset_typ;

typedef struct MC_BR_OffsetVelocity
{
	/* VAR_INPUT (analog) */
	unsigned long Slave;
	float CyclicVelocity;
	float Acceleration;
	struct MC_ADV_OFFSETVELOCITY_REF AdvancedParameters;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float ActualShiftValue;
	/* VAR (analog) */
	unsigned long C_Slave;
	struct MC_0127_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit Error;
	plcbit VelocityAttained;
} MC_BR_OffsetVelocity_typ;

typedef struct MC_BR_OffsetZone
{
	/* VAR_INPUT (analog) */
	unsigned long Slave;
	float Shift;
	float Velocity;
	float Acceleration;
	float ZoneStartPosition;
	float ZoneEndPosition;
	struct MC_ADV_OFFSETZONE_REF AdvancedParameters;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float ActualShiftValue;
	/* VAR (analog) */
	unsigned long C_Slave;
	struct MC_0128_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitData;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit Error;
	plcbit ShiftAttained;
	plcbit DataInitialized;
} MC_BR_OffsetZone_typ;

typedef struct MC_BR_GetParIDInfo
{
	/* VAR_INPUT (analog) */
	unsigned short ParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_PARID_INFO_REF ParIDInfo;
	/* VAR (analog) */
	struct MC_0106_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_GetParIDInfo_typ;

typedef struct MC_BR_ParTrace
{
	/* VAR_INPUT (analog) */
	unsigned short Command;
	struct MC_PARTRACECONFIG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_ERRORRECORD_REF ErrorRecord;
	/* VAR (analog) */
	struct MC_0080_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_ParTrace_typ;

typedef struct MC_BR_ParTraceConfig
{
	/* VAR_INPUT (analog) */
	unsigned short Command;
	unsigned long AdrTraceConfig;
	struct MC_DATOBJ_REF DataObject;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_ERRORRECORD_REF ErrorRecord;
	/* VAR (analog) */
	struct MC_0102_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_ParTraceConfig_typ;

typedef struct MC_BR_Phasing
{
	/* VAR_INPUT (analog) */
	unsigned long Slave;
	float Shift;
	float Velocity;
	float Acceleration;
	float ApplicationDistance;
	unsigned short ApplicationMode;
	unsigned short ShiftMode;
	struct MC_ADVANCEDSHIFTPAR_REF AdvancedParameters;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float ActualShiftValue;
	/* VAR (analog) */
	unsigned long C_Slave;
	signed long C_Shift;
	float C_Velocity;
	float C_Acceleration;
	signed long C_ApplicationDistance;
	unsigned short C_ApplicationMode;
	unsigned short C_SelectedMaster;
	unsigned short C_ShiftMode;
	struct MC_ADVANCEDSHIFTPAR_REF C_AdvancedParameters;
	unsigned short C_ErrorID;
	unsigned short CC_ErrorID;
	unsigned short C_AxisState;
	unsigned char NextState;
	unsigned char state;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned long Factor;
	float RtN;
	unsigned short VarIndex;
	unsigned short MpgenIndex;
	unsigned char C_MpgenStatus;
	unsigned short MpgenStatusOffset;
	unsigned char MpgenStatusRecIndex;
	unsigned char Reserve;
	unsigned short MpgenValueOffset;
	unsigned char MpgenValueRecIndex;
	unsigned char FbID;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitData;
	plcbit PerformVelocityControl;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit Error;
	plcbit ShiftAttained;
	plcbit DataInitialized;
	/* VAR (digital) */
	plcbit C_InitData;
	plcbit C_PerformVelocityControl;
	plcbit C_Active;
	plcbit C_Busy;
	plcbit C_Error;
	plcbit C_ShiftAttained;
	plcbit C_DataInitialized;
	plcbit InitDataActive;
} MC_BR_Phasing_typ;

typedef struct MC_BR_PowerMeter
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned char Mode;
	unsigned short IntervalTime;
	struct MC_BR_EVINPUT_REF EventInput;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_POWERDATA_REF PowerData;
	unsigned short MissedIntervals;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0089_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit RestartInterval;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
} MC_BR_PowerMeter_typ;

typedef struct MC_BR_ReadAutPosition
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float AutPosition;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ErrorID;
	unsigned char LockIDPar;
	unsigned char Reserve1;
	signed long C_AutPosition;
	unsigned long C_DataAddress;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_ReadAutPosition_typ;

typedef struct MC_BR_ReadAxisError
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short Mode;
	struct MC_ERRORTEXTCONFIG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_ERRORRECORD_REF ErrorRecord;
	unsigned short FunctionBlockErrorCount;
	unsigned short AxisErrorCount;
	unsigned short AxisWarningCount;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0105_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit Acknowledge;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	plcbit ErrorRecordAvailable;
} MC_BR_ReadAxisError_typ;

typedef struct MC_BR_ReadCyclicPosition
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short ParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_CYCLIC_POSITION CyclicPosition;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0082_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
} MC_BR_ReadCyclicPosition_typ;

typedef struct MC_BR_ReadDriveStatus
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned long AdrDriveStatus;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned char state;
	unsigned short C_ErrorID;
	unsigned long C_AdrDriveStatus;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_BR_ReadDriveStatus_typ;

typedef struct MC_BR_ReadNetTraceStatus
{
	/* VAR_INPUT (analog) */
	struct MC_NETTRACECONFIG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short TraceState;
	/* VAR (analog) */
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_BR_ReadNetTraceStatus_typ;

typedef struct MC_BR_ReadParID
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short ParID;
	unsigned long DataAddress;
	unsigned short DataType;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ParID;
	unsigned char LockIDPar;
	unsigned char Reserve1;
	unsigned long C_DataAddress;
	unsigned long Reserve2;
	unsigned short C_DataType;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_ReadParID_typ;

typedef struct MC_BR_ReadParIDText
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short ParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	plcstring DataText[34];
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ParID;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_ReadParIDText_typ;

typedef struct MC_BR_ReadParTraceStatus
{
	/* VAR_INPUT (analog) */
	struct MC_PARTRACECONFIG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short TraceState;
	/* VAR (analog) */
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_BR_ReadParTraceStatus_typ;

typedef struct MC_BR_ReceiveParIDOnPLC
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short ParID;
	unsigned char SendChannel;
	unsigned char Mode;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_CYCLIC_VALUE_REF CyclicValue;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0113_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
} MC_BR_ReceiveParIDOnPLC_typ;

typedef struct MC_BR_ResetAutPar
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned char GlobalParams;
	unsigned char StateIndex;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0136_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_ResetAutPar_typ;

typedef struct MC_BR_SaveAxisPar
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	plcstring DataObjectName[13];
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned long DataObjectIdent;
	/* VAR (analog) */
	unsigned long C_Axis;
	plcstring C_DataObjectName[13];
	unsigned char state;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned char* pInit;
	unsigned char* pError;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_BR_SaveAxisPar_typ;

typedef struct MC_BR_SaveCamProfileObj
{
	/* VAR_INPUT (analog) */
	plcstring DataObjectName[13];
	unsigned long DataAddress;
	unsigned short DataObjectVersion;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_ERRORRECORD_REF ErrorRecord;
	unsigned long DataObjectIdent;
	/* VAR (analog) */
	struct MC_0116_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_SaveCamProfileObj_typ;

typedef struct MC_BR_SetHardwareInputs
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0108_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit HomeSwitch;
	plcbit PosHWSwitch;
	plcbit NegHWSwitch;
	plcbit Trigger1;
	plcbit Trigger2;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit Error;
	plcbit InputsSet;
} MC_BR_SetHardwareInputs_typ;

typedef struct MC_BR_SetupController
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short Command;
	struct MC_SETUP_CONTROLLER_CFG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_SETUP_OUTPUT_REF SetupOutput;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0090_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
} MC_BR_SetupController_typ;

typedef struct MC_BR_SetupFromParTabObj
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short Command;
	plcstring DataObjectName[13];
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_SETUP_OUTPUT_REF SetupOutput;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0145_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
} MC_BR_SetupFromParTabObj_typ;

typedef struct MC_BR_SetupInductionMotor
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short Command;
	struct MC_SETUP_IND_MOTOR_CFG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_SETUP_OUTPUT_REF SetupOutput;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0088_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
} MC_BR_SetupInductionMotor_typ;

typedef struct MC_BR_SetupIsqRipple
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short Command;
	struct MC_SETUP_ISQ_RIPPLE_CFG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_SETUP_OUTPUT_REF SetupOutput;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0101_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
} MC_BR_SetupIsqRipple_typ;

typedef struct MC_BR_SetupMotorPhasing
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short Command;
	struct MC_SETUP_MOTOR_PHA_CFG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_SETUP_OUTPUT_REF SetupOutput;
	struct MC_SETUP_PHASING_RESULT_REF SetupResult;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0097_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
} MC_BR_SetupMotorPhasing_typ;

typedef struct MC_BR_SetupSynchronMotor
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short Command;
	struct MC_SETUP_SYNC_MOTOR_CFG_REF Configuration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	struct MC_SETUP_OUTPUT_REF SetupOutput;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0129_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
} MC_BR_SetupSynchronMotor_typ;

typedef struct MC_BR_Simulation
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short SimulationCommand;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0071_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_BR_Simulation_typ;

typedef struct MC_BR_TouchProbe
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_BR_TRIGGER_REF TriggerInput;
	float Period;
	float PeriodChange;
	float ExpectedValue;
	float WindowNegative;
	float WindowPositive;
	unsigned short Mode;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float RecordedPeriodicValue;
	signed long RecordedValue;
	float DeltaExpectedValue;
	unsigned long ProbeCounter;
	unsigned long MissedTriggers;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_BR_TRIGGER_REF C_TriggerInput;
	signed long C_Period;
	signed long C_PeriodChange;
	signed long C_ExpectedValue;
	signed long C_WindowNegative;
	signed long C_WindowPositive;
	unsigned short C_Mode;
	unsigned short C_ErrorID;
	float C_RecordedPeriodicValue;
	signed long C_RecordedValue;
	float C_DeltaExpectedValue;
	unsigned long C_ProbeCounter;
	unsigned long C_MissedTriggers;
	signed long PeriodOffset;
	signed long LatchValue;
	signed long LatchDeltaIv;
	unsigned char state;
	unsigned char NextState;
	unsigned short DataTyp;
	unsigned char LockIDPar;
	unsigned char LockID;
	signed long ActualPosition;
	unsigned short LatchIndex;
	unsigned short BitIndex;
	unsigned short BitValueOffset;
	unsigned char BitValueRecIndex;
	unsigned char SptID;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Active;
	plcbit C_Busy;
	plcbit C_Error;
	plcbit NewValue;
	plcbit UpdatePeriod;
	plcbit UseAxisPeriod;
} MC_BR_TouchProbe_typ;

typedef struct MC_BR_VelocityControl
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float CyclicVelocity;
	float CyclicVelocityCorrection;
	float CyclicTorque;
	unsigned char TorqueMode;
	float Acceleration;
	float Deceleration;
	float SctrlKv;
	float SctrlTn;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0095_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitSctrl;
	/* VAR_OUTPUT (digital) */
	plcbit Active;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit SctrlInitialized;
} MC_BR_VelocityControl_typ;

typedef struct MC_BR_WriteParID
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short ParID;
	unsigned long DataAddress;
	unsigned short DataType;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ParID;
	unsigned char LockIDPar;
	unsigned char Reserve1;
	unsigned long C_DataAddress;
	unsigned long Reserve2;
	unsigned short C_DataType;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_WriteParID_typ;

typedef struct MC_BR_WriteParIDText
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned short ParID;
	plcstring DataText[34];
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ParID;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_BR_WriteParIDText_typ;

typedef struct MC_CamIn
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	float MasterOffset;
	float SlaveOffset;
	float MasterScaling;
	float SlaveScaling;
	unsigned char StartMode;
	unsigned char CamTableID;
	unsigned short MasterParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned char LockIDPar;
	unsigned char LockIDInSync;
	unsigned long C_Master;
	unsigned long C_Slave;
	signed long C_MasterOffset;
	signed long C_SlaveOffset;
	signed long C_MasterScaling;
	signed long C_SlaveScaling;
	unsigned char C_StartMode;
	unsigned char LockID;
	unsigned short C_CamTableID;
	unsigned short C_MasterParID;
	unsigned short C_ErrorID;
	signed long OldMaCamOffset;
	signed long MaPosition;
	unsigned short DataTyp;
	unsigned short MpgenIndex;
	unsigned short AutActualStateIndexOffset;
	unsigned char AutActualStateIndexRecIndex;
	unsigned char LockIDReceive;
	unsigned short AutActualCamIndexOffset;
	unsigned char AutActualCamIndexRecIndex;
	unsigned char LockIDSend;
	unsigned short AutMaCamOffsetOffset;
	unsigned char AutMaCamOffsetRecIndex;
	unsigned char LockIDMa;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char state;
	unsigned char MoveID;
	unsigned short CC_ErrorID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit InSync;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	plcbit EndOfProfile;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Periodic;
	plcbit C_InSync;
	plcbit C_CommandAborted;
	plcbit C_Error;
	plcbit C_EndOfProfile;
} MC_CamIn_typ;

typedef struct MC_CamOut
{
	/* VAR_INPUT (analog) */
	unsigned long Slave;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Slave;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_CamOut_typ;

typedef struct MC_CamTableSelect
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	plcstring CamTable[13];
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned char CamTableID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	plcstring C_CamTable[13];
	unsigned char Reserve;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	plcbit Periodic;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Periodic;
	plcbit C_Error;
} MC_CamTableSelect_typ;

typedef struct MC_DigitalCamSwitch
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_CAMSWITCH_REF Switches;
	struct MC_OUTPUT_REF Outputs;
	struct MC_TRACK_REF TrackOptions;
	unsigned long EnableMask;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	struct MC_CAMSWITCH_REF C_Switches;
	struct MC_OUTPUT_REF C_Outputs;
	struct MC_TRACK_REF C_TrackOptions;
	unsigned long C_EnableMask;
	unsigned char C_CamConActRec;
	unsigned char nextParRec;
	unsigned char SelectRecMode;
	unsigned char LockIDSend;
	unsigned short C_ErrorID;
	unsigned short CC_ErrorID;
	unsigned short CamConIndex;
	unsigned short LogicIndex;
	unsigned short VarIndex;
	unsigned short CamConActRecOffset;
	unsigned char CamConActRecRecIndex;
	unsigned char LockIDMa;
	unsigned char LockIDPar;
	unsigned char LockID;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char state;
	unsigned char SptID;
	unsigned char LockIDReceive;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitSwitches;
	plcbit InitTrackOptions;
	/* VAR_OUTPUT (digital) */
	plcbit InOperation;
	plcbit Busy;
	plcbit SwitchesInitialized;
	plcbit TrackOptionsInitialized;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_InOperation;
	plcbit C_Error;
	plcbit C_Busy;
	plcbit EdgeInitSwitches;
	plcbit EdgeInitTrackOptions;
} MC_DigitalCamSwitch_typ;

typedef struct MC_GearIn
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	signed short RatioNumerator;
	unsigned short RatioDenominator;
	float Acceleration;
	float Deceleration;
	unsigned short MasterParID;
	float MasterParIDMaxVelocity;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned char LockID;
	unsigned long C_Master;
	unsigned long C_Slave;
	signed long C_RatioNumerator;
	signed long C_RatioDenominator;
	float C_Acceleration;
	float C_Deceleration;
	unsigned short C_MasterParID;
	unsigned short CC_ErrorID;
	float C_MasterParIDMaxVelocity;
	unsigned short C_ErrorID;
	unsigned short MpgenIndex;
	unsigned short AutActualStateIndexOffset;
	unsigned char AutActualStateIndexRecIndex;
	unsigned char LockIDMa;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned char MoveID;
	unsigned char LockIDSend;
	unsigned char LockIDReceive;
	unsigned char SavedFrDrvCnt;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit InGear;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_InGear;
	plcbit C_CommandAborted;
	plcbit C_Error;
	plcbit WaitForTelegrams;
} MC_GearIn_typ;

typedef struct MC_GearInPos
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	signed short RatioNumerator;
	unsigned short RatioDenominator;
	float MasterSyncPosition;
	float SlaveSyncPosition;
	unsigned char SyncMode;
	float MasterStartDistance;
	float Velocity;
	float Acceleration;
	unsigned short MasterParID;
	float MasterParIDMaxVelocity;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	signed long C_RatioNumerator;
	signed long C_RatioDenominator;
	signed long Reserve1;
	signed long Reserve2;
	unsigned char C_SyncMode;
	unsigned char LockID;
	unsigned char LockIDPar;
	signed long C_MasterStartDistance;
	signed long C_MasterSyncPosition;
	signed long C_SlaveSyncPosition;
	float C_Velocity;
	float C_Acceleration;
	unsigned short C_MasterParID;
	float C_MasterParIDMaxVelocity;
	unsigned short C_ErrorID;
	signed long MaPosition;
	unsigned short DataTyp;
	signed long MA_LastSyncPosition;
	signed long SL_LastSyncPosition;
	unsigned short MpgenIndex;
	unsigned char Reserve3;
	unsigned char LockIDReceive;
	unsigned short AutActualCamTypeOffset;
	unsigned char AutActualCamTypeRecIndex;
	unsigned char LockIDSend;
	unsigned short AutActualStateIndexOffset;
	unsigned char AutActualStateIndexRecIndex;
	unsigned char LockIDMa;
	unsigned char sendSlot;
	unsigned char readSlot;
	unsigned char state;
	unsigned char MoveID;
	unsigned short CC_ErrorID;
	unsigned short Reserve4;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit StartSync;
	plcbit InSync;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_StartSync;
	plcbit C_InSync;
	plcbit C_CommandAborted;
	plcbit C_Error;
	plcbit CC_Error;
} MC_GearInPos_typ;

typedef struct MC_GearOut
{
	/* VAR_INPUT (analog) */
	unsigned long Slave;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Slave;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_GearOut_typ;

typedef struct MC_Halt
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Deceleration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	float C_Deceleration;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char MoveID;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit cmdExecute;
	plcbit C_Done;
	plcbit C_CommandAborted;
	plcbit C_Error;
} MC_Halt_typ;

typedef struct MC_Home
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Position;
	unsigned char HomingMode;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	signed long C_Position;
	unsigned char C_HomingMode;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char MoveID;
	float CC_Position;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_CommandAborted;
	plcbit C_Error;
} MC_Home_typ;

typedef struct MC_LimitLoad
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Load;
	unsigned char Direction;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0133_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Busy;
	plcbit Ready;
	plcbit Active;
	plcbit Error;
} MC_LimitLoad_typ;

typedef struct MC_MoveAbsolute
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Position;
	float Velocity;
	float Acceleration;
	float Deceleration;
	unsigned char Direction;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	signed long C_Position;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	unsigned char C_Direction;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	signed long C_CommandedOffset;
	unsigned char state;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit cmdExecute;
	plcbit C_Done;
	plcbit C_CommandAborted;
	plcbit C_Error;
} MC_MoveAbsolute_typ;

typedef struct MC_MoveAdditive
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Distance;
	float Velocity;
	float Acceleration;
	float Deceleration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	signed long C_Distance;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	unsigned short C_ErrorID;
	signed long C_CommandedPosition;
	signed long C_CommandedOffset;
	unsigned char state;
	unsigned char LockIDPar;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit cmdExecute;
	plcbit C_Done;
	plcbit C_CommandAborted;
	plcbit C_Error;
} MC_MoveAdditive_typ;

typedef struct MC_MoveVelocity
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Velocity;
	float Acceleration;
	float Deceleration;
	unsigned char Direction;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	float C_Velocity;
	float C_Acceleration;
	float C_Deceleration;
	unsigned char C_Direction;
	unsigned char LockIDPar;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit InVelocity;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit cmdExecute;
	plcbit C_InVelocity;
	plcbit C_CommandAborted;
	plcbit C_Error;
} MC_MoveVelocity_typ;

typedef struct MC_Phasing
{
	/* VAR_INPUT (analog) */
	unsigned long Master;
	unsigned long Slave;
	float PhaseShift;
	float Velocity;
	float Acceleration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Master;
	unsigned long C_Slave;
	signed long C_PhaseShift;
	float C_Velocity;
	float C_Acceleration;
	unsigned short C_ErrorID;
	unsigned short MpgenIndex;
	unsigned short MpgenStatusOffset;
	unsigned char MpgenStatusRecIndex;
	unsigned char LockIDPar;
	unsigned char SavedFrDrvCnt;
	unsigned char state;
	unsigned char FbID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_CommandAborted;
	plcbit C_Error;
	plcbit WaitForTelegrams;
} MC_Phasing_typ;

typedef struct MC_Power
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned char state;
	unsigned short C_ErrorID;
	unsigned long C_Axis;
	unsigned long startTicks;
	unsigned short AxisTypeCtrlOffAxisState;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Status;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_Power_typ;

typedef struct MC_ReadActualPosition
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float Position;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_ReadActualPosition_typ;

typedef struct MC_ReadActualTorque
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float Torque;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short TorqueOffset;
	unsigned char TorqueRecIndex;
	unsigned char LockID;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_ReadActualTorque_typ;

typedef struct MC_ReadActualVelocity
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float Velocity;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_ReadActualVelocity_typ;

typedef struct MC_ReadAxisError
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	unsigned long DataAddress;
	unsigned short DataLength;
	plcstring DataObjectName[13];
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	unsigned short AxisErrorID;
	unsigned short AxisErrorCount;
	/* VAR (analog) */
	unsigned long C_Axis;
	plcstring C_DataObjectName[13];
	unsigned short Reserve;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit Acknowledge;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Acknowledge;
	plcbit C_OldAcknowledge;
	plcbit writeText;
	plcbit C_Error;
} MC_ReadAxisError_typ;

typedef struct MC_ReadBoolParameter
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	signed short ParameterNumber;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	plcbit Value;
	/* VAR (digital) */
	plcbit C_Error;
} MC_ReadBoolParameter_typ;

typedef struct MC_ReadDigitalInput
{
	/* VAR_INPUT (analog) */
	struct MC_INPUT_REF Input;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_INPUT_REF C_Input;
	unsigned short C_ErrorID;
	unsigned short ReadDigitalInputOffset;
	unsigned char ReadDigitalInputRecIndex;
	unsigned char LockID;
	unsigned short ReadDigitalInputValue;
	unsigned short ReadDigitalInputMask;
	unsigned char state;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	plcbit Value;
	/* VAR (digital) */
	plcbit C_Error;
} MC_ReadDigitalInput_typ;

typedef struct MC_ReadDigitalOutput
{
	/* VAR_INPUT (analog) */
	struct MC_OUTPUT_REF Output;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_OUTPUT_REF C_Output;
	unsigned short C_ErrorID;
	unsigned short ReadDigitalOutputOffset;
	unsigned char ReadDigitalOutputRecIndex;
	unsigned char LockID;
	unsigned short ReadDigitalOutputValue;
	unsigned short ReadDigitalOutputMask;
	unsigned char state;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	plcbit Value;
	/* VAR (digital) */
	plcbit C_Error;
} MC_ReadDigitalOutput_typ;

typedef struct MC_ReadParameter
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	signed short ParameterNumber;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float Value;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_ReadParameter_typ;

typedef struct MC_ReadStatus
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Valid;
	plcbit Busy;
	plcbit Error;
	plcbit Errorstop;
	plcbit Disabled;
	plcbit Stopping;
	plcbit StandStill;
	plcbit DiscreteMotion;
	plcbit ContinuousMotion;
	plcbit SynchronizedMotion;
	plcbit Homing;
	/* VAR (digital) */
	plcbit C_Error;
} MC_ReadStatus_typ;

typedef struct MC_Reset
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_Reset_typ;

typedef struct MC_SetOverride
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float VelFactor;
	float AccFactor;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	float C_VelFactor;
	float C_AccFactor;
	float OldVelFactor;
	unsigned short C_ErrorID;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	/* VAR_OUTPUT (digital) */
	plcbit Enabled;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Error;
} MC_SetOverride_typ;

typedef struct MC_Stop
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Deceleration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	unsigned short C_ErrorID;
	float C_Deceleration;
	unsigned char state;
	unsigned char MoveID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Error;
	plcbit C_CommandAborted;
} MC_Stop_typ;

typedef struct MC_TouchProbe
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	struct MC_TRIGGER_REF TriggerInput;
	float FirstPosition;
	float LastPosition;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	float RecordedPosition;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_TRIGGER_REF C_TriggerInput;
	float C_FirstPosition;
	float C_LastPosition;
	unsigned short C_ErrorID;
	float C_RecordedPosition;
	unsigned char SavedToDrvCnt;
	unsigned char Reserve2;
	unsigned char state;
	unsigned char LockID;
	unsigned char LockIDPar;
	unsigned short cycleTime;
	signed long LatchPos;
	unsigned short LatchStatusOffset;
	unsigned char LatchStatusRecIndex;
	unsigned char Reserve1;
	unsigned short LatchPosOffset;
	unsigned char LatchPosRecIndex;
	unsigned char SptID;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	plcbit WindowOnly;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit CommandAborted;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Done;
	plcbit C_Busy;
	plcbit C_Execute;
	plcbit C_WindowOnly;
	plcbit C_Error;
	plcbit C_CommandAborted;
	plcbit InputSourceChanged;
	plcbit EdgeChanged;
	plcbit PosSourceChanged;
} MC_TouchProbe_typ;

typedef struct MC_TorqueControl
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Torque;
	float TorqueRamp;
	float Velocity;
	float Acceleration;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0096_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit InTorque;
	plcbit Busy;
	plcbit Active;
	plcbit CommandAborted;
	plcbit Error;
	plcbit AxisLimitActive;
} MC_TorqueControl_typ;

typedef struct MC_BR_TorqueControl
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	float Torque;
	float TorqueRamp;
	float PosMaxVelocity;
	float NegMaxVelocity;
	float Acceleration;
	unsigned short Mode;
	float TimeLimit;
	unsigned short StartParID;
	unsigned short TorqueParID;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_0100_IS_TYP IS;
	/* VAR_INPUT (digital) */
	plcbit Enable;
	plcbit InitData;
	plcbit StartSignal;
	/* VAR_OUTPUT (digital) */
	plcbit InTorque;
	plcbit Busy;
	plcbit Active;
	plcbit CommandAborted;
	plcbit Error;
	plcbit DataInitialized;
	plcbit WaitingForStart;
	plcbit AxisLimitActive;
} MC_BR_TorqueControl_typ;

typedef struct MC_WriteBoolParameter
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	signed short ParameterNumber;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	signed short C_ParameterNumber;
	unsigned short Reserve;
	unsigned char state;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	plcbit Value;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
} MC_WriteBoolParameter_typ;

typedef struct MC_WriteDigitalOutput
{
	/* VAR_INPUT (analog) */
	struct MC_OUTPUT_REF Output;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	struct MC_OUTPUT_REF C_Output;
	unsigned short C_ErrorID;
	unsigned short WriteDigitalOutputMask;
	unsigned char state;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	plcbit Value;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Value;
	plcbit C_Done;
	plcbit C_Error;
} MC_WriteDigitalOutput_typ;

typedef struct MC_WriteParameter
{
	/* VAR_INPUT (analog) */
	unsigned long Axis;
	signed short ParameterNumber;
	float Value;
	/* VAR_OUTPUT (analog) */
	unsigned short ErrorID;
	/* VAR (analog) */
	unsigned long C_Axis;
	signed short C_ParameterNumber;
	float C_Value;
	unsigned short C_ErrorID;
	unsigned char state;
	unsigned char LockIDPar;
	/* VAR_INPUT (digital) */
	plcbit Execute;
	/* VAR_OUTPUT (digital) */
	plcbit Done;
	plcbit Busy;
	plcbit Error;
	/* VAR (digital) */
	plcbit C_Execute;
	plcbit C_Done;
	plcbit C_Error;
} MC_WriteParameter_typ;



/* Prototyping of functions and function blocks */
void MC_AbortTrigger(struct MC_AbortTrigger* inst);
void MC_BR_AutCommand(struct MC_BR_AutCommand* inst);
void MC_BR_AutControl(struct MC_BR_AutControl* inst);
void MC_BR_AutoCamDwell(struct MC_BR_AutoCamDwell* inst);
void MC_BR_AxisErrorCollector(struct MC_BR_AxisErrorCollector* inst);
void MC_BR_BrakeControl(struct MC_BR_BrakeControl* inst);
void MC_BR_BrakeOperation(struct MC_BR_BrakeOperation* inst);
void MC_BR_CalcCamFromPoints(struct MC_BR_CalcCamFromPoints* inst);
void MC_BR_CalcCamFromSections(struct MC_BR_CalcCamFromSections* inst);
void MC_BR_CalcPointsFromCam(struct MC_BR_CalcPointsFromCam* inst);
void MC_BR_CalcSectionsFromCam(struct MC_BR_CalcSectionsFromCam* inst);
void MC_BR_CamDwell(struct MC_BR_CamDwell* inst);
void MC_BR_CamTransition(struct MC_BR_CamTransition* inst);
void MC_BR_CheckAutCompensation(struct MC_BR_CheckAutCompensation* inst);
void MC_BR_CheckEndlessPosition(struct MC_BR_CheckEndlessPosition* inst);
void MC_BR_CommandError(struct MC_BR_CommandError* inst);
void MC_BR_ConfigPowerStageCheck(struct MC_BR_ConfigPowerStageCheck* inst);
void MC_BR_CrossCutterControl(struct MC_BR_CrossCutterControl* inst);
void MC_BR_CyclicRead(struct MC_BR_CyclicRead* inst);
void MC_BR_CyclicReadDataInfo(struct MC_BR_CyclicReadDataInfo* inst);
void MC_BR_CyclicWrite(struct MC_BR_CyclicWrite* inst);
void MC_BR_DigitalCamSwitch(struct MC_BR_DigitalCamSwitch* inst);
void MC_BR_DownloadCamProfileObj(struct MC_BR_DownloadCamProfileObj* inst);
void MC_BR_DownloadCamProfileData(struct MC_BR_DownloadCamProfileData* inst);
void MC_BR_DownloadParSequ(struct MC_BR_DownloadParSequ* inst);
void MC_BR_EventMoveAbsolute(struct MC_BR_EventMoveAbsolute* inst);
void MC_BR_EventMoveAdditive(struct MC_BR_EventMoveAdditive* inst);
void MC_BR_EventMoveVelocity(struct MC_BR_EventMoveVelocity* inst);
void MC_BR_GearIn(struct MC_BR_GearIn* inst);
void MC_BR_GetCamMasterPosition(struct MC_BR_GetCamMasterPosition* inst);
void MC_BR_GetCamSlavePosition(struct MC_BR_GetCamSlavePosition* inst);
void MC_BR_GetErrorText(struct MC_BR_GetErrorText* inst);
void MC_BR_GetHardwareInfo(struct MC_BR_GetHardwareInfo* inst);
void MC_BR_GetParIDTransferInfo(struct MC_BR_GetParIDTransferInfo* inst);
void MC_BR_HomeAcpEncoder(struct MC_BR_HomeAcpEncoder* inst);
void MC_BR_InitAutData(struct MC_BR_InitAutData* inst);
void MC_BR_InitAutEvent(struct MC_BR_InitAutEvent* inst);
void MC_BR_InitAutPar(struct MC_BR_InitAutPar* inst);
void MC_BR_InitAutState(struct MC_BR_InitAutState* inst);
void MC_BR_InitAxisPar(struct MC_BR_InitAxisPar* inst);
void MC_BR_InitAxisSubjectPar(struct MC_BR_InitAxisSubjectPar* inst);
void MC_BR_InitCyclicRead(struct MC_BR_InitCyclicRead* inst);
void MC_BR_InitCyclicWrite(struct MC_BR_InitCyclicWrite* inst);
void MC_BR_InitEndlessPosition(struct MC_BR_InitEndlessPosition* inst);
void MC_BR_InitEndlessPosAcpEnc(struct MC_BR_InitEndlessPosAcpEnc* inst);
void MC_BR_InitMasterParIDTransfer(struct MC_BR_InitMasterParIDTransfer* inst);
void MC_BR_InitModPos(struct MC_BR_InitModPos* inst);
void MC_BR_InitParList(struct MC_BR_InitParList* inst);
void MC_BR_InitParSequ(struct MC_BR_InitParSequ* inst);
void MC_BR_InitParTabObj(struct MC_BR_InitParTabObj* inst);
void MC_BR_InitReceiveNetworkData(struct MC_BR_InitReceiveNetworkData* inst);
void MC_BR_InitReceiveNetworkEnc(struct MC_BR_InitReceiveNetworkEnc* inst);
void MC_BR_InitReceiveParID(struct MC_BR_InitReceiveParID* inst);
void MC_BR_InitSendParID(struct MC_BR_InitSendParID* inst);
void MC_BR_JogVelocity(struct MC_BR_JogVelocity* inst);
void MC_BR_JogLimitPosition(struct MC_BR_JogLimitPosition* inst);
void MC_BR_JogTargetPosition(struct MC_BR_JogTargetPosition* inst);
void MC_BR_LimitLoad(struct MC_BR_LimitLoad* inst);
void MC_BR_LimitLoadCam(struct MC_BR_LimitLoadCam* inst);
void MC_BR_LoadAxisPar(struct MC_BR_LoadAxisPar* inst);
void MC_BR_MoveAbsoluteTriggStop(struct MC_BR_MoveAbsoluteTriggStop* inst);
void MC_BR_MoveAdditiveTriggStop(struct MC_BR_MoveAdditiveTriggStop* inst);
void MC_BR_MoveCyclicPosition(struct MC_BR_MoveCyclicPosition* inst);
void MC_BR_MoveCyclicPositionExt(struct MC_BR_MoveCyclicPositionExt* inst);
void MC_BR_MoveCyclicVelocity(struct MC_BR_MoveCyclicVelocity* inst);
void MC_BR_MoveCyclicVelocityExt(struct MC_BR_MoveCyclicVelocityExt* inst);
void MC_BR_MoveVelocityTriggStop(struct MC_BR_MoveVelocityTriggStop* inst);
void MC_BR_NetTrace(struct MC_BR_NetTrace* inst);
void MC_BR_NetworkInit(struct MC_BR_NetworkInit* inst);
void MC_BR_Offset(struct MC_BR_Offset* inst);
void MC_BR_OffsetVelocity(struct MC_BR_OffsetVelocity* inst);
void MC_BR_OffsetZone(struct MC_BR_OffsetZone* inst);
void MC_BR_GetParIDInfo(struct MC_BR_GetParIDInfo* inst);
void MC_BR_ParTrace(struct MC_BR_ParTrace* inst);
void MC_BR_ParTraceConfig(struct MC_BR_ParTraceConfig* inst);
void MC_BR_Phasing(struct MC_BR_Phasing* inst);
void MC_BR_PowerMeter(struct MC_BR_PowerMeter* inst);
void MC_BR_ReadAutPosition(struct MC_BR_ReadAutPosition* inst);
void MC_BR_ReadAxisError(struct MC_BR_ReadAxisError* inst);
void MC_BR_ReadCyclicPosition(struct MC_BR_ReadCyclicPosition* inst);
void MC_BR_ReadDriveStatus(struct MC_BR_ReadDriveStatus* inst);
void MC_BR_ReadNetTraceStatus(struct MC_BR_ReadNetTraceStatus* inst);
void MC_BR_ReadParID(struct MC_BR_ReadParID* inst);
void MC_BR_ReadParIDText(struct MC_BR_ReadParIDText* inst);
void MC_BR_ReadParTraceStatus(struct MC_BR_ReadParTraceStatus* inst);
void MC_BR_ReceiveParIDOnPLC(struct MC_BR_ReceiveParIDOnPLC* inst);
void MC_BR_ResetAutPar(struct MC_BR_ResetAutPar* inst);
void MC_BR_SaveAxisPar(struct MC_BR_SaveAxisPar* inst);
void MC_BR_SaveCamProfileObj(struct MC_BR_SaveCamProfileObj* inst);
void MC_BR_SetHardwareInputs(struct MC_BR_SetHardwareInputs* inst);
void MC_BR_SetupController(struct MC_BR_SetupController* inst);
void MC_BR_SetupFromParTabObj(struct MC_BR_SetupFromParTabObj* inst);
void MC_BR_SetupInductionMotor(struct MC_BR_SetupInductionMotor* inst);
void MC_BR_SetupIsqRipple(struct MC_BR_SetupIsqRipple* inst);
void MC_BR_SetupMotorPhasing(struct MC_BR_SetupMotorPhasing* inst);
void MC_BR_SetupSynchronMotor(struct MC_BR_SetupSynchronMotor* inst);
void MC_BR_Simulation(struct MC_BR_Simulation* inst);
void MC_BR_TouchProbe(struct MC_BR_TouchProbe* inst);
void MC_BR_VelocityControl(struct MC_BR_VelocityControl* inst);
void MC_BR_WriteParID(struct MC_BR_WriteParID* inst);
void MC_BR_WriteParIDText(struct MC_BR_WriteParIDText* inst);
void MC_CamIn(struct MC_CamIn* inst);
void MC_CamOut(struct MC_CamOut* inst);
void MC_CamTableSelect(struct MC_CamTableSelect* inst);
void MC_DigitalCamSwitch(struct MC_DigitalCamSwitch* inst);
void MC_GearIn(struct MC_GearIn* inst);
void MC_GearInPos(struct MC_GearInPos* inst);
void MC_GearOut(struct MC_GearOut* inst);
void MC_Halt(struct MC_Halt* inst);
void MC_Home(struct MC_Home* inst);
void MC_LimitLoad(struct MC_LimitLoad* inst);
void MC_MoveAbsolute(struct MC_MoveAbsolute* inst);
void MC_MoveAdditive(struct MC_MoveAdditive* inst);
void MC_MoveVelocity(struct MC_MoveVelocity* inst);
void MC_Phasing(struct MC_Phasing* inst);
void MC_Power(struct MC_Power* inst);
void MC_ReadActualPosition(struct MC_ReadActualPosition* inst);
void MC_ReadActualTorque(struct MC_ReadActualTorque* inst);
void MC_ReadActualVelocity(struct MC_ReadActualVelocity* inst);
void MC_ReadAxisError(struct MC_ReadAxisError* inst);
void MC_ReadBoolParameter(struct MC_ReadBoolParameter* inst);
void MC_ReadDigitalInput(struct MC_ReadDigitalInput* inst);
void MC_ReadDigitalOutput(struct MC_ReadDigitalOutput* inst);
void MC_ReadParameter(struct MC_ReadParameter* inst);
void MC_ReadStatus(struct MC_ReadStatus* inst);
void MC_Reset(struct MC_Reset* inst);
void MC_SetOverride(struct MC_SetOverride* inst);
void MC_Stop(struct MC_Stop* inst);
void MC_TouchProbe(struct MC_TouchProbe* inst);
void MC_TorqueControl(struct MC_TorqueControl* inst);
void MC_BR_TorqueControl(struct MC_BR_TorqueControl* inst);
void MC_WriteBoolParameter(struct MC_WriteBoolParameter* inst);
void MC_WriteDigitalOutput(struct MC_WriteDigitalOutput* inst);
void MC_WriteParameter(struct MC_WriteParameter* inst);



#endif /* _ACP10_MC_ */

#ifdef __cplusplus
};
#endif


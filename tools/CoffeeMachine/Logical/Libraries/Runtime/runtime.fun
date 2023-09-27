(********************************************************************
 * COPYRIGHT (C) BERNECKER + RAINER, AUSTRIA, A-5142 EGGELSBERG
 ********************************************************************
 * Library: Runtime
 * File: Runtime.fun
 * Created: 11.11.2003
 ********************************************************************
 * Functions and function blocks of library Runtime
 ********************************************************************)
FUNCTION_BLOCK r_trig 			(*for internal use only - do not use this function in user programs*)
	VAR_INPUT
		CLK	:BOOL;
	END_VAR
	VAR_OUTPUT
		Q	:BOOL;
	END_VAR
	VAR
		M	:BOOL;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK f_trig 			(*for internal use only - do not use this function in user programs*)
	VAR_INPUT
		CLK	:BOOL;
	END_VAR
	VAR_OUTPUT
		Q	:BOOL;
	END_VAR
	VAR
		M	:BOOL;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION_BLOCK rf_trig 			(*for internal use only - do not use this function in user programs*)
	VAR_INPUT
		CLK	:BOOL;
	END_VAR
	VAR_OUTPUT
		Q	:BOOL;
	END_VAR
	VAR
		M	:BOOL;
	END_VAR
END_FUNCTION_BLOCK
FUNCTION GetTime : TIME 		(*for internal use only - do not use this function in user programs*)
END_FUNCTION
FUNCTION_BLOCK SFCActionControl (*for internal use only - do not use this function in user programs*)
	VAR_INPUT
		N	:BOOL;
		R0	:BOOL;
		S0	:BOOL;
		L	:BOOL;
		D	:BOOL;
		P	:BOOL;
		SD	:BOOL;
		DS	:BOOL;
		SL	:BOOL;
		T	:TIME;
	END_VAR
	VAR_OUTPUT
		Q	:BOOL;
	END_VAR
	VAR
		S_FF_SET	:USINT;
		S_FF_R1	:USINT;
		S_FF_Q	:USINT;
		dummy1	:USINT;
		L_TMR_PT	:TIME;
		L_TMR_ET	:TIME;
		L_TMR_STAR	:TIME;
		L_TMR_IN	:USINT;
		L_TMR_Q	:USINT;
		L_TMR_M	:USINT;
		dummy2	:USINT;
		D_TMR_PT	:TIME;
		D_TMR_ET	:TIME;
		D_TMR_STAR	:TIME;
		D_TMR_IN	:USINT;
		D_TMR_Q	:USINT;
		D_TMR_M	:USINT;
		dummy3	:USINT;
		P_TRIG_CLK	:USINT;
		P_TRIG_Q	:USINT;
		P_TRIG_M	:USINT;
		dummy4	:USINT;
		SD_TMR_PT	:TIME;
		SD_TMR_ET	:TIME;
		SD_TMR_STA	:TIME;
		SD_TMR_IN	:USINT;
		SD_TMR_Q	:USINT;
		SD_TMR_M	:USINT;
		dummy5	:USINT;
		SD_FF_SET	:USINT;
		SD_FF_R1	:USINT;
		SD_FF_Q	:USINT;
		DS_FF_SET	:USINT;
		DS_FF_R1	:USINT;
		DS_FF_Q	:USINT;
		DS_TMR_PT	:TIME;
		DS_TMR_ET	:TIME;
		DS_TMR_STA	:TIME;
		DS_TMR_IN	:USINT;
		DS_TMR_Q	:USINT;
		DS_TMR_M	:USINT;
		dummy6	:USINT;
		SL_FF_SET	:USINT;
		SL_FF_R1	:USINT;
		SL_FF_Q	:USINT;
		dummy7	:USINT;
		SL_TMR_PT	:TIME;
		SL_TMR_ET	:TIME;
		SL_TMR_STA	:TIME;
		SL_TMR_IN	:USINT;
		SL_TMR_Q	:USINT;
		SL_TMR_M	:USINT;
		dummy8	:USINT;
	END_VAR
END_FUNCTION_BLOCK

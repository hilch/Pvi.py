/********************************************************************
 * COPYRIGHT -- B&R
 ********************************************************************
 * Program: Heating
 * File: Heating.c
 * Author: B&R
 * Created: June 12, 2007
 ********************************************************************
 * Implementation of program Heating
 ********************************************************************/

#include <bur/plctypes.h>

#ifdef _DEFAULT_INCLUDES
 #include <AsDefault.h>
#endif

/* prototyping */
BOOL inWindow(REAL set, REAL act, REAL window);	

void _INIT HeatingINIT( void )
{
	/* PID parameters for water flow heater */
	tempLCRPIDpara.WX_max   = 100.0;
	tempLCRPIDpara.WX_min   = 0.0;
	tempLCRPIDpara.invert   = 0;
	tempLCRPIDpara.deadband = 0.0;
	tempLCRPIDpara.dY_max   = 0.0;
	tempLCRPIDpara.Kp       = 1.8; 		/*2.7;*/
	tempLCRPIDpara.Tn       = 12.0; 	/*6.2;*/
	tempLCRPIDpara.Tv       = 0.0; 		/*1.6;*/
	tempLCRPIDpara.Tf       = 0.0; 		/*0.16;*/
	tempLCRPIDpara.Kw       = 1.0;           
	tempLCRPIDpara.Kfbk     = 1.0;		/* windup damping enabled */
	tempLCRPIDpara.fbk_mode = LCRPID_FBK_MODE_INTERN;
	tempLCRPIDpara.d_mode   = LCRPID_D_MODE_X;
	
	gHeating.cmd.updatePIDpar = 1;
	
	/* simulation of water pipe */
	simLCRPT2.V     = 3.9;
	simLCRPT2.T1    = 0.9;
	simLCRPT2.T2    = 15.3;
	simLCRPT2.y_set = 20.0;       		/* for simulation start at minimum controller output */
	simLCRPT2.set   = 1;
        
	/* Parameters for PID controller */
	tempLCRPID.Y_max  = 100.0;
	tempLCRPID.Y_min  = 20.0 / simLCRPT2.V;       /* limited to defined environmental temperature */
	tempLCRPID.A      = 0.0;
	tempLCRPID.Y_man  = 0.0;
	tempLCRPID.Y_fbk  = 0.0;
	tempLCRPID.hold_I = 0;
	tempLCRPID.mode   = LCRPID_MODE_CLOSE;
	
}

void _CYCLIC HeatingCYCLIC( void )
{
	/* update PID parameters */
	tempLCRPIDpara.enable = 1;
	tempLCRPIDpara.enter  = gHeating.cmd.updatePIDpar;   
	LCRPIDpara(&tempLCRPIDpara);	/* LCRPIDpara function block call */

	gHeating.cmd.updatePIDpar = 0;


	/* start heating as soon as machine is switched on */
	tempLCRPID.enable = 1;
	if (gMainLogic.cmd.switchOnOff)
	{
		tempLCRPID.mode = LCRPID_MODE_AUTO;
	}
	else
	{
		tempLCRPID.mode = LCRPID_MODE_CLOSE;
	}
	tempLCRPID.ident  = tempLCRPIDpara.ident; /* ident of PIDpara -> provides parameters (Kp, Tn, Tv, ...) */
	tempLCRPID.W      = gMainLogic.par.recipe.setTemp;
	tempLCRPID.X      = gHeating.status.actTemp;
	LCRPID(&tempLCRPID);

	aoHeating = (INT)tempLCRPID.Y;

	/* PT2 element */
	simLCRPT2.enable  = 1;
	simLCRPT2.x = tempLCRPID.Y;
	LCRPT2(&simLCRPT2);
	simLCRPT2.set = 0;

	gHeating.status.actTemp = simLCRPT2.y;
	
	/* generate temperature OK flag if temperature is within a certain tolerance window */
	gHeating.status.setTempOK = inWindow(gMainLogic.par.recipe.setTemp, gHeating.status.actTemp, 1.0);
}

BOOL inWindow(REAL set, REAL act, REAL window)
{
	REAL delta = set - act;
	
	if (delta < 0) delta *= -1;

	if (delta < window)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

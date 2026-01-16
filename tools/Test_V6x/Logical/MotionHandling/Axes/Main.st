
PROGRAM _INIT
	gAxisHandling.ax[AX_X].name := 'X';
	gAxisHandling.ax[AX_X].pAxis := ADR(gAxisX);
	axX ACCESS ADR(gAxisHandling.ax[AX_X]);

	size1 := SIZEOF(axX);
	axX.n := 99;

	gAxisHandling.ax[AX_Y].name := 'Y';
	gAxisHandling.ax[AX_Y].pAxis := ADR(gAxisY);
	axY ACCESS ADR(gAxisHandling.ax[AX_Y]);
	 
END_PROGRAM

PROGRAM _CYCLIC

END_PROGRAM

PROGRAM _EXIT
	 
END_PROGRAM


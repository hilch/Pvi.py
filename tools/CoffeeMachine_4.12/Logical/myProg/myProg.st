(********************************************************************
 * COPYRIGHT -- B&R Industrial Automation GmbH
 ********************************************************************
 * Program: myProg
 * File: myProg.st
 * Author: hilchenbachc
 * Created: November 22, 2022
 ********************************************************************
 * Implementation of program myProg
 ********************************************************************)

PROGRAM _INIT
	myComplexStruct.usint := 11;
	myComplexStruct.uint  := 12;
	myComplexStruct.udint := 13;
	myComplexStruct.sint := -11;
	myComplexStruct.int  := -12;
	myComplexStruct.dint := -13;
	myComplexStruct.real := 3.1415;
	myComplexStruct.lreal := 2 * myComplexStruct.real;

	FOR i := 0 TO 9 DO
		myComplexStruct.vector[i+1] := 200 + i;
		FOR j := 0 TO 3 DO
			myComplexStruct.matrix[i,j] := 1000 + (10 * i + j);
		END_FOR
	END_FOR
	myComplexStruct.myEnum := drei;
	myComplexStruct.derived2[3] := 3;
	myComplexStruct.derived2[4] := 4;
	myComplexStruct.derived2[5] := 5;
	myComplexStruct.derived2[6] := 6;
	sizeof_myComplexStruct := SIZEOF(myComplexStruct);	

END_PROGRAM

PROGRAM _CYCLIC

END_PROGRAM

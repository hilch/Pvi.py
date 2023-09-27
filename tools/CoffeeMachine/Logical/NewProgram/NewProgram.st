(********************************************************************
 * COPYRIGHT -- B&R Industrial Automation GmbH
 ********************************************************************
 * Program: NewProgram
 * File: NewProgram.st
 * Author: hilchenbachc
 * Created: October 28, 2022
 ********************************************************************
 * Implementation of program NewProgram
 ********************************************************************)

PROGRAM _INIT

timedelta := T#-3s;

_mystruct.a_bool := TRUE;
_mystruct.text1 := "Unicode";
_mystruct.text2 := 'ASCII';

FOR n := 0 TO 9 DO
	_mystruct.inner1.an_int_array[n] := -5-n;
END_FOR

_mystruct.an_int := -3;
_mystruct.inner1.inner2.an_usint := 7;
_mystruct.inner1.inner2.an_usint := 9;
_mystruct.inner1.inner2.inner3.an_usint := 11;
_mystruct.inner1.inner2.inner3.ton.PT := T#34ms;

//FOR n := 0 TO 9 DO
//	myStructArray[n] := _mystruct;
//	myStructArray[n].an_int := -11-n;
//	myStructArray[n].inner1.inner2.an_usint := INT_TO_USINT(n);
//END_FOR



 sizeofmystruct := SIZEOF(_mystruct);

//floatarray[0] := 3.14;

END_PROGRAM


PROGRAM _CYCLIC

_mystruct.ton( PT := T#4s56ms, IN := TRUE );

END_PROGRAM

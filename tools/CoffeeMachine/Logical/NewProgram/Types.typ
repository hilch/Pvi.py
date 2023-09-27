(********************************************************************
 * COPYRIGHT -- B&R Industrial Automation GmbH
 ********************************************************************
 * Program: NewProgram
 * File: Types.typ
 * Author: hilchenbachc
 * Created: October 31, 2022
 ********************************************************************
 * Local data types of program NewProgram
 ********************************************************************)

TYPE
	InnerInnerInnerStruct : 	STRUCT 
		an_usint : USINT;
		ton : TON := (PT:=T#1234ms);
	END_STRUCT;
	InnerInnerStruct : 	STRUCT 
		an_usint : USINT;
		inner3 : InnerInnerInnerStruct;
	END_STRUCT;
	InnerStruct : 	STRUCT 
		an_int_array : ARRAY[0..9]OF INT;
		inner2 : InnerInnerStruct;
	END_STRUCT;
	MyStruct : 	STRUCT 
		a_bool : BOOL;
		ton : TON;
		text1 : WSTRING[13];
		text2 : STRING[13];
		inner1 : InnerStruct;
		an_int : INT;
	END_STRUCT;
END_TYPE

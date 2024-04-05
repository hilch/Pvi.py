
TYPE
	myStructType : 	STRUCT 
		member : USINT;
	END_STRUCT;
	myEnumType : 
		(
		eins,
		zwei,
		drei
		);
	myDerivedType :ARRAY[3..6]OF USINT;
	myComplexStructType : 	STRUCT 
		element : USINT;
		positionDataElements : ARRAY[2..2]OF MC_ENDLESS_POSITION;
		myStruct1 : myStructType;
		myStruct2 : myStructType;
		myEnum : myEnumType;
		myDerived : myDerivedType;
	END_STRUCT;
END_TYPE

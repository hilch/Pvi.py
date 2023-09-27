(********************************************************************
 * COPYRIGHT -- Bernecker + Rainer
 ********************************************************************
 * Program: visTrend
 * File: visTrend.typ
 * Author: B&R
 * Created: June 11, 2008
 ********************************************************************
 * Local data types of program visTrend
 ********************************************************************)

TYPE
	Trend_type : 	STRUCT  (*Trend Type*)
		Cursor2StatusDatapoint : UINT; (*Status datapoint of Cursor1*)
		Cursor2Valid : UINT; (*Valid datapoint of Cursor2*)
		Cursor1Valid : UINT; (*Valid datapoint of Cursor1*)
		Cursor1StatusDatapoint : UINT; (*Status datapoint of Cursor1*)
		Cursor2Position : REAL; (*Postion of Cursor2*)
		Cursor1Position : REAL; (*Position of Cursor1*)
		TrendTimeScale : TrendTimeScale_type; (*Instance of TrendTimeScale_type*)
		TrendCurve : ARRAY[0..1] OF TrendCurve_type; (*Instance of TendCurve_type*)
		TrendValueScale : TrendValueScale_type; (*Instance of TendValueScale_type*)
	END_STRUCT;
	TrendCurve_type : 	STRUCT  (*Trend Curve Type*)
		Value : REAL; (*Value of Curve*)
		Cursor2ValueDatapoint : REAL; (*Value of Cursor2*)
		Cursor1ValueDatapoint : REAL;
		StatusDatapoint : UINT;
	END_STRUCT;
	TrendValueScale_type : 	STRUCT  (*TrendValueScale Type*)
		StatusDatapoint : UINT;
		ZoomDatapoint : REAL;
		ScrollDatapoint : REAL;
	END_STRUCT;
	TrendCtrl_type : 	STRUCT  (*Trend Control Type*)
		SelectItemDataPoint : USINT;
	END_STRUCT;
	UserTrend : 	STRUCT  (*User Trend Type*)
		TimeStamp : DATE_AND_TIME;
		TrendData : ARRAY[0..599] OF REAL;
		SampleCount : UDINT;
		SampleOffset : UDINT;
	END_STRUCT;
	TrendTimeScale_type : 	STRUCT  (*TrendTimeScale Type*)
		Cursor2TimeDatapoint : DINT;
		ScrollDatapoint : REAL;
		ModeDatapoint : USINT;
		ZoomDatapoint : REAL;
		StatusDatapoint : USINT;
		Cursor1TimeDatapoint : DINT;
	END_STRUCT;
END_TYPE

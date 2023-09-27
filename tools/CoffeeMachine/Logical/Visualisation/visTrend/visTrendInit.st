(********************************************************************
 * COPYRIGHT -- Bernecker + Rainer
 ********************************************************************
 * Program: visTrend
 * File: visTrendInit.st
 * Author: B&R
 * Created: June 11, 2008
 ********************************************************************
 * Implementation of program visTrend
 ********************************************************************)

PROGRAM _INIT


TrendControl.Cursor1Position := 0;		(* Left position of cursor 1 *)
TrendControl.Cursor2Position := 1;		(* Right position of cursor 2 *)

displayTimeRange := 15;		(* show 15 seconds default *)

scrollOnOff := TRUE;	(* auto scroll enabled *)
viewBuffer := TRUE;		(* defult view complete buffer *)


END_PROGRAM


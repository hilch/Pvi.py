(********************************************************************
 * COPYRIGHT -- Bernecker + Rainer
 ********************************************************************
 * Program: visTrend
 * File: visTrendCyclic.st
 * Author: B&R
 * Created: June 11, 2008
 ********************************************************************
 * Implementation of program visTrend
 ********************************************************************)

PROGRAM _CYCLIC

(* Used for color map 0 = invalied value / 1 = valid value *)

TrendControl.Cursor1Valid := (TrendControl.TrendCurve[0].StatusDatapoint AND 1024) / 1024 ;
TrendControl.Cursor2Valid := (TrendControl.TrendCurve[0].StatusDatapoint AND 2048) / 2048 ;

TrendControl.TrendTimeScale.ModeDatapoint := scrollOnOff;

(* control for view complete buffer or a time range *)

IF (viewBuffer = TRUE) THEN
	TrendControl.TrendTimeScale.ZoomDatapoint := 1;
	TrendControl.TrendTimeScale.ModeDatapoint := 1;
	statusTimeRange := 1;		(* hide iInput control for time range *)
	trendRangeMax := trendSampleCount;
	trendRangeMin := 0;
	statusScrollRange := 1;
ELSE
	newTimeRange := TRUE;
	statusTimeRange := 0;		(* show input control for time range *)
	statusScrollRange := scrollOnOff;
END_IF;

(* a new time range was terminated => new calculation of trend content *)

IF (newTimeRange = TRUE) THEN
	newTimeRange := FALSE;
	
	(* Zoom factor = SampleCount / samples to view
	   configured trend data: SampleCount = 5000
	                          SampleRate = 100 ms
	   configured trend buffer = 5000 * 100 = 50000 ms
	   zoom factor = 5000 / 10 * seconds to display *)
	
	
	TrendControl.TrendTimeScale.ZoomDatapoint := trendSampleCount / ((1000 / trendSampleRate) * displayTimeRange);
	(*TrendControl.TrendTimeScale.ModeDatapoint := 1;*)
	trendRangeMin := trendSampleCount - ((1000 / trendSampleRate) * displayTimeRange); 
	
END_IF;

END_PROGRAM

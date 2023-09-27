(********************************************************************
 * COPYRIGHT (C) BERNECKER + RAINER, AUSTRIA, A-5142 EGGELSBERG
 ********************************************************************
 * Library: Visapi
 * File: Visapi.fun
 * Created: 11.11.2003
 ********************************************************************
 * Functions and function blocks of library Visapi
 ********************************************************************)
FUNCTION VA_Attach : UINT (*attach to a VC SG4 drawbox control*)
	VAR_INPUT
		enable : BOOL;	(*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiType : UDINT; (*reserved for later use*)
		uiPara : UDINT;(*pointer to STRING which specifies the location fo the drawbox control*)
	END_VAR
END_FUNCTION

FUNCTION VA_BlitBitmap : UINT (*draw a part of a bitmap*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pBitmap : UDINT; (*pointer to the bitmap structure*)
		iDestX : DINT; (*x coordinate where the loaded graphic is drawn*)
		iDestY : DINT; (*y coordinate where the loaded graphic is drawn*)
		iClipX1 : DINT; (*x coordinate of the upper left corner of the clipping area*)
		iClipY1 : DINT; (*y coordinate of the upper left corner of the clipping area*)
		iClipX2 : DINT; (*x coordinate of the lower right corner of the clipping area*)
		iClipY2 : DINT; (*y coordinate of the lower right corner of the clipping area*)
		uiFlags : UDINT; (*flag that specifies whether the parameters are being evaluated for the clipping area*)
	END_VAR
END_FUNCTION

FUNCTION VA_Configure : UINT (*function is only used internally*)
	VAR_INPUT
		enable : BOOL; 
		ucProjectName : STRING[80];
		uiOption : UDINT;
		uiValue : UDINT;
	END_VAR
END_FUNCTION

FUNCTION VA_CopyScreenRect : UINT (*copy a screen content to another position*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		x1 : UINT; (*x coordinate of the upper left corner of the rectangle to be copied*)
		y1 : UINT; (*y coordinate of the upper left corner of the rectangle to be copied*)
		x2 : UINT; (*x coordinate of the lower right corner of the rectangle to be copied*)
		y2 : UINT; (*y coordinate of the lower right corner of the rectangle to be copied*)
		dx : INT; (*x coordinate of the lower right corner of the rectangle to be copied*)
		dy : INT; (*number of pixels in Y direction in which the rectangle should be copied*)
	END_VAR
END_FUNCTION

FUNCTION VA_DelAlarmHistory : UINT (*delete alarm history*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetActiveAlarmCount : UINT (*get active alarmcount*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		AlarmCount : UDINT; (*number of active alarms*)
	END_VAR
END_FUNCTION

FUNCTION VA_Detach : UINT (*detach from a VC SG4 drawbox control*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_DrawBitmap : UINT (*draw a bitmap*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		index : UINT; (*index of the bitmap in the project*)
		x : UINT; (*x coordinate of the upper left corner of the bitmap*)
		y : UINT; (*y coordinate of the upper left corner of the bitmap*)
	END_VAR
END_FUNCTION

FUNCTION VA_Ellipse : UINT (*draw an ellipse / circle*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		x : UINT; (*x coordinate of the middle point of the ellipse*)
		y : UINT; (*y coordinate of the middle point of the ellipse*)
		heigth : UINT; (*height of the ellipse in pixels*)
		width : UINT; (*width of the ellipse in pixels*)
		fill : UINT; (*ellipse fill color*)
		color : UINT; (*ellipse border color*)
	END_VAR
END_FUNCTION

FUNCTION VA_ExchangeFont : UINT (*function is only used internally*)
	VAR_INPUT
		enable : BOOL; 
		VCHandle : UDINT; 
		cIndex : USINT;
		cNewIndex : USINT;
	END_VAR
END_FUNCTION

FUNCTION VA_ExtractKeyMatrix : UINT (*read key matrix information and use of timeout*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pKeyMatrix : UDINT; (*pointer to start address of the key address array*)
		uiKeysToRead : UDINT; (*number of keys to be read*)
		puiKeyRead : UDINT; (*number of keys read*)
		uiTimeoutInMsec : UDINT; (*timeout in ms.*)
		puiAgeInMsec : UDINT; (*pointer to integer where time is written how long it takes to read the key matrix*)
	END_VAR
END_FUNCTION

FUNCTION VA_FreeBitmap : UINT (*release handle from a bitmap on the target*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pBitmap : UDINT; (*pointer to the bitmap structure*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetActAlarmList : UINT (*read entry from actual alarm list*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pcAlarmLine : DINT; (*pointer to STRING which should record the alarm line*)
		plLen : DINT; (*pointer to DINT which contains the length of the alarm line*)
		iFunction : UINT; (*function to execute 1 = Read First alarm, 2 = Read next alarm*)
		cSeperator : USINT; (*separation character to be inserted into the alarm line*)
		cDateTimeFormat : USINT; (*desired format for date and time output in the alarm list*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetAlCurPos : UINT (*get alarm control cursor position*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pGroupNumber : DINT; (*pointer to DINT which contains the group number of the alarm entry at the current cursor position*)
		pAlarmNumber : DINT; (*pointer to DINT which contains the alarm number of the alarm entry at the current cursor position*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetAlarmList : UINT (*read entry from historical alarm list*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pcAlarmLine : DINT; (*pointer to STRING which should record the alarm line*)
		plLen : DINT; (*pointer to DINT which contains the length of the alarm line*)
		iFunction : UINT; (*function to execute 1 = read first alarm, 2 = read next alarm*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetBrightness : UINT (*get brightness of the display*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pValue : UDINT; (*pointer to brightness value set for the display*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetCalStatus : UINT (*get calibration status while calibrating touch*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetContrast : UINT (*get display contrast*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetDisplayInfo : UINT (*read display information*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		InfoType : UDINT; (*type of info to read*)
		pValue : UDINT; (*pointer to UDINT where the display information is written to*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetExAlarmList : UINT (*read entries from alarm list*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pcAlarmLine : DINT; (*pointer to STRING which should record the alarm line*)
		plLen : DINT; (*pointer to DINT which contains the length of the alarm line*)
		iFunction : UINT; (*function to execute 1 = read first alarm, 2 = read next alarm*)
		cSeperator : USINT; (*separation character to be inserted into the alarm line*)
		cDateTimeFormat : USINT; (*desired format for date and time output in the alarm list*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetKeyMatrix : UINT (*read key matrix information*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pKeyMatrix : UDINT; (*pointer to USINT array*)
		KeysToRead : UDINT; (*number of keys to be read*)
		pKeysRead : UDINT; (*pointer to integer containing the number of keys read*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetPaletteColor : UDINT (*get RGB value of the given color index*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiIndex : USINT; (*index of the color which should be retrieved (0-255)*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetPanelStatus : UINT (*get status of connected panel*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		puiPanelStatus : UDINT; (*pointer to UDINT variable containing the panel status*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetTextByTextGroup : UINT (*read text from textgroup of the active language*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		TG_id : UDINT; (*id number of the text group to be read*)
		TGT_id : UINT; (*id number of the line to be read in the text group*)
		pcText : UDINT; (*pointer to STRING containing the text of the textgroup*)
		psTextlength : UDINT; (*pointer to UDINT variable*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetTouchAction : UINT (*get touch action of the display touch*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiType : UDINT; (*retrieval type 0 = processed, 1 = realtime*)
		pStatus : UDINT; (*pointer to UDINT variable containing the status*)
	END_VAR
END_FUNCTION

FUNCTION VA_LangIsAvailable : UINT (*check if language index is available.*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiIndex : UDINT; (*index of language*)
		pucIsInstalled : UDINT; (*status whether the language on the target system is available*)
	END_VAR
END_FUNCTION

FUNCTION VA_Line : UINT (*draw a line*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		x1 : UINT; (*x coordinate for the start position of the line*)
		y1 : UINT; (*y coordinate for the start position of the line*)
		x2 : UINT; (*x coordinate for the end position of the line*)
		y2 : UINT; (*y coordinate for the end position of the line*)
		color : UINT; (*line color*)
	END_VAR
END_FUNCTION

FUNCTION VA_LoadBitmap : UINT (*get handle for a bitmap on the target*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT;(*handle of visualization object*)
		ucDevice : STRING[80]; (*pointer to STRING which contains the file device*)
		ucPath : STRING[80]; (*pointer to STRING which contains the path of the PNG file*)
		ppBitmap : UDINT; (*pointer to pointer to Bitmap structure*)
	END_VAR
END_FUNCTION

FUNCTION VA_NGetAlCurPos : UINT (*get alarm control cursor position*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pGroupNumber : DINT; (*pointer to DINT variable containing the group number*)
		pAlarmNumber : DINT; (*pointer to DINT variable containing the alarm number*)
	END_VAR
END_FUNCTION

FUNCTION VA_NGetCalStatus : UINT (*get calibration status while calibrating touch*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pValue : UDINT; (*pointer to UDINT containing the current state*)
	END_VAR
END_FUNCTION

FUNCTION VA_NGetContrast : UINT (*get display contrast*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pValue : UDINT; (*pointer to UDINT containing contrast value*)
	END_VAR
END_FUNCTION

FUNCTION VA_NGetPaletteColor : UDINT (*get RGB value of the given color index*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiIndex : USINT; (*index of the color which should be retrieved (0-255)*)
		pValue : UDINT; (*pointer to UDINT containing color value*)
	END_VAR
END_FUNCTION

FUNCTION VA_Quit : UINT (*quit single alarm*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		usGroupNumber : UINT; (*group number where the alarm to be acknowledged is located*)
		usAlarmNumber : UINT; (*alarm number of the alarm which should be acknowledged*)
	END_VAR
END_FUNCTION

FUNCTION VA_QuitAlarms : UINT (*quit all alarms of the given alarm group*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		wGroupNumber : UINT; (*group number which should be acknowledged*)
	END_VAR
END_FUNCTION

FUNCTION VA_Rect : UINT (*draw a rectangle*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		x1 : UINT; (*x coordinate of the upper left corner of the rectangle*)
		y1 : UINT; (*y coordinate of the upper left corner of the rectangle*)
		width : UINT; (*width of the rectangle*)
		height : UINT; (*height of the rectangle*)
		fill : UINT; (*filling color of the rectangle*)
		color : UINT; (*border color of the rectangle*)
	END_VAR
END_FUNCTION

FUNCTION VA_Redraw : UINT (*redraw screen content / update VC SG4 drawbox control*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_Saccess : UINT (*get right to access device driver*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_SaveSettings : UINT (*save display settings*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiAction : UINT; (*action 1 = store, 2 = check whether storing is active*)
	END_VAR
END_FUNCTION

FUNCTION VA_SetBacklight : UINT (*enable/disable display backlight*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		bSet : BOOL; (*0 = turn backlight off, 1 = turn backlight on*)
	END_VAR
END_FUNCTION

FUNCTION VA_SetBrightness : UINT (*set the brightness of the display*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiPercent : UDINT; (*brightness intensity*)
	END_VAR
END_FUNCTION

FUNCTION VA_SetClipRegion : UINT (*function is only used internally*)
	VAR_INPUT
		enable : BOOL; 
		VCHandle : UDINT; 
		uiX1 : UDINT;
		uiY1 : UDINT;
		uiX2 : UDINT;
		uiY2 : UDINT;
	END_VAR
END_FUNCTION

FUNCTION VA_SetContrast : UINT (*set the contrast of the display*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiPercent : UDINT; (*contrast intensity*)
	END_VAR
END_FUNCTION

FUNCTION VA_SetPaletteColor : UINT (*set RGB value for a color index*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		index : USINT; (*index of color to be changed*)
		color : UDINT; (*new color given as BRG value*)
	END_VAR
END_FUNCTION

FUNCTION VA_SetUserParam : UINT (*modify internal driver parameters*)
	VAR_INPUT
		enable : BOOL;
		VCHandle : UDINT;
		Type : USINT;
		pParameter : UDINT;
	END_VAR
END_FUNCTION

FUNCTION VA_Setup : UDINT (*initializes the device driver*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		pProjectName : STRING[80]; (*pointer to STRING containing the name of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_SetupX : UINT (*initializes the device driver*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*pointer to handle of visualization object*)
		pProjectName : STRING[80]; (*pointer to STRING containing the name of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_Shutdown : UINT (*deinitialize device driver*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_Srelease : UINT (*release device driver*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*pointer to handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_StartProject : UINT (*start visualization*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*pointer to handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_StartVisuByName : UINT (*start visualization*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		pProjectName : STRING[80]; (*pointer to STRING containing the name of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_StartTouchCal : UINT (*start touch calibration*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_StopProject : UINT (*stop visualization*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_Textout : UINT (*output text*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		font_index : UINT; (*index of the font to be used*)
		x : UINT; (*x coordinate of the text to be output*)
		y : UINT; (*y coordinate of the text to be output*)
		fC : USINT; (*foreground color of the text.*)
		bC : USINT;(*background color of the text.*)
		pText : STRING[80]; (*pointer to STRING containing the text to be output*)
	END_VAR
END_FUNCTION

FUNCTION VA_TimeSynchronize : UINT (*synchronize time with server CPU.*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VC_Handle : UDINT; (*handle of visualization object*)
	END_VAR
END_FUNCTION

FUNCTION VA_wcAlarmGetList : UINT (*read entry from historical alarm list (Unicode)*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pcAlarmLine : DINT; (*pointer to STRING which should record the alarm line*)
		plLen : DINT; (*pointer to DINT which contains the length of the alarm line*)
		iFunction : UINT; (*function to execute 1 = read first alarm, 2 = read next alarm*)
	END_VAR
END_FUNCTION

FUNCTION VA_wcGetActAlarmList : UINT (*read entry from actual alarm list (Unicode)*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pcAlarmLine : DINT; (*pointer to STRING which should record the alarm line*)
		plLen : DINT; (*pointer to DINT which contains the length of the alarm line*)
		iFunction : UINT; (*function to execute 1 = read first alarm, 2 = read next alarm*)
		usSeperator : UINT; (*separation character to be inserted into the alarm line*)
		cDateTimeFormat : USINT; (*desired format for date and time output in the alarm list*)
	END_VAR
END_FUNCTION

FUNCTION VA_wcGetExAlarmList : UINT (*read entry from historical alarm list with defined format (Unicode)*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		pcAlarmLine : DINT; (*pointer to STRING which should record the alarm line*)
		plLen : DINT; (*pointer to DINT which contains the length of the alarm line*)
		iFunction : UINT; (*function to execute 1 = read first alarm, 2 = read next alarm*)
		usSeperator : UINT; (*separation character to be inserted into the alarm line*)
		cDateTimeFormat : USINT; (*desired format for date and time output in the alarm list*)
	END_VAR
END_FUNCTION

FUNCTION VA_wcGetTextByTextGroup : UINT (*read text from textgroup of the active language (Unicode)*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		TG_id : UDINT; (*id number of the text group to be read*)
		TGT_id : UINT; (*id number of the line to be read in the text group*)
		pwText : UDINT; (*pointer to UINT array where text group text is stored*)
		psTextLength : UDINT; (*pointer to UDINT containing the text to be read*)
	END_VAR
END_FUNCTION

FUNCTION VA_wcTextout : UINT (*output unicode text (Unicode)*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		font_index : UINT; (*index of the font to be used*)
		x : UINT; (*x coordinate of the text to be output*)
		y : UINT; (*y coordinate of the text to be output*)
		fC : USINT; (*foreground color of the text.*)
		bC : USINT; (*background color of the text*)
		pwText : UDINT; (*pointer to STRING containg the text to be output*)
	END_VAR
END_FUNCTION


FUNCTION VA_GetActualLang : UINT (*intern*)
END_FUNCTION

FUNCTION VA_ClearTouchEventBuffer : UINT (*intern*)
END_FUNCTION

FUNCTION VA_RegisterClient : UINT (*intern*)
END_FUNCTION

FUNCTION VA_StartProcess : UINT (*start process*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiProcessID : UDINT; (*id of process to start*)
		psArguments : UDINT; (*optional arguments*)
		puiExtendedErrorCode : UDINT; (*pointer to UDINT containing extended error code*)
	END_VAR
END_FUNCTION
	
FUNCTION VA_TerminateProcess : UINT (*stop running process*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiProcessID : UDINT; (*id of process to stop*)
		puiExtendedErrorCode : UDINT; (*pointer to UDINT containing extended error code*)
	END_VAR
END_FUNCTION

FUNCTION VA_GetProcessExitCode : UINT (*get process exit code*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiProcessID : UDINT; (*id of process to stop*)
		puiExitCode : UDINT; (*pointer to UDINT containing exit code*)
		puiExtendedErrorCode : UDINT; (*pointer to UDINT containing extended error code*)
	END_VAR
END_FUNCTION

FUNCTION VA_SetProcessZOrder : UINT (*set process windows z-order*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiProcessID : UDINT; (*id of process to stop*)
		uiZOrderFlags : UDINT; (*z-order flags*)
	END_VAR
END_FUNCTION

FUNCTION VA_SetVisualizationZOrder : UINT (*set visualization windows z-order*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiZOrderFlags : UDINT; (*z-order flags*)
	END_VAR
END_FUNCTION

FUNCTION VA_RunJScript : UINT (*intern*)
	VAR_INPUT
		enable : BOOL; (*enables execution*)
		VCHandle : UDINT; (*handle of visualization object*)
		uiJSStatusDP : UDINT; (*number of the JSStatusDP*)
		pScriptName : UDINT; (*filename of the java-script*)
	END_VAR
END_FUNCTION

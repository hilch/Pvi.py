/* Automation Studio Generated Header File, Format Version 1.00 */
/* do not change */
#ifndef ASTIME_H_
#define ASTIME_H_
#define _WEAK	__attribute__((__weak__))

#include <bur/plctypes.h>



/* Constants */
_WEAK const unsigned long DATE_AND_TIME_MAX = 4102444799U;
_WEAK const signed long TIME_MAX = 2073600000;
_WEAK const signed long TIME_MIN = -2073600000;
_WEAK const unsigned char timEXSETTIME_NO_LOGENTRY = 1;
_WEAK const unsigned char timEXSETTIME_NO_OPTION = 0;


/* Datatypes */
typedef struct DTStructure
{
	unsigned short year;
	unsigned char month;
	unsigned char day;
	unsigned char wday;
	unsigned char hour;
	unsigned char minute;
	unsigned char second;
	unsigned short millisec;
	unsigned short microsec;
} DTStructure;

typedef struct TIMEStructure
{
	signed char day;
	unsigned char hour;
	unsigned char minute;
	unsigned char second;
	unsigned short millisec;
	unsigned short microsec;
} TIMEStructure;



/* Datatypes of function blocks */
typedef struct DTExSetTime
{
	/* VAR_INPUT (analogous) */
	DATE_AND_TIME DT1;
	unsigned char Option;
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	/* VAR_INPUT (digital) */
	plcbit enable;
} DTExSetTime_typ;

typedef struct DTSetTime
{
	/* VAR_INPUT (analogous) */
	DATE_AND_TIME DT1;
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	/* VAR_INPUT (digital) */
	plcbit enable;
} DTSetTime_typ;

typedef struct DTGetTime
{
	/* VAR_OUTPUT (analogous) */
	unsigned short status;
	DATE_AND_TIME DT1;
	/* VAR_INPUT (digital) */
	plcbit enable;
} DTGetTime_typ;



/* Prototyping of functions and function blocks */
unsigned long DiffDT(DATE_AND_TIME DT2, DATE_AND_TIME DT1);
unsigned long DiffT(plctime TIME2, plctime TIME1);
unsigned long DT_TO_DTStructure(DATE_AND_TIME DT1, unsigned long pDTStructure);
DATE_AND_TIME DTStructure_TO_DT(unsigned long pDTStructure);
unsigned long TIME_TO_TIMEStructure(plctime TIME1, unsigned long pTIMEStructure);
plctime TIMEStructure_TO_TIME(unsigned long pTIMEStructure);
unsigned long ascDT(DATE_AND_TIME DT1, unsigned long pStr, unsigned long len);
unsigned long ascTIME(plctime TIME1, unsigned long pStr, unsigned long len);
unsigned long ascDTStructure(unsigned long pDTStructure, unsigned long pStr, unsigned long len);
unsigned long ascTIMEStructure(unsigned long pTIMEStructure, unsigned long pStr, unsigned long len);
void DTExSetTime(DTExSetTime_typ* inst);
void DTSetTime(DTSetTime_typ* inst);
void DTGetTime(DTGetTime_typ* inst);



#endif /* ASTIME_H_ */


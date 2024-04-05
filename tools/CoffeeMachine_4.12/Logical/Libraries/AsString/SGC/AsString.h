/* Automation Studio Generated Header File, Format Version 1.00 */
/* do not change */
#ifndef ASSTRING_H_
#define ASSTRING_H_
#define _WEAK	__attribute__((__weak__))

#include <bur/plc.h>



/* Constants */


/* Datatypes */


/* Datatypes of function blocks */


/* Prototyping of functions and function blocks */
unsigned short ftoa(float value, unsigned long pString);
unsigned short itoa(signed long value, unsigned long pString);
float atof(unsigned long pString);
signed long atoi(unsigned long pString);

#endif /* ASSTRING_H_ */


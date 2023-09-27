/****************************************************************************/
/*                                                                          */
/*  sys_lib.h                                                               */
/*  Declarations and Prototypes for libsys_lib.a                            */
/*                                                                          */
/*      Automation Studio                                                   */
/*  Copyright Bernecker&Rainer 1998                                         */
/*                                                                          */
/****************************************************************************/
/*  $Header: /68K/br/AsLibrary/sys_lib/i386/sys_lib.h 8     1.10.02 13:06 Halseggerd $ */

#ifndef _SYS_LIB_H_
#ifdef __cplusplus
extern "C" {
#endif
#define	_SYS_LIB_H_

#include <bur/plctypes.h>

#define     TMP_MODE    0x8000          /* temporary suspend/resume for */
                                        /* PLC and user task */

/* Error codes of the SYS_LIB services */

#define ERR_BUR_WRROW           2061    /* illegal row */
#define ERR_BUR_WRCOL           2062    /* illegal column */
#define ERR_BUR_WR_CHAR         2063    /* invalid ASCII character */

#define ERR_BUR_NOMEM           3030    /* out of memory */

#define ERR_BUR_WROFFSET        3301    /* illegal offset */
#define ERR_BUR_ILLSTATE        3302    /* illegal state of object */
#define ERR_BUR_DUPOBJ          3305    /* object exists */
#define ERR_BUR_EXISTS          3306    /* entry exists */

#define ERR_BUR_ILLTYP          3311    /* invalid I/O type */
                                        /* e.g. BURTRAP V1.10 to SPSSW V1.05 */
#define ERR_BUR_ILLLEN          3314    /* invalid data length */
#define ERR_BUR_ILLPAR          3317    /* illegal parameter */
#define ERR_BUR_INSTALL         3318    /* error install datamodule */
#define ERR_BUR_WRONG_MODTYP    3319    /* wrong Moduletype */

#define ERR_BUR_ILLOBJ          3324    /* object does not exist */
#define ERR_BUR_ILLOBJTYP       3328    /* invalid object type */
#define ERR_BUR_NOENTRY         3332    /* no entry */
#define ERR_BUR_ILLIDENT        3336    /* illegal ident */
#define ERR_BUR_NOTIME          3584    /* time not available */

#define ERR_BUR_TMP_ALLOC       3601    /* not enough continuous memory */
#define ERR_BUR_TMP_FREE        3701    /* invalid pointer/length */

/* State for object PLC task */
#define     Z_ST_created        1
#define     Z_ST_running        2
#define     Z_ST_blocked        3
#define     Z_ST_exist          0x00
#define     Z_ST_installed      0x82
#define     Z_ST_PVinstalled    0x83
#define     Z_ST_IOinstalled    0x84
#define     Z_ST_IOdeinstalled  0x85
#define     Z_ST_PVdeinstalled  0x86
#define     Z_ST_delete         0x87
#define     Z_ST_stdebug        0x88
#define     Z_ST_tmp_suspended  0x90

/* PV data types */
#define     PB_DT_STRUCT        0       /* structure */
#define     PB_DT_BOOL          1       /* boolean */
#define     PB_DT_INT8          2       /* integer8 */
#define     PB_DT_INT16         3       /* integer16 */
#define     PB_DT_INT32         4       /* integer32 */
#define     PB_DT_BYTE          5       /* unsigned integer8 */
#define     PB_DT_WORD          6       /* unsigned integer16 */
#define     PB_DT_LONG          7       /* unsigned integer32 */
#define     PB_DT_FLOAT         8       /* floating point */
#define     PB_DT_VIS           9       /* visible string*/
#define     PB_DT_OCTET         10      /* octet string */
#define     PB_DT_DATE          11      /* date */
#define     PB_DT_TIME          12      /* time of day */
#define     PB_DT_DIFF          13      /* time difference */
#define     PB_DT_BIT           14      /* bit string */
#define     PB_DT_ARRAY         15      /* array */


typedef struct RTCtime_typ {
            /* 1. UDINT */
            UINT     year;       /* year, starting with zero */
            USINT    month;      /* month: 1 - 12 */
            USINT    day;        /* day:   1 - 31 */
            /* 2. UDINT */
            USINT    reserve;
            USINT    hour;       /* hour:   0 - 23 */
            USINT    minute;     /* minute: 0 - 59 */
            USINT    second;     /* second: 0 - 59 */
            /* 3. UDINT */
            UINT     millisec;   /* millisecond: 0 - 999 */
            UINT     microsec;   /* microsecond: 0 - 999 */
        } RTCtime_typ;


/* structure for MO_list */
typedef struct MO_List_typ {
        char    name[14];        /* name of the module (ASCII) */
        USINT   grp;             /* groups */
        USINT   type;            /* module type */
        USINT   state;           /* state of the module */
        USINT   reserve;
        UDINT   adress;          /* physical address of the module */
        UDINT   memtype;         /* memory type (0=OTP,1=RAM,2=EPROM,3=FLASH */
        } MO_List_typ;           /* 5=FIXRAM) */

/* structue for PV_xlist */
typedef struct PV_xList_typ {
	
		char		name[33];    /* name of PV (ASCII)		*/
		USINT		data_typ;	 /* data type of PV			*/
		UDINT		data_len;	 /* data length of PV		*/
		UDINT		dimension;	 /* dimension of PV			*/
		UDINT		adress;		 /* physical address of PV	*/
		}PV_xList_typ;

/* structure for ERR_read */
typedef struct ERR_typ {
        UINT    err_nr;         /* error number */
        UDINT   err_info;       /* additional information */
        char    t_name[5];      /* name of the running task */
        USINT   err_type;       /* error type (1=fatal, 2=warning, 3=info) */
        UINT    err_year;       /* time of the error in RTC format */
        USINT   err_month;
        USINT   err_day;
        USINT   err_reserve;
        USINT   err_hour;
        USINT   err_minute;
        USINT   err_second;
        UINT    err_millisec;
        UINT    err_microsec;
        } ERR_typ;

/* structure for ERR_xread */
typedef struct ERR_xtyp {
        UINT    err_nr;         /* error number */
        UDINT   err_info;       /* additional information */
        char    t_name[5];      /* name of the running task */
        USINT   err_type;       /* error type (1=Fatal, 2=Warning, 3=Info) */
        UINT    err_year;       /* time of the error in RTC format */
        USINT   err_month;
        USINT   err_day;
        USINT   err_reserve;
        USINT   err_hour;
        USINT   err_minute;
        USINT   err_second;
        UINT    err_millisec;
        UINT    err_microsec;
        USINT   err_string[34]; /* 32 byte string with 0 termination */
        } ERR_xtyp;

/* structure for MO_ver */
typedef struct MoVerStruc_typ {
		USINT   version[10];		/* Version of the BR Module */
        UINT    year;
        USINT   month;
        USINT   day;
        USINT   reserve;
        USINT   hour;
        USINT   minute;
        USINT   second;
        } MoVerStruc_typ;

/* structure for the FUB Bit2Byte */
typedef struct Bit2Byte {
		/* non boolean input parameter */
        UDINT   bitadr;
        UINT    length;
		/* non boolean output parameter*/
        UDINT   byteadr;
		/* non boolean static local */
        USINT	byte_00;
        USINT   byte_01;
        USINT   byte_02;
        USINT   byte_03;
        USINT   byte_04;
        USINT   byte_05;
        USINT   byte_06;
        USINT   byte_07;
        USINT   byte_08;
        USINT   byte_09;
        USINT   byte_10;
        USINT   byte_11;
        USINT   byte_12;
        USINT   byte_13;
        USINT   byte_14;
        USINT	byte_15;
		/* boolean input parameter */
		/* boolean output parameter */
		/* boolean static local */
        BOOL	bmem000;
        BOOL	bmem001;
        BOOL	bmem002;
        BOOL	bmem003;
        BOOL	bmem004;
        BOOL	bmem005;
        BOOL	bmem006;
        BOOL	bmem007;
        BOOL	bmem008;
        BOOL	bmem009;
        BOOL	bmem010;
        BOOL	bmem011;
        BOOL	bmem012;
        BOOL	bmem013;
        BOOL	bmem014;
        BOOL	bmem015;
        BOOL	bmem016;
        BOOL	bmem017;
        BOOL	bmem018;
        BOOL	bmem019;
        BOOL	bmem020;
        BOOL	bmem021;
        BOOL	bmem022;
        BOOL	bmem023;
        BOOL	bmem024;
        BOOL	bmem025;
        BOOL	bmem026;
        BOOL	bmem027;
        BOOL	bmem028;
        BOOL	bmem029;
        BOOL	bmem030;
        BOOL	bmem031;
        BOOL	bmem032;
        BOOL	bmem033;
        BOOL	bmem034;
        BOOL	bmem035;
        BOOL	bmem036;
        BOOL	bmem037;
        BOOL	bmem038;
        BOOL	bmem039;
        BOOL	bmem040;
        BOOL	bmem041;
        BOOL	bmem042;
        BOOL	bmem043;
        BOOL	bmem044;
        BOOL	bmem045;
        BOOL	bmem046;
        BOOL	bmem047;
        BOOL	bmem048;
        BOOL	bmem049;
        BOOL	bmem050;
        BOOL	bmem051;
        BOOL	bmem052;
        BOOL	bmem053;
        BOOL	bmem054;
        BOOL	bmem055;
        BOOL	bmem056;
        BOOL	bmem057;
        BOOL	bmem058;
        BOOL	bmem059;
        BOOL	bmem060;
        BOOL	bmem061;
        BOOL	bmem062;
        BOOL	bmem063;
        BOOL	bmem064;
        BOOL	bmem065;
        BOOL	bmem066;
        BOOL	bmem067;
        BOOL	bmem068;
        BOOL	bmem069;
        BOOL	bmem070;
        BOOL	bmem071;
        BOOL	bmem072;
        BOOL	bmem073;
        BOOL	bmem074;
        BOOL	bmem075;
        BOOL	bmem076;
        BOOL	bmem077;
        BOOL	bmem078;
        BOOL	bmem079;
        BOOL	bmem080;
        BOOL	bmem081;
        BOOL	bmem082;
        BOOL	bmem083;
        BOOL	bmem084;
        BOOL	bmem085;
        BOOL	bmem086;
        BOOL	bmem087;
        BOOL	bmem088;
        BOOL	bmem089;
        BOOL	bmem090;
        BOOL	bmem091;
        BOOL	bmem092;
        BOOL	bmem093;
        BOOL	bmem094;
        BOOL	bmem095;
        BOOL	bmem096;
        BOOL	bmem097;
        BOOL	bmem098;
        BOOL	bmem099;
        BOOL	bmem100;
        BOOL	bmem101;
        BOOL	bmem102;
        BOOL	bmem103;
        BOOL	bmem104;
        BOOL	bmem105;
        BOOL	bmem106;
        BOOL	bmem107;
        BOOL	bmem108;
        BOOL	bmem109;
        BOOL	bmem110;
        BOOL	bmem111;
        BOOL	bmem112;
        BOOL	bmem113;
        BOOL	bmem114;
        BOOL	bmem115;
        BOOL	bmem116;
        BOOL	bmem117;
        BOOL	bmem118;
        BOOL	bmem119;
        BOOL	bmem120;
        BOOL	bmem121;
        BOOL	bmem122;
        BOOL	bmem123;
        BOOL	bmem124;
        BOOL	bmem125;
        BOOL	bmem126;
        BOOL	bmem127;
        BOOL	bmem128;
        BOOL	bmem129;
        BOOL	bmem130;
        BOOL	bmem131;
        BOOL	bmem132;
        BOOL	bmem133;
        BOOL	bmem134;
        BOOL	bmem135;
        BOOL	bmem136;
        BOOL	bmem137;
        BOOL	bmem138;
        BOOL	bmem139;
		} Bit2Byte_typ;

/* structure for the FUB Byte2Bit */
typedef struct Byte2Bit {
		/* non boolean input parameter */
		UDINT	byteadr;
		UINT    length;
		/* non boolean output parameter*/
		UDINT   bitadr;
		/* non boolean static local */
		/* boolean input parameter */
		/* boolean output parameter */
		/* boolean static local */
		BOOL	bmem000;
		BOOL	bmem001;
		BOOL	bmem002;
		BOOL	bmem003;
		BOOL	bmem004;
		BOOL	bmem005;
		BOOL	bmem006;
		BOOL	bmem007;
		BOOL	bmem008;
		BOOL	bmem009;
		BOOL	bmem010;
		BOOL	bmem011;
		BOOL	bmem012;
		BOOL	bmem013;
		BOOL	bmem014;
		BOOL	bmem015;
		BOOL	bmem016;
		BOOL	bmem017;
		BOOL	bmem018;
		BOOL	bmem019;
		BOOL	bmem020;
		BOOL	bmem021;
		BOOL	bmem022;
		BOOL	bmem023;
		BOOL	bmem024;
		BOOL	bmem025;
		BOOL	bmem026;
		BOOL	bmem027;
		BOOL	bmem028;
		BOOL	bmem029;
		BOOL	bmem030;
		BOOL	bmem031;
		BOOL	bmem032;
		BOOL	bmem033;
		BOOL	bmem034;
		BOOL	bmem035;
		BOOL	bmem036;
		BOOL	bmem037;
		BOOL	bmem038;
		BOOL	bmem039;
		BOOL	bmem040;
		BOOL	bmem041;
		BOOL	bmem042;
		BOOL	bmem043;
		BOOL	bmem044;
		BOOL	bmem045;
		BOOL	bmem046;
		BOOL	bmem047;
		BOOL	bmem048;
		BOOL	bmem049;
		BOOL	bmem050;
		BOOL	bmem051;
		BOOL	bmem052;
		BOOL	bmem053;
		BOOL	bmem054;
		BOOL	bmem055;
		BOOL	bmem056;
		BOOL	bmem057;
		BOOL	bmem058;
		BOOL	bmem059;
		BOOL	bmem060;
		BOOL	bmem061;
		BOOL	bmem062;
		BOOL	bmem063;
		BOOL	bmem064;
		BOOL	bmem065;
		BOOL	bmem066;
		BOOL	bmem067;
		BOOL	bmem068;
		BOOL	bmem069;
		BOOL	bmem070;
		BOOL	bmem071;
		BOOL	bmem072;
		BOOL	bmem073;
		BOOL	bmem074;
		BOOL	bmem075;
		BOOL	bmem076;
		BOOL	bmem077;
		BOOL	bmem078;
		BOOL	bmem079;
		BOOL	bmem080;
		BOOL	bmem081;
		BOOL	bmem082;
		BOOL	bmem083;
		BOOL	bmem084;
		BOOL	bmem085;
		BOOL	bmem086;
		BOOL	bmem087;
		BOOL	bmem088;
		BOOL	bmem089;
		BOOL	bmem090;
		BOOL	bmem091;
		BOOL	bmem092;
		BOOL	bmem093;
		BOOL	bmem094;
		BOOL	bmem095;
		BOOL	bmem096;
		BOOL	bmem097;
		BOOL	bmem098;
		BOOL	bmem099;
		BOOL	bmem100;
		BOOL	bmem101;
		BOOL	bmem102;
		BOOL	bmem103;
		BOOL	bmem104;
		BOOL	bmem105;
		BOOL	bmem106;
		BOOL	bmem107;
		BOOL	bmem108;
		BOOL	bmem109;
		BOOL	bmem110;
		BOOL	bmem111;
		BOOL	bmem112;
		BOOL	bmem113;
		BOOL	bmem114;
		BOOL	bmem115;
		BOOL	bmem116;
		BOOL	bmem117;
		BOOL	bmem118;
		BOOL	bmem119;
		BOOL	bmem120;
		BOOL	bmem121;
		BOOL	bmem122;
		BOOL	bmem123;
		BOOL	bmem124;
		BOOL	bmem125;
		BOOL	bmem126;
		BOOL	bmem127;
		BOOL	bmem128;
		BOOL	bmem129;
		BOOL	bmem130;
		BOOL	bmem131;
		BOOL	bmem132;
		BOOL	bmem133;
		BOOL	bmem134;
		BOOL	bmem135;
		BOOL	bmem136;
		BOOL	bmem137;
		BOOL	bmem138;
		BOOL	bmem139;
		} Byte2Bit_typ;

/***************/
/* Prototyping */
/***************/

UINT PV_xgetadr		(char *pv_name, UDINT *pv_adresse, UDINT *data_len);
UINT PV_xlist		(UINT prev_index, UINT *index, PV_xList_typ *pvl_p);	
UINT PV_item		(char *pv_name, UINT index, char *itemname);
UINT PV_ninfo		(char *pv_name, UDINT *data_typ_p, UDINT *data_len_p,
					 UINT *dimension_p);

UINT SYSreset		(BOOL enable, USINT mode);
UINT MO_list		(UINT prev_index, UINT *index, MO_List_typ *mol_p);

UINT ST_ident		(char *st_name_p, USINT st_grp, UDINT *st_ident);
UINT ST_tmp_suspend	(UDINT st_ident);
UINT ST_tmp_resume  (UDINT st_ident);
UINT ST_allsuspend	(void);
UINT ST_info		(UDINT st_ident, USINT *state, USINT *tcnr);
UINT ST_name		(UDINT st_ident, char *st_name_p, USINT *st_grp);

UINT TMP_alloc		(UDINT memlng, void **memptr);
UINT TMP_free		(UDINT memlng, void *memptr);
					
UINT RTC_gettime	(RTCtime_typ *rtctime);
UINT RTC_settime	(RTCtime_typ *rtctime);
UINT TIM_musec		(void);
UINT TIM_ticks		(void);
					
UINT ERR_warning	(UINT errornr, UDINT errorinfo);
UINT ERR_fatal		(UINT errornr, UDINT errorinfo);
UINT ERR_read		(UINT entry_nr, ERR_typ *err_p);
UINT ERRxwarning	(UINT errornr, UDINT errorinfo, unsigned char* errorstring);
UINT ERRxread		(UINT entry_nr, ERR_xtyp *err_p);
UINT ERRxfatal		(UINT errornr, UDINT errorinfo, unsigned char* errorstring);
					
UINT DIS_str		(UDINT row, UDINT col, char *string);
UINT DIS_chr		(UDINT row, UDINT col, char character);
UINT DIS_clr		(void);
				
UINT MO_ver			(STRING *pName, USINT grp, MoVerStruc_typ* pMoVerStruc);

void Bit2Byte		(Bit2Byte_typ*	Bit2Byte_ptr);
void Byte2Bit		(Byte2Bit_typ*	Byte2Bit_ptr);

#ifdef __cplusplus
}
#endif
#endif /* _SYS_LIB_H_ */


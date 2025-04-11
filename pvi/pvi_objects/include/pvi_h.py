#
# Pvi.py
# Python connector for B&R Pvi (process visualization interface)
#
#  https://github.com/hilch/Pvi.py
# Permission is hereby granted, free of charge, 
# to any person obtaining a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import ctypes
import winreg
import os

from ctypes import c_int32, wintypes, Structure, WinDLL
from enum import IntEnum, Enum


class T_POBJ_TYPE(IntEnum):
    POBJ_PVI = 0		# global
    POBJ_LINE = 1		# line
    POBJ_DEVICE = 2	    # device
    POBJ_STATION = 3	# station (PLC)
    POBJ_CPU = 4		# CPU
    POBJ_MODULE = 5		# modul
    POBJ_TASK = 6		# task
    POBJ_PVAR = 7		# process variable


PVI_HMSG_NIL = 1

SET_PVIFUNCTION = 0xfffffffc

POBJ_EVENT_PVI_CONNECT = 240
POBJ_EVENT_PVI_DISCONN = 241
POBJ_EVENT_PVI_ARRANGE = 242


class PvType(Enum):
    '''
    Type of process variable PV
    '''
    UNKNOWN = "?"
    I8	= "i8"
    '''
    1 byte signed integer
    '''
    I16	= "i16"
    '''
    2 byte signed integer
    '''
    I32 = "i32"
    '''
    4 byte signed integer
    '''
    I64 = "i64"
    '''
    8 byte signed integer
    '''
    U8 = "u8"
    '''
    1 byte unsigned integer
    '''
    U16 = "u16"
    '''
    byte unsigned integer
    '''
    U32 = "u32"
    '''
    4 byte unsigned integer
    '''
    U64 = "u64"
    '''
    8 byte unsigned integer
    '''
    F32 = "f32"
    '''
    4 byte float
    '''
    F64 = "f64"
    '''
    8 byte float (double)
    '''
    BOOLEAN = "boolean"
    '''
    bit (size = 1 byte)
    '''
    STRING = "string"
    '''
    byte character string
    '''
    WSTRING = "wstring"
    '''
    wide character string
    '''
    STRUCT = "struct"
    '''
    structure
    '''
    DATA = "data"
    '''
    generic type
    '''
    TIME = "time"
    '''
    time
    '''
    DT = "dt"
    '''
    date and time
    '''
    DATE = "date"
    '''
    date
    '''
    TOD = "tod"
    '''
    time of day
    '''



# response and event message information structure:
# typedef struct t_response_info
# {
# 	DWORD		LinkID;				// link object identifier
#	DWORD		nMode;				// request/response/event mode
#	DWORD		nType;				// type of access or event
#	DWORD		ErrCode;			// != 0 -> error state
#	DWORD		Status;				// response/event status
# }	T_RESPONSE_INFO;

class T_RESPONSE_INFO(Structure):
    _fields_ = [
        ("LinkID",wintypes.DWORD),
        ("nMode", wintypes.DWORD),
        ("nType", wintypes.DWORD),
        ("ErrCode", wintypes.DWORD),
        ("Status", wintypes.DWORD)
    ]
 

# // structure for PROCEEDING events:
# typedef struct t_proceeding_info
# {
# 	DWORD	nAccess;					// access type of the active request
# 	DWORD	Percent;					// progress of the active request (0%..100%)
# 	char	Info[32];					// optional text
# } T_PROCEEDING_INFO;

STRING_ProceedingInfo = ctypes.c_char*(32)

class T_PROCEEDING_INFO(Structure):
    _fields_ = [
        ("nAccess",wintypes.DWORD),
        ("Percent", wintypes.DWORD),
        ("Info", STRING_ProceedingInfo),
    ]

# structure for PVI license information:
# define PVI_LCNAME_LEN			64		// max length for license name
# typedef struct t_pvi_info_licence
# {
#   BYTE	PviWorkState[2];			// working state
#   BYTE	_PviWorkState[2];			// inverted working state
#   DWORD	Res1;						// reserved
#  char	LcName[PVI_LCNAME_LEN+1];	// B&R license name
# } T_PVI_INFO_LICENCE;

# // PVI license information in structure element PviWorkState[0]:
# #define PVIWORK_STATE_NULL		0			// undefined working state
# #define PVIWORK_STATE_TRIAL		1			// working state: trial
# #define PVIWORK_STATE_RUNTIME	2			// working state: runtime
# #define PVIWORK_STATE_DEVELOPER	3			// historical - do not use
# #define PVIWORK_STATE_LOCKED	4			// working state: locked

# // PVI license information in structure element PviWorkState[1]:
# #define PVIWORK_BURPC			(1<<0)		// bit indicates B&R IPC
# #define PVIWORK_BURLC			(1<<1)		// bit indicates B&R license
# #define PVIWORK_KEYRT			(1<<2)		// bit indicates PVI dongle (runtime)
# #define PVIWORK_KEYDV			(1<<3)		// historical - do not use


PVI_LCNAME_LEN = 64
STRING_LcName = ctypes.c_char*(PVI_LCNAME_LEN+1)

class T_PVI_INFO_LICENCE(Structure):
    _fields_ = [
        ("PviWorkState0",wintypes.BYTE),    
        ("PviWorkState1",wintypes.BYTE),            
        ("_PviWorkState0",wintypes.BYTE),               
        ("_PviWorkState1",wintypes.BYTE),                       
        ("Res1",wintypes.DWORD),           
        ("LcName",STRING_LcName)           
    ]


# Accessing Types:
POBJ_ACC_OBJECT = 1		# read process object type
POBJ_ACC_VERSION =2		# read object version
POBJ_ACC_ERROR = 3		# read last error code

POBJ_ACC_EVMASK = 5			# read/write event mask
POBJ_ACC_LIST = 6		# read list of object names
POBJ_ACC_LIST_EXTERN = 7		# read list of line object names

POBJ_ACC_CONNECT = 10		# read/write connection description
POBJ_ACC_DATA = 11		# read/write object data
POBJ_ACC_STATUS = 12		# read/write object state
POBJ_ACC_TYPE = 13		# read/write object type (attributes, format)
POBJ_ACC_TYPE_EXTERN = 14		# read external object type (attributes, format)
POBJ_ACC_REFRESH = 15		# read/write data refresh time
POBJ_ACC_HYSTERESE = 16		# read/write data hysterese
POBJ_ACC_DEFAULT = 17		# read default data
POBJ_ACC_FUNCTION = 18		# read/write data function
POBJ_ACC_TYPE_INTERN = 19		# read internal object type (attributes, format)

POBJ_ACC_UPLOAD = 20		# upload module/file
POBJ_ACC_DOWNLOAD = 21		# download module/file
POBJ_ACC_DATE_TIME = 22		# read/write date and time
POBJ_ACC_MEM_DELETE = 23		# clear memory
POBJ_ACC_MEM_INFO = 24		# read memory informations
POBJ_ACC_MOD_TYPE = 25		# read type of module
POBJ_ACC_UPLOAD_STM = 26		# upload module/file (stream)
POBJ_ACC_DOWNLOAD_STM = 27		# download module/file (stream)
POBJ_ACC_MOD_DATA = 28		# read/write module data
POBJ_ACC_MOD_DELETE = 29		# delete module

POBJ_ACC_LIST_LINE = 30		# extended list of line object names
POBJ_ACC_LIST_DEVICE = 31		# extended list of device object names
POBJ_ACC_LIST_STATION = 32		# extended list of station object names
POBJ_ACC_LIST_CPU = 33		# extended list of CPU object names
POBJ_ACC_LIST_MODULE = 34		# extended list of module object names
POBJ_ACC_LIST_TASK = 35		# extended list of task object names
POBJ_ACC_LIST_PVAR = 36		# extended list of variable object names

POBJ_ACC_CPU_INFO = 50		# read CPU information

POBJ_ACC_CANCEL = 128		# cancel current request
POBJ_ACC_USERTAG = 129		# user tag string

POBJ_ACC_INFO_LICENCE = 200		# read PVI licence information
POBJ_ACC_LIST_CLIENTS = 210		# read list of all PVI clients
POBJ_ACC_PVI_VERSION = 211		# read PVI version string

POBJ_ACC_SNAPSHOT = 240		# snapshot function
POBJ_ACC_PVILOG = 241		# read/write PVI data logger parameter
POBJ_ACC_PVIMAN_PARAM = 242		# read/write PVI manager parameter
POBJ_ACC_PVIMAN_EXIT = 243		# stop PVI manager

POBJ_ACC_LINEBASE = 256		# base number for advanced line services

POBJ_ACC_LN_COMM_DST = 291		# read communication parameter
POBJ_ACC_LN_LKN_LIST = 296		# linknode list
POBJ_ACC_LN_XML_LIC_STATUS = 351		# read licence state (XML format)
POBJ_ACC_LN_XML_CPU_INFO = 400		# read cpu informations (XML format)
POBJ_ACC_LN_XML_MOD_INFO = 401		# read module informations (XML format)
POBJ_ACC_LN_XML_TASK_INFO = 402		# read task informations (XML format)
POBJ_ACC_LN_XML_MOD_LIST = 403		# read module list (XML format)
POBJ_ACC_LN_XML_MEM_INFO = 404		# read storage informations (XML format)
POBJ_ACC_LN_XML_HW_INFO = 405		# read hardware informations (XML format)
POBJ_ACC_LN_XML_RED_INFO = 406		# read redundancy informations (XML format)
POBJ_ACC_LN_XML_TC_INFO = 408		# read task class informations (XML format)
POBJ_ACC_LN_XML_LOGM_INFO = 416		# read logger module info (XML format)
POBJ_ACC_LN_XML_LOGM_DATA = 417		# read logger module data (XML format)

# Event Types:
POBJ_EVENT_ERROR = 3		# error state event

POBJ_EVENT_CONNECT = 10		# connect event
POBJ_EVENT_DATA = 11		# data event
POBJ_EVENT_STATUS = 12		# status event
POBJ_EVENT_DATAFORM = 13		# data format event

POBJ_EVENT_PROCEEDING = 128		# progress in % (0..100)
POBJ_EVENT_USERTAG = 129		# user tag event

POBJ_EVENT_PVI_CONNECT = 240		# connection to PVI established
POBJ_EVENT_PVI_DISCONN = 241		# connection to PVI lost
POBJ_EVENT_PVI_ARRANGE = 242		# arrange PVI objects

POBJ_EVENT_LINEBASE = 256		# base number for advanced line events

POBJ_EVENT_LN_XML_MOD_LIST = 403		# module list event (XML format)
POBJ_EVENT_LN_XML_RED_CTRL = 440		# redundancy event (XML format)


pviDllPath = os.environ.get("PVIPY_PVIDLLPATH")
if pviDllPath == None:
    accessRegistry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    pviKey = winreg.OpenKey(accessRegistry,r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\PviMan.exe")
    for n in range(10):
        try:
            value = list(winreg.EnumValue( pviKey, n))
            if value[0] == "Path" and value[2] == winreg.REG_SZ:
                pviDllPath = value[1]
                break
        except OSError:
            break

if pviDllPath == None:
    print("Pvi is not installed")
    exit(1)

pviDll = WinDLL ( str(pviDllPath) + r"\PviCom64.dll")


#
# int PviXInitialize (DWORD hPvi, INT Timeout, INT RetryTime, LPCSTR pInitParam, LPVOID pRes)
#

pviDll.PviXInitialize.argtypes = [ctypes.POINTER(wintypes.DWORD), wintypes.INT, wintypes.INT, wintypes.LPCSTR, wintypes.LPVOID]
pviDll.PviXInitialize.restype = c_int32
def PviXInitialize( hPvi, Timeout, RetryTime, pInitParam, pRes ):
    result = pviDll.PviXInitialize( hPvi, Timeout, RetryTime, bytes( pInitParam, 'ascii'), pRes )
    return result

#
# int PviXDeinitialize(DWORD hPvi)
#
pviDll.PviXDeinitialize.argtypes = [wintypes.DWORD]
pviDll.PviXDeinitialize.restype = c_int32
def PviXDeinitialize( hPvi ):
    result = pviDll.PviXDeinitialize( hPvi )
    return result

#
# int PviXSetGlobEventMsg (DWORD hPvi, DWORD nGlobEvent, LPVOID hEventMsg, DWORD EventMsgNo, LPARAM EventParam)
#

pviDll.PviXSetGlobEventMsg.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID, wintypes.DWORD, wintypes.LPARAM ]
pviDll.PviXSetGlobEventMsg.restype = c_int32
def PviXSetGlobEventMsg( hPvi, nGlobEvent, hEventMsg, EventMsgNo, EventParam ):
    result = pviDll.PviXSetGlobEventMsg( hPvi, nGlobEvent, hEventMsg, EventMsgNo, EventParam )
    return result

#
# int PviXGetNextResponse (DWORD hPvi, WPARAM* pwParam, LPARAM* plParam, LPVOID* phMsg, HANDLE hEvent)
#



pviDll.PviXGetNextResponse.argtypes = [wintypes.DWORD, ctypes.POINTER(wintypes.WPARAM), 
                                        ctypes.POINTER(wintypes.LPARAM), ctypes.POINTER(wintypes.LPVOID), wintypes.HANDLE]    
pviDll.PviXGetNextResponse.restype = c_int32
def PviXGetNextResponse( hPvi, pwParam, plParam, phMsg, hEvent):
    result = pviDll.PviXGetNextResponse( hPvi, pwParam, plParam, phMsg, hEvent )
    return result



#
# int PviXGetResponseInfo (DWORD hPvi, WPARAM wParam, LPARAM* pParam, LPDWORD pDataLen, T_RESPONSE_INFO* pInfo, DWORD InfoLen)
#

pviDll.PviXGetResponseInfo.argtypes = [wintypes.DWORD, wintypes.WPARAM, ctypes.POINTER(wintypes.LPARAM), 
                                       ctypes.POINTER(wintypes.DWORD), ctypes.POINTER(T_RESPONSE_INFO), wintypes.DWORD]
pviDll.PviXGetResponseInfo.restype = c_int32
def PviXGetResponseInfo( hPvi, wParam, pParam, pDataLen, pInfo, InfoLen):
    result = pviDll.PviXGetResponseInfo( hPvi, wParam, pParam, pDataLen, pInfo, InfoLen )
    return result

#
# int PviXLink (DWORD hPvi, LPDWORD pLinkID, LPCSTR pObjectName, LPVOID hEventMsg, DWORD EventMsgNo, LPARAM EventParam, LPCSTR pLinkDescriptor)
# 

pviDll.PviXLink.argtypes = [wintypes.DWORD, wintypes.LPDWORD, wintypes.LPCSTR, wintypes.LPVOID, wintypes.DWORD, wintypes.LPARAM, wintypes.LPCSTR]
pviDll.PviXLink.restype = c_int32
def PviXLink( hPvi, pLinkID, pObjectName, hEventMsg, EventMsgNo, EventParam, pLinkDescriptor ):
    result = pviDll.PviXLink( hPvi, pLinkID, pObjectName, hEventMsg, EventMsgNo, EventParam, pLinkDescriptor)
    return result


#
# int PviXUnlink (DWORD hPvi, DWORD LinkID)
#

pviDll.PviXUnlink.argtypes = [wintypes.DWORD, wintypes.DWORD]
pviDll.PviXUnlink.restype = c_int32
def PviXUnlink( hPvi, pLinkID ) -> int:
    result = pviDll.PviXUnlink( hPvi, pLinkID)
    return result



#
# int PviXCreate (DWORD hPvi, LPDWORD pLinkID, LPCSTR pObjectName, DWORD ObjectTyp, LPCSTR pObjektDescriptor, 
#                           LPVOID hEventMsg, DWORD EventMsgNo, LPARAM EventParam, LPCSTR pLinkDescriptor)
#

pviDll.PviXCreate.argtypes = [wintypes.DWORD, wintypes.LPDWORD, wintypes.LPCSTR, wintypes.DWORD, wintypes.LPCSTR, 
                              wintypes.LPVOID, wintypes.DWORD, wintypes.LPARAM, wintypes.LPCSTR ]
pviDll.PviXCreate.restype = c_int32
def PviXCreate( hPvi, pLinkID, pObjectName, ObjectTyp, pObjectDescriptor, hEventMsg, EventMsgNo, EventParam, pLinkDescriptor ):
    result = pviDll.PviXCreate( hPvi, pLinkID, pObjectName, ObjectTyp, pObjectDescriptor, hEventMsg, EventMsgNo, EventParam, pLinkDescriptor)
    return result

#
# int PviXRead (DWORD hPvi, DWORD LinkID, DWORD nAccess, 
#               LPVOID pArgData, LONG ArgDataLen, LPVOID pData, LONG DataLen)
#

pviDll.PviXRead.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, 
                            wintypes.LPVOID, wintypes.LONG, wintypes.LPVOID, wintypes.LONG]
pviDll.PviXRead.restype = c_int32
def PviXRead( hPvi, LinkID, nAccess, pArgData, ArgDataLen, pData, DataLen):
    result = pviDll.PviXRead( hPvi, LinkID, nAccess, pArgData, ArgDataLen, pData, DataLen)
    return result

#
# int PviXReadRequest (DWORD hPvi, DWORD LinkID, DWORD nAccess, LPVOID hResMsg, 
#                       DWORD ResMsgNo, LPARAM ResParam)
#

pviDll.PviXReadRequest.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID, 
                                   wintypes.DWORD, wintypes.LPARAM]
pviDll.PviXReadRequest.restype = c_int32
def PviXReadRequest( hPvi, LinkID, nAccess, hResMsg, ResMsgNo, ResParam):
    result = pviDll.PviXReadRequest( hPvi, LinkID, nAccess, hResMsg, ResMsgNo, ResParam)
    return result

#
# int PviXReadArgumentRequest (DWORD hPvi, DWORD LinkID, DWORD nAccess, LPVOID pArgData, LONG ArgDataLen, 
#                               LPVOID hResMsg, DWORD ResMsgNo, LPARAM ResParam)
#

pviDll.PviXReadArgumentRequest.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID, wintypes.LONG,
                                           wintypes.LPVOID, wintypes.DWORD, wintypes.LPARAM]
pviDll.PviXReadArgumentRequest.restype = c_int32
def PviXReadArgumentRequest( hPvi, LinkID, nAccess, pArgData, ArgDataLen, hResMsg, ResMsgNo, ResParam):
    result = pviDll.PviXReadArgumentRequest( hPvi, LinkID, nAccess, pArgData, ArgDataLen, hResMsg, ResMsgNo, ResParam)
    return result

#
# int PviXReadResponse (DWORD hPvi, WPARAM wParam, LPVOID pData, LONG DataLen)
#

pviDll.PviXReadResponse.argtypes = [wintypes.DWORD, wintypes.WPARAM, wintypes.LPVOID, wintypes.LONG]
pviDll.PviXReadResponse.restype = c_int32
def PviXReadResponse( hPvi, wParam, pData, DataLen ):
    result = pviDll.PviXReadResponse( hPvi, wParam, pData, DataLen )
    return result


#
# int PviXWriteRequest (DWORD hPvi, DWORD LinkID, DWORD nAccess, LPVOID pData, LONG DataLen, 
#                       LPVOID hResMsg, DWORD ResMsgNo, LPARAM ResParam)
#

pviDll.PviXWriteRequest.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID, wintypes.LONG,
                                    wintypes.LPVOID, wintypes.DWORD, wintypes.LPARAM]
pviDll.PviXWriteRequest.restype = c_int32
def PviXWriteRequest( hPvi, LinkID, nAccess, pData, DataLen, hResMsg, ResMsgNo, ResParam ):
    result = pviDll.PviXWriteRequest( hPvi, LinkID, nAccess, pData, DataLen, hResMsg, ResMsgNo, ResParam )
    return result

#
# int PviXWriteResultResponse (DWORD hPvi, WPARAM wParam, LPVOID pRstData, LONG RstDataLen)
#     

pviDll.PviXWriteResultResponse.argtypes = [wintypes.DWORD, wintypes.WPARAM, wintypes.LPVOID, wintypes.LONG]
pviDll.PviXWriteResultResponse.restype = c_int32
def PviXWriteResultResponse( hPvi, wParam, pRstData, RstDataLen ):
    result = pviDll.PviXWriteResultResponse( hPvi, wParam, pRstData, RstDataLen )
    return result


#
# int PviXWriteResultResponse (DWORD hPvi, WPARAM wParam)
#     

pviDll.PviXWriteResponse.argtypes = [wintypes.DWORD, wintypes.WPARAM]
pviDll.PviXWriteResponse.restype = c_int32
def PviXWriteResponse( hPvi, wParam ):
    result = pviDll.PviXWriteResponse( hPvi, wParam )
    return result



#
# int PviXWrite (DWORD hPvi, DWORD LinkID, DWORD nAccess, LPVOID pData, LONG DataLen, 
#                LPVOID pRstData, LONG RstDataLen)
#

pviDll.PviXWrite.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID, wintypes.LONG,
                             wintypes.LPVOID, wintypes.LONG]
pviDll.PviXWrite.restype = c_int32
def PviXWrite( hPvi, LinkID, nAccess, pData, DataLen, pRstData, RstDataLen ):
    result = pviDll.PviXWrite( hPvi, LinkID, nAccess, pData, DataLen, pRstData, RstDataLen )
    return result
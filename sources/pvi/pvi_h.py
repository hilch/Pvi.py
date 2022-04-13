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

import winreg

from ctypes import *
from ctypes import c_uint32 as DWORD
from ctypes import c_uint64 as WPARAM
from ctypes import c_int64 as LPARAM
from ctypes import c_void_p as HANDLE
from enum import IntEnum


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
        ("LinkID",DWORD),
        ("nMode", DWORD),
        ("nType", DWORD),
        ("ErrCode", DWORD),
        ("Status", DWORD)
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


accessRegistry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
pviKey = winreg.OpenKey(accessRegistry,r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\PviMan.exe")
pviDllPath = None
for n in range(10):
    try:
        value = list(winreg.EnumValue( pviKey, n))
        if value[0] == "Path" and value[2] == winreg.REG_SZ:
            pviDllPath = value[1]
    except OSError:
        break

if pviDllPath == None:
    print("Pvi is not installed")
    exit(1)

pviDll = WinDLL ( pviDllPath + r"\PviCom64.dll")

#
# int PviInitialize (INT Timeout, INT RetryTime, LPCSTR pInitParam, LPVOID pRes)
#

pviDll.PviInitialize.argtypes = [c_int32, c_int32, c_char_p, c_void_p]
pviDll.PviInitialize.restype = c_int32
def PviInitialize( Timeout, RetryTime, pInitParam, pRes ):
    result = pviDll.PviInitialize( Timeout, RetryTime, bytes( pInitParam, 'ascii'), pRes )
    return result

pviDll.PviDeinitialize.restype = c_int32
result = pviDll.PviDeinitialize()
def PviDeinitialize():
    return result

#
# int PviSetGlobEventMsg (DWORD nGlobEvent, LPVOID hEventMsg, DWORD EventMsgNo, LPARAM EventParam)
#

pviDll.PviSetGlobEventMsg.argtypes = [c_uint32, c_void_p, c_uint32, c_int64 ]
pviDll.PviSetGlobEventMsg.restype = c_int32
def PviSetGlobEventMsg(nGlobEvent, hEventMsg, EventMsgNo, EventParam ):
    result = pviDll.PviSetGlobEventMsg( nGlobEvent, hEventMsg, EventMsgNo, EventParam )
    return result

#
# int PviGetNextResponse (WPARAM* pwParam, LPARAM* plParam, LPVOID* phMsg, HANDLE hEvent)
#

pviDll.PviGetNextResponse.argtypes = [c_void_p, c_void_p, c_void_p, c_void_p]    
pviDll.PviGetNextResponse.restype = c_int32
def PviGetNextResponse( pwParam, plParam, phMsg, hEvent):
    result = pviDll.PviGetNextResponse( pwParam, plParam, phMsg, hEvent )
    return result



#
# int PviGetResponseInfo (WPARAM wParam, LPARAM* pParam, LPDWORD pDataLen, T_RESPONSE_INFO* pInfo, DWORD InfoLen)
#

pviDll.PviGetResponseInfo.argtypes = [c_uint64, c_void_p, c_void_p, c_void_p, c_uint32 ]
pviDll.PviGetResponseInfo.restype = c_int32
def PviGetResponseInfo( wParam, pParam, pDataLen, pInfo, InfoLen):
    result = pviDll.PviGetResponseInfo( wParam, pParam, pDataLen, pInfo, InfoLen )
    return result

#
# int PviLink (LPDWORD pLinkID, LPCSTR pObjectName, LPVOID hEventMsg, DWORD EventMsgNo, LPARAM EventParam, LPCSTR pLinkDescriptor)
# 

pviDll.PviLink.argtypes = [c_void_p, c_char_p, c_void_p, c_uint32, c_uint64, c_char_p ]
pviDll.PviLink.restype = c_int32
def PviLink(pLinkID, pObjectName, hEventMsg, EventMsgNo, EventParam, pLinkDescriptor ):
    result = pviDll.PviLink(pLinkID, pObjectName, hEventMsg, EventMsgNo, EventParam, pLinkDescriptor)
    return result


#
# int PviUnlink (DWORD LinkID)
#

pviDll.PviUnlink.argtypes = [c_uint32]
pviDll.PviUnlink.restype = c_int32
def PviUnlink(pLinkID ) -> int:
    result = pviDll.PviUnlink(pLinkID)
    return result



#
# int PviCreate (LPDWORD pLinkID, LPCSTR pObjectName, DWORD ObjectTyp, LPCSTR pObjektDescriptor, LPVOID hEventMsg, DWORD EventMsgNo, LPARAM EventParam, LPCSTR pLinkDescriptor)
#

pviDll.PviCreate.argtypes = [c_void_p, c_char_p, c_uint32, c_char_p, c_void_p, c_uint32, c_uint64, c_char_p]
pviDll.PviCreate.restype = c_int32
def PviCreate( pLinkID, pObjectName, ObjectTyp, pObjectDescriptor, hEventMsg, EventMsgNo, EventParam, pLinkDescriptor ):
    result = pviDll.PviCreate(pLinkID, pObjectName, ObjectTyp, pObjectDescriptor, hEventMsg, EventMsgNo, EventParam, pLinkDescriptor)
    return result

#
# int PviRead (DWORD LinkID, DWORD nAccess, LPVOID pArgData, LONG ArgDataLen, LPVOID pData, LONG DataLen)
#

pviDll.PviRead.argtypes = [c_uint32, c_uint32, c_void_p, c_int64, c_void_p, c_int64]
pviDll.PviRead.restype = c_int32
def PviRead(LinkID, nAccess, pArgData, ArgDataLen, pData, DataLen):
    result = pviDll.PviRead(LinkID, nAccess, pArgData, ArgDataLen, pData, DataLen)
    return result

#
# int PviReadRequest (DWORD LinkID, DWORD nAccess, LPVOID hResMsg, DWORD ResMsgNo, LPARAM ResParam)
#

pviDll.PviReadRequest.argtypes = [c_uint32, c_uint32, c_void_p, c_uint32, c_int64]
pviDll.PviReadRequest.restype = c_int32
def PviReadRequest(LinkID, nAccess, hResMsg, ResMsgNo, ResParam):
    result = pviDll.PviReadRequest(LinkID, nAccess, hResMsg, ResMsgNo, ResParam)
    return result

#
# int PviReadArgumentRequest (DWORD LinkID, DWORD nAccess, LPVOID pArgData, LONG ArgDataLen, LPVOID hResMsg, DWORD ResMsgNo, LPARAM ResParam)
#

pviDll.PviReadArgumentRequest.argtypes = [c_uint32, c_uint32, c_void_p, c_int64, c_void_p, c_uint32, c_int64]
pviDll.PviReadArgumentRequest.restype = c_int32
def PviReadArgumentRequest( LinkID, nAccess, pArgData, ArgDataLen, hResMsg, ResMsgNo, ResParam):
    result = pviDll.PviReadArgumentRequest(LinkID, nAccess, pArgData, ArgDataLen, hResMsg, ResMsgNo, ResParam)
    return result

#
# int PviReadResponse (WPARAM wParam, LPVOID pData, LONG DataLen)
#

pviDll.PviReadResponse.argtypes = [c_uint64, c_void_p, c_int64]
pviDll.PviReadResponse.restype = c_int32
def PviReadResponse( wParam, pData, DataLen ):
    result = pviDll.PviReadResponse( wParam, pData, DataLen )
    return result


#
# int PviWriteRequest (DWORD LinkID, DWORD nAccess, LPVOID pData, LONG DataLen, LPVOID hResMsg, DWORD ResMsgNo, LPARAM ResParam)
#

pviDll.PviWriteRequest.argtypes = [c_uint32, c_uint32, c_void_p, c_int32, c_void_p, c_uint32, c_int64]
pviDll.PviWriteRequest.restype = c_int32
def PviWriteRequest( LinkID, nAccess, pData, DataLen, hResMsg, ResMsgNo, ResParam ):
    result = pviDll.PviWriteRequest( LinkID, nAccess, pData, DataLen, hResMsg, ResMsgNo, ResParam )
    return result

#
# int PviWriteResponse (WPARAM wParam)
#     

pviDll.PviWriteResponse.argtypes = [c_uint64]
pviDll.PviWriteResponse.restype = c_int32
def PviWriteResponse( wParam ):
    result = pviDll.PviWriteResponse( wParam )
    return result

#
# int PviWrite (DWORD LinkID, DWORD nAccess, LPVOID pData, LONG DataLen, LPVOID pRstData, LONG RstDataLen)
#

pviDll.PviWrite.argtypes = [c_uint32, c_uint32, c_void_p, c_int32, c_void_p, c_int32]
pviDll.PviWrite.restype = c_int32
def PviWrite( LinkID, nAccess, pData, DataLen, pRstData, RstDataLen ):
    result = pviDll.PviWrite( LinkID, nAccess, pData, DataLen, pRstData, RstDataLen )
    return result
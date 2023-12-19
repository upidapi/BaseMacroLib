# https://learn.microsoft.com/en-us/windows/win32/api/winsock2/nf-winsock2-wsalookupservicebeginw
from Core import *
from Guid import GUID


class ControlFlags:
    DEEP = 0x0001
    CONTAINERS = 0x0002
    NOCONTAINERS = 0x0004
    NEAREST = 0x0008
    RETURN_NAME = 0x0010
    RETURN_TYPE = 0x0020
    RETURN_VERSION = 0x0040
    RETURN_COMMENT = 0x0080
    RETURN_ADDR = 0x0100
    RETURN_BLOB = 0x0200
    RETURN_ALIASES = 0x0400
    RETURN_QUERY_STRING = 0x0800
    RETURN_ALL = 0x0FF0
    FLUSHPREVIOUS = 0x1000
    FLUSHCACHE = 0x2000
    RES_SERVICE = 0x8000


class WSAVersion(RStructure):
    """
    typedef struct _WSAVersion {
      DWORD          dwVersion;
      WSAECOMPARATOR ecHow;
    } WSAVERSION, *PWSAVERSION, *LPWSAVERSION;
    """
    _fields_ = [
        ("dwVersion", DWORD),
        ("ecHow", DWORD),
    ]


class AFPROTOCOLS(RStructure):
    """
    typedef struct _AFPROTOCOLS {
      INT iAddressFamily;
      INT iProtocol;
    } AFPROTOCOLS, *PAFPROTOCOLS, *LPAFPROTOCOLS;
    """

    _fields_ = [
        ("iAddressFamily", c_int),
        ("iProtocol", c_int),
    ]


# class SOCKADDR(RStructure):
#     """
#     struct sockaddr {
#         ushort  sa_family;
#         char    sa_data[14];
#     };
#     """
#
#     _fields_ = [
#         ("sa_family", ctypes.c_ushort),
#         ("sa_data", c_char * 14),
#     ]
#
#
# class SOCKET_ADDRESS(RStructure):
#     """
#     typedef struct _SOCKET_ADDRESS {
#       LPSOCKADDR lpSockaddr;
#       INT        iSockaddrLength;
#     } SOCKET_ADDRESS, *PSOCKET_ADDRESS, *LPSOCKET_ADDRESS;
#     """
#
#     _fields_ = [
#         ("lpSockaddr", POINTER(SOCKADDR)),
#         ("iSockaddrLength", c_int),
#     ]


class CSADDR_INFO(RStructure):
    """
    typedef struct _CSADDR_INFO {
      SOCKET_ADDRESS LocalAddr;
      SOCKET_ADDRESS RemoteAddr;
      INT            iSocketType;
      INT            iProtocol;
    } CSADDR_INFO, *PCSADDR_INFO, *LPCSADDR_INFO;
    """

    _fields_ = [
        ("LocalAddr", c_int),
        ("RemoteAddr", c_int),
        ("iSocketType", c_int),
        ("iProtocol", c_int),
    ]


class BLOB(RStructure):
    """
    typedef struct _BLOB {
      ULONG cbSize;
    #if ...
      BYTE  *pBlobData;
    #else
      BYTE  *pBlobData;
    #endif
    } BLOB, *LPBLOB;
    """

    _fields_ = [
        ("cbSize", ULONG),
        ("pBlobData", POINTER(ctypes.c_byte)),
    ]


class WSAQuerySetW(RStructure):
    """
    typedef struct _WSAQuerySetW {
      DWORD         dwSize;
      LPWSTR        lpszServiceInstanceName;
      LPGUID        lpServiceClassId;
      LPWSAVERSION  lpVersion;
      LPWSTR        lpszComment;
      DWORD         dwNameSpace;
      LPGUID        lpNSProviderId;
      LPWSTR        lpszContext;
      DWORD         dwNumberOfProtocols;
      LPAFPROTOCOLS lpafpProtocols;
      LPWSTR        lpszQueryString;
      DWORD         dwNumberOfCsAddrs;
      LPCSADDR_INFO lpcsaBuffer;
      DWORD         dwOutputFlags;
      LPBLOB        lpBlob;
    } WSAQUERYSETW, *PWSAQUERYSETW, *LPWSAQUERYSETW;
    """
    _fields_ = [
        ("dwSize", DWORD),
        ("lpszServiceInstanceName", wintypes.LPWSTR),
        ("lpServiceClassId", POINTER(GUID)),
        ("lpVersion", POINTER(WSAVersion)),
        ("lpszComment", wintypes.LPWSTR),
        ("dwNameSpace", DWORD),
        ("lpNSProviderId", POINTER(GUID)),
        ("lpszContext", wintypes.LPWSTR),
        ("dwNumberOfProtocols", DWORD),
        ("lpafpProtocols", POINTER(AFPROTOCOLS)),
        ("lpszQueryString", wintypes.LPWSTR),
        ("dwNumberOfCsAddrs", DWORD),
        ("lpcsaBuffer", POINTER(CSADDR_INFO)),
        ("dwOutputFlags", DWORD),
        ("lpBlob", POINTER(BLOB)),
    ]


class WSAData(RStructure):
    """
    typedef struct WSAData {
      WORD           wVersion;
      WORD           wHighVersion;
    #if ...
      unsigned short iMaxSockets;
    #if ...
      unsigned short iMaxUdpDg;
    #if ...
      char           *lpVendorInfo;
    #if ...
      char           szDescription[WSADESCRIPTION_LEN + 1];
    #if ...
      char           szSystemStatus[WSASYS_STATUS_LEN + 1];
    #else
      char           szDescription[WSADESCRIPTION_LEN + 1];
    #endif
    #else
      char           szSystemStatus[WSASYS_STATUS_LEN + 1];
    #endif
    #else
      unsigned short iMaxSockets;
    #endif
    #else
      unsigned short iMaxUdpDg;
    #endif
    #else
      char           *lpVendorInfo;
    #endif
    } WSADATA;
    """
    _fields_ = [
        ("wVersion", WORD),
        ("wHighVersion", WORD),
    ]


ws = WinDlls.WinSock2


start_data = WSAData()
if (error_code := ws.WSAStartup(0x202, byref(start_data))) != 0:
    raise OSError(f"init error {error_code:=}")

print(start_data)


# https://github.com/MoSync/MoSync/blob/master/tools/ReleasePackageBuild/build_package_tools/include/ws2bth.h
NS_BTH = 32


# https://docs.btframework.com/bluetooth/vcl/index.htm?wclUUIDs.L2CAP_PROTOCOL_UUID.htm

# 00001803-0000-1000-8000-00805F9B34FB
L2CAP_PROTOCOL_UUID = GUID("{00001803-0000-1000-8000-00805F9B34FB}")
# L2CAP_PROTOCOL_UUID = "{00001803-0000-1000-8000-00805F9B34FB}"

addr = "AC:80:0A:2E:81:6A"

c = WSAQuerySetW(
    dwSize=ctypes.sizeof(WSAQuerySetW),
    lpServiceClassId=ctypes.pointer(
        L2CAP_PROTOCOL_UUID
    ),
    dwNameSpace=DWORD(NS_BTH),
    dwNumberOfCsAddrs=DWORD(0),
    lpszContext=ctypes.c_wchar_p(addr)
)


handle = wintypes.HANDLE(None)
ctl_flags = DWORD(
        ControlFlags.FLUSHCACHE |
        ControlFlags.RETURN_NAME |
        ControlFlags.RETURN_TYPE |
        ControlFlags.RETURN_ADDR |
        ControlFlags.RETURN_BLOB |
        ControlFlags.RETURN_COMMENT
)

ws.WSALookupServiceBeginW.argtypes = (
    POINTER(WSAQuerySetW),
    DWORD,
    POINTER(HANDLE)
)
ws.WSALookupServiceBeginW.restype = c_int

# returns socket error
a = ws.WSALookupServiceBeginW(
    byref(c),
    ctl_flags,
    byref(handle)
)

print(a, ws.WSAGetLastError())

from __future__ import annotations

from Main.Core import *
from Main.MyBluetooth import GUID, SYSTEMTIME


class LE_UUID(RStructure):
    _fields_ = [
        ("isShortUuid", BOOL),
        ("ShortUuid", USHORT),
        ("LongUuid", GUID)]


class LE_GATT_SERVICE(RStructure):
    _fields_ = [
        ("ServiceUuid", LE_UUID),
        ("AttributeHandle", USHORT)]


class ADDRESS(ctypes.Union):
    _fields_ = [
        ("ullLong", c_ulonglong),
        ("rgBytes", BYTE * 6)]

class DEVICE_SEARCH_PARAMS(RStructure):
    _fields_ = [
        ("dwSize", DWORD),
        ("fReturnAuthenticated", BOOL),
        ("fReturnRemembered", BOOL),
        ("fReturnUnknown", BOOL),
        ("fReturnConnected", BOOL),
        ("fIssueInquiry", BOOL),
        ("cTimeoutMultiplier", c_ulong),
        ("hRadio", HANDLE)]


class DEVICE_INFO(RStructure):
    _fields_ = [
        ("dwSize", DWORD),
        ("Address", ADDRESS),
        ("ulClassofDevice", c_ulong),
        ("fConnected", BOOL),
        ("fRemembered", BOOL),
        ("fAuthenticated", BOOL),
        ("stLastSeen", SYSTEMTIME),
        ("stLastUsed", SYSTEMTIME),
        ("szName", WCHAR * 248)]


__all__ = [
    LE_UUID,
    LE_GATT_SERVICE,
    ADDRESS,
    DEVICE_SEARCH_PARAMS,
    DEVICE_INFO,
]

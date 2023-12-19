# https://github.com/enthought/comtypes/blob/main/comtypes/GUID.py
from ctypes import *

BYTE = c_byte
WORD = c_ushort
DWORD = c_ulong

_ole32 = oledll.ole32

_StringFromCLSID = _ole32.StringFromCLSID
_CoTaskMemFree = windll.ole32.CoTaskMemFree
_ProgIDFromCLSID = _ole32.ProgIDFromCLSID
_CLSIDFromString = _ole32.CLSIDFromString
_CLSIDFromProgID = _ole32.CLSIDFromProgID
_CoCreateGuid = _ole32.CoCreateGuid

# Note: Comparing GUID instances by comparing their buffers
# is slightly faster than using ole32.IsEqualGUID.


class GUID(Structure):
    _fields_ = [("Data1", DWORD),
                ("Data2", WORD),
                ("Data3", WORD),
                ("Data4", BYTE * 8)]

    def __init__(self, name=None):
        super().__init__()
        if name is not None:
            _CLSIDFromString(str(name), byref(self))

    def __repr__(self):
        return f'GUID({self})'

    def __str__(self):
        p = c_wchar_p()
        _StringFromCLSID(byref(self), byref(p))
        result = p.value
        _CoTaskMemFree(p)
        return result

    @classmethod
    def from_progid(cls, progid):
        """Get guid from progid, ...
        """
        if hasattr(progid, "_reg_clsid_"):
            progid = progid._reg_clsid_
        if isinstance(progid, cls):
            return progid
        elif isinstance(progid, str):
            if progid.startswith("{"):
                return cls(progid)
            inst = cls()
            _CLSIDFromProgID(str(progid), byref(inst))
            return inst
        else:
            raise TypeError("Cannot construct guid from %r" % progid)

    def as_progid(self):
        "Convert a GUID into a progid"
        progid = c_wchar_p()
        _ProgIDFromCLSID(byref(self), byref(progid))
        result = progid.value
        _CoTaskMemFree(progid)
        return result

    @classmethod
    def create_new(cls):
        "Create a brand new guid"
        guid = cls()
        _CoCreateGuid(byref(guid))
        return guid


GUID_null = GUID()

# example usage
# L2CAP_PROTOCOL_UUID = GUID("{00001803-0000-1000-8000-00805F9B34FB}")

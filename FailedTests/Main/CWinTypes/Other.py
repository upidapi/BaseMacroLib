import ctypes
from ctypes import wintypes

from ctypes import (
    POINTER,
    byref,
    c_ulong,
    c_ulonglong,
    c_int,
    c_char,
)

from ctypes.wintypes import (
    DWORD,
    WORD,
    BOOL,
    BYTE,
    USHORT,
    ULONG,
    WCHAR,
    HANDLE
)


class RStructure(ctypes.Structure):
    def __repr__(self):
        def convert(value):
            # if value.__class__ == object:
            #     return value

            if isinstance(value, str | int):
                return value

            if isinstance(value, list | tuple):
                return [convert(x) for x in value]

            try:
                return value.value
            except AttributeError:
                pass

            # try:
            #     return hex(value)
            # except TypeError:
            #     pass
            #
            # try:
            #     return value.raw
            # except AttributeError:
            #     pass
            #
            # try:
            #     return value[:]
            # except TypeError:
            #     pass

            # x = {
            #     key: value.__getattribute__(key)
            #     for key in dir(value)
            #     if not (key.startswith("__") and key.endswith("__"))
            #     and key != "_b_base_"
            # }

            if isinstance(value, ctypes.Structure | ctypes.Union):
                return [f"{x[0]}: {convert(getattr(value, x[0]))}" for x in value.__class__._fields_]

            return value

        def conv_to_struct():
            out = {}
            for x in self.__class__._fields_:
                a = convert(getattr(self, x[0]))

                out[x[0]] = a

            return out

        def print_list_ish(items: list[str], is_par_data: [bool], _indent=0):
            last_par = True
            out = ""
            for item, is_par in zip(items, is_par_data):
                prev = "\n" + "    " * (_indent + 1)
                a = "" if is_par and last_par else prev

                out += \
                    (f"{a}"
                     f"{item},")

                last_par = is_par

            return out

        def p_print_dict(a, _indent=0):
            if isinstance(a, dict):
                x = print_list_ish([
                    f"{key}: {p_print_dict(item, _indent=_indent + 1)}"
                    for key, item in a.items()
                ],
                    [False for _, item in a.items()],
                    _indent=_indent
                )

                return f"{{{x}\n{'    ' * _indent}}},"
            elif isinstance(a, list | tuple):
                x = print_list_ish(
                    [
                        p_print_dict(item, _indent=_indent + 1)
                        for item in a
                    ],
                    [isinstance(item, dict | list | tuple) for item in a],
                    _indent=_indent
                )

                if isinstance(a, list):
                    return f"[{x}\n{'    ' * _indent}]"
                elif isinstance(a, tuple):
                    return f"({x}\n{'    ' * _indent})"
            else:
                return f"{str(a)}"

        b = conv_to_struct()

        return p_print_dict(b)


class WinDlls:
    # winsock2 dll
    WinSock2 = ctypes.windll.ws2_32
    BluetoothAPIs = ctypes.windll.BluetoothAPIs
    SetupApi = ctypes.windll.Setupapi
    Kernel32 = ctypes.windll.Kernel32


__all__ = [
    "ctypes",
    "wintypes",

    "POINTER",
    "byref",
    "c_ulong",
    "c_ulonglong",
    "c_int",
    "c_char",

    "DWORD",
    "WORD",
    "BOOL",
    "BYTE",
    "USHORT",
    "ULONG",
    "WCHAR",
    "HANDLE",

    "RStructure",
    "WinDlls"
]

class GUID(RStructure):
    _fields_ = [
        ("Data1", DWORD),
        ("Data2", WORD),
        ("Data3", WORD),
        ("Data4", BYTE * 8)
    ]


class SYSTEMTIME(RStructure):
    _fields_ = [
        ("wYear", WORD),
        ("wMonth", WORD),
        ("wDayOfWeek", WORD),
        ("wDay", WORD),
        ("wHour", WORD),
        ("wMinute", WORD),
        ("wSecond", WORD),
        ("wMilliseconds", WORD)]
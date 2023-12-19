# http://stackoverflow.com/questions/25434320/windows-8-1-bluetooth-le-cant-get-device-interface
# http://stackoverflow.com/questions/19808624/how-to-connect-to-the-bluetooth-low-energy-device
# http://doxygen.reactos.org/d0/de4/devguid_8h_source.html
# http://pinvoke.net/default.aspx/setupapi.setupdigetclassdevs
# https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/device/bluetooth/bluetooth_low_energy_defs_win.h

# source
# https://gist.github.com/tshirtman/44e8efeefb2c59ec017e

import ctypes
from time import sleep
from ctypes import (
    POINTER,
    byref,
    sizeof,
    create_unicode_buffer,
    WinError,
    c_ulong,
    c_ulonglong,
    c_int,
    c_char,
    HRESULT
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

# HRESULT = BYTE * 4
# HRESULT.__str__ = lambda self: 'HRESULT:' + ' '.join(map(bin, self))
HRESULT.__str__ = lambda self: bin(self.value)[3:].zfill(32)

BTH_ADDR = c_ulonglong
HDEVINFO = c_int
LPTSTR = POINTER(c_char)
TCHAR = c_char

PBYTE = POINTER(BYTE)

SPDRP_DEVICEDESC = DWORD(0x00000000)
SPDRP_HARDWAREID = DWORD(0x00000001)
SPDRP_COMPATIBLEIDS = DWORD(0x00000002)
SPDRP_UNUSED0 = DWORD(0x00000003)
SPDRP_SERVICE = DWORD(0x00000004)
SPDRP_UNUSED1 = DWORD(0x00000005)
SPDRP_UNUSED2 = DWORD(0x00000006)
SPDRP_CLASS = DWORD(0x00000007)
SPDRP_CLASSGUID = DWORD(0x00000008)
SPDRP_DRIVER = DWORD(0x00000009)
SPDRP_CONFIGFLAGS = DWORD(0x0000000A)
SPDRP_MFG = DWORD(0x0000000B)
SPDRP_FRIENDLYNAME = DWORD(0x0000000C)
SPDRP_LOCATION_INFORMATION = DWORD(0x0000000D)
SPDRP_PHYSICAL_DEVICE_OBJECT_NAME = DWORD(0x0000000E)
SPDRP_CAPABILITIES = DWORD(0x0000000F)
SPDRP_UI_NUMBER = DWORD(0x00000010)
SPDRP_UPPERFILTERS = DWORD(0x00000011)
SPDRP_LOWERFILTERS = DWORD(0x00000012)
SPDRP_BUSTYPEGUID = DWORD(0x00000013)
SPDRP_LEGACYBUSTYPE = DWORD(0x00000014)
SPDRP_BUSNUMBER = DWORD(0x00000015)
SPDRP_ENUMERATOR_NAME = DWORD(0x00000016)
SPDRP_SECURITY = DWORD(0x00000017)
SPDRP_SECURITY_SDS = DWORD(0x00000018)
SPDRP_DEVTYPE = DWORD(0x00000019)
SPDRP_EXCLUSIVE = DWORD(0x0000001A)
SPDRP_CHARACTERISTICS = DWORD(0x0000001B)
SPDRP_ADDRESS = DWORD(0x0000001C)
SPDRP_UI_NUMBER_DESC_FORMAT = DWORD(0x0000001D)
SPDRP_DEVICE_POWER_DATA = DWORD(0x0000001E)
SPDRP_REMOVAL_POLICY = DWORD(0x0000001F)
SPDRP_REMOVAL_POLICY_HW_DEFAULT = DWORD(0x00000020)
SPDRP_REMOVAL_POLICY_OVERRIDE = DWORD(0x00000021)
SPDRP_INSTALL_STATE = DWORD(0x00000022)
SPDRP_LOCATION_PATHS = DWORD(0x00000023)

ERROR_INSUFFICIENT_BUFFER = 0x7A
ERROR_INVALID_DATA = 0xD
ERROR_SUCCESS = 0x0
ERROR_INVALID_FUNCTION = 0x1
ERROR_FILE_NOT_FOUND = 0x2
ERROR_PATH_NOT_FOUND = 0x3
ERROR_NO_MORE_ITEMS = 0x103


def new(structure, **kwargs):
    s = structure()
    for k, v in kwargs.items():
        setattr(s, k, v)
    return s


class RStructure(ctypes.Structure):
    def __repr__(self):
        return str(
            {
                x[0]: convert(getattr(self, x[0]))
                for x in self.__class__.fields_
            })


class GUID(RStructure):
    _fields_ = [
        ("Data1", DWORD),
        ("Data2", WORD),
        ("Data3", WORD),
        ("Data4", BYTE * 8)
    ]


# from virtualbox sourcecode (devpropdef.h)
DEVPROPGUID = GUID
DEVPROPID = ULONG


class DEVPROPKEY(RStructure):
    _fields_ = [
        ("fmtid", DEVPROPGUID),
        ("pid", DEVPROPID)]


PDEVPROPKEY = POINTER(DEVPROPKEY)


def convert(value):
    try:
        return value.value
    except AttributeError:
        pass
    try:
        return hex(value)
    except TypeError:
        pass
    try:
        return value.raw
    except AttributeError:
        pass

    return [hex(USHORT(x).value) for x in value]
    # return [hex(x) for x in value]
    # return value[:]

    # try:
    #     return [hex(USHORT(x).value) for x in value]
    # except:
    #     pass
    # try:
    #     return [hex(x) for x in value]
    # except:
    #     pass
    # try:
    #     return value[:]
    # except:
    #     pass



# GUID_DEVCLASS_BLUETOOTH = GUID(
#     Data1=0xE0CBF06C,
#     Data2=0xCD8B,
#     Data3=0x4647,
#     Data4=(BYTE * 8).from_buffer_copy(
#         bytearray([
#             0xBB, 0x8A, 0x26, 0x3B, 0x43, 0xF0, 0xF9, 0x74
#         ])
#     )
# )

# 00001803-0000-1000-8000-00805F9B34FB
GUID_DEVCLASS_BLUETOOTH = GUID(
    Data1=0xe0cbf06c,
    Data2=0xcd8b,
    Data3=0x4647,
    Data4=(BYTE * 8).from_buffer_copy(
        bytearray([
            0xbb, 0x8a, 0x26, 0x3b, 0x43, 0xf0, 0xf9, 0x74
        ])
    )
)

GUID_BTHPORT_DEVICE_INTERFACE = GUID(
    Data1=0x0850302A,
    Data2=0xB344,
    Data3=0x4FDA,
    Data4=(BYTE * 8).from_buffer_copy(
        bytearray([
            0x9B, 0xE9, 0x90, 0x57, 0x6B, 0x8D, 0x46, 0xF0
        ])
    )
)

DIGCF_PRESENT = 0x02
DIGCF_DEVINTERFACE = 0x10

GENERIC_READ = 0x8000000
GENERIC_WRITE = 0x4000000

FILE_SHARE_READ = 0x01
FILE_SHARE_WRITE = 0x02

OPEN_EXISTING = 0x03

FILE_FLAG_OVERLAPPED = 0x4000000

INVALID_HANDLE_VALUE = 0xffffffff

BLUETOOTH_GATT_FLAG_NONE = 0x0


class BTH_LE_UUID(RStructure):
    _fields_ = [
        ("isShortUuid", BOOL),
        ("ShortUuid", USHORT),
        ("LongUuid", GUID)]


class BTH_LE_GATT_SERVICE(RStructure):
    _fields_ = [
        ("ServiceUuid", BTH_LE_UUID),
        ("AttributeHandle", USHORT)]


class SP_DEVINFO_DATA(RStructure):
    _fields_ = [
        ("cbSize", DWORD),
        ("ClassGuid", GUID),
        ("DevInst", DWORD),
        ("Reserved", POINTER(c_ulong))]


class SP_DEVICE_INTERFACE_DATA(RStructure):
    _fields_ = [
        ("cbSize", DWORD),
        ("InterfaceClassGuid", GUID),
        ("Flags", DWORD),
        ("Reserved", POINTER(c_ulong))]


class SP_INTERFACE_DEVICE_DETAIL_DATA(RStructure):
    _fields_ = [
        ("cbSize", DWORD),
        ("DevicePath", TCHAR)]


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


class BLUETOOTH_ADDRESS(ctypes.Union):
    _fields_ = [
        ("ullLong", BTH_ADDR),
        ("rgBytes", BYTE * 6)]


class BLUETOOTH_FIND_RADIO_PARAMS(RStructure):
    _fields_ = [
        ("dwSize", DWORD)]


class BLUETOOTH_DEVICE_SEARCH_PARAMS(RStructure):
    _fields_ = [
        ("dwSize", DWORD),
        ("fReturnAuthenticated", BOOL),
        ("fReturnRemembered", BOOL),
        ("fReturnUnknown", BOOL),
        ("fReturnConnected", BOOL),
        ("fIssueInquiry", BOOL),
        ("cTimeoutMultiplier", c_ulong),
        ("hRadio", HANDLE)]


class BLUETOOTH_DEVICE_INFO(RStructure):
    _fields_ = [
        ("dwSize", DWORD),
        ("Address", BLUETOOTH_ADDRESS),
        ("ulClassofDevice", c_ulong),
        ("fConnected", BOOL),
        ("fRemembered", BOOL),
        ("fAuthenticated", BOOL),
        ("stLastSeen", SYSTEMTIME),
        ("stLastUsed", SYSTEMTIME),
        ("szName", WCHAR * 248)]


BT = ctypes.windll.BluetoothAPIs
SAPI = ctypes.windll.Setupapi
WBAse = ctypes.windll.Kernel32

GetLastError = WBAse.GetLastError


def list_devices():
    hdi = SAPI.SetupDiGetClassDevsW(
        byref(GUID_DEVCLASS_BLUETOOTH),
        None,
        None,
        DIGCF_PRESENT
    )

    devinfo_data = SP_DEVINFO_DATA(
        cbSize=sizeof(SP_DEVINFO_DATA)
    )
    i = 0

    while SAPI.SetupDiEnumDeviceInfo(hdi, i, byref(devinfo_data)):
        i += 1
        name = get_device_info(hdi, i, devinfo_data, SPDRP_FRIENDLYNAME)
        if not name.strip().startswith('Twiz'):
            continue

        desc = get_device_info(hdi, i, devinfo_data, SPDRP_DEVICEDESC)
        service = get_device_info(hdi, i, devinfo_data, SPDRP_SERVICE)
        enumerator = get_device_info(hdi, i, devinfo_data, SPDRP_ENUMERATOR_NAME)
        device_class = get_device_info(hdi, i, devinfo_data, SPDRP_CLASS)
        device_class_guid = get_device_info(hdi, i, devinfo_data, SPDRP_CLASSGUID)
        address = get_device_info(hdi, i, devinfo_data, SPDRP_ADDRESS)
        hwid = get_device_info(hdi, i, devinfo_data, SPDRP_HARDWAREID)
        power = get_device_info(hdi, i, devinfo_data, SPDRP_DEVICE_POWER_DATA)

        print(f'''
            name: {name}
            desc: {desc}
            service: {service}
            enumerator: {enumerator}
            device_class: {device_class}
            device_class_guid: {device_class_guid}
            address: {address}
            hwid: {hwid}
            power: {power}\
        ''')

        break

    else:
        return

    # service = new(BTH_LE_GATT_SERVICE)
    # count = USHORT()
    # pka = PDEVPROPKEY()
    #
    # SAPI.SetupDiGetDevicePropertyKeys(
    #     hdi,
    #     byref(devinfo_data),
    #     pka,
    #     byref(count),
    #     DWORD(0))
    #
    # keys = new(DEVPROPID * count)
    # SAPI.SetupDiGetDevicePropertyKeys(hdi, byref(devinfo_data), keys, byref(count), 0)
    #
    # Tentative way to uget GATTGetServices, no result
    # err = ULONG(BT.BluetoothGATTGetServices(
    #     hdi, i, None, byref(count), BLUETOOTH_GATT_FLAG_NONE))
    #
    # if err.value & (1 << 32) != 0:
    #     raise RuntimeError("couldn't get services, HRESULT {}".format(bin(err).zfill(32)))
    #
    # # print err
    # print "{} services found".format(count.value)
    # services = new(BTH_LE_GATT_SERVICE * count.value)
    #
    # BT.BluetoothGATTGetServices(hdi, count, byref(services), byref(count),
    #                             BLUETOOTH_GATT_FLAG_NONE)
    #
    # service uid
    # gattServiceGUID = new(GUID,
    #                       Data1=0x1901,
    #                       Data2=0,
    #                       Data3=0x1000,
    #                       Data4=(BYTE * 8)(0x00, 0x80, 0x5f, 0x9b, 0x34, 0xfb))

    gattServiceGUID = devinfo_data.ClassGuid
    # gattServiceGUID = SAPI.SetupDiClassGuidsFromName(
    #     )
    print(gattServiceGUID)

    # hdi = SAPI.SetupDiGetClassDevsW(
    #     byref(gattServiceGUID),
    #     # None, None, DIGCF_DEVINTERFACE)
    #     # None, None, DIGCF_PRESENT)
    #     None, None, DIGCF_PRESENT | DIGCF_DEVINTERFACE)

    hdi = SAPI.SetupDiGetClassDevsW(
        byref(GUID_BTHPORT_DEVICE_INTERFACE),
        0, 0, DIGCF_PRESENT)

    print(HRESULT(hdi), hdi)
    if hdi == INVALID_HANDLE_VALUE:
        print("device not found")
        return

    interface_data = new(SP_DEVICE_INTERFACE_DATA,
                         cbSize=sizeof(SP_DEVICE_INTERFACE_DATA))

    i = DWORD(0)
    while (
            SAPI.SetupDiEnumDeviceInterfaces(
                hdi,
                None,  # byref(devinfo_data),
                byref(gattServiceGUID),
                i,
                byref(interface_data))
            # hdi, byref(devinfo_data), byref(gattServiceGUID), i, byref(interface_data))
    ):
        i += 1
        print(i)
        bytesneeded = DWORD()
        # first time just to get the needed size, sigh
        SAPI.SetupDiGetDeviceInterfaceDetails(
            hdi, byref(devinfo_data), None, 0, byref(bytesneeded), None)

        # apparently should check for ERROR_INSUFFICIENT_BUFFER before
        # that
        class STRUCT(RStructure):
            _fields_ = [
                ("cbSize", DWORD),
                ("DevicePath", TCHAR * bytesneeded)]

        details = new(STRUCT, cbSize=sizeof(STRUCT))

        if (
                SAPI.SetupDiGetDeviceInterfaceDetails(
                    hdi,
                    byref(devinfo_data),
                    byref(details),
                    bytesneeded,
                    None,
                    byref(devinfo_data))
        ):
            gatt_handle = WBAse.CreateFileW(
                details.DevicePath,
                GENERIC_READ |
                GENERIC_WRITE |
                FILE_SHARE_READ |
                FILE_SHARE_WRITE,
                None,
                OPEN_EXISTING,
                FILE_FLAG_OVERLAPPED,
                None)
            if gatt_handle != INVALID_HANDLE_VALUE:
                print("success!")
            else:
                print("nope!!")
        else:
            print("nope!")

    print("finished")
    err = GetLastError()
    if err != ERROR_NO_MORE_ITEMS:
        raise WinError(err)

    SAPI.SetupDiDestroyDeviceInfoList(hdi)


def get_device_info(hdi, i, devinfo_data, propertyname):
    data_t = DWORD()
    buffer = LPTSTR()
    buffersize = DWORD(0)

    while (
            not SAPI.SetupDiGetDeviceRegistryPropertyW(
                hdi,
                byref(devinfo_data),
                propertyname,
                data_t,
                byref(buffer),  # may need a cast (PBYTE)
                # PBYTE(buffer),
                buffersize,
                byref(buffersize)
            )
    ):
        err = GetLastError()
        if err == ERROR_INSUFFICIENT_BUFFER:
            # print buffersize
            # buffer = (c_char * buffersize.value)()
            buffer = create_unicode_buffer(buffersize.value)

        elif err == ERROR_INVALID_DATA:
            break
        else:
            raise WinError(err)

    try:
        return buffer.value.decode('utf-8')
    except:
        return ''


while True:
    list_devices()
    sleep(1)
    print("loop")

from Core import *

ws = ctypes.windll.ws2_32


class WSAData(RStructure):
    _fields_ = [
        ("wVersion", WORD),
        ("wHighVersion", WORD),
    ]


start_data = WSAData()

ws.WSAStartup(0x202, byref(start_data))

# if (error_code := ws.WSAStartup(0x202, byref(start_data))) != 0:
#     raise OSError(f"init error {error_code:=}")

print(start_data)

import ctypes
import time
from ctypes.wintypes import BOOL, HWND, LPARAM


@ctypes.WINFUNCTYPE(BOOL, HWND, LPARAM)
def callback(hwnd, _):
    print(hwnd)
    return True


ctypes.windll.user32.EnumWindows(callback, 0)

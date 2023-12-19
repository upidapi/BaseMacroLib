import ctypes
import time


class POINT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_long),
        ('y', ctypes.c_long)
    ]


def get_mouse():
    point = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
    #                  pass our point by ref ^^^^^
    # this lets GetCursorPos fill its x and y fields

    return point.x, point.y


while True:
    print(get_mouse())
    time.sleep(0.05)

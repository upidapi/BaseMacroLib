import ctypes

class POINT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_long),
        ('y', ctypes.c_long)
    ]


def get_cursor_pos() -> (int, int):
    point = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(point))

    return point.x, point.y

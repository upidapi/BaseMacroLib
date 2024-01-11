import ctypes

from lib.Keyboard.Vk import compile_to_vks


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ('dx', ctypes.c_long),
        ('dy', ctypes.c_long),
        ('mouseData', ctypes.c_long),
        ('dwFlags', ctypes.c_long),
        ('time', ctypes.c_long),
        ('dwExtraInfo', ctypes.POINTER(ctypes.c_ulong))
    ]


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ('wVk', ctypes.c_short),
        ('wScan', ctypes.c_short),
        ('dwFlags', ctypes.c_long),
        ('time', ctypes.c_long),
        ('dwExtraInfo', ctypes.POINTER(ctypes.c_ulong))
    ]


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [
        ('uMsg', ctypes.c_long),
        ('wParamL', ctypes.c_short),
        ('wParamH', ctypes.c_short)
    ]


class INPUTUNION(ctypes.Union):
    _fields_ = [
        ('mi', MOUSEINPUT),
        ('ki', KEYBDINPUT),
        ('hi', HARDWAREINPUT)
    ]


class INPUT(ctypes.Structure):
    _fields_ = [
        ('type', ctypes.c_long),
        ('value', INPUTUNION)
    ]


INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEY_UP_EVENT = 0x0002
KEY_DOWN_EVENT = 0x0000


def _press_vk(down: bool, vk):
    inputs = INPUT(type=INPUT_KEYBOARD, value=INPUTUNION(ki=KEYBDINPUT(
        wVk=vk,
        wScan=0,
        dwFlags=KEY_DOWN_EVENT if down else KEY_UP_EVENT,
        time=0,
        dwExtraInfo=None
    )))
    ctypes.windll.user32.SendInput(1, ctypes.byref(inputs), ctypes.sizeof(inputs))


def _press_vks(down: bool, *vk: int | str):
    vks = compile_to_vks(*vk)
    for vk in vks:
        _press_vk(down, vk)


def press_keys(*vk: int | str):
    _press_vks(True, *vk)


def un_press_keys(*vk: int | str):
    _press_vks(False, *vk)


def click_keys(*vk: int | str):
    """
    clicks a list of keys in order before un-clicking al of them in the reverse

    @example
    # send an "a" with the "shift" and "alt" keys pressed

    click_keys("+!a")
    """
    # possibly start by un-pressing the key
    press_keys(True, *vk)
    un_press_keys(False, *vk[::-1])


def typewrite_keys(*vk: int | str):
    """
    clicks the keys, one by one

    @example
    # typewrite "hello"

    typewrite_keys("hello")
    """
    vks = compile_to_vks(*vk)
    for vk in vks:
        _press_vk(True, vk)
        _press_vk(False, vk)


if __name__ == '__main__':
    typewrite_keys("hello")




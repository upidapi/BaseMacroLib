import ctypes
from typing import Literal

from lib.Keyboard.Vk import Vk
from lib.Keyboard.SendVk import press_keys, un_press_keys, click_keys


def set_mouse_pos(x: int, y: int):
    ctypes.windll.user32.SetCursorPos(x, y)


_mouse_buttons = Literal["left", "middle", "right"]


def _button_to_vk(button: _mouse_buttons) -> int:
    return {
        "left": Vk.mouse_left,
        "middle": Vk.mouse_middle,
        "right": Vk.mouse_right,
    }.get(button)


def press_mouse_button(button: _mouse_buttons):
    press_keys(
        _button_to_vk(button)
    )


def un_press_mouse_button(button: _mouse_buttons):
    un_press_keys(
        _button_to_vk(button)
    )


def click_mouse_button(button: _mouse_buttons):
    click_keys(
        _button_to_vk(button)
    )


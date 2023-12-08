import dataclasses
from typing import Set, Callable

import pyWinhook
import pythoncom
from pyWinhook import MouseEvent as RawMouseEvent, KeyboardEvent as RawKeyboardEvent


# class RawMouseEvent(RawMouseEvent):
#     pass


class MouseEvents:
    mouse_move = 0

    left_mouse_down = 1
    left_mouse_up = 2

    right_mouse_down = 3
    right_mouse_up = 4

    middle_mouse_down = 5
    middle_mouse_up = 6

    wheel_up = 7
    wheel_down = 8


@dataclasses.dataclass
class MouseEvent:
    event_type: int

    time: int
    pos: [int, int]
    injected: bool

    raw_event: RawMouseEvent


def print_mouse_info(event: RawMouseEvent):
    if event.Wheel:
        event_type = {
            1: MouseEvents.wheel_up,
            -1: MouseEvents.wheel_down,
        }[event.Wheel]
    else:
        event_type = {
            0x0200: MouseEvents.mouse_move,
            0x0201: MouseEvents.left_mouse_down,
            0x0202: MouseEvents.left_mouse_up,
            0x0204: MouseEvents.right_mouse_down,
            0x0205: MouseEvents.right_mouse_up,
            0x0207: MouseEvents.middle_mouse_down,
            0x0208: MouseEvents.middle_mouse_up,
        }[event.Message]

    print(MouseEvent(event_type, event.Time, event.Position, event.Injected, event).__dict__)
    return True


_bound_hotkeys: dict[set[int], Callable[[], None]]


def bind_hotkey(keys: set[int], callback: Callable[[], None]):
    _bound_hotkeys[keys] = callback


def print_keyboard_info(event: RawKeyboardEvent):
    print({
        **event.__dict__,
        "Message": event.GetMessageName(),
        "GetKey": event.GetKey(),
        "IsAlt": bool(event.IsAlt()),
        "IsExtended": bool(event.IsExtended()),
        "IsInjected": bool(event.IsInjected()),
        "IsTransition": bool(event.IsTransition()),
    })

    return True


hm = pyWinhook.HookManager()

# hm.SubscribeMouseAllButtons(print_mouse_info)
# hm.SubscribeMouseWheel(print_mouse_info)
hm.SubscribeMouseAll(print_mouse_info)

hm.HookMouse()

# hm.Subscre(print_keyboard_info)
# hm.HookKeyboard()

# noinspection PyUnresolvedReferences
pythoncom.PumpMessages()
hm.UnhookMouse()

# unice
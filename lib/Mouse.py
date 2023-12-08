from dataclasses import dataclass
from typing import Literal

from pyWinhook import \
    MouseEvent as RawMouseEvent, \
    HookConstants, HookManager


class MouseEvent:
    @dataclass
    class _BaseEvent:
        time: int
        pos: [int, int]
        injected: bool

        raw: RawMouseEvent

        def print_event(self):
            print(f"event_type={type(self)}"
                  f"event_dict={self.__dict__}"
                  f"raw_event_dict={self.raw.__dict__}")

    @dataclass
    class Move(_BaseEvent):
        pass

    @dataclass
    class Click(_BaseEvent):
        button: Literal["left", "middle", "right"]

    @dataclass
    class UnClick(_BaseEvent):
        button: Literal["left", "middle", "right"]

    @dataclass
    class Scroll(_BaseEvent):
        direction: Literal["up", "down"]

    event_types: Move | Click | UnClick | Scroll


def convert_to_dataclass(event: RawMouseEvent) -> MouseEvent.event_types:
    if event.Wheel:
        direction: Literal["up", "down"]

        if event.Wheel == 1:
            direction = "up"
        elif event.Wheel == -1:
            direction = "down"
        else:
            raise TypeError(f"event.Wheel is not 1 or -1 ({event.Wheel:=})")

        return MouseEvent.Scroll(
            time=event.Time,
            pos=event.Position,
            injected=event.Injected,
            raw=event,
            direction=direction
        )

    if event.Message == HookConstants.WM_MOUSEMOVE:
        return MouseEvent.Move(
            time=event.Time,
            pos=event.Position,
            injected=event.Injected,
            raw=event,
        )

    button: Literal["left", "middle", "right"]
    action: Literal["up", "down"]

    try:
        button, action = {
            HookConstants.WM_LBUTTONDOWN: ("left", "down"),
            HookConstants.WM_LBUTTONUP: ("left", "up"),
            HookConstants.WM_MBUTTONDOWN: ("middle", "down"),
            HookConstants.WM_MBUTTONUP: ("middle", "up"),
            HookConstants.WM_RBUTTONDOWN: ("right", "down"),
            HookConstants.WM_RBUTTONUP: ("right", "up"),
        }[event.Message]
    except IndexError:
        raise TypeError(f"invalid event message, {event.__dict__:=}")

    if action == "down":
        return MouseEvent.Click(
            time=event.Time,
            pos=event.Position,
            injected=event.Injected,
            raw=event,
            button=button
        )

    if action == "up":
        return MouseEvent.UnClick(
            time=event.Time,
            pos=event.Position,
            injected=event.Injected,
            raw=event,
            button=button
        )

    raise TypeError(f"invalid event signature, {event.__dict__:=}")


def __init__(hm: HookManager):
    # hm = HookManager()

    # hm.SubscribeMouseAllButtons(print_mouse_info)
    # hm.SubscribeMouseWheel(print_mouse_info)
    hm.SubscribeMouseAll(print_mouse_info)

    hm.HookMouse()

    # run program
    # pythoncom.PumpMessages()

    # exit
    hm.UnhookMouse()

from typing import Callable

from lib import MouseEvent, KeyboardEvent
from lib.Event import EventStack
from lib.KeyState import v_keys_pressed
from lib.Vk import Vk, v_code_to_keyname

_char_to_code_map = {
    "\b": Vk.backspace,
    "\t": Vk.tab,

    "\r": Vk.enter,
    " ": Vk.space,

    "0": Vk.n_0,
    "1": Vk.n_1,
    "2": Vk.n_2,
    "3": Vk.n_3,
    "4": Vk.n_4,
    "5": Vk.n_5,
    "6": Vk.n_6,
    "7": Vk.n_7,
    "8": Vk.n_8,
    "9": Vk.n_9,

    "a": Vk.a,
    "b": Vk.b,
    "c": Vk.c,
    "d": Vk.d,
    "e": Vk.e,
    "f": Vk.f,
    "g": Vk.g,
    "h": Vk.h,
    "i": Vk.i,
    "j": Vk.j,
    "k": Vk.k,
    "l": Vk.l,
    "m": Vk.m,
    "n": Vk.n,
    "o": Vk.o,
    "p": Vk.p,
    "q": Vk.q,
    "r": Vk.r,
    "s": Vk.s,
    "t": Vk.t,
    "u": Vk.u,
    "v": Vk.v,
    "w": Vk.w,
    "x": Vk.x,
    "y": Vk.y,
    "z": Vk.z,

    # borrowed from ahk
    "!": Vk.alt,
    "^": Vk.ctrl,
    "+": Vk.shift,
    "#": Vk.win_l
}


def _compile_to_vks(*parts: int | str):
    out = []
    for part in parts:
        if isinstance(part, int):
            out.append(part)
            continue

        for char in part:
            out.append(
                _char_to_code_map.get(char)
            )

    return out


_k_event_callback = Callable[[KeyboardEvent], None]

_key_bound_functions: [[int], _k_event_callback] = []


def bind_func_to_key(keybind: [int | str], func: Callable[[KeyboardEvent], None]):
    _key_bound_functions.append([
        _compile_to_vks(keybind),
        func
    ])


_break_callback = Callable[[], bool]


def _check_keybind_activated(event: EventStack.all_events):
    """
    Did a keybind get activated from {event}?

    If so, call that keybind callback.
    """
    if not isinstance(event, KeyboardEvent.event_types):
        return

    for keybind_keys, key_bound_func in _key_bound_functions:
        if event.vk_code not in keybind_keys:
            return

        if not v_keys_pressed(*keybind_keys):
            return

        key_bound_func()


def listen(break_cond: _break_callback = lambda: False):
    """
    starts listening to the events

    :param break_cond:
    :return:
    """

    es = EventStack()

    for event in es.get_conveyor(break_cond):
        _check_keybind_activated(event)


def print_events(
        mouse_move=False,
        mouse_click=True,
        mouse_unclick=True,
        mouse_scroll=True,

        keyboard_keydown=True,
        keyboard_keyup=True,
        keyboard_key_send=True,
):
    es = EventStack()

    for event in es.get_conveyor():
        # print(type(event))

        string_event = str(type(event)).split(".")[-1][:-2]

        if isinstance(event, KeyboardEvent.event_types):
            if \
                    isinstance(event, KeyboardEvent.KeyDown) and keyboard_keydown or \
                    isinstance(event, KeyboardEvent.KeyUp) and keyboard_keyup or \
                    isinstance(event, KeyboardEvent.KeySend) and keyboard_key_send:

                print(f"{string_event}: {v_code_to_keyname(event.vk_code)} \"{event.unicode}\"")

        if isinstance(event, MouseEvent.event_types):
            if isinstance(event, MouseEvent.Move):
                if mouse_move:
                    print(f"{string_event}: {event.pos}")
                continue

            if isinstance(event, MouseEvent.Scroll):
                if mouse_scroll:
                    print(f"{string_event}: {event.pos} {event.direction}")
                continue

            if \
                    isinstance(event, MouseEvent.Click) and mouse_click or \
                    isinstance(event, MouseEvent.UnClick) and mouse_unclick:
                print(f"{string_event}: {event.pos} {event.button}")


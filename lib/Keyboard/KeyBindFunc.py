from typing import Callable

from lib.Event import EventStack, KeyboardEvent
from lib.Keyboard.KeyState import v_keys_pressed
from lib.Keyboard.Vk import compile_to_vks

_k_event_callback = Callable[[KeyboardEvent], None]

_key_bound_functions: [[int], _k_event_callback] = []


def bind_func_to_key(keybind: [int | str], func: Callable[[KeyboardEvent], None]):
    _key_bound_functions.append([
        compile_to_vks(keybind),
        func
    ])


_break_callback = Callable[[], bool]


def check_keybind_activated(event: EventStack.all_events):
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


def listen_for_key_binds(break_cond: _break_callback = lambda: False):
    """
    starts listening to the events

    :param break_cond:
    :return:
    """

    es = EventStack()

    for event in es.get_conveyor(break_cond):
        check_keybind_activated(event)
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


k = ""
i = 0


# after 59 lines
# only print "? right" every other line

# while '10111000101111001000101001001' != the last 29 lines
while '10111000101111001000101001001' != k[-29:]:
    line = input()
    k += line

    if i < 29 and '10111000101111001000101001001'[i] != line:
        print("? flip")
        input()

    print("? right")
    i += 1

# print the amount of lines more it took to match ?
print("!", i - 29)


p,k,i,m,a,b=bin(9**9)[2:],"",0,input,print,"? flip"
while p!=k[-29:]:
 l=m();k+=l
 if i<29 and p[i]!=l:a(b);m()
 a("? right");i+=1
a("!",i-29)

# every other line staring at the first
# ignoring about half
# for the first 29 of those return "? flip"
# after that don't return anything
# also save the line into k

# every other line staring at the second one return "? right"

# do this until the last 29 chars of k == '10111000101111001000101001001'



def check_keybind_activated(event: EventStack.all_events):
    """
    Did a keybind get activated from {event}?

    If so, call that keybind callback.
    """

    if not isinstance(event, KeyboardEvent.KeyDown):
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

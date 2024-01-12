import BthConnect
from lib.Event import EventStack
from lib.Helpers import print_events
from lib.Keyboard import Vk
from lib.Keyboard.KeyBindFunc import bind_func_to_key, listen_for_key_binds, check_keybind_activated
from lib.Keyboard.SendVk import click_keys

bind_func_to_key(
    Vk.num_1,
    lambda: print(1)
)
bind_func_to_key(
    Vk.num_2,
    lambda: print(2)
)

listen_for_key_binds()

# print_events()

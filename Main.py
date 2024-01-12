import BthConnect
from lib.Event import EventStack
from lib.Keyboard import Vk
from lib.Keyboard.KeyBindFunc import bind_func_to_key, listen_for_key_binds, check_keybind_activated
from lib.Keyboard.SendVk import click_keys

bind_func_to_key(
    Vk.f13,
    lambda: click_keys(Vk.pause_media)
)

bind_func_to_key(
    Vk.f14,
    BthConnect.connect
)


es = EventStack()
for event in es.get_conveyor():
    check_keybind_activated(event)

    print()


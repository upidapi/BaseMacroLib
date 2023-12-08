from dataclasses import dataclass
from typing import Literal

import pythoncom
from CustomWinHook import KeyboardEvent as RawKeyboardEvent, HookManager


def print_mouse_info(event: RawKeyboardEvent):
    print({
        "IsExtended": bool(event.IsExtended()),
        "IsInjected": bool(event.IsInjected()),
        "IsAlt": bool(event.IsAlt()),
        "IsTransition": bool(event.IsTransition()),
        "KeyID": event.KeyID,
        "ScanCode": event.ScanCode,
        "Ascii": f"{event.Ascii} {chr(int(event.Ascii))}",
        'Message': event.Message
    })

    return True


def __init__():  # hm: HookManager):
    hm = HookManager()

    # hm.SubscribeMouseAllButtons(print_mouse_info)
    # hm.SubscribeMouseWheel(print_mouse_info)
    hm.SubscribeKeyAll(print_mouse_info)

    hm.HookKeyboard()

    # # run program
    # while True:
    #     pythoncom.PumpWaitingMessages()
    pythoncom.PumpMessages()

    # exit
    hm.UnhookKeyboard()


__init__()

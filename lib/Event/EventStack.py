import time
from typing import Callable

import pythoncom

from CustomWinHook.pyWinhook import HookManager
from lib.Event.Keyboard import KeyboardEvent
from lib.Event.Mouse import MouseEvent


class EventStack:
    all_events = KeyboardEvent.event_types | MouseEvent.event_types

    def __init__(self):
        hm = HookManager()
        self.hm = hm

        hm.HookKeyboard()
        hm.HookMouse()

        hm.SubscribeKeyAll(
            lambda e: self._push_events(
                KeyboardEvent.parse_raw_event(e)
            )
        )

        hm.SubscribeMouseAll(
            lambda e: self._push_events(
                MouseEvent.parse_raw_event(e)
            )
        )

        self._queued_events: list[EventStack.all_events] = []

    def __del__(self):
        """
        clean up after the EventStack is destroyed
        """
        hm = self.hm

        hm.SubscribeKeyAll(None)
        hm.SubscribeMouseAll(None)

        hm.HookKeyboard()
        hm.HookMouse()

        print("cleaned up event stack")

    def _push_events(self, events: [all_events]):
        for event in events:
            self._queued_events.append(event)

    def clear(self):
        self._queued_events = []

    def fetch(self):
        pythoncom.PumpWaitingMessages()
        queued_events = self._queued_events
        self.clear()
        return queued_events

    def get_conveyor(self, break_cond: Callable[[], bool] = lambda: False):
        """
        Gets the next event, forever. If there's no events queued. Then it
        waits for an event before yielding.

        # ------------------example------------------
        # this would print all keyboard keydown events

        es = EventStack()

        for event in es.get_conveyor():
            if isinstance(event, KeyboardEvent.KeyDown):
                event.print_event()
        """
        try:
            while True:
                while True:
                    if break_cond():
                        raise StopIteration

                    pythoncom.PumpWaitingMessages()

                    if self._queued_events:
                        break

                    time.sleep(0.001)

                yield self._queued_events.pop(0)
        except KeyboardInterrupt:
            self.__del__()

            raise KeyboardInterrupt


# es = EventStack()
#
#
# for event in es.get_conveyor():
#     if isinstance(event, KeyboardEvent.KeyDown | KeyboardEvent.KeySend):
#         event.print_event()


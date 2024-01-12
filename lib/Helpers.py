from lib.Event import EventStack, KeyboardEvent, MouseEvent
from lib.Keyboard.Vk import v_code_to_keyname


def print_event(

):

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


if __name__ == '__main__':
    print_events()

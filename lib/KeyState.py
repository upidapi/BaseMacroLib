import win32api


def get_nth_bit(num, n):
    (num >> n) & 1


def get_v_key_state(v_key):
    state_data = win32api.GetKeyState(v_key)
    return {
        "pressed": bool(get_nth_bit(state_data, 15)),
        "toggled": bool(get_nth_bit(state_data, 0)),
    }

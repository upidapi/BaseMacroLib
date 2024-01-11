import win32api


def _get_nth_bit(num, n):
    (num >> n) & 1


def get_v_key_state(v_key):
    state_data = win32api.GetKeyState(v_key)
    return {
        "pressed": bool(_get_nth_bit(state_data, 15)),
        "toggled": bool(_get_nth_bit(state_data, 0)),
    }


def _is_pressed(v_key):
    state_data = win32api.GetKeyState(v_key)
    return bool(_get_nth_bit(state_data, 15))


def v_keys_pressed(*v_keys):
    return all((
        _is_pressed(v_key)
        for v_key in v_keys
    ))

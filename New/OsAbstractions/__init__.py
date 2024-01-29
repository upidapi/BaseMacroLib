import platform as _platform


_system = _platform.system()
if _system == 'Windows':
    from Windows.mouse import WindowsMouse as Mouse 
    from Windows.keyboard import WindowsKeyboard as Keyboard 
    from Windows.vk import WindowsVk as Vk 

elif _system == 'Linux':
    from Linux.mouse import LinuxMouse as Mouse 
    from Linux.keyboard import LinuxKeyboard as Keyboard 
    from Linux.vk import LinuxVk as Vk 

elif _system == 'Darwin':
    try:
        from Darwin.mouse import DarwinMouse as Mouse
        from Darwin.keyboard import DarwinKeyboard as Keyboard
        from Darwin.vk import DarwinVk as Vk

    except ImportError as e:
        # This can happen during setup if pyobj wasn't already installed
        raise e
else:
    raise OSError(f"Unsupported platform \"{_system}\"")

# _keyname_to_v_code_map = {
#     key: val for key, val in Vk.__dict__.items()
#     if not (key.startswith("__") and key.endswith("__"))
# }

# _v_code_to_keyname_map = {val: key for key, val in _keyname_to_v_code_map.items()}


# def keyname_to_v_code(keyname):
#     return _keyname_to_v_code_map[keyname]


# def v_code_to_keyname(v_code):
#     return _v_code_to_keyname_map[v_code]

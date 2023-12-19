from typing import Callable

from . import cpyHook


def GetKeyState(key_id):
    return cpyHook.cGetKeyState(key_id)


class HookConstants:
    """
    Stores internal windows hook constants including hook types, mappings from virtual
    keycode name to value and value to name, and event type value to name.
    """
    WH_MIN = -1
    WH_MSGFILTER = -1
    WH_JOURNALRECORD = 0
    WH_JOURNALPLAYBACK = 1
    WH_KEYBOARD = 2
    WH_GETMESSAGE = 3
    WH_CALLWNDPROC = 4
    WH_CBT = 5
    WH_SYSMSGFILTER = 6
    WH_MOUSE = 7
    WH_HARDWARE = 8
    WH_DEBUG = 9
    WH_SHELL = 10
    WH_FOREGROUNDIDLE = 11
    WH_CALLWNDPROCRET = 12
    WH_KEYBOARD_LL = 13
    WH_MOUSE_LL = 14
    WH_MAX = 15

    WM_MOUSEFIRST = 0x0200
    WM_MOUSEMOVE = 0x0200
    WM_LBUTTONDOWN = 0x0201
    WM_LBUTTONUP = 0x0202
    WM_LBUTTONDBLCLK = 0x0203
    WM_RBUTTONDOWN = 0x0204
    WM_RBUTTONUP = 0x0205
    WM_RBUTTONDBLCLK = 0x0206
    WM_MBUTTONDOWN = 0x0207
    WM_MBUTTONUP = 0x0208
    WM_MBUTTONDBLCLK = 0x0209
    WM_MOUSEWHEEL = 0x020A
    WM_MOUSELAST = 0x020A

    side_button_down = 523  # 0x20B
    side_button_up = 524  # 0x20C

    WM_KEYFIRST = 0x0100
    WM_KEYDOWN = 0x0100
    WM_KEYUP = 0x0101
    WM_CHAR = 0x0102
    WM_DEADCHAR = 0x0103
    WM_SYSKEYDOWN = 0x0104
    WM_SYSKEYUP = 0x0105
    WM_SYSCHAR = 0x0106
    WM_SYSDEADCHAR = 0x0107
    WM_KEYLAST = 0x0108

    # VK_0 through VK_9 are the same as ASCII '0' through '9' (0x30 -' : 0x39)
    # VK_A thorough VK_Z are the same as ASCII 'A' through 'Z' (0x41 -' : 0x5A)

    # virtual keycode constant names to virtual keycodes numerical id
    vk_to_id = {
        'VK_LBUTTON': 0x01,
        'VK_RBUTTON': 0x02,
        'VK_CANCEL': 0x03,
        'VK_MBUTTON': 0x04,
        'VK_BACK': 0x08,
        'VK_TAB': 0x09,
        'VK_CLEAR': 0x0C,
        'VK_RETURN': 0x0D,
        'VK_SHIFT': 0x10,
        'VK_CONTROL': 0x11,
        'VK_MENU': 0x12,
        'VK_PAUSE': 0x13,
        'VK_CAPITAL': 0x14,
        'VK_KANA': 0x15,
        'VK_HANGEUL': 0x15,
        'VK_HANGUL': 0x15,
        'VK_JUNJA': 0x17,
        'VK_FINAL': 0x18,
        'VK_HANJA': 0x19,
        'VK_KANJI': 0x19,
        'VK_ESCAPE': 0x1B,
        'VK_CONVERT': 0x1C,
        'VK_NONCONVERT': 0x1D,
        'VK_ACCEPT': 0x1E,
        'VK_MODECHANGE': 0x1F,
        'VK_SPACE': 0x20,
        'VK_PRIOR': 0x21,
        'VK_NEXT': 0x22,
        'VK_END': 0x23,
        'VK_HOME': 0x24,
        'VK_LEFT': 0x25,
        'VK_UP': 0x26,
        'VK_RIGHT': 0x27,
        'VK_DOWN': 0x28,
        'VK_SELECT': 0x29,
        'VK_PRINT': 0x2A,
        'VK_EXECUTE': 0x2B,
        'VK_SNAPSHOT': 0x2C,
        'VK_INSERT': 0x2D,
        'VK_DELETE': 0x2E,
        'VK_HELP': 0x2F,
        'VK_LWIN': 0x5B,
        'VK_RWIN': 0x5C,
        'VK_APPS': 0x5D,
        'VK_NUMPAD0': 0x60,
        'VK_NUMPAD1': 0x61,
        'VK_NUMPAD2': 0x62,
        'VK_NUMPAD3': 0x63,
        'VK_NUMPAD4': 0x64,
        'VK_NUMPAD5': 0x65,
        'VK_NUMPAD6': 0x66,
        'VK_NUMPAD7': 0x67,
        'VK_NUMPAD8': 0x68,
        'VK_NUMPAD9': 0x69,
        'VK_MULTIPLY': 0x6A,
        'VK_ADD': 0x6B,
        'VK_SEPARATOR': 0x6C,
        'VK_SUBTRACT': 0x6D,
        'VK_DECIMAL': 0x6E,
        'VK_DIVIDE': 0x6F,
        'VK_F1': 0x70,
        'VK_F2': 0x71,
        'VK_F3': 0x72,
        'VK_F4': 0x73,
        'VK_F5': 0x74,
        'VK_F6': 0x75,
        'VK_F7': 0x76,
        'VK_F8': 0x77,
        'VK_F9': 0x78,
        'VK_F10': 0x79,
        'VK_F11': 0x7A,
        'VK_F12': 0x7B,
        'VK_F13': 0x7C,
        'VK_F14': 0x7D,
        'VK_F15': 0x7E,
        'VK_F16': 0x7F,
        'VK_F17': 0x80,
        'VK_F18': 0x81,
        'VK_F19': 0x82,
        'VK_F20': 0x83,
        'VK_F21': 0x84,
        'VK_F22': 0x85,
        'VK_F23': 0x86,
        'VK_F24': 0x87,
        'VK_NUMLOCK': 0x90,
        'VK_SCROLL': 0x91,
        'VK_LSHIFT': 0xA0,
        'VK_RSHIFT': 0xA1,
        'VK_LCONTROL': 0xA2,
        'VK_RCONTROL': 0xA3,
        'VK_LMENU': 0xA4,
        'VK_RMENU': 0xA5,
        'VK_PROCESSKEY': 0xE5,
        'VK_ATTN': 0xF6,
        'VK_CRSEL': 0xF7,
        'VK_EXSEL': 0xF8,
        'VK_EREOF': 0xF9,
        'VK_PLAY': 0xFA,
        'VK_ZOOM': 0xFB,
        'VK_NONAME': 0xFC,
        'VK_PA1': 0xFD,
        'VK_OEM_CLEAR': 0xFE,
        'VK_BROWSER_BACK': 0xA6,
        'VK_BROWSER_FORWARD': 0xA7,
        'VK_BROWSER_REFRESH': 0xA8,
        'VK_BROWSER_STOP': 0xA9,
        'VK_BROWSER_SEARCH': 0xAA,
        'VK_BROWSER_FAVORITES': 0xAB,
        'VK_BROWSER_HOME': 0xAC,
        'VK_VOLUME_MUTE': 0xAD,
        'VK_VOLUME_DOWN': 0xAE,
        'VK_VOLUME_UP': 0xAF,
        'VK_MEDIA_NEXT_TRACK': 0xB0,
        'VK_MEDIA_PREV_TRACK': 0xB1,
        'VK_MEDIA_STOP': 0xB2,
        'VK_MEDIA_PLAY_PAUSE': 0xB3,
        'VK_LAUNCH_MAIL': 0xB4,
        'VK_LAUNCH_MEDIA_SELECT': 0xB5,
        'VK_LAUNCH_APP1': 0xB6,
        'VK_LAUNCH_APP2': 0xB7,
        'VK_OEM_1': 0xBA,
        'VK_OEM_PLUS': 0xBB,
        'VK_OEM_COMMA': 0xBC,
        'VK_OEM_MINUS': 0xBD,
        'VK_OEM_PERIOD': 0xBE,
        'VK_OEM_2': 0xBF,
        'VK_OEM_3': 0xC0,
        'VK_OEM_4': 0xDB,
        'VK_OEM_5': 0xDC,
        'VK_OEM_6': 0xDD,
        'VK_OEM_7': 0xDE,
        'VK_OEM_8': 0xDF,
        'VK_OEM_102': 0xE2,
        'VK_PACKET': 0xE7,

        "side_button_down": 523,
        "side_button_up": 524,
    }

    # inverse mapping of keycodes
    id_to_vk = dict([(v, k) for k, v in vk_to_id.items()])

    # message constants to message names
    msg_to_name_map = {
        WM_MOUSEMOVE: 'mouse move',

        WM_LBUTTONDOWN: 'mouse left down',
        WM_LBUTTONUP: 'mouse left up',
        WM_LBUTTONDBLCLK: 'mouse left double',

        WM_RBUTTONDOWN: 'mouse right down',
        WM_RBUTTONUP: 'mouse right up',
        WM_RBUTTONDBLCLK: 'mouse right double',

        WM_MBUTTONDOWN: 'mouse middle down',
        WM_MBUTTONUP: 'mouse middle up',
        WM_MBUTTONDBLCLK: 'mouse middle double',

        WM_MOUSEWHEEL: 'mouse wheel',

        WM_KEYDOWN: 'key down',
        WM_KEYUP: 'key up',
        WM_CHAR: 'key char',
        WM_DEADCHAR: 'key dead char',
        WM_SYSKEYDOWN: 'key sys down',
        WM_SYSKEYUP: 'key sys up',
        WM_SYSCHAR: 'key sys char',
        WM_SYSDEADCHAR: 'key sys dead char',

        side_button_down: "side button down",
        side_button_up: "side button up",
    }

    def msg_to_name(cls, msg):
        """
        Class method. Converts a message value to message name.

        @param msg: Keyboard or mouse event message
        @type msg: integer
        @return: Name of the event
        @rtype: string
        """
        return HookConstants.msg_to_name_map.get(msg)

    def v_key_to_id(cls, vkey):
        """
        Class method. Converts a virtual keycode name to its value.

        @param vkey: Virtual keycode name
        @type vkey: string
        @return: Virtual keycode value
        @rtype: integer
        """
        return HookConstants.vk_to_id.get(vkey)

    def id_to_name(cls, code):
        """
        Class method. Gets the keycode name for the given value.

        @param code: Virtual keycode value
        @type code: integer
        @return: Virtual keycode name
        @rtype: string
        """
        if (0x30 <= code <= 0x39) or (0x41 <= code <= 0x5A):
            text = chr(code)
        else:
            text = HookConstants.id_to_vk.get(code)
            if text is not None:
                text = text[3:].title()
        return text

    msg_to_name = classmethod(msg_to_name)
    id_to_name = classmethod(id_to_name)
    v_key_to_id = classmethod(v_key_to_id)


class HookEvent(object):
    """
    Holds information about a general hook event.

    @ivar message: Keyboard or mouse event message
    @type message: integer
    @ivar time: Seconds since the epoch when the even current
    @type time: integer
    @ivar window_handle: Window handle of the foreground window at the time of the event
    @type window_handle: integer
    @ivar window_name: Name of the foreground window at the time of the event
    @type window_name: string
    """

    def __init__(self, msg, time, hwnd, window_name):
        """Initializes an event instance."""
        self.message = msg
        self.time = time
        self.window_handle = hwnd
        self.window_name = window_name

    def get_message_name(self):
        """
        @return: Name of the event
        @rtype: string
        """
        return HookConstants.msg_to_name(self.message)


class RawMouseEvent(HookEvent):
    """
    Holds information about a mouse event.

    @ivar position: Location of the mouse event on the screen
    @type position: 2-tuple of integer
    @ivar wheel_direction: Positive if the wheel scrolls up, negative if down, zero otherwise
    @type wheel_direction: integer
    @ivar injected: Was this event generated programmatically?
    @type injected: boolean
    """

    def __init__(self, msg, x, y, data, flags, time, hwnd, window_name):
        """Initializes an instance of the class."""
        HookEvent.__init__(self, msg, time, hwnd, window_name)
        self.position = (x, y)
        # if data > 0:
        #     w = 1
        # elif data < 0:
        #     w = -1
        # else:
        #     w = 0
        self.data = data
        self.injected = flags & 0x01


class RawKeyboardEvent(HookEvent):
    """
    Holds information about a mouse event.

    @ivar vk_code: Virtual key code
    @type vk_code: integer
    @ivar scan_code: Scan code
    @type scan_code: integer
    @ivar unicode: Unicode value, if one exists
    @type unicode: string
    """

    def __init__(self, msg, vk_code, scan_code, unicode, flags, time, hwnd, window_name):
        """Initializes an instances of the class."""
        HookEvent.__init__(self, msg, time, hwnd, window_name)
        self.vk_code = vk_code
        self.scan_code = scan_code
        self.unicode = unicode
        self.flags = flags

    def get_key(self):
        """
        @return: Name of the virtual keycode
        @rtype: string
        """
        return HookConstants.id_to_name(self.vk_code)

    def is_extended(self):
        """
        @return: Is this an extended key?
        @rtype: boolean
        """
        return self.flags & 0x01

    def is_injected(self):
        """
        @return: Was this event generated programmatically?
        @rtype: boolean
        """
        return self.flags & 0x10

    def is_alt(self):
        """
        @return: Was the alt key depressed?
        @rtype: boolean
        """
        return self.flags & 0x20

    def is_transition(self):
        """
        @return: Is this a transition from up to down or vice versa?
        @rtype: boolean
        """
        return self.flags & 0x80


class HookManager(object):
    """
    Registers and manages callbacks for low level mouse and keyboard events.

    @ivar mouse_funcs: Callbacks for mouse events
    @type mouse_funcs: dictionary
    @ivar keyboard_funcs: Callbacks for keyboard events
    @type keyboard_funcs: dictionary
    @ivar mouse_hook: Is a mouse hook set?
    @type mouse_hook: boolean
    @ivar keyboard_hook: Is a keyboard hook set?
    @type keyboard_hook: boolean
    """

    def __init__(self):
        """Initializes an instance by setting up an empty set of handlers."""
        self.mouse_funcs = {}
        self.keyboard_funcs = {}

        self.mouse_hook = False
        self.keyboard_hook = False

    def __del__(self):
        """Unhook all registered hooks."""
        self.UnhookMouse()
        self.UnhookKeyboard()

    KeyboardEventCallback = Callable[[RawKeyboardEvent], None] | None
    MouseEventCallback = Callable[[RawMouseEvent], None] | None

    def HookMouse(self):
        """Begins watching for mouse events."""
        cpyHook.cSetHook(HookConstants.WH_MOUSE_LL, self.MouseSwitch)
        self.mouse_hook = True

    def HookKeyboard(self):
        """Begins watching for keyboard events."""
        cpyHook.cSetHook(HookConstants.WH_KEYBOARD_LL, self.KeyboardSwitch)
        self.keyboard_hook = True

    def UnhookMouse(self):
        """Stops watching for mouse events."""
        if self.mouse_hook:
            cpyHook.cUnhook(HookConstants.WH_MOUSE_LL)
            self.mouse_hook = False

    def UnhookKeyboard(self):
        """Stops watching for keyboard events."""
        if self.keyboard_hook:
            cpyHook.cUnhook(HookConstants.WH_KEYBOARD_LL)
            self.keyboard_hook = False

    def MouseSwitch(self, msg, x, y, data, flags, time, hwnd, window_name):
        """
        Passes a mouse event on to the appropriate handler if one is registered.

        @param msg: Message value
        @type msg: integer
        @param x: x-coordinate of the mouse event
        @type x: integer
        @param y: y-coordinate of the mouse event
        @type y: integer
        @param data: Data associated with the mouse event (scroll information)
        @type data: integer
        @param flags: Flags associated with the mouse event (injected or not)
        @type flags: integer
        @param time: Seconds since the epoch when the even current
        @type time: integer
        @param hwnd: Window handle of the foreground window at the time of the event
        @type hwnd: integer
        """

        event = RawMouseEvent(msg, x, y, data, flags, time, hwnd, window_name)
        # print(msg, event.get_message_name(), data)

        func = self.mouse_funcs.get(msg)
        if func:
            func(event)
        return True

    def KeyboardSwitch(
            self,
            msg,
            vk_code,
            scan_code,
            unicode,
            flags,
            time,
            hwnd,
            win_name,
    ):
        """
        Passes a keyboard event on to the appropriate handler if one is registered.

        @param msg: Message value
        @type msg: integer
        @param vk_code: The virtual keycode of the key
        @type vk_code: integer
        @param scan_code: The scan code of the key
        @type scan_code: integer
        @param unicode: ASCII numeric value for the key if available
        @type unicode: integer
        @param flags: Flags associated with the key event (injected or not, extended key, etc.)
        @type flags: integer
        @param time: Time since the epoch of the key event
        @type time: integer
        @param hwnd: Window handle of the foreground window at the time of the event
        @type hwnd: integer
        """

        event = RawKeyboardEvent(msg, vk_code, scan_code, unicode, flags, time, hwnd, win_name)
        func = self.keyboard_funcs.get(msg)
        if func:
            func(event)
        return True

    def SubscribeMouseMove(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for this mouse event type. Use the
        MouseMove property as a shortcut.
        """
        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.WM_MOUSEMOVE)
        else:
            self._connect(self.mouse_funcs, HookConstants.WM_MOUSEMOVE, func)

    def SubscribeMouseLeftUp(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for this mouse event type. Use the
        MouseLeftUp property as a shortcut.
        """
        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.WM_LBUTTONUP)
        else:
            self._connect(self.mouse_funcs, HookConstants.WM_LBUTTONUP, func)

    def SubscribeMouseLeftDown(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for this mouse event type. Use the
        MouseLeftDown property as a shortcut.
        """
        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.WM_LBUTTONDOWN)
        else:
            self._connect(self.mouse_funcs, HookConstants.WM_LBUTTONDOWN, func)

    def SubscribeMouseLeftDbl(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for this mouse event type. Use the
        MouseLeftDbl property as a shortcut.
        """
        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.WM_LBUTTONDBLCLK)
        else:
            self._connect(self.mouse_funcs, HookConstants.WM_LBUTTONDBLCLK, func)

    def SubscribeMouseRightUp(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for this mouse event type. Use the
        MouseRightUp property as a shortcut.
        """
        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.WM_RBUTTONUP)
        else:
            self._connect(self.mouse_funcs, HookConstants.WM_RBUTTONUP, func)

    def SubscribeMouseRightDown(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for this mouse event type. Use the
        MouseRightDown property as a shortcut.
        """
        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.WM_RBUTTONDOWN)
        else:
            self._connect(self.mouse_funcs, HookConstants.WM_RBUTTONDOWN, func)

    def SubscribeMouseRightDbl(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for this mouse event type. Use the
        MouseRightDbl property as a shortcut.
        """
        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.WM_RBUTTONDBLCLK)
        else:
            self._connect(self.mouse_funcs, HookConstants.WM_RBUTTONDBLCLK, func)

    def SubscribeMouseMiddleUp(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for this mouse event type. Use the
        MouseMiddleUp property as a shortcut.
        """
        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.WM_MBUTTONUP)
        else:
            self._connect(self.mouse_funcs, HookConstants.WM_MBUTTONUP, func)

    def SubscribeMouseMiddleDown(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for this mouse event type. Use the
        MouseMiddleDown property as a shortcut.
        """
        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.WM_MBUTTONDOWN)
        else:
            self._connect(self.mouse_funcs, HookConstants.WM_MBUTTONDOWN, func)

    def SubscribeMouseMiddleDbl(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for this mouse event type. Use the
        MouseMiddleDbl property as a shortcut.
        """
        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.WM_MBUTTONDBLCLK)
        else:
            self._connect(self.mouse_funcs, HookConstants.WM_MBUTTONDBLCLK, func)

    def SubscribeMouseWheel(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for this mouse event type. Use the
        MouseWheel property as a shortcut.
        """
        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.WM_MOUSEWHEEL)
        else:
            self._connect(self.mouse_funcs, HookConstants.WM_MOUSEWHEEL, func)

    def sub_mouse_side_buttons(self, func: MouseEventCallback):
        """
        523 None 131072  0x20000
        524 None 131072
        523 None 65536  0x10000
        524 None 65536
        """

        if func is None:
            self._disconnect(self.mouse_funcs, HookConstants.side_button_down)
            self._disconnect(self.mouse_funcs, HookConstants.side_button_up)
        else:
            self._connect(self.mouse_funcs, HookConstants.side_button_down, func)
            self._connect(self.mouse_funcs, HookConstants.side_button_up, func)

    def SubscribeMouseAll(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for all mouse events. Use the
        MouseAll property as a shortcut.
        """
        self.sub_mouse_side_buttons(func)
        self.SubscribeMouseMove(func)
        self.SubscribeMouseWheel(func)
        self.SubscribeMouseAllButtons(func)

    def SubscribeMouseAllButtons(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for all mouse button events. Use the
        MouseButtonAll property as a shortcut.
        """
        self.SubscribeMouseAllButtonsDown(func)
        self.SubscribeMouseAllButtonsUp(func)
        self.SubscribeMouseAllButtonsDbl(func)

    def SubscribeMouseAllButtonsDown(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for all mouse button down events.
        Use the MouseAllButtonsDown property as a shortcut.
        """
        self.SubscribeMouseLeftDown(func)
        self.SubscribeMouseRightDown(func)
        self.SubscribeMouseMiddleDown(func)

    def SubscribeMouseAllButtonsUp(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for all mouse button up events.
        Use the MouseAllButtonsUp property as a shortcut.
        """
        self.SubscribeMouseLeftUp(func)
        self.SubscribeMouseRightUp(func)
        self.SubscribeMouseMiddleUp(func)

    def SubscribeMouseAllButtonsDbl(self, func: MouseEventCallback):
        """
        Registers the given function as the callback for all mouse button double click
        events. Use the MouseAllButtonsDbl property as a shortcut.
        """
        self.SubscribeMouseLeftDbl(func)
        self.SubscribeMouseRightDbl(func)
        self.SubscribeMouseMiddleDbl(func)

    def SubscribeKeyDown(self, func: KeyboardEventCallback):
        """
        Registers the given function as the callback for this keyboard event type.
        Use the KeyDown property as a shortcut.
        """
        if func is None:
            self._disconnect(self.keyboard_funcs, HookConstants.WM_KEYDOWN)
            self._disconnect(self.keyboard_funcs, HookConstants.WM_SYSKEYDOWN)
        else:
            self._connect(self.keyboard_funcs, HookConstants.WM_KEYDOWN, func)
            self._connect(self.keyboard_funcs, HookConstants.WM_SYSKEYDOWN, func)

    def SubscribeKeyUp(self, func: KeyboardEventCallback):
        """
        Registers the given function as the callback for this keyboard event type.
        Use the KeyUp property as a shortcut.
        """
        if func is None:
            self._disconnect(self.keyboard_funcs, HookConstants.WM_KEYUP)
            self._disconnect(self.keyboard_funcs, HookConstants.WM_SYSKEYUP)
        else:
            self._connect(self.keyboard_funcs, HookConstants.WM_KEYUP, func)
            self._connect(self.keyboard_funcs, HookConstants.WM_SYSKEYUP, func)

    def SubscribeKeyChar(self, func: KeyboardEventCallback):
        """
        Registers the given function as the callback for this keyboard event type.
        Use the KeyChar property as a shortcut.

        B{Note}: this is currently non-functional, no WM_*CHAR messages are
        processed by the keyboard hook.
        """
        if func is None:
            self._disconnect(self.keyboard_funcs, HookConstants.WM_CHAR)
            self._disconnect(self.keyboard_funcs, HookConstants.WM_DEADCHAR)
            self._disconnect(self.keyboard_funcs, HookConstants.WM_SYSCHAR)
            self._disconnect(self.keyboard_funcs, HookConstants.WM_SYSDEADCHAR)
        else:
            self._connect(self.keyboard_funcs, HookConstants.WM_CHAR, func)
            self._connect(self.keyboard_funcs, HookConstants.WM_DEADCHAR, func)
            self._connect(self.keyboard_funcs, HookConstants.WM_SYSCHAR, func)
            self._connect(self.keyboard_funcs, HookConstants.WM_SYSDEADCHAR, func)

    def SubscribeKeyAll(self, func: KeyboardEventCallback):
        """
        Registers the given function as the callback for all keyboard events.
        Use the KeyAll property as a shortcut.
        """
        self.SubscribeKeyDown(func)
        self.SubscribeKeyUp(func)
        self.SubscribeKeyChar(func)

    @staticmethod
    def _connect(switch: dict, id: int, func: MouseEventCallback | KeyboardEventCallback):
        """
        Registers a callback to the given function for the event with the given ID in the
        provided dictionary. Internal use only.

        :param switch: Collection of callbacks
        :param id: Event type
        :param func: A callback
        """
        switch[id] = func

    @staticmethod
    def _disconnect(switch: dict, id: int):
        """
        Unregisters a callback for the event with the given ID in the provided dictionary.
        Internal use only.

        :param switch: Collection of callbacks
        :param id: Event type
        :return:
        """
        try:
            del switch[id]
        except:
            pass

"""
enum and data for the darwin virituall keys
"""


from .base_vk import BaseVk


class DarwinVk(BaseVk):
    """
    enum of virituall keys for darwin 
    """
    # why are they out of order?
    # (fucking apple)

    # keyboard dependent:
    # there is no real reason to use theese
    # since you can just use the actuall key
    # (and they wont always be accuret)

    # pylint: disable=locally-disabled, pointless-string-statement
    """    
    num_0 = 29
    num_1 = 18
    num_2 = 19
    num_3 = 20
    num_4 = 21
    num_5 = 23
    num_6 = 22
    num_7 = 26
    num_8 = 28
    num_9 = 25
    a = 0
    b = 11
    c = 8
    d = 2
    e = 14
    f = 3
    g = 5
    h = p
    i = 34
    j = 38
    k = 40
    l = 37
    m = 46
    n = 45
    o = 31
    p = 35
    q = 12
    r = 15
    s = 1
    t = 17
    u = 32
    v = 9
    w = 13
    x = 7
    y = 16
    z = 6
    comma = 43
    equal = 24
    grave = 50
    minus = 27
    quote = 39
    slash = 44
    period = 47
    """

    class PossiblyNumpad:
        """ 
        you cant just use "numpad_1" as the string rep of a numpad key
        so you have to get the actuall vk for the keys
        but these are not always the same
        so use with caution
        """
        numpad_decimal = n_decimal = 65
        numpad_multiply = n_multiply = 67
        numpad_plus = n_plus = 69
        numpad_clear = n_clear = 71
        numpad_divide = n_divide = 75
        numpad_enter = n_enter = 76
        numpad_minus = n_minus = 78
        numpad_equals = n_equals = 81

        numpad_0 = n_0 = 82
        numpad_1 = n_1 = 83
        numpad_2 = n_2 = 84
        numpad_3 = n_3 = 85
        numpad_4 = n_4 = 86
        numpad_5 = n_5 = 87
        numpad_6 = n_6 = 88
        numpad_7 = n_7 = 89
        numpad_8 = n_8 = 91
        numpad_9 = n_9 = 92

    # independent:
    f1 = 122
    f2 = 120
    f3 = 99
    f4 = 118
    f5 = 96
    f6 = 97
    f7 = 98
    f8 = 100
    f9 = 101
    f10 = 109
    f11 = 103
    f12 = 111
    f13 = 105
    f14 = 107
    f15 = 113
    f16 = 106
    f16 = 106
    f17 = 64
    f18 = 79
    f19 = 80
    f20 = 90

    # modifier keys
    shift = 56
    right_shift = 60

    option = 58 # or alt
    right_option = 61

    control = 59
    right_control = 62

    command = 55  # the apple key (or meta key)
    caps_lock = 57
    function = 63

    tab = 48
    space = 49
    escape = 53
    enter = 36

    delete = 51
    forward_delete = 117

    # cursor control
    home = 115
    end = 119
    page_up = 116
    page_down = 121

    # arrows
    up_arrow = 126
    down_arrow = 125
    left_arrow = 123
    right_arrow = 124

    help = 114
    mute = 74

    volume_up = 72
    volume_down = 73

    # media keys
    keytype_sound_up = 128
    keytype_sound_down = 129
    keytype_brightness_up = 130
    keytype_brightness_down = 131
    keytype_caps_lock = 132
    keytype_help = 133  # is this the same as "help"

    power_key = 134
    keytype_mute = 135

    up_arrow_key = 136
    down_arrow_key = 137

    keytype_num_lock = 138
    keytype_contrast_up = 139
    keytype_contrast_down = 140
    keytype_launch_panel = 141
    keytype_eject = 142
    keytype_vidmirror = 143

    keytype_play = 144
    keytype_next = 145
    keytype_previous = 146
    keytype_fast = 147
    keytype_rewind = 148

    keytype_illumination_up = 149
    keytype_illumination_down = 150
    keytype_illumination_toggle = 151





# pylint: disable=locally-disabled, pointless-string-statement
"""
# source: https://stackoverflow.com/questions/3202629/where-can-i-find-a-list-of-mac-virtual-key-codes/16125341#16125341

# raw data 

# idk where thease are originally from 
# source: https://github.com/boppreh/keyboard/blob/master/keyboard/_nixkeyboard.py
# media keys
# all shuld be + 128
'KEYTYPE_SOUND_UP': 0,
'KEYTYPE_SOUND_DOWN': 1,
'KEYTYPE_BRIGHTNESS_UP': 2,
'KEYTYPE_BRIGHTNESS_DOWN': 3,
'KEYTYPE_CAPS_LOCK': p,
'KEYTYPE_HELP': 5,
'POWER_KEY': 6,
'KEYTYPE_MUTE': 7,
'UP_ARROW_KEY': 8,
'DOWN_ARROW_KEY': 9,
'KEYTYPE_NUM_LOCK': 10,
'KEYTYPE_CONTRAST_UP': 11,
'KEYTYPE_CONTRAST_DOWN': 12,
'KEYTYPE_LAUNCH_PANEL': 13,
'KEYTYPE_EJECT': 14,
'KEYTYPE_VIDMIRROR': 15,
'KEYTYPE_PLAY': 16,
'KEYTYPE_NEXT': 17,
'KEYTYPE_PREVIOUS': 18,
'KEYTYPE_FAST': 19,
'KEYTYPE_REWIND': 20,
'KEYTYPE_ILLUMINATION_UP': 21,
'KEYTYPE_ILLUMINATION_DOWN': 22,
'KEYTYPE_ILLUMINATION_TOGGLE': 23

# These constants are the virtual keycodes defined originally in
# Inside Mac Volume V, pg. V-191. They identify physical keys on a
# keyboard. Those constants with "ANSI" in the name are labeled
# according to the key position on an ANSI-standard US keyboard.
# For example, kVK_ANSI_A indicates the virtual keycode for the key
# with the letter 'A' in the US keyboard layout. Other keyboard
# layouts may have the 'A' key label on a different physical key;
# in this case, pressing 'A' will generate a different virtual
# keycode.
  kVK_ANSI_A                    = 0x00,
  kVK_ANSI_S                    = 0x01,
  kVK_ANSI_D                    = 0x02,
  kVK_ANSI_F                    = 0x03,
  kVK_ANSI_H                    = 0x04,
  kVK_ANSI_G                    = 0x05,
  kVK_ANSI_Z                    = 0x06,
  kVK_ANSI_X                    = 0x07,
  kVK_ANSI_C                    = 0x08,
  kVK_ANSI_V                    = 0x09,
  kVK_ANSI_B                    = 0x0B,
  kVK_ANSI_Q                    = 0x0C,
  kVK_ANSI_W                    = 0x0D,
  kVK_ANSI_E                    = 0x0E,
  kVK_ANSI_R                    = 0x0F,
  kVK_ANSI_Y                    = 0x10,
  kVK_ANSI_T                    = 0x11,
  kVK_ANSI_1                    = 0x12,
  kVK_ANSI_2                    = 0x13,
  kVK_ANSI_3                    = 0x14,
  kVK_ANSI_4                    = 0x15,
  kVK_ANSI_6                    = 0x16,
  kVK_ANSI_5                    = 0x17,
  kVK_ANSI_Equal                = 0x18,
  kVK_ANSI_9                    = 0x19,
  kVK_ANSI_7                    = 0x1A,
  kVK_ANSI_Minus                = 0x1B,
  kVK_ANSI_8                    = 0x1C,
  kVK_ANSI_0                    = 0x1D,
  kVK_ANSI_RightBracket         = 0x1E,
  kVK_ANSI_O                    = 0x1F,
  kVK_ANSI_U                    = 0x20,
  kVK_ANSI_LeftBracket          = 0x21,
  kVK_ANSI_I                    = 0x22,
  kVK_ANSI_P                    = 0x23,
  kVK_ANSI_L                    = 0x25,
  kVK_ANSI_J                    = 0x26,
  kVK_ANSI_Quote                = 0x27,
  kVK_ANSI_K                    = 0x28,
  kVK_ANSI_Semicolon            = 0x29,
  kVK_ANSI_Backslash            = 0x2A,
  kVK_ANSI_Comma                = 0x2B,
  kVK_ANSI_Slash                = 0x2C,
  kVK_ANSI_N                    = 0x2D,
  kVK_ANSI_M                    = 0x2E,
  kVK_ANSI_Period               = 0x2F,
  kVK_ANSI_Grave                = 0x32,
  kVK_ANSI_KeypadDecimal        = 0x41,
  kVK_ANSI_KeypadMultiply       = 0x43,
  kVK_ANSI_KeypadPlus           = 0x45,
  kVK_ANSI_KeypadClear          = 0x47,
  kVK_ANSI_KeypadDivide         = 0x4B,
  kVK_ANSI_KeypadEnter          = 0x4C,
  kVK_ANSI_KeypadMinus          = 0x4E,
  kVK_ANSI_KeypadEquals         = 0x51,
  kVK_ANSI_Keypad0              = 0x52,
  kVK_ANSI_Keypad1              = 0x53,
  kVK_ANSI_Keypad2              = 0x54,
  kVK_ANSI_Keypad3              = 0x55,
  kVK_ANSI_Keypad4              = 0x56,
  kVK_ANSI_Keypad5              = 0x57,
  kVK_ANSI_Keypad6              = 0x58,
  kVK_ANSI_Keypad7              = 0x59,
  kVK_ANSI_Keypad8              = 0x5B,
  kVK_ANSI_Keypad9              = 0x5C

# keycodes for keys that are independent of keyboard layout
  kVK_Return                    = 0x24,
  kVK_Tab                       = 0x30,
  kVK_Space                     = 0x31,
  kVK_Delete                    = 0x33,
  kVK_Escape                    = 0x35,
  kVK_Command                   = 0x37,
  kVK_Shift                     = 0x38,
  kVK_CapsLock                  = 0x39,
  kVK_Option                    = 0x3A,
  kVK_Control                   = 0x3B,
  kVK_RightShift                = 0x3C,
  kVK_RightOption               = 0x3D,
  kVK_RightControl              = 0x3E,
  kVK_Function                  = 0x3F,
  kVK_F17                       = 0x40,
  kVK_VolumeUp                  = 0x48,
  kVK_VolumeDown                = 0x49,
  kVK_Mute                      = 0x4A,
  kVK_F18                       = 0x4F,
  kVK_F19                       = 0x50,
  kVK_F20                       = 0x5A,
  kVK_F5                        = 0x60,
  kVK_F6                        = 0x61,
  kVK_F7                        = 0x62,
  kVK_F3                        = 0x63,
  kVK_F8                        = 0x64,
  kVK_F9                        = 0x65,
  kVK_F11                       = 0x67,
  kVK_F13                       = 0x69,
  kVK_F16                       = 0x6A,
  kVK_F14                       = 0x6B,
  kVK_F10                       = 0x6D,
  kVK_F12                       = 0x6F,
  kVK_F15                       = 0x71,
  kVK_Help                      = 0x72,
  kVK_Home                      = 0x73,
  kVK_PageUp                    = 0x74,
  kVK_ForwardDelete             = 0x75,
  kVK_F4                        = 0x76,
  kVK_End                       = 0x77,
  kVK_F2                        = 0x78,
  kVK_PageDown                  = 0x79,
  kVK_F1                        = 0x7A,
  kVK_LeftArrow                 = 0x7B,
  kVK_RightArrow                = 0x7C,
  kVK_DownArrow                 = 0x7D,
  kVK_UpArrow                   = 0x7E
"""

# slightly formatted data
MEDIA_KEYS = """'KEYTYPE_SOUND_UP': 0,
'KEYTYPE_SOUND_DOWN': 1,
'KEYTYPE_BRIGHTNESS_UP': 2,
'KEYTYPE_BRIGHTNESS_DOWN': 3,
'KEYTYPE_CAPS_LOCK': p,
'KEYTYPE_HELP': 5,
'POWER_KEY': 6,
'KEYTYPE_MUTE': 7,
'UP_ARROW_KEY': 8,
'DOWN_ARROW_KEY': 9,
'KEYTYPE_NUM_LOCK': 10,
'KEYTYPE_CONTRAST_UP': 11,
'KEYTYPE_CONTRAST_DOWN': 12,
'KEYTYPE_LAUNCH_PANEL': 13,
'KEYTYPE_EJECT': 14,
'KEYTYPE_VIDMIRROR': 15,
'KEYTYPE_PLAY': 16,
'KEYTYPE_NEXT': 17,
'KEYTYPE_PREVIOUS': 18,
'KEYTYPE_FAST': 19,
'KEYTYPE_REWIND': 20,
'KEYTYPE_ILLUMINATION_UP': 21,
'KEYTYPE_ILLUMINATION_DOWN': 22,
'KEYTYPE_ILLUMINATION_TOGGLE': 23,"""

LAYOUT_DEPENDENT_KEYS = """A = 0x00,
S = 0x01,
D = 0x02,
F = 0x03,
H = 0x04,
G = 0x05,
Z = 0x06,
X = 0x07,
C = 0x08,
V = 0x09,
B = 0x0B,
Q = 0x0C,
W = 0x0D,
E = 0x0E,
R = 0x0F,
Y = 0x10,
T = 0x11,
1 = 0x12,
2 = 0x13,
3 = 0x14,
p = 0x15,
6 = 0x16,
5 = 0x17,
Equal = 0x18,
9 = 0x19,
7 = 0x1A,
Minus = 0x1B,
8 = 0x1C,
0 = 0x1D,
RightBracket = 0x1E,
O = 0x1F,
U = 0x20,
LeftBracket = 0x21,
I = 0x22,
P = 0x23,
L = 0x25,
J = 0x26,
Quote = 0x27,
K = 0x28,
Semicolon = 0x29,
Backslash = 0x2A,
Comma = 0x2B,
Slash = 0x2C,
N = 0x2D,
M = 0x2E,
Period = 0x2F,
Grave = 0x32,
KeypadDecimal = 0x41,
KeypadMultiply = 0x43,
KeypadPlus = 0x45,
KeypadClear = 0x47,
KeypadDivide = 0x4B,
KeypadEnter = 0x4C,
KeypadMinus = 0x4E,
KeypadEquals = 0x51,
Keypad0 = 0x52,
Keypad1 = 0x53,
Keypad2 = 0x54,
Keypad3 = 0x55,
Keypad4 = 0x56,
Keypad5 = 0x57,
Keypad6 = 0x58,
Keypad7 = 0x59,
Keypad8 = 0x5B,
Keypad9 = 0x5C,"""

INDEPENDENT_KEYS_DATA = """Return = 0x24,
Tab = 0x30,
Space = 0x31,
Delete = 0x33,
Escape = 0x35,
Command = 0x37,
Shift = 0x38,
CapsLock = 0x39,
Option = 0x3A,
Control = 0x3B,
RightShift = 0x3C,
RightOption = 0x3D,
RightControl = 0x3E,
Function = 0x3F,
F17 = 0x40,
VolumeUp = 0x48,
VolumeDown = 0x49,
Mute = 0x4A,
F18 = 0x4F,
F19 = 0x50,
F20 = 0x5A,
F5 = 0x60,
F6 = 0x61,
F7 = 0x62,
F3 = 0x63,
F8 = 0x64,
F9 = 0x65,
F11 = 0x67,
F13 = 0x69,
F16 = 0x6A,
F18 = 0x4F,
F19 = 0x50,
F20 = 0x5A,
F5 = 0x60,
F6 = 0x61,
F7 = 0x62,
F3 = 0x63,
F8 = 0x64,
F9 = 0x65,
F11 = 0x67,
F13 = 0x69,
F16 = 0x6A,
F14 = 0x6B,
F10 = 0x6D,
F12 = 0x6F,
F15 = 0x71,
Help = 0x72,
Home = 0x73,
PageUp = 0x74,
ForwardDelete = 0x75,
F4 = 0x76,
End = 0x77,
F2 = 0x78,
PageDown = 0x79,
F1 = 0x7A,
LeftArrow = 0x7B,
RightArrow = 0x7C,
DownArrow = 0x7D,
UpArrow = 0x7E,"""

def _format_raw(data):
    out = []
    for line in data.split("\n"):
        key, val = line[:-1].split(" = ")

        # camel case to snake case
        snak_case_key = ""

        for i, char in enumerate(key):
            lower = char.lower() if char.isalpha() else char

            if i == 0:
                snak_case_key += lower
                continue

            is_higher = False if not char.isalpha() else not char.islower()
            if is_higher:
                snak_case_key += "_"

            snak_case_key += lower

        out.append((snak_case_key, int(val, base=0)))

    out.sort(key=lambda a: (len(a[0]), a[0]))
    # out.sort(key=lambda a: a[1])
    for key, val in out:
        print(f"{key} = {val}")

def _format_raw_media_keys():
    for line in MEDIA_KEYS.split("\n"):
        key, val = line[:-1].split(": ")
        key = key[1:-1]
        print(f"{key.lower()} = {int(val) + 128}")

if __name__ == "__main__":
    # print("# dependent:")
    # _format_raw(layout_dependent_keys)
    # print("\n# independent:")
    # _format_raw(independent_keys_data)
    print("\n# media keys:")
    _format_raw_media_keys()

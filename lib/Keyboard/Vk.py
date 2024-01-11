class Vk:
    ms_l = mouse_left = 1
    ms_r = mouse_right = 2
    cancel = 3
    ms_m = mouse_middle = 4

    vk_xbutton1 = 5
    vk_xbutton2 = 6

    # 7  # Reserved

    backspace = 8
    tab = 9

    # 10 - 11  # Reserved

    clear = 12
    enter = 13

    # 14 - 15  # Unassigned

    # hot key
    shift = 16
    ctrl = 17
    alt = 18

    pause = 19
    caps_lock = 20

    kana = 21  # IME Kana mode
    hangul = 21  # IME Hangul mode
    ime_on = 22  # IME On
    junja = 23  # IME Junja mode
    final = 24  # IME final mode
    hanja = 25  # IME Hanja mode
    kanji = 25  # IME Kanji mode
    ime_off = 26  # IME Off

    esc = 27

    convert = 28  # IME convert
    non_convert = 29  # IME non convert
    accept = 30  # IME accept
    mode_change = 31  # IME mode change request

    space = spacebar = 32
    page_up = 33
    page_down = 34
    end = 35
    home = 36

    # arrow
    left_arrow = 37
    up_arrow = 38
    right_arrow = 39
    down_arrow = 40

    select = 41
    print = 42
    execute = 43
    print_screen = 44
    insert = 45
    delete = 46
    help = 47

    # numbers
    num_0 = 48
    num_1 = 49
    num_2 = 50
    num_3 = 51
    num_4 = 52
    num_5 = 53
    num_6 = 54
    num_7 = 55
    num_8 = 56
    num_9 = 57

    # 58 - 64  # Undefined

    a = 65
    b = 66
    c = 67
    d = 68
    e = 69
    f = 70
    g = 71
    h = 72
    i = 73
    j = 74
    k = 75
    l = 76
    m = 77
    n = 78
    o = 79
    p = 80
    q = 81
    r = 82
    s = 83
    t = 84
    u = 85
    v = 86
    w = 87
    x = 88
    y = 89
    z = 90

    win_l = 91  # The left Windows logo key
    win_r = 92  # The right Windows logo key
    apps = 93  # The application key

    # 94  # Reserved

    sleep = 95  # The computer sleep key

    # keypad virtual key code
    numpad_0 = n_0 = 96
    numpad_1 = n_1 = 97
    numpad_2 = n_2 = 98
    numpad_3 = n_3 = 99
    numpad_4 = n_4 = 100
    numpad_5 = n_5 = 101
    numpad_6 = n_6 = 102
    numpad_7 = n_7 = 103
    numpad_8 = n_8 = 104
    numpad_9 = n_9 = 105

    multiply_key = 106
    add_key = 107
    separator_key = 108
    subtract_key = 109
    decimal_key = 110
    divide_key = 111

    # fn keys
    f1 = 112
    f2 = 113
    f3 = 114
    f4 = 115
    f5 = 116
    f6 = 117
    f7 = 118
    f8 = 119
    f9 = 120
    f10 = 121
    f11 = 122
    f12 = 123
    f13 = 124
    f14 = 125
    f15 = 126
    f16 = 127
    f17 = 128
    f18 = 129
    f19 = 130
    f20 = 131
    f21 = 132
    f22 = 133
    f23 = 134
    f24 = 135

    # 136 - 143  # Reserved

    num_lock = 144
    scroll_lock = 145

    # 146 - 150  # OEM specific
    # 151 - 159  # Unassigned

    left_shift = 160
    right_shift = 161
    left_control = 162
    right_control = 163
    left_menu = 164
    right_menu = 165

    browser_back = 166
    browser_forward = 167
    browser_refresh = 168
    browser_stop = 169
    browser_search = 170
    browser_favorites = 171
    browser_start_and_home = 172

    volume_mute = 173
    volume_Down = 174
    volume_up = 175

    next_track = 176
    previous_track = 177
    stop_media = 178
    play = 179
    pause_media = 179

    start_mail = 180
    select_media = 181
    start_application_1 = 182
    start_application_2 = 183

    # - = 184 - 185  # Reserved

    # Used for miscellaneous characters; it can vary by keyboard.
    # For the US standard keyboard
    oem_1 = 186  # the ;: key

    # For any country/region
    oem_plus = 187  # the + key
    oem_comma = 188  # the , key
    oem_minus = 189  # the - key
    oem_period = 190  # the . key

    # Used for miscellaneous characters; it can vary by keyboard.
    # For the US standard keyboard
    oem_2 = 191  # the /? key
    oem_3 = 192  # the `~ key

    # - = 193 - 218  # Reserved

    # Used for miscellaneous characters; it can vary by keyboard.
    # For the US standard keyboard
    oem_4 = 219  # the [{ key
    oem_5 = 220  # the \| key
    oem_6 = 221  # the ]} key
    oem_7 = 222  # the '" key
    oem_8 = 223

    # - = 224  # Reserved
    # - = 225  # OEM specific

    oem_102 = 226  # The <> keys on the US standard keyboard, or the \| key on the non-US 102-key keyboard

    # - = 227 - 228  # OEM specific

    process_key = 229  # IME PROCESS key

    # - = 230  # OEM specific

    # Used to pass Unicode characters as if they were keystrokes.
    # The VK_PACKET key is the low word of a 32-bit Virtual Key value
    # used for non-keyboard input methods. For more information,
    # see Remark in KEYBDINPUT, SendInput, WM_KEYDOWN, and WM_KEYUP
    packet = 231

    # - = 232  # Unassigned
    # - = 233 - 245  # OEM specific

    attn_key = 246  # Attn key
    cr_sel_key = 247  # CrSel key
    ex_sel_key = 248  # ExSel key
    ere_of_key = 249  # Erase EOF key
    play_key = 250  # Play key
    zoom_key = 251  # Zoom key
    noname = 252  # Reserved
    pa1 = 253  # PA1 key
    clear_key = 254  # Clear key


_raw_key_data = """VK_LBUTTON	0x01	Left mouse button
VK_RBUTTON	0x02	Right mouse button
VK_CANCEL	0x03	Control-break processing
VK_MBUTTON	0x04	Middle mouse button
VK_XBUTTON1	0x05	X1 mouse button
VK_XBUTTON2	0x06	X2 mouse button
-	0x07	Reserved
VK_BACK	0x08	BACKSPACE key
VK_TAB	0x09	TAB key
-	0x0A-0B	Reserved
VK_CLEAR	0x0C	CLEAR key
VK_RETURN	0x0D	ENTER key
-	0x0E-0F	Unassigned
VK_SHIFT	0x10	SHIFT key
VK_CONTROL	0x11	CTRL key
VK_MENU	0x12	ALT key
VK_PAUSE	0x13	PAUSE key
VK_CAPITAL	0x14	CAPS LOCK key
VK_KANA	0x15	IME Kana mode
VK_HANGUL	0x15	IME Hangul mode
VK_IME_ON	0x16	IME On
VK_JUNJA	0x17	IME Junja mode
VK_FINAL	0x18	IME final mode
VK_HANJA	0x19	IME Hanja mode
VK_KANJI	0x19	IME Kanji mode
VK_IME_OFF	0x1A	IME Off
VK_ESCAPE	0x1B	ESC key
VK_CONVERT	0x1C	IME convert
VK_NONCONVERT	0x1D	IME nonconvert
VK_ACCEPT	0x1E	IME accept
VK_MODECHANGE	0x1F	IME mode change request
VK_SPACE	0x20	SPACEBAR
VK_PRIOR	0x21	PAGE UP key
VK_NEXT	0x22	PAGE DOWN key
VK_END	0x23	END key
VK_HOME	0x24	HOME key
VK_LEFT	0x25	LEFT ARROW key
VK_UP	0x26	UP ARROW key
VK_RIGHT	0x27	RIGHT ARROW key
VK_DOWN	0x28	DOWN ARROW key
VK_SELECT	0x29	SELECT key
VK_PRINT	0x2A	PRINT key
VK_EXECUTE	0x2B	EXECUTE key
VK_SNAPSHOT	0x2C	PRINT SCREEN key
VK_INSERT	0x2D	INS key
VK_DELETE	0x2E	DEL key
VK_HELP	0x2F	HELP key
0   0x30   0 key
1   0x31   1 key
2   0x32   2 key
3   0x33   3 key
4   0x34   4 key
5   0x35   5 key
6   0x36   6 key
7   0x37   7 key
8   0x38   8 key
9   0x39   9 key
-	0x3A-40	Undefined
A   0x41   A key
B   0x42   B key
C   0x43   C key
D   0x44   D key
E   0x45   E key
F   0x46   F key
G   0x47   G key
H   0x48   H key
I   0x49   I key
J   0x4A   J key
K   0x4B   K key
L   0x4C   L key
M   0x4D   M key
N   0x4E   N key
O   0x4F   O key
P   0x50   P key
Q   0x51   Q key
R   0x52   R key
S   0x53   S key
T   0x54   T key
U   0x55   U key
V   0x56   V key
W   0x57   W key
X   0x58   X key
Y   0x59   Y key
Z   0x5A   Z key
VK_LWIN    0x5B	Left Windows key
VK_RWIN    0x5C	Right Windows key
VK_APPS    0x5D	Applications key
-	0x5E	Reserved
VK_SLEEP	0x5F	Computer Sleep key
VK_NUMPAD0	0x60	Numeric keypad 0 key
VK_NUMPAD1	0x61	Numeric keypad 1 key
VK_NUMPAD2	0x62	Numeric keypad 2 key
VK_NUMPAD3	0x63	Numeric keypad 3 key
VK_NUMPAD4	0x64	Numeric keypad 4 key
VK_NUMPAD5	0x65	Numeric keypad 5 key
VK_NUMPAD6	0x66	Numeric keypad 6 key
VK_NUMPAD7	0x67	Numeric keypad 7 key
VK_NUMPAD8	0x68	Numeric keypad 8 key
VK_NUMPAD9	0x69	Numeric keypad 9 key
VK_MULTIPLY	0x6A	Multiply key
VK_ADD	0x6B	Add key
VK_SEPARATOR	0x6C	Separator key
VK_SUBTRACT	0x6D	Subtract key
VK_DECIMAL	0x6E	Decimal key
VK_DIVIDE	0x6F	Divide key
VK_F1	0x70	F1 key
VK_F2	0x71	F2 key
VK_F3	0x72	F3 key
VK_F4	0x73	F4 key
VK_F5	0x74	F5 key
VK_F6	0x75	F6 key
VK_F7	0x76	F7 key
VK_F8	0x77	F8 key
VK_F9	0x78	F9 key
VK_F10	0x79	F10 key
VK_F11	0x7A	F11 key
VK_F12	0x7B	F12 key
VK_F13	0x7C	F13 key
VK_F14	0x7D	F14 key
VK_F15	0x7E	F15 key
VK_F16	0x7F	F16 key
VK_F17	0x80	F17 key
VK_F18	0x81	F18 key
VK_F19	0x82	F19 key
VK_F20	0x83	F20 key
VK_F21	0x84	F21 key
VK_F22	0x85	F22 key
VK_F23	0x86	F23 key
VK_F24	0x87	F24 key
-	0x88-8F	Reserved
VK_NUMLOCK	0x90	NUM LOCK key
VK_SCROLL	0x91	SCROLL LOCK key
-	0x92-96	OEM specific
-	0x97-9F	Unassigned
VK_LSHIFT	0xA0	Left SHIFT key
VK_RSHIFT	0xA1	Right SHIFT key
VK_LCONTROL	0xA2	Left CONTROL key
VK_RCONTROL	0xA3	Right CONTROL key
VK_LMENU	0xA4	Left ALT key
VK_RMENU	0xA5	Right ALT key
VK_BROWSER_BACK	0xA6	Browser Back key
VK_BROWSER_FORWARD	0xA7	Browser Forward key
VK_BROWSER_REFRESH	0xA8	Browser Refresh key
VK_BROWSER_STOP	0xA9	Browser Stop key
VK_BROWSER_SEARCH	0xAA	Browser Search key
VK_BROWSER_FAVORITES	0xAB	Browser Favorites key
VK_BROWSER_HOME	0xAC	Browser Start and Home key
VK_VOLUME_MUTE	0xAD	Volume Mute key
VK_VOLUME_DOWN	0xAE	Volume Down key
VK_VOLUME_UP	0xAF	Volume Up key
VK_MEDIA_NEXT_TRACK	0xB0	Next Track key
VK_MEDIA_PREV_TRACK	0xB1	Previous Track key
VK_MEDIA_STOP	0xB2	Stop Media key
VK_MEDIA_PLAY_PAUSE	0xB3	Play/Pause Media key
VK_LAUNCH_MAIL	0xB4	Start Mail key
VK_LAUNCH_MEDIA_SELECT	0xB5	Select Media key
VK_LAUNCH_APP1	0xB6	Start Application 1 key
VK_LAUNCH_APP2	0xB7	Start Application 2 key
-	0xB8-B9	Reserved
VK_OEM_1	0xBA	Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the ;: key
VK_OEM_PLUS	0xBB	For any country/region, the + key
VK_OEM_COMMA	0xBC	For any country/region, the , key
VK_OEM_MINUS	0xBD	For any country/region, the - key
VK_OEM_PERIOD	0xBE	For any country/region, the . key
VK_OEM_2	0xBF	Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the /? key
VK_OEM_3	0xC0	Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the `~ key
-	0xC1-DA	Reserved
VK_OEM_4	0xDB	Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the [{ key
VK_OEM_5	0xDC	Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the \\| key
VK_OEM_6	0xDD	Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the ]} key
VK_OEM_7	0xDE	Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '" key
VK_OEM_8	0xDF	Used for miscellaneous characters; it can vary by keyboard.
-	0xE0	Reserved
-	0xE1	OEM specific
VK_OEM_102	0xE2	The <> keys on the US standard keyboard, or the \\| key on the non-US 102-key keyboard
-	0xE3-E4	OEM specific
VK_PROCESSKEY	0xE5	IME PROCESS key
-	0xE6	OEM specific
VK_PACKET	0xE7	Used to pass Unicode characters as if they were keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information, see Remark in KEYBDINPUT, SendInput, WM_KEYDOWN, and WM_KEYUP
-	0xE8	Unassigned
-	0xE9-F5	OEM specific
VK_ATTN	0xF6	Attn key
VK_CRSEL	0xF7	CrSel key
VK_EXSEL	0xF8	ExSel key
VK_EREOF	0xF9	Erase EOF key
VK_PLAY	0xFA	Play key
VK_ZOOM	0xFB	Zoom key
VK_NONAME	0xFC	Reserved
VK_PA1	0xFD	PA1 key
VK_OEM_CLEAR	0xFE	Clear key"""


def _format_raw_data():
    lines = _raw_key_data.split("\n")
    for line in lines:
        parts = [a for part in line.split("\t") for a in part.split(" ")]
        parts = [part for part in parts if part != ""]
        name = parts[0]
        vk = parts[1]
        description = " ".join(parts[2:])

        num = [str(int(x, 16)) for x in f"0x{vk.replace('0x', '')}".split("-")]

        print(f"{name.lower()} = {'-'.join(num)}  # {description}")


_keyname_to_v_code_map = {
    key: val for key, val in Vk.__dict__.items()
    if not (key.startswith("--") and key.endswith("--"))
}

_v_code_to_keyname_map = {val: key for key, val in _keyname_to_v_code_map.items()}


def keyname_to_v_code(keyname):
    return _keyname_to_v_code_map[keyname]


def v_code_to_keyname(v_code):
    return _v_code_to_keyname_map[v_code]


_char_to_code_map = {
    "\b": Vk.backspace,
    "\t": Vk.tab,

    "\r": Vk.enter,
    " ": Vk.space,

    "0": Vk.n_0,
    "1": Vk.n_1,
    "2": Vk.n_2,
    "3": Vk.n_3,
    "4": Vk.n_4,
    "5": Vk.n_5,
    "6": Vk.n_6,
    "7": Vk.n_7,
    "8": Vk.n_8,
    "9": Vk.n_9,

    "a": Vk.a,
    "b": Vk.b,
    "c": Vk.c,
    "d": Vk.d,
    "e": Vk.e,
    "f": Vk.f,
    "g": Vk.g,
    "h": Vk.h,
    "i": Vk.i,
    "j": Vk.j,
    "k": Vk.k,
    "l": Vk.l,
    "m": Vk.m,
    "n": Vk.n,
    "o": Vk.o,
    "p": Vk.p,
    "q": Vk.q,
    "r": Vk.r,
    "s": Vk.s,
    "t": Vk.t,
    "u": Vk.u,
    "v": Vk.v,
    "w": Vk.w,
    "x": Vk.x,
    "y": Vk.y,
    "z": Vk.z,

    # borrowed from ahk
    "!": Vk.alt,
    "^": Vk.ctrl,
    "+": Vk.shift,
    "#": Vk.win_l
}


def compile_to_vks(*parts: int | str):
    """
    compiles a list of Vks and chars
    into a list of just Vks
    """
    out = []
    for part in parts:
        if isinstance(part, int):
            out.append(part)
            continue

        for char in part:
            try:
                out.append(
                    _char_to_code_map.get(char)
                )
            except KeyError:
                raise TypeError(f"the char \"{char}\" doesn't directly map to any vk")

    return out


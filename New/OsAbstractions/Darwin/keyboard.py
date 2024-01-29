import os
import threading
from collections import defaultdict
import time

import ctypes
import ctypes.util
from New.OsAbstractions.Abstract.keyboard import AbsKeyboard

import Quartz
from AppKit import NSEvent

from New.Temp._keyboard_event import KeyboardEvent
from New.Temp._canonical_names import normalize_name


Carbon = ctypes.cdll.LoadLibrary(ctypes.util.find_library('Carbon'))


class KeyMap(object):
    non_layout_keys = dict((vk, normalize_name(name)) for vk, name in {
        # Layout specific keys from https://stackoverflow.com/a/16125341/252218
        # Unfortunately no source for layout-independent keys was found.
        0x24: 'return',
        0x30: 'tab',
        0x31: 'space',
        0x33: 'delete',
        0x35: 'escape',
        0x37: 'command',
        0x38: 'shift',
        0x39: 'capslock',
        0x3a: 'option',
        0x3b: 'control',
        0x3c: 'right shift',
        0x3d: 'right option',
        0x3e: 'right control',
        0x3f: 'function',
        0x40: 'f17',
        0x48: 'volume up',
        0x49: 'volume down',
        0x4a: 'mute',
        0x4f: 'f18',
        0x50: 'f19',
        0x5a: 'f20',
        0x60: 'f5',
        0x61: 'f6',
        0x62: 'f7',
        0x63: 'f3',
        0x64: 'f8',
        0x65: 'f9',
        0x67: 'f11',
        0x69: 'f13',
        0x6a: 'f16',
        0x6b: 'f14',
        0x6d: 'f10',
        0x6f: 'f12',
        0x71: 'f15',
        0x72: 'help',
        0x73: 'home',
        0x74: 'page up',
        0x75: 'forward delete',
        0x76: 'f4',
        0x77: 'end',
        0x78: 'f2',
        0x79: 'page down',
        0x7a: 'f1',
        0x7b: 'left',
        0x7c: 'right',
        0x7d: 'down',
        0x7e: 'up',
    }.items())
    layout_specific_keys = {}

    def __init__(self):
        # Virtual key codes are usually the same for any given key, unless you have a different
        # keyboard layout. The only way I've found to determine the layout relies on (supposedly
        # deprecated) Carbon APIs. If there's a more modern way to do this, please update this
        # section.

        # Set up data types and exported values:

        CFTypeRef = ctypes.c_void_p
        CFDataRef = ctypes.c_void_p
        CFIndex = ctypes.c_uint64
        OptionBits = ctypes.c_uint32
        UniCharCount = ctypes.c_uint8
        UniChar = ctypes.c_uint16
        uni_char_4 = UniChar * 4

        class CFRange(ctypes.Structure):
            _fields_ = [('loc', CFIndex),
                        ('len', CFIndex)]

        ktis_property_unicode_key_layout_data = ctypes.c_void_p.in_dll(
            Carbon, 'kTISPropertyUnicodeKeyLayoutData'
        )
        shift_key = 0x0200
        # alpha_key = 0x0400
        # option_key = 0x0800
        # control_key = 0x1000
        kuc_key_action_display = 3
        kuc_key_translat_no_dead_keys_bit = 0

        # Set up function calls:
        Carbon.CFDataGetBytes.argtypes = [CFDataRef] #, CFRange, UInt8
        Carbon.CFDataGetBytes.restype = None
        Carbon.CFDataGetLength.argtypes = [CFDataRef]
        Carbon.CFDataGetLength.restype = CFIndex
        Carbon.CFRelease.argtypes = [CFTypeRef]
        Carbon.CFRelease.restype = None
        Carbon.LMGetKbdType.argtypes = []
        Carbon.LMGetKbdType.restype = ctypes.c_uint32
        Carbon.TISCopyCurrentKeyboardInputSource.argtypes = []
        Carbon.TISCopyCurrentKeyboardInputSource.restype = ctypes.c_void_p
        Carbon.TISCopyCurrentASCIICapableKeyboardLayoutInputSource.argtypes = []
        Carbon.TISCopyCurrentASCIICapableKeyboardLayoutInputSource.restype = ctypes.c_void_p
        Carbon.TISGetInputSourceProperty.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        Carbon.TISGetInputSourceProperty.restype = ctypes.c_void_p
        Carbon.UCKeyTranslate.argtypes = [ctypes.c_void_p,
                                          ctypes.c_uint16,
                                          ctypes.c_uint16,
                                          ctypes.c_uint32,
                                          ctypes.c_uint32,
                                          OptionBits,      # keyTranslateOptions
                                          ctypes.POINTER(ctypes.c_uint32), # deadKeyState
                                          UniCharCount,    # maxStringLength
                                          ctypes.POINTER(UniCharCount), # actualStringLength
                                          uni_char_4]
        Carbon.UCKeyTranslate.restype = ctypes.c_uint32

        # Get keyboard layout
        klis = Carbon.TISCopyCurrentKeyboardInputSource()
        k_layout = Carbon.TISGetInputSourceProperty(klis, ktis_property_unicode_key_layout_data)
        if k_layout is None:
            klis = Carbon.TISCopyCurrentASCIICapableKeyboardLayoutInputSource()
            k_layout = Carbon.TISGetInputSourceProperty(klis, ktis_property_unicode_key_layout_data)
        k_layout_size = Carbon.CFDataGetLength(k_layout)
        # TODO - Verify this works instead of initializing with empty string
        k_layout_buffer = ctypes.create_string_buffer(k_layout_size)
        Carbon.CFDataGetBytes(k_layout, CFRange(0, k_layout_size), ctypes.byref(k_layout_buffer))

        # Generate character representations of key codes
        for key_code in range(0, 128):
            # TODO - Possibly add alt modifier to key map
            non_shifted_char = uni_char_4()
            shifted_char = uni_char_4()
            keys_down = ctypes.c_uint32()
            char_count = UniCharCount()

            Carbon.UCKeyTranslate(
                k_layout_buffer,
                key_code,
                kuc_key_action_display,
                0, # No modifier
                Carbon.LMGetKbdType(),
                kuc_key_translat_no_dead_keys_bit,
                ctypes.byref(keys_down),
                4,
                ctypes.byref(char_count),
                non_shifted_char
            )

            non_shifted_key = ''.join(chr(non_shifted_char[i]) for i in range(char_count.value))

            Carbon.UCKeyTranslate(
                k_layout_buffer,
                key_code,
                kuc_key_action_display,
                shift_key >> 8, # Shift
                Carbon.LMGetKbdType(),
                kuc_key_translat_no_dead_keys_bit,
                ctypes.byref(keys_down),
                4,
                ctypes.byref(char_count),
                shifted_char
            )

            shifted_key = ''.join(chr(shifted_char[i]) for i in range(char_count.value))

            self.layout_specific_keys[key_code] = (non_shifted_key, shifted_key)
        # Cleanup
        Carbon.CFRelease(klis)

    def character_to_vk(self, character):
        """ Returns a tuple of (scan_code, modifiers) where ``scan_code`` is a numeric scan code
        and ``modifiers`` is an array of string modifier names (like 'shift') """
        for vk in self.non_layout_keys:
            if self.non_layout_keys[vk] == character.lower():
                return (vk, [])
        for vk, char in self.layout_specific_keys.items():
            if char[0] == character:
                return (vk, [])
            if char[1] == character:
                return (vk, ['shift'])
        raise ValueError(f"Unrecognized character: {character}")

    def vk_to_character(self, vk, modifiers=None):
        """ Returns a character corresponding to the specified scan code (with given
        modifiers applied) """
        modifiers = modifiers and []

        if vk in self.non_layout_keys:
            # Not a character
            return self.non_layout_keys[vk]

        if vk in self.layout_specific_keys:
            if 'shift' in modifiers:
                return self.layout_specific_keys[vk][1]
            return self.layout_specific_keys[vk][0]

        # Invalid vk
        raise ValueError(f"Invalid scan code: {vk}")


class KeyController(object):
    def __init__(self):
        self.key_map = KeyMap()
        self.current_modifiers = {
            "shift": False,
            "caps": False,
            "alt": False,
            "ctrl": False,
            "cmd": False,
        }
        self.media_keys = {
            'KEYTYPE_SOUND_UP': 0,
            'KEYTYPE_SOUND_DOWN': 1,
            'KEYTYPE_BRIGHTNESS_UP': 2,
            'KEYTYPE_BRIGHTNESS_DOWN': 3,
            'KEYTYPE_CAPS_LOCK': 4,
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
        }

    def press(self, key_code):
        """ Sends a 'down' event for the specified scan code """
        if key_code >= 128:
            # Media key
            ev = NSEvent.\
                otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                14, # type
                (0, 0), # location
                0xa00, # flags
                0, # timestamp
                0, # window
                0, # ctx
                8, # subtype
                ((key_code-128) << 16) | (0xa << 8), # data1
                -1 # data2
            )
            Quartz.CGEventPost(0, ev.CGEvent())
            return

        # Regular key
        # Update modifiers if necessary
        if key_code == 0x37: # cmd
            self.current_modifiers["cmd"] = True
        elif key_code in (0x38, 0x3C): # shift or right shift
            self.current_modifiers["shift"] = True
        elif key_code == 0x39: # caps lock
            self.current_modifiers["caps"] = True
        elif key_code == 0x3A: # alt
            self.current_modifiers["alt"] = True
        elif key_code == 0x3B: # ctrl
            self.current_modifiers["ctrl"] = True

        # Apply modifiers if necessary
        event_flags = 0
        if self.current_modifiers["shift"]:
            event_flags += Quartz.kCGEventFlagMaskShift
        if self.current_modifiers["caps"]:
            event_flags += Quartz.kCGEventFlagMaskAlphaShift
        if self.current_modifiers["alt"]:
            event_flags += Quartz.kCGEventFlagMaskAlternate
        if self.current_modifiers["ctrl"]:
            event_flags += Quartz.kCGEventFlagMaskControl
        if self.current_modifiers["cmd"]:
            event_flags += Quartz.kCGEventFlagMaskCommand
        event = Quartz.CGEventCreateKeyboardEvent(None, key_code, True)
        Quartz.CGEventSetFlags(event, event_flags)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        time.sleep(0.01)

    def release(self, key_code):
        """ Sends an 'up' event for the specified scan code """
        if key_code >= 128:
            # Media key
            ev = NSEvent.\
                otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                14, # type
                (0, 0), # location
                0xb00, # flags
                0, # timestamp
                0, # window
                0, # ctx
                8, # subtype
                ((key_code-128) << 16) | (0xb << 8), # data1
                -1 # data2
            )
            Quartz.CGEventPost(0, ev.CGEvent())
            return

        # Regular key
        # Update modifiers if necessary
        if key_code == 0x37: # cmd
            self.current_modifiers["cmd"] = False
        elif key_code in (0x38, 0x3C): # shift or right shift
            self.current_modifiers["shift"] = False
        elif key_code == 0x39: # caps lock
            self.current_modifiers["caps"] = False
        elif key_code == 0x3A: # alt
            self.current_modifiers["alt"] = False
        elif key_code == 0x3B: # ctrl
            self.current_modifiers["ctrl"] = False

        # Apply modifiers if necessary
        event_flags = 0
        if self.current_modifiers["shift"]:
            event_flags += Quartz.kCGEventFlagMaskShift
        if self.current_modifiers["caps"]:
            event_flags += Quartz.kCGEventFlagMaskAlphaShift
        if self.current_modifiers["alt"]:
            event_flags += Quartz.kCGEventFlagMaskAlternate
        if self.current_modifiers["ctrl"]:
            event_flags += Quartz.kCGEventFlagMaskControl
        if self.current_modifiers["cmd"]:
            event_flags += Quartz.kCGEventFlagMaskCommand
        event = Quartz.CGEventCreateKeyboardEvent(None, key_code, False)
        Quartz.CGEventSetFlags(event, event_flags)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        time.sleep(0.01)

    def map_char(self, character):
        """
        it can convert all keys that are on the current layout
        but only the default ones and their shift verson

        for example 
            "a" => (code_for_a, [])
            "1" => (code_for_1, [])
            "!" => (code_for_1, ["shift"])

            # since "alt-gr" needs to be pressed, 
            # that means that it cant find it
            "@" => error
            
        the "only shift" thing isn't a tecniall limitation 
        but only a someone was wo lazy to implement it limitation
        """
        if character in self.media_keys:
            return (128+self.media_keys[character],[])

        return self.key_map.character_to_vk(character)

    def map_scan_code(self, scan_code):
        is_media_key = scan_code >= 128
        if is_media_key:
            character = [k for k, v in enumerate(self.media_keys) if v == scan_code-128]

            if len(character):
                return character[0]

            return None

        return self.key_map.vk_to_character(scan_code)


class KeyEventListener(object):
    def __init__(self, callback, blocking=False):
        self.blocking = blocking
        self.callback = callback
        self.listening = True
        self.tap = None
        self.modifier_scancodes = defaultdict(list)
        self.pressed_modifiers = set()

    def run(self):
        """ Creates a listener and loops while waiting for an event. Intended to run as
        a background thread. """
        self.tap = Quartz.CGEventTapCreate(
            Quartz.kCGSessionEventTap,
            Quartz.kCGHeadInsertEventTap,
            Quartz.kCGEventTapOptionDefault,
            Quartz.CGEventMaskBit(Quartz.kCGEventKeyDown) |
            Quartz.CGEventMaskBit(Quartz.kCGEventKeyUp) |
            Quartz.CGEventMaskBit(Quartz.kCGEventFlagsChanged),
            self.handler,
            None)
        loopsource = Quartz.CFMachPortCreateRunLoopSource(None, self.tap, 0)
        loop = Quartz.CFRunLoopGetCurrent()
        Quartz.CFRunLoopAddSource(loop, loopsource, Quartz.kCFRunLoopDefaultMode)
        Quartz.CGEventTapEnable(self.tap, True)

        while self.listening:
            Quartz.CFRunLoopRunInMode(Quartz.kCFRunLoopDefaultMode, 5, False)

    def handler(self, _, e_type, event, __):
        scan_code = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeycode)
        key_name = name_from_scancode(scan_code)
        flags = Quartz.CGEventGetFlags(event)
        event_type = ""
        is_keypad = flags & Quartz.kCGEventFlagMaskNumericPad
        if e_type == Quartz.kCGEventKeyDown:
            event_type = "down"
        elif e_type == Quartz.kCGEventKeyUp:
            event_type = "up"

        elif e_type == Quartz.kCGEventFlagsChanged:
            event_found = False

            # in order to distinguish things like right shift pressed, left shift pressed
            # then left shift released, right shift released, we keep track of the
            # scan codes for each modifier key

            for bitmask, key_name_suffixes in (
                    (Quartz.kCGEventFlagMaskShift, ("shift", )),
                    (Quartz.kCGEventFlagMaskAlphaShift, ("caps lock", )),
                    (Quartz.kCGEventFlagMaskControl, ("ctrl",)),
                    (Quartz.kCGEventFlagMaskCommand, ("command", "windows")),
                    (Quartz.kCGEventFlagMaskAlternate, ("option", "alt")),
            ):
                ends_with_suffix = any(key_name.endswith(suffix) for suffix in key_name_suffixes)
                if ends_with_suffix:
                    event_found = True
                    # it doesn't matter here if we clobber suffixes 
                    # from the same modifier like option/alt
                    key_name_suffix = key_name_suffixes[0]
                    if not flags & bitmask:
                        event_type = "up"
                        self.modifier_scancodes[key_name_suffix] = [] # just to be sure...
                        for suffix in key_name_suffixes:
                            self.pressed_modifiers.discard(suffix)
                    else:
                        if scan_code in self.modifier_scancodes[key_name_suffix]:
                            event_type = "up"
                            self.modifier_scancodes[key_name_suffix].remove(scan_code)
                            for suffix in key_name_suffixes:
                                self.pressed_modifiers.discard(suffix)
                        else:
                            event_type = "down"
                            self.modifier_scancodes[key_name_suffix].append(scan_code)
                            for suffix in key_name_suffixes:
                                self.pressed_modifiers.add(suffix)
                    if event_found:
                        break
            if not event_found:
                event_type = "up"

        if self.blocking:
            return None

        pressed_modifiers_tuple = tuple(sorted(self.pressed_modifiers))
        self.callback(KeyboardEvent(
            event_type,
            scan_code,
            name=key_name,
            is_keypad=is_keypad,
            modifiers=pressed_modifiers_tuple
        ))
        return event

key_controller = KeyController()

""" Exported functions below """

class Kayboard(AbsKeyboard):
    def init():
        pass
        # key_controller = KeyController()

    def press(scan_code):
        key_controller.press(scan_code)

    def release(scan_code):
        key_controller.release(scan_code)

    def map_name(name):
        yield key_controller.map_char(name)

    def name_from_scancode(scan_code):
        return key_controller.map_scan_code(scan_code)

    def listen(callback):
        KeyEventListener(callback).run()

    def type_unicode(character):
        output_source = Quartz.CGEventSourceCreate(Quartz.kCGEventSourceStateHIDSystemState)
        # Key down
        event = Quartz.CGEventCreateKeyboardEvent(
            output_source,
            0,
            True
        )
        Quartz.CGEventKeyboardSetUnicodeString(
            event,
            len(character.encode('utf-16-le')) // 2,
            character
        )
        Quartz.CGEventPost(
            Quartz.kCGSessionEventTap,
            event
        )
        # Key up
        event = Quartz.CGEventCreateKeyboardEvent(
            output_source,
            0,
            False
        )
        Quartz.CGEventKeyboardSetUnicodeString(
            event,
            len(character.encode('utf-16-le')) // 2,
            character
        )
        Quartz.CGEventPost(
            Quartz.kCGSessionEventTap,
            event
        )

# -*- coding: utf-8 -*-
import struct

import os
import sys
import atexit

import warnings
from time import time as now
from threading import Thread
from glob import glob
try:
    from queue import Queue
except ImportError:
    from Queue import Queue
import re
from collections import namedtuple
import fcntl


# event_bin_format
EVENT_BIN_FORMAT = 'llHHI'

# Taken from include/linux/input.h
# https://www.kernel.org/doc/Documentation/input/event-codes.txt
EV_SYN = 0x00
EV_KEY = 0x01
EV_REL = 0x02
EV_ABS = 0x03
EV_MSC = 0x04


UI_SET_EVBIT = 0x40045564
UI_SET_KEYBIT = 0x40045565
BUS_USB = 0x03
UI_DEV_CREATE = 0x5501
UI_DEV_DESTROY = 0x5502


def make_uinput():
    if not os.path.exists('/dev/uinput'):
        raise IOError('No uinput module found.')

    # Requires uinput driver, but it's usually available.
    with open("/dev/uinput", 'wb') as uinput:
        fcntl.ioctl(uinput, UI_SET_EVBIT, EV_KEY)

        for i in range(256):
            fcntl.ioctl(uinput, UI_SET_KEYBIT, i)

        uinput_user_dev = "80sHHHHi64i64i64i64i"
        axis = [0] * 64 * 4
        uinput.write(struct.pack(uinput_user_dev, b"Virtual Keyboard", BUS_USB, 1, 1, 1, 0, *axis))
        uinput.flush() # Without this you may get Errno 22: Invalid argument.

        fcntl.ioctl(uinput, UI_DEV_CREATE)
        #fcntl.ioctl(uinput, UI_DEV_DESTROY)

        return uinput


class EventDevice(object):
    def __init__(self, path):
        self.path = path
        self.input_file = None
        self.output_file = None

    @property
    def input_file(self):
        if self.input_file is None:
            try:
                self.input_file = open(self.path, 'rb')
            except IOError as e:
                if e.strerror == 'Permission denied':
                    print(
                        f"# ERROR: Failed to read device '{self.path}'. "
                        f"You must be in the 'input' group to access global events. "
                        f"Use 'sudo usermod -a -G input USERNAME'"
                        f"to add user to the required group."
                    )
                    sys.exit()

            def try_close():
                try:
                    # this shuld probably call the function
                    # but it was like this in the source code
                    self.input_file.close
                except AttributeError:
                    pass
            atexit.register(try_close)
        return self.input_file

    @property
    def output_file(self):
        if self.output_file is None:
            self.output_file = open(self.path, 'wb')
            atexit.register(self.output_file.close)
        return self.output_file

    def read_event(self):
        data = self.input_file.read(struct.calcsize(EVENT_BIN_FORMAT))
        seconds, microseconds, event_type, code, value = struct.unpack(EVENT_BIN_FORMAT, data)
        return seconds + microseconds / 1e6, event_type, code, value, self.path

    def write_event(self, event_type, code, value):
        integer, fraction = divmod(now(), 1)
        seconds = int(integer)
        microseconds = int(fraction * 1e6)
        data_event = struct.pack(EVENT_BIN_FORMAT, seconds, microseconds, event_type, code, value)

        # Send a sync event to ensure other programs update.
        sync_event = struct.pack(EVENT_BIN_FORMAT, seconds, microseconds, EV_SYN, 0, 0)

        self.output_file.write(data_event + sync_event)
        self.output_file.flush()

class AggregatedEventDevice(object):
    def __init__(self, devices, output=None):
        self.event_queue = Queue()
        self.devices = devices
        self.output = output or self.devices[0]
        def start_reading(device):
            while True:
                self.event_queue.put(device.read_event())
        for device in self.devices:
            thread = Thread(target=start_reading, args=[device])
            thread.daemon = True
            thread.start()

    def read_event(self):
        return self.event_queue.get(block=True)

    def write_event(self, event_type, code, value):
        self.output.write_event(event_type, code, value)


DeviceDescription = namedtuple(
    'DeviceDescription', 'event_file is_mouse is_keyboard'
)
DEVICE_PATTERN = r"""N: Name="([^"]+?)".+?H: Handlers=([^\n]+)"""
def list_devices_from_proc(type_name):
    try:
        with open('/proc/bus/input/devices', encoding="utf-8") as f:
            description = f.read()
    except FileNotFoundError:
        return

    for _, handlers in re.findall(DEVICE_PATTERN, description, re.DOTALL):
        path = '/dev/input/event' + re.search(r'event(\d+)', handlers).group(1)
        if type_name in handlers:
            yield EventDevice(path)


def list_devices_from_by_id(name_suffix, by_id=True):
    inp_path = 'by-id' if by_id else 'by-path'
    for path in glob(
        f'/dev/input/{inp_path}/*-event-{name_suffix}'):
        yield EventDevice(path)


def aggregate_devices(type_name):
    # Some systems have multiple keyboards with different range of allowed keys
    # on each one, like a notebook with a "keyboard" device exclusive for the
    # power button. Instead of figuring out which keyboard allows which key to
    # send events, we create a fake device and send all events through there.
    try:
        uinput = make_uinput()
        fake_device = EventDevice('uinput Fake Device')
        fake_device.input_file = uinput
        fake_device.output_file = uinput
    except IOError:
        warnings.warn(
            'Failed to create a device file using `uinput` module. '
            'Sending of events may be limited or unavailable depending on plugged-in devices.', 
            stacklevel=2)
        fake_device = None

    # We don't aggregate devices from different sources to avoid
    # duplicates.

    devices_from_proc = list(list_devices_from_proc(type_name))
    if devices_from_proc:
        return AggregatedEventDevice(devices_from_proc, output=fake_device)

    # breaks on mouse for virtualbox
    # was getting /dev/input/by-id/usb-VirtualBox_USB_Tablet-event-mouse
    devices_from_by_id = \
        list(list_devices_from_by_id(type_name)) \
        or list(list_devices_from_by_id(type_name, by_id=False))

    if devices_from_by_id:
        return AggregatedEventDevice(devices_from_by_id, output=fake_device)

    # If no keyboards were found we can only use the fake device to send keys.
    assert fake_device
    return fake_device

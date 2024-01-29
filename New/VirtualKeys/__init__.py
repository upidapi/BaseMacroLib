import platform as _platform

from .darwin_vk import DarwinVk
from .linux_vk import LinuxVk
from .windows_vk import WindowsVk


_system = _platform.system()
try:
    CurVk = {
        'Windows': WindowsVk,
        'Linux': LinuxVk,
        'Darwin': DarwinVk,
    }[_system]
except IndexError as e:
    raise OSError(f"Unsupported platform \"{_system}\"") from e

import ctypes

import math
import time

for i in range(200):
    x = int(500 + math.cos(i / 5) * i)
    y = int(500 + math.sin(i / 5) * i)
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.05)

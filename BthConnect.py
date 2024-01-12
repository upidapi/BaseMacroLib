# https://superuser.com/questions/1426949/scripting-connecting-disconnecting-a-paired-bluetooth-device
import subprocess

headphones_name = "WH-1000XM4"
headphones_addr = "AC:80:0A:2E:81:6A"

"""
search for devices and their addresses and services
btdiscovery -s [-i1]
"""


def _run_ps_script(script: str):
    return subprocess.check_output(["powershell", "/C", script])


def _get_headphones_addr():
    output = _run_ps_script(f"""
        btdiscovery -d"%a%" -n"{headphones_name}" -i1  
    """)
    return output[1:18]


def disconnect():
    # doesn't always work, IDK why

    _run_ps_script(f"""
    btcom -b {headphones_addr} -r -s110E
    """)


def connect():
    # the initial remove is to ensure that is was "fully" disconnected last time.
    # If you manually remove it (using settings) then, for some reason, then the
    # "connect" doesn't work at all.

    _run_ps_script(f"""
    btcom -b {headphones_addr} -r -s110E
    btcom -b {headphones_addr} -c -s110E
    """)


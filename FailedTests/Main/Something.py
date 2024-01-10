import bluetooth

print("Performing inquiry...")

nearby_devices = bluetooth.discover_devices(duration=1, lookup_names=True,
                                            flush_cache=True)

for addr, name in nearby_devices:
    int_addr = int("".join(addr.split(":")), 16)

    print(name, addr, int_addr)


# pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez

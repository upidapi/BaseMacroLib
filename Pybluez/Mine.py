import time

import bluetooth


server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("", bluetooth.PORT_ANY))
server_socket.listen(1)

client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")
data_received = client_socket.recv(1024)

time.sleep(10)

client_socket.close()
server_socket.close()

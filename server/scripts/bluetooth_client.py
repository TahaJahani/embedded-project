import socket

serverMACAddress = 'B8:27:EB:E1:82:65'
port = 7
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    command = input("Enter Bluetooth Command: ")
    if command == "quit":
        break
    s.send(command)
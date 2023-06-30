import socket
import threading

serverMACAddress = 'B8:27:EB:E1:82:65'
port = 7
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress, port))


def read_messages():
    while 1:
        message = s.recv(1024).decode("UTF-8")
        print("Received:" + message)


threading.Thread(target=read_messages).start()
while 1:
    command = input("Enter Bluetooth Command: ")
    if command == "quit":
        break
    s.send(bytes(command, 'UTF-8'))

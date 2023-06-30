import socket
import time

from Client import fan
from bcolors import bcolors

hostMACAddress = 'B8:27:EB:E1:82:65'
port = 7
backlog = 1
size = 1024
client = None
s = None


def listen():
    global s, client
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.bind((hostMACAddress, port))
    s.listen(backlog)
    try:
        client, address = s.accept()
        print("Client Accepted")
    except:
        print(bcolors.FAIL + "Error connecting to client" + bcolors.ENDC)


def send_message(message):
    global client
    if client is None:
        print("Client not connected yet.")
        return
    client.send(bytes(message, 'UTF-8'))
    time.sleep(0.5)


def read_message():
    global client
    if client is None:
        print("Client not connected yet")
        return
    while 1:
        data = client.recv(1024)
        if data:
            str_data = str(data)
            if str_data == "turn_off":
                fan.turn_off_fan()
            elif str_data == "turn_on":
                fan.turn_on_fan()
            elif str_data == "quit":
                close()
                break


def close():
    global s, client
    if s is None or client is None:
        return
    client.close()
    s.close()
    s = None
    client = None

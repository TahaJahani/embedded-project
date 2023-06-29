import socket
import time

import fan

serverMACAddress = '3C:F0:11:11:AE:E9'
port = 7
s = None


def connect():
    global s
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.connect((serverMACAddress, port))


def send_message(message):
    global s
    if s is None:
        connect()
    s.send(bytes(message, 'UTF-8'))
    time.sleep(0.5)


def read_message():
    global s
    if s is None:
        connect()
    while 1:
        data = s.recv(1024)
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
    global s
    if s is None:
        return
    s.close()
    s = None

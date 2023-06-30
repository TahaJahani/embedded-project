import threading

import bluetooth_server
import fan
import gps
from manager import Manager


def get_debug_input():
    while True:
        distance = int(input("Enter a valid distance:"))
        Manager.distance_updated(distance)


if __name__ == "__main__":
    mode = int(input("Enter Mode: 1.Debug    2.Real\n"))
    fan.setup()
    bluetooth_server.listen()
    threading.Thread(target=bluetooth_server.read_message).start()
    threading.Thread(target=gps.gps_thread).start()
    if mode == 1:
        threading.Thread(target=get_debug_input).start()

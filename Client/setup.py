import threading

import bluetooth
import fan
import gps

if __name__ == "__main__":
    fan.setup()
    bluetooth.connect()
    threading.Thread(target=bluetooth.read_message).start()
    # threading.Thread(target=gps.gps_thread).start()

import pynmea2
import serial

from distance_utils import Location, calculate_spherical_distance
from manager import Manager

first_location = None


def gps_thread():
    print("Waiting For First Location...")
    first_location = get_location()
    print("Location Updated! Running program...")
    while True:
        current_location = get_location()
        distance = calculate_spherical_distance(first_location, current_location)
        Manager.distance_updated(distance)


def get_location() -> Location:
    while True:
        port = "/dev/ttyAMA0"
        ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        try:
            dataout = pynmea2.NMEAStreamReader()
            newdata = ser.readline().decode("utf-8")
            if newdata.startswith("$GNRMC"):
                newmsg = pynmea2.parse(newdata)
                lat = newmsg.latitude
                lng = newmsg.longitude
                return Location(lat, lng)
        except:
            pass

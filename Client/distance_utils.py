from math import sin, cos, atan2, sqrt


class Location:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"({self.lat}, {self.lon})"


def calculate_spherical_distance(location1: Location, location2: Location, r=6373):
    lat1, lon1 = location1.lat, location1.lon
    lat2, lon2 = location2.lat, location2.lon
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = r * c
    return distance
from geolite2 import geolite2


def locate_ip(ip_address):
    reader = geolite2.reader()
    location = reader.get(ip_address)

    data = {
        "continent": (location["continent"]["names"]["en"]),
        "country": (location["country"]["names"]["en"]),
        "state": (location["subdivisions"][0]["names"]["en"]),
        "city": (location["city"]["names"]["en"]),
        "postal": (location["postal"]["code"]),
        "latitude": (location["location"]["latitude"]),
        "longitude": (location["location"]["longitude"]),
        "time zone": (location["location"]["time_zone"])
    }

    for key, value in data.items():
        print(f"{key.title()}: {value}")


address = input("Enter an IP address to locate: ")
ip_address = address
locate_ip(ip_address)

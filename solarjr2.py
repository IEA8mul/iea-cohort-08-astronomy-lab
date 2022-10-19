#!/usr/bin/env python3
import datetime
import os
import requests
import sys


# ASTRONOMYAPI_ID = os.environ.get("ASTRONOMYAPI_ID")

ASTRONOMYAPI_ID="adb8f84e-3dad-445b-acc5-92beddb1113a"

# ASTRONOMYAPI_SECRET = os.environ.get("ASTRONOMYAPI_SECRET")

ASTRONOMYAPI_SECRET="22e15557d1fd330bf114fd8948d33c8542c036f19041b97c166e43ba8cb775fea5aec3551f6ebee38d512f4b3c144c5645600cb96fed05af15d506d9c8717eaea42bdd103fc963fdbdc68e3b52bbd44b7bced65767ef7015d9de9a654318b93bf9b275f99f47b38d15c9ee67998f301c"


def get_observer_location():
    """Returns the longitude and latitude for the location of this machine.

    Returns:
    str: latitude
    str: longitude"""

    url = "http://ip-api.com/json/"
    try:
        response = requests.get(url)
        if not response.status_code == 200:
            return None, None

    except requests.exceptions.ConnectionError:
        return None, None
    except requests.exceptions.Timeout:
        return None, None

    data = response.json()

    # NOTE: Replace with your real return values!
    return data.get("lat"), data.get("lon")


def get_sun_position(latitude, longitude, body="sun"):
    """Returns the current position of the sun in the sky at the specified location

    Parameters:
    latitude (str)
    longitude (str)

    Returns:
    float: azimuth
    float: altitude
    """
    body = body or "sun"
    url = f"https://api.astronomyapi.com/api/v2/bodies/positions/{body}"
    now = datetime.datetime.now()
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "elevation": 0,
        "from_date": now.date().isoformat(),
        "to_date": now.date().isoformat(),
        "time": now.strftime("%H:%M:%S"),
    }

    try:
        response = requests.get(
            url, params=params,
            auth=(ASTRONOMYAPI_ID, ASTRONOMYAPI_SECRET))
        if not response.status_code == 200:
            return None, None
    except requests.exceptions.ConnectionError:
        return None, None
    except requests.exceptions.Timeout:
        return None, None

    data = response.json()
    body_data = data["data"]["table"]["rows"][0]["cells"][0]
    position = body_data["position"]["horizontal"]
    alt = position["altitude"]["degrees"]
    az = position["azimuth"]["degrees"]

    return az, alt


def print_position(azimuth, altitude):
    """Prints the position of the sun in the sky using the supplied coordinates

    Parameters:
    azimuth (float)
    altitude (float)"""

    print(
        f"The Sun is currently seen at: "
        f"{altitude} deg altitude, {azimuth} deg azimuth."
    )


if __name__ == "__main__":
    latitude, longitude = get_observer_location()
    if latitude is None or longitude is None:
        print("Could not find your location by IP!")
        sys.exit(1)
    azimuth, altitude = get_sun_position(latitude, longitude)
    if azimuth is None or altitude is None:
        print("Could not get Sun position from Astronomy API")
        sys.exit(2)
    print_position(azimuth, altitude)



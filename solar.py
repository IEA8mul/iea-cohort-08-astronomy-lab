#!/usr/bin/env python3
import requests
import datetime
ASTRONOMYAPI_ID="<your api id>"
ASTRONOMYAPI_SECRET="<your api secret key>"
def get_observer_location():
"""Returns the longitude and latitude for the location of this machine.
Returns:
str: latitude
str: longitude"""
# NOTE: Replace with your real return values!
return None, None
def get_sun_position(latitude, longitude):
"""Returns the current position of the sun in the sky at the specified location
Parameters:
latitude (str)
longitude (str)
Returns:
float: azimuth
float: altitude
"""
# NOTE: Replace with your real return values!
return 0, 0
def print_position(azimuth, altitude):
"""Prints the position of the sun in the sky using the supplied coordinates
Parameters:
azimuth (float)
altitude (float)"""
print("The Sun is currently at:")
if __name__ == "__main__":
latitude, longitude = get_location()
azimuth, altitude = get_sun_position()
print_position(azimuth, altitude)

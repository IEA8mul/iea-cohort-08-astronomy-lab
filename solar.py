#!/usr/bin/env python3
import requests
import datetime
ASTRONOMYAPI_ID="<adb8f84e-3dad-445b-acc5-92beddb1113a>"
ASTRONOMYAPI_SECRET="<22e15557d1fd330bf114fd8948d33c8542c036f19041b97c166e43ba8cb775fea5aec3551f6ebee38d512f4b3c144c5645600cb96fed05af15d506d9c8717eaea42bdd103fc963fdbdc68e3b52bbd44b7bced65767ef7015d9de9a654318b93bf9b275f99f47b38d15c9ee67998f301c>"
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

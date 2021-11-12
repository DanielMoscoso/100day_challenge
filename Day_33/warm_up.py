import requests

"""
API response meanings:
    -1xx: Hold on
    -2xx: Here you go
    -3xx: Go away (you dont have permission)
    -4xx: You screwed up (this does not even exist)
    -5xx: I (the server) screwed up
"""

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

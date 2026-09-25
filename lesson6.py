import requests

def get_temperature(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["current_weather"]["temperature"]

cities = {
    "Malmö": (55.6, 13.0),
    "Karachi": (24.86, 67.01),
    "Stockholm": (59.32, 18.06)
}

for name, (lat, lon) in cities.items():
    print(name, ":" , get_temperature(lat,lon))

#print("Malmö:", get_temperature(55.6, 13.0))
#print("Karachi:", get_temperature(24.86, 67.01))
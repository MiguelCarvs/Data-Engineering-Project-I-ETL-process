import requests

def extract_weather(latitude, longitude):

    #Params definition
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,precipitation,wind_speed_10m,wind_direction_10m,relative_humidity_2m"
    }

    #Fetching data from server HTTP with a GET query
    response = requests.get(base_url, params=params)

    api_response = response.json()

    #Converts especific keys in python's dict
    weather = {
        "time": api_response["current"]["time"],
        "temperature": api_response["current"]["temperature_2m"],
        "humidity": api_response["current"]["relative_humidity_2m"],
        "wind_direction": api_response["current"]["wind_direction_10m"],
        "wind_speed": api_response["current"]["wind_speed_10m"],
    }

    return weather

print(extract_weather(-23.55, -46.63))
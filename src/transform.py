import requests
from extract import extract_weather

    #Converts especific keys in python's dict
def transform_weather(api_response):    
    weather = {
        "time": api_response["current"]["time"],
        "temperature": api_response["current"]["temperature_2m"],
        "humidity": api_response["current"]["relative_humidity_2m"],
        "wind_direction": api_response["current"]["wind_direction_10m"],
        "wind_speed": api_response["current"]["wind_speed_10m"],
    }
    return weather

if __name__ == "__main__":
    api_response = extract_weather()
    weather = tranform_weather(api_response)

print(weather)
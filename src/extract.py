import requests

def extract_weather():

    latitude = -23.55
    longitude = -46.63

    #Params definition
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,precipitation,wind_speed_10m,wind_direction_10m,relative_humidity_2m"
    }

    #Fetching data from server HTTP with a GET query
    try:
        response = requests.get(base_url, params=params, timeout=10)

        response.raise_for_status()

        api_response = response.json()

        return api_response
    except requests.exceptions.ConnectionError:
        print("Unable to connect to the server.")
        raise
    except requests.exceptions.HTTPError:
        print("The API returned an HTTP error.")
        raise
    except requests.exceptions.Timeout:
        print("Response time exceeded the limit.")
        raise

if __name__ == "__main__":
    print(extract_weather())
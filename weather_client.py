import requests
import json
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap

API_KEY = "2aebc7d910223a38e11fedeaa670a5af"
WeatherURL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city) -> Dict:
    res = requests.get(WeatherURL, params={"q": city, "appid": API_KEY})
    return res.json()

## Example: Spotify

# Define the API endpoint
SpotifyURL = "https://api.spotify.com/v1/search"

def get_songs(name) -> Dict:
    # Define the API parameters
    params = {
        "q": name,
        "type": "artist"
    }

    # Define the authorization header
    headers = {
        "Authorization": "Bearer BQAE-grAg7l9-iZR6-S8xUIiSqP94tSk-HE5aK6m0jybVZ01jOp9wTzZAX2fQmc-P7klS5gR698K70EczRL-de4kuacqhTh9BDzJAjvuSsYYo7vwiaC0"
    }
    # Send the API request and get the response
    response = requests.get(SpotifyURL, params=params, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data from the response
        return response.json()

def main():
    choice = input("w for weather or s for spotify: ")
    if(choice == "w"):
        city = input("City: ")
        temp = json.dumps(get_weather(city), indent=4)
        print(temp)
    elif(choice == "s"):
        name = input("What artist would you like to search? ")
        temp = json.dumps(get_songs(name), indent=4)
        print(temp)

if __name__ == "__main__":
    main()
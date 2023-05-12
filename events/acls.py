from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import requests
import json


def get_photo(city, state):
    params = {"query": f"{city}, {state}", "per_page": 1}
    url = 'https://api.pexels.com/v1/search?'
    headers = {'Authorization': PEXELS_API_KEY}
    response = requests.get(url, headers=headers, params=params)
    picture = json.loads(response.content)
    return {"picture_url": picture["photos"][0]["src"]["original"]}


def get_weather_data(city, state):
    location_url = "http://api.openweathermap.org/geo/1.0/direct?"
    loc_params = {
        "q": f"{city}, {state}, US",
        "appid": OPEN_WEATHER_API_KEY,
    }
    response = requests.get(location_url, params=loc_params)
    location = json.loads(response.content)
    lat = location[0]["lat"]
    lon = location[0]["lon"]

    weather_url = "https://api.openweathermap.org/data/2.5/weather?"
    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial",
    }
    weather_response = requests.get(weather_url, params=weather_params)
    weather = json.loads(weather_response.content)
    return {
        "temperature": weather["main"]["temp"],
        "description": weather["weather"][0]["description"]
    }

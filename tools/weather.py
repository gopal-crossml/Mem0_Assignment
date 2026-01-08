"""
Weather Tool using OpenWeatherMap API
"""

import requests
import os

from langchain.tools import tool

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


@tool
def get_weather(city: str) -> dict:
    """
    Summary:
        Fetch live weather information for a specified city using the OpenWeatherMap API.

    Args:
        city (str): Name of the city for which weather data is requested.

    Returns:
        dict: A dictionary containing:
            - temperature (float): Current temperature in Celsius.
            - condition (str): Text description of the current weather.
        If an error occurs, returns a dictionary with:
            - error (str): Error message describing the failure.
    """
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
        )
        response = requests.get(url)
        data = response.json()

        return {
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }
    except Exception as e:
        return {"error": str(e)}

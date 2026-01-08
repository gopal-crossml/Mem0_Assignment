import os

from dotenv import load_dotenv

# Loading environment variable
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY", "")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
MEM0_API_KEY = os.getenv("MEM0_API_KEY")


if not gemini_api_key:
    raise EnvironmentError("Gemini API Key is not found.")

if not WEATHER_API_KEY:
    raise EnvironmentError("Weather API key is not found.")

if not MEM0_API_KEY:
    raise EnvironmentError("mem0 API key is not found")

USER_ID = "assigned user"
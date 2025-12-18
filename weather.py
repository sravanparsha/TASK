import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import os

OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY", "356e4ce6db91cabfeed9d8ed55887c2d")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

class WeatherAPIError(Exception): pass
class CityNotFoundError(WeatherAPIError): pass
class InvalidAPIKeyError(WeatherAPIError): pass

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(min=1, max=8),
    retry=retry_if_exception_type(requests.exceptions.RequestException),
    reraise=True
)
def fetch_weather(city: str) -> dict:
    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        if resp.status_code == 404:
            raise CityNotFoundError(f"City '{city}' not found.")
        if resp.status_code == 401:
            raise InvalidAPIKeyError("Invalid OpenWeather API key.")
        if resp.status_code == 429:
            raise WeatherAPIError("Weather API rate limit exceeded.")
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException:
        raise

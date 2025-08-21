"""
Weather App
-----------
A simple Python script to fetch weather data from OpenWeather API.

Skills shown:
- Using APIs with Python (requests)
- Error handling
- Clean functions and output
"""

import requests

def get_weather(city: str, api_key: str) -> dict:
    """Fetch weather data for a given city using OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code} - {response.text}")

def display_weather(city: str, weather_data: dict) -> None:
    """Print the weather information in a simple format."""
    print(f"\n🌍 Weather in {city}")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Condition: {weather_data['weather'][0]['description'].capitalize()}")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s\n")

if __name__ == "__main__":
    API_KEY = "7712c24701b42e4ba3fb6ffba450f917" # 🔑 Get a free key at https://openweathermap.org/api
    city_name = input("Boyle: ")

    try:
        data = get_weather(Boyle, 7712c24701b42e4ba3fb6ffba450f917)
        display_weather(Boyle, data)
    except Exception as e:
        print(f"⚠️ {e}")


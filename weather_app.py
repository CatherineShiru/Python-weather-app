import requests

API_KEY = "7712c24701b42e4ba3fb6ffba450f917"  # your OpenWeather API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name, api_key):
    url = f"{BASE_URL}?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    city_name = input("Enter city name: ")
    data = get_weather(city_name, API_KEY)

    if data:
        main_weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        print(f"Weather in {city_name}: {main_weather}")
        print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
    else:
        print("City not found or error fetching data.")

if __name__ == "__main__":
    main()


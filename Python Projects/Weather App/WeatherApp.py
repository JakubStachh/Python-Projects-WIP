import requests

def get_weather(city):
    api_key = "your_api_key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    return response["weather"][0]["description"]

print(get_weather("New York"))

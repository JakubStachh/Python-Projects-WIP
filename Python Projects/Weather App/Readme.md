# 🚀 Weather API Fetcher

## 📚 Description
This function `get_weather` fetches the current weather description for a given city using the OpenWeather API. It takes a city name as input and returns the weather description.

---

## 📐 Function Definition

```python
import requests

def get_weather(city):
    api_key = "your_api_key"  # Replace with your actual OpenWeather API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    return response["weather"][0]["description"]

print(get_weather("New York"))
```

## ✅ Example Usage
```python
print(get_weather("New York"))  # Output: "clear sky", "rain", etc.
```
## 🧪 Example Output
```
clear sky
```

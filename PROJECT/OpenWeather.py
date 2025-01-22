import requests

def weather_info():
    api_key = "2a9a9fdacd0fd19e9a2945d6cdebf74f"  #free API key from OpenWeatherMap
    city = input("Enter city name: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Current weather in {city}: {temp}°C, {description}")
    else:
        print("City not found or API error.")

weather_info()

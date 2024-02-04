# Basic Weather App Project
# Nupur Kirwai
# importing requests and json
import requests
#pip install requests
import json
#declaring a function to get weather data
def get_data(api_key, area):
    url = "http://api.openweathermap.org/data/2.5/weather"
    #setting the parameters
    params = {
        'q': area,
        'units': 'metric',
        'appid': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print(f"Unable to fetch weather data.")
#creating function to display the data fetched
def display(weather_data):
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        conditions = weather_data['weather'][0]['description']

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Conditions: {conditions}")
    else:
        print("Unable to fetch weather data.")

if __name__ == "__main__":
    #initialising the api key 
    api_key = '0b0b8d443aedc2f40b7dd8f5a3d4c1bb' 
    print("Welcome to Weather Forecast!")
    #taking input of the city code you want the weather for
    area = input("Enter a City or ZIP code: ")
    print("The Weather Report is:")
    
    weather_data = get_data(api_key, area)
    #displaying the data
    if weather_data:
        display(weather_data)

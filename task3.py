"""
Use the Weather API builder at https://open-meteo.com/en/docs to generate an API call for a city. We are going to make use of the REQUESTS.Request method to retrieve this data and unpack it with json.loads into a variable that we can use. Retrieve the data and present it in a more organized format. You may use text output or a window using Tkinter.  Our goal is to format the result in a reasonably organized format.
"""

import requests
import json
import tkinter as tk


def fetch_weather_data(city):
    url = f"https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current_weather=true"
    

    response = requests.get(url)

    weather_data = response.json()
    current_weather = weather_data['current_weather']
    temperature = current_weather['temperature']
    wind_speed = current_weather['windspeed']
    wind_direction = current_weather['winddirection']
    weather_description = current_weather['weathercode']

    return f"Weather Data for {city}:\n" \
           f"Temperature: {temperature}°C\n" \
           f"Wind Speed: {wind_speed} km/h\n" \
           f"Wind Direction: {wind_direction}°\n" \
           f"Weather Description: {weather_description}"

def display_weather(city):
    weather_info = fetch_weather_data(city)

    window = tk.Tk()
    window.title("Weather Information")

    label = tk.Label(window, text=weather_info, font=("Comic Sans MS", 12), padx=20, pady=20)
    label.pack()

    window.mainloop()

city = input("What city?: ")
display_weather(city)
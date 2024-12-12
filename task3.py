"""
Use the Weather API builder at https://open-meteo.com/en/docs to generate an API call for a city. We are going to make use of the REQUESTS.Request method to retrieve this data and unpack it with json.loads into a variable that we can use. Retrieve the data and present it in a more organized format. You may use text output or a window using Tkinter.  Our goal is to format the result in a reasonably organized format.
"""

import requests
import json
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

#returns weather conditions and country name
def getCityWeather(city):
    try:
        #first find the coordinates of your city 
        #(we'll be using geocoding api that's very popular)
        geocode = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geocode_response = requests.get(geocode)
        #response.raise_for_status()
        coords = geocode_response.json()

        if "results" not in coords or not coords["results"]:
            messagebox.showerror("Error", "Could not retrieve coordinates data. Check name or or something else is wrong :(")
            return 

        #This program returns weather for top city result in geocode api
        top_city = coords["results"][0]
        country = top_city["country"]
        lat = top_city["latitude"]
        lon = top_city["longitude"]

        #Use coords to get weather from open-meteo
        meteo = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        meteo_response = requests.get(meteo)
        #weather_response.raise_for_status()
        weather = meteo_response.json()

        return weather["current_weather"], country

    except requests.RequestException as e:
        print(f"err: {e}")
        return

#changes tkinter output label to weather conditions, city and country name output
def displayWeather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Empty input", "Please Enter a City Name")
        return

    weather, country = getCityWeather(city)

    if weather is None:
        messagebox.showerror("Error", "Could not retrieve open meteo data. Check name or something else is wrong :(")
        return

    output = (
        f"City: {city}\n"
        f"Country: {country}\n"
        f"Temperature: {weather['temperature']} °C\n"
        f"Wind Speed: {weather['windspeed']} km/h\n"
        f"Wind Direction: {weather['winddirection']} °\n"
        f"Weather Code: {weather['weathercode']}"
    )

    output_label.config(text=output)

#Tkinter part

root = tk.Tk()
root.title("Yurii Weather")

#must have formatting for peak ui/ux and a e s t h e t i c s
font = tkFont.nametofont("TkDefaultFont")
font.configure(family="Comic Sans MS", size=10)
root.option_add("*Font", font)

frame = tk.Frame(root)
frame.pack(pady=10)

city_label = tk.Label(frame, text="Enter City:")
city_label.grid(row=0, column=0, padx=5)

city_entry = tk.Entry(frame)
city_entry.grid(row=0, column=1, padx=5)

get_weather_button = tk.Button(frame, text="Get Weather", command=displayWeather)
get_weather_button.grid(row=0, column=2, padx=5)

output_label = tk.Label(root, text="", justify="left", font=("Comic Sans MS", 12))
output_label.pack(pady=10)

root.mainloop()
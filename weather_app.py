import tkinter as tk
from tkinter import *
import requests
import json

win = tk.Tk()
win.title('WeatherApp')
#win.configure(bg ='gray')
win.geometry('500x200')

api = "c703c966f9be8a0c4869b86832a0898f"
url = "http://api.openweathermap.org/data/2.5/weather?"
query_units = 'metric'

def weather():
    location = entry.get()
    answer = url + 'appid=' + api + '&q=' + location + '&units=' + query_units
    response = requests.get(answer)
    res = response.json()
    if res['cod'] != '404':
        x = res['main']
        temperature = x['temp']
        pressure = x['pressure']
        humidity = x['humidity']
        y = res['weather']
        weather_description = y[0]['description']
        label = tk.Label(win, text =(('Temperature of '), location , ' (in Celcius ) ', temperature , '\n\n'
                          'Atmospheric pressure (in hPa Unit) ', pressure , '\n\n',
                          'Humidity is : ', humidity, '% ', '\n\n'
                          'Description ', weather_description ), fg = 'blue')
        label.grid(row = 2, column = 0)
        label.config(font=('sans', 14))

    else:
        label2 = tk.Label(win, text = 'Enter Correct City')
        label2.grid(row = 2, column = 0)

label = tk.Label(win, text= 'Enter City Name Below : ', fg = 'brown',)
label.grid(row = 0, column = 0)
label.config(font=('times', 20, 'bold'))

# Create the input Location window

entry = tk.Entry(win)
entry.grid(row = 1, column = 0, columnspan = 14) #padx= 100)

# Creat the search button
btn = tk.Button(win, text = 'Search', command = weather)
btn.grid(row = 1, column = 1)





win.mainloop()

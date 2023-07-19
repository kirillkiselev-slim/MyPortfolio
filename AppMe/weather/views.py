import datetime
import os
import requests
from django.shortcuts import render


os.chdir('./weather')
def city(request):

    with open("./hidden/API_KEY.txt", "r") as api_file:
        line =  api_file.readline()
        API_KEY = line.strip("\n")

    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

    if request.method == 'POST':
        city = request.POST['city']
        weather_data = find_weather(city, API_KEY, current_weather_url)

        context = {
            'weather_data': weather_data
        }
        return render(request, 'weather/city.html', context=context)
    else:
        return render(request, 'weather/city.html')


def find_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'icon': response['weather'][0]['icon']
    }

    return weather_data

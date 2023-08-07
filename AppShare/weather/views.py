import os
import requests
from django.shortcuts import render, redirect
from .forms import User_city
from .models import UserCity
from django.contrib import messages
from django.contrib.auth.decorators import login_required

os.chdir('./weather')

@login_required()
def get_city(request):
    if request.method == 'POST':
        form = User_city(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            user_city, created = UserCity.objects.get_or_create(user=request.user)

            user_city.city = city
            user_city.save()
            return redirect("/weather")
        else:
            messages.error(request, "Enter a valid city")
    else:
        form = User_city()
    context = {
        'form': form
    }
    return render(request, 'weather/city.html', context)


@login_required()
def all_users_weather(request):

    with open("./hidden/API_KEY.txt", "r") as api_file:
        line =  api_file.readline()
        API_KEY = line.strip("\n")

    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    cities = UserCity.objects.all()

    weather_data_dict = {}
    for city_obj in cities:
        city = city_obj.city
        weather_data = find_weather(city,API_KEY, current_weather_url)

        weather_data_dict[city_obj.user] = weather_data
        sorted_weather_data = dict(
            sorted(weather_data_dict.items(), key=lambda item: item[1]['temperature'], reverse=True))

        context = {
            'weather_data': sorted_weather_data,
        }

    return render(request, 'weather/weather-users.html', context=context)



def find_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'icon': response['weather'][0]['icon']
    }
    return weather_data
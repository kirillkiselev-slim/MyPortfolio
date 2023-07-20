import os
import requests
from django.shortcuts import render, redirect, get_object_or_404
from .forms import User_city
from .models import UserCity
from django.contrib import messages

os.chdir('./weather')

def get_city(request):
    if request.method == 'POST':
        form = User_city(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            user_city, created = UserCity.objects.get_or_create(user=request.user)

            user_city.city = city
            user_city.save()
            return redirect("./")
        else:
            messages.error(request, "Enter a valid city")
    else:
        form = User_city()
    context = {
        'form': form
    }
    return render(request, 'weather/city.html', context)

# def city(request):
#
#     with open("./hidden/API_KEY.txt", "r") as api_file:
#         line =  api_file.readline()
#         API_KEY = line.strip("\n")
#
#     current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
#
#     if request.method == 'POST':
#         city = request.POST['city']
#         weather_data = find_weather(city, API_KEY, current_weather_url)
#
#         context = {
#             'weather_data': weather_data
#         }
#         return render(request, 'weather/city.html', context=context)
#     else:
#         return render(request, 'weather/city.html')
#
#
# def find_weather(city, api_key, current_weather_url):
#     response = requests.get(current_weather_url.format(city, api_key)).json()
#
#     weather_data = {
#         'city': city,
#         'temperature': round(response['main']['temp'] - 273.15, 2),
#         'icon': response['weather'][0]['icon']
#     }
#
#     return weather_data

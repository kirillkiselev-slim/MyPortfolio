import datetime

import requests
from django.shortcuts import render

def index(request):
    API_KEY = open("hidden/API_KEY.txt", "r")
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

    if request.method == 'POST':

    else:
        return render('')
# Create your views here.

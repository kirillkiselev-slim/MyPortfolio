import requests
from django import forms
from .models import UserCity
class User_city(forms.ModelForm):
    class Meta:
        model = UserCity
        fields = ["city"]

    def clean_city(self):
        with open("./hidden/API_KEY.txt", "r") as api_file:
            line = api_file.readline()
            API_KEY = line.strip("\n")
            city = self.cleaned_data.get('city')
            current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
            response = requests.get(current_weather_url.format(city, API_KEY)).json()
            if response['cod'] == '404':
                raise forms.ValidationError('Enter a valid city')
            elif city in response['name']:
                return city
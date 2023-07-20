from django.urls import path
from .views import get_city #find_weather



APP_NAME = 'weather'
urlpatterns = [
    path('city', get_city, name='city'),
    #path('weather/users',find_weather, name='users-weather'),
]
from django.urls import path
from .views import city, find_weather



APP_NAME = 'weather'
urlpatterns = [
    path('weather/', city, name='city'),
    #path('weather/users',find_weather, name='users-weather'),
]
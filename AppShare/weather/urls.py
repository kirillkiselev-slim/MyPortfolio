from django.urls import path
from .views import get_city, all_users_weather



APP_NAME = 'weather'
urlpatterns = [
    path('city/', get_city, name='city'),
    path('weather/',all_users_weather,  name='weather'),
]
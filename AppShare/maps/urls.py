from django.urls import path
from .views import country, display_map



APP_NAME = 'maps'
urlpatterns = [
    path('maps/', country, name='country'),
    path('maps/map', display_map, name='map'),
]
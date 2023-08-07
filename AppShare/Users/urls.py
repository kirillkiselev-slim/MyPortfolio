from django.contrib import admin
from Users.views import homepage, register_request, login_request, logoutUser
from django.urls import path


APP_NAME = 'users'
urlpatterns = [
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logoutUser, name='logout'),
]

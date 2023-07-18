from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import requests
from .forms import UserCountry
from django.contrib import messages
from .models import Location  #UserLocation
import folium
import csv

@login_required()
def country(request):
    countries = Location.objects.all()
    if request.method == 'POST':
        form = UserCountry(request.POST)
        if form.is_valid():
            country = form.cleaned_data.get('country')
            user_location, created = UserLocation.objects.get_or_create(user=request.user)

            # Update the user_country field with the chosen country
            user_location.user_country = country
            user_location.save()
            return redirect('./map')
        else:
            messages.error(request, "Make sure to choose your country")
    else:
        form = UserCountry()
    context = {'countries': countries,'form': form}
    return render(request, 'maps/country.html', context)

@login_required()
def display_map(request):
    user_countries = UserLocation.objects.all()
    print(user_countries)

    # Get all countries with their coordinates
    countries = Location.objects.all()
    print(countries)

    # Create a list to store the usernames and countries
    country_usernames = {}

    for user_country in user_countries:
        # Find the corresponding country object
        country = countries.get(country=user_country.user_country)

        # Get the coordinates of the country
        #coordinates = (country.latitude, country.longitude)

        # Add the username to the country's list of usernames
        if country.country not in country_usernames:
            country_usernames[country.country] = []
        country_usernames[country.country].append(user_country.user.username)

    context = {'country_usernames': country_usernames, 'countries':countries}
    return render(request, 'maps/map.html', context)






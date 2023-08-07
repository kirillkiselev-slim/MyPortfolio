from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserCountry
from django.contrib import messages
from .models import Location, UserLocation


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

    countries = Location.objects.all()

    country_usernames = {}

    for user_country in user_countries:
        # Find the corresponding country object
        country = countries.get(country=user_country.user_country)

        # Add the username to the country's list of usernames
        if country.country not in country_usernames:
            country_usernames[country.country] = []
        country_usernames[country.country].append(user_country.user.username)

    context = {'country_usernames': country_usernames, 'countries':countries}
    return render(request, 'maps/map.html', context)






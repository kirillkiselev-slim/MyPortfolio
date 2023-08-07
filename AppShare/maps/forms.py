from django import forms
from .models import Location


class UserCountry(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["country"]

    def clean_country(self, *args, **kwargs):
        country = self.cleaned_data.get('country')
        countries = []
        for location in Location.objects.all():
            countries.append(location.country)
        if country not in countries:
                raise forms.ValidationError("Not a valid country")
        return country

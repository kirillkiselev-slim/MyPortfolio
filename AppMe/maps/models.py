from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    country = models.CharField(max_length=200)
    latitude = models.FloatField(default=55.7512)
    longitude = models.FloatField(default=37.6174)


    def __str__(self):
        return self.country


class UserLocation(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # country = models.ForeignKey(Location, on_delete=models.CASCADE)
#
    user_country = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user_country

# Create your models here.

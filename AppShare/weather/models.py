from django.db import models
from django.contrib.auth.models import User
class UserCity(models.Model):
    city = models.CharField(max_length=160)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
       return self.city

# Create your models here.

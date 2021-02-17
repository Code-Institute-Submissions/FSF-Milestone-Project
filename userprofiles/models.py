from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


# class taken from tutorials with the addition of name, more or less.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    second_name = models.CharField(max_length=30, blank=True)
    country = CountryField(blank_label="Choose Country *", blank=True)
    county = models.CharField(max_length=60, blank=True)
    town_city = models.CharField(max_length=30)
    address1 = models.CharField(max_length=80, blank=False)
    address2 = models.CharField(max_length=80, blank=True)
    postcode = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

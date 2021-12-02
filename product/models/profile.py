import re

import geopy
from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import reverse


geolocator = geopy.Nominatim(user_agent='greenier')


def phone_number_validator(value):
    if len(value) != 10:
        if not re.match(r'^\+?1?\d{9,15}$', value):
            raise ValidationError('The phone number did not match the requirements.')


class Profile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100)
    points = models.DecimalField(default=0, max_digits=30, decimal_places=2)
    rating = models.DecimalField(default=4.0, max_digits=2, decimal_places=1)

    def __str__(self):
        return self.user.username

    def update_geocode(self):
        if self.location:
            try:
                location = geolocator.geocode(self.location)
                if location == None:
                    raise ValidationError('The location could not be found.')
                geocode = Geocode.objects.get_or_create(profile=self)[0]
                geocode.update_geocode(location.latitude, location.longitude, location.raw)
                geocode.save()
            except geopy.exc.GeocoderTimedOut:
                pass

    @property
    def valid(self):
        try:
            self.full_clean()
            return True
        except ValidationError:
            return False

    def clean(self):
        if self.phone:
            phone_number_validator(self.phone)
        self.update_geocode()
        return super().clean()

    def get_absolute_url(self):
        return reverse('profile_detail', args=[self.user.username])


class Geocode(models.Model):
    profile = models.OneToOneField(Profile, related_name='geocode', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=30, decimal_places=20, default=0)
    longitude = models.DecimalField(max_digits=30, decimal_places=20, default=0)
    raw = models.TextField(max_length=500, blank=True)

    def update_geocode(self, latitude, longtitude, raw):
        self.latitude = latitude
        self.longitude = longtitude
        self.raw = raw

    def geocode(self):
        return geopy.Point(self.latitude, self.longitude)

    update_geocode.alters_data = True

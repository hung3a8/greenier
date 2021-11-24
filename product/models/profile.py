import re

from django.core.exceptions import ValidationError
from django.db import models


def phone_number_validator(value):
    if len(value) != 10:
        if not re.match(r'^\+?1?\d{9,15}$', value):
            raise ValidationError('The phone number did not match the requirements.')


class Profile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile', on_delete=models.CASCADE)
    first_name = models.TextField(max_length=30, null=True)
    last_name = models.TextField(max_length=30, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

    def clean(self):
        if self.phone:
            phone_number_validator(self.phone)
        return super().clean()

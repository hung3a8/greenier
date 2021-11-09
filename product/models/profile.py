"""
User should have: 
- name
- phone number
- email
- bio
- date of birth
- current greenier points

How can we map items with user ?
"""

import re

from django.core.exceptions import ValidationError
from django.db import models


def phone_number_validator(value):
    if len(value) != 10:
        if not re.match(r'^\+?1?\d{9,15}$', value):
            raise ValidationError("The phone number did not match the requirements.")


class Profile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254)
    bio = models.TextField(max_length=500, blank=True)

    points = models.BigIntegerField()

    def __str__(self):
        return self.user.username

    def clean(self):
        if self.phone:
            phone_number_validator(self.phone)
        return super().clean()
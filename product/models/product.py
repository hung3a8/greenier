import re

from django.core.exceptions import ValidationError
from django.db import models
from .profile import Profile

class Product(models.Model):
  name = models.CharField(max_length=100)
  cost = models.DecimalField()
  duration = models.DurationField()

  of_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  def __str__(self):
      return self.name
  

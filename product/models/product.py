from django.db import models
from django.urls import reverse
from product.models.profile import Profile


class Product(models.Model):
    of_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bought = models.BooleanField(default=False)

    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    duration = models.DurationField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

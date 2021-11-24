from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=100, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

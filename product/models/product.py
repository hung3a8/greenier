"""
A product should have:
- title
- unit & number (should we ?)
- illustration images (no more than 10, where should we store it ?)
- price
- description
- expiry date
- mapped user
Greenier points of item should be derived linearly on price
After user declare price, Greenier will add a small amount of "system tax" (maybe 5-10%), and this tax-added price
will be shown to other user inspecting and buying the item.

Preliminary, needs some more validation (maybe)
"""

from django.core.exceptions import ValidationError
from django.db import models

from .profile import Profile


class Product(models.Model):
    title = models.TextField(maxlength=100)
    images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(maxlength=1000)
    expiry = models.DurationField()

    # trying to link product with a user
    of_user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})

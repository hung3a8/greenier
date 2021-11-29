from django.db import models
from django.shortcuts import reverse

from .profile import Profile


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    seller = models.ForeignKey(Profile, null=True, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    display_image = models.CharField(max_length=200, default='', help_text='URL for image.')
    description = models.TextField(max_length=500)
    categories = models.ManyToManyField(Category, related_name='products', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

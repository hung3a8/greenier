from django.core.exceptions import ValidationError
from django.db import models


class Navbar(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()
    regex = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def clean(self):
        if self.parent is not None:
            if self.parent.parent is not None:
                raise ValidationError('Navbar child can have only one parent')
            if self.parent == self:
                raise ValidationError('Navbar can not be parent of itself')
        super(Navbar, self).clean()

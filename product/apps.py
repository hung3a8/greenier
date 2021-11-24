from django.apps import AppConfig
from django.db import DatabaseError


class ProductConfig(AppConfig):
    name = 'product'

    def ready(self):
        from . import signals, jinja2  # noqa: F401, imported for side effects

        from product.models import Profile
        from django.contrib.auth.models import User

        try:
            for user in User.objects.filter(profile=None):
                # These poor profileless users
                profile = Profile(user=user)
                profile.save()
        except DatabaseError:
            pass

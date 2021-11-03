import re

from django.conf import settings
from product.models import Navbar


def navbar(request):
    navbar = Navbar.objects.filter(parent=None).order_by('position')

    chosen_item = None
    for item in navbar:
        if re.match(item.regex, request.path):
            chosen_item = item.name
            break
        else:
            for child in item.children.all():
                if re.match(child.regex, request.path):
                    chosen_item = item.name
                    break

    return {
        'navbar_items': navbar,
        'navbar_items_chosen': chosen_item,
    }


def site_name(request):
    return {'SITE_NAME': settings.SITE_NAME,
            'SITE_LONG_NAME': settings.SITE_LONG_NAME,
            'SITE_ADMIN_EMAIL': settings.SITE_ADMIN_EMAIL}

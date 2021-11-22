from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

from product.admin.interface import FlatPageAdminCustom, NavbarAdmin
from product.admin.profile import ProfileAdmin
from product.models import Navbar, Profile

admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Profile, ProfileAdmin)
# Flat page registration
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminCustom)

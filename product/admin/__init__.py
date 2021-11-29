from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

from product.models import Category, Navbar, Product, Profile
from .interface import FlatPageAdminCustom, NavbarAdmin
from .product import CategoryAdmin, ProductAdmin
from .profile import ProfileAdmin


admin.site.register(Category, CategoryAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Product, ProductAdmin)
# Flat page registration
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminCustom)

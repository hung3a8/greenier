from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.db import models
from martor.widgets import AdminMartorWidget


class NavbarAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'active')
    search_fields = ('name', 'url')
    ordering = ('position',)


class FlatPageAdminCustom(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

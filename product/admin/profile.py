from django import forms
from django.contrib import admin

from product.models import Profile
from martor.widgets import AdminMartorWidget


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'bio': AdminMartorWidget(attrs={'cols': 80, 'rows': 10}),
        }


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User', {'fields': ['user']}),
        ('Profile', {'fields': ['bio', 'phone', 'location']}),
    ]
    form = ProfileForm
    list_display = ('user', 'phone', 'location')

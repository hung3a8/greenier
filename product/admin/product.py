from django import forms
from django.contrib.admin import ModelAdmin
from martor.widgets import AdminMartorWidget

from product.models import Product
from product.widgets import AdminHeavySelect2MultipleWidget, AdminHeavySelect2Widget


class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'seller': AdminHeavySelect2Widget(data_view='product_user_select2',
                                              attrs={'style': 'width: 100%', 'data-placeholder': 'Select a seller'}),
            'categories': AdminHeavySelect2MultipleWidget(data_view='product_category_select2',
                                                          attrs={'style': 'width: 100%'}),
            'description': AdminMartorWidget(attrs={'cols': 80, 'rows': 10}),
        }


class ProductAdmin(ModelAdmin):
    model = Product
    fieldsets = [
        ('Basic info', {'fields': ['name', 'seller']}),
        ('Product info', {'fields': ['price', 'categories', 'display_image', 'description']}),
    ]
    list_display = ('id', 'name', 'seller', 'price')
    search_fields = ('name', 'seller__username')
    form = ProductAdminForm

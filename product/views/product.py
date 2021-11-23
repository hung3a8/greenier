from django.views.generic import CreateView, UpdateView
from product.models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'cost', 'duration', 'description']
    template_name = 'product/product_create.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'cost', 'duration', 'description']
    template_name = 'product/product_update.html'

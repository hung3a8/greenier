from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from product.models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'cost', 'duration', 'description']
    template_name = 'product/product_create.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'cost', 'duration', 'description']
    template_name = 'product/product_update.html'

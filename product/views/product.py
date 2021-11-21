from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from product.models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 10
    template_name = 'product/product_list.html'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'cost', 'duration', 'description']
    template_name = 'product/product_create.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'cost', 'duration', 'description']
    template_name = 'product/product_update.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product/product_delete.html"

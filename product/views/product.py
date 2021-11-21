from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from product.models import Product

class ProductListView(ListView):
    model = Product
    paginate_by = 10

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'cost', 'duration', 'description']

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'cost', 'duration', 'description']

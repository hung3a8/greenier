from django.views.generic import DetailView, UpdateView

from product.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product_update.html'

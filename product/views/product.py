from django.views.generic import DetailView, ListView, UpdateView

from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product_update.html'

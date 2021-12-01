from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.views.generic import DetailView, ListView, UpdateView
from martor.templatetags.martortags import markdownify

from product.models import Cart, Category, Product


class ProductMarketView(ListView):
    paginate_by = 24
    model = Product
    template_name = 'product/market.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['only_product'] = product_detail(self.request, self.one_object_only).content.decode() \
            if self.one_object_only else None
        return context

    def get(self, request, *args, **kwargs):
        self.one_object_only = request.GET.get('id', None)
        return super().get(request, *args, **kwargs)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    return JsonResponse({
        'id': pk,
        'name': product.name,
        'price': product.price,
        'seller': product.seller.user.username,
        'description': mark_safe(markdownify(product.description)),
        'category': [category.name for category in product.categories.all()],
        'carousel': product.display_image.split('\n'),
    })


class ProductCartView(LoginRequiredMixin, DetailView):
    model = Cart

    template_name = 'product/cart.html'

    def get_object(self, queryset=None):
        try:
            return Cart.objects.get(user=self.request.user.profile)
        except Cart.DoesNotExist:
            return Cart.objects.create(user=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


def update_cart(request):
    pk = request.POST.get('id', None)
    quantity = request.POST.get('quantity', None)
    cart = request.user.profile.cart
    if quantity == 'DEL':
        result = cart.delete_product(pk)
    else:
        result = cart.update_cart(pk, quantity)
    return JsonResponse({
        'result': 'Success' if result else 'Fail',
        'id': pk,
        'quantity': quantity,
    }, status=200 if result else 400)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product_update.html'

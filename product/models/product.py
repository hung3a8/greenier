from django.db import models
from django.shortcuts import reverse

from .profile import Profile


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    seller = models.ForeignKey(Profile, null=True, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    display_image = models.TextField(default='', help_text='URL for image.')
    description = models.TextField(max_length=500)
    categories = models.ManyToManyField(Category, related_name='products', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_market') + '?id=' + str(self.id)


class Cart(models.Model):
    user = models.OneToOneField(Profile, related_name='cart', on_delete=models.CASCADE,
                                help_text='User who owns this cart. There can only be one cart per user.')
    products = models.ManyToManyField(Product, related_name='carts', through='CartProduct', blank=True)

    def __str__(self):
        return self.user.user.username + "'s cart"

    def get_absolute_url(self):
        return reverse('cart_detail', args=[str(self.id)])

    def update_cart(self, product_id, quantity):
        """
        Add new product or update the quantity of a product in the cart.
        """
        try:
            cart_product = self.cart_products.get(product__pk=product_id)
            cart_product.quantity = quantity
            cart_product.save()
            print(cart_product.quantity)
            return True
        except CartProduct.DoesNotExist:
            product = Product.objects.get(pk=product_id)
            cart_product = self.cart_products.create(cart=self, product=product, quantity=quantity)
            return True
        except Exception:
            return False

    def delete_product(self, product_id):
        """
        Remove a product from the cart.
        """
        try:
            self.cart_products.get(product__pk=product_id).delete()
            return True
        except CartProduct.DoesNotExist:
            return False


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

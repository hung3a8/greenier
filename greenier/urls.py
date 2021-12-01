"""greenier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from product.views import TitledView, home, product, profile, register, user, widgets
from product.views.select2 import CategorySelect2View, UserSelect2View


register_patterns = [
    url(r'^login/$', user.CustomLoginView.as_view(), name='auth_login'),
    url(r'^logout/$', user.UserLogoutView.as_view(), name='auth_logout'),
    url(r'^register/$', register.RegistrationView.as_view(), name='registration_register'),
    url(r'^register/complete$',
        TitledView.as_view(title='Registration completed', template_name='registration/registration_complete.html'),
        name='registration_complete'),
    url(r'^register/closed/$',
        TitledView.as_view(title='Registraion closed', template_name='registration/registration_closed.html'),
        name='registration_closed'),
    url(r'^activate/complete/$',
        TitledView.as_view(title='Activation completed', template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$', register.ActivationView.as_view(), name='registration_activate'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^martor/', include('martor.urls')),
    path('accounts/', include(register_patterns)),
    url(r'^$', home.HomePageView.as_view(), name='home'),
    url(r'^user/(?P<user>[\w-]+)/', include([
        url(r'^$', profile.ProfileDetailView.as_view(), name='profile_detail'),
        url(r'^update$', profile.ProfileUpdateView.as_view(), name='profile_update'),
    ])),

    url(r'^market/(?P<page>\d+)?$', product.ProductMarketView.as_view(), name='product_market'),
    url(r'^cart/', include([
        url(r'^$', product.ProductCartView.as_view(), name='cart_detail'),
        url(r'^update$', product.update_cart, name='cart_update'),
    ])),

    url(r'^product/', include([
        url(r'^(?P<pk>\d+)/', include([
            url(r'^$', product.product_detail, name='product_detail'),
            url(r'^edit/$', product.ProductUpdateView.as_view(), name='product_update'),
        ])),
        url(r'^create/$', product.ProductCreateView.as_view(), name='product_create'),
    ])),

    url(r'^product-select2/', include([
        url(r'^user/$', UserSelect2View.as_view(), name='product_user_select2'),
        url(r'^category/$', CategorySelect2View.as_view(), name='product_category_select2'),
    ])),

    url(r'^api/', include([
        url(r'^filemage/upload/$', widgets.upload_image, name='filemage_upload'),
    ])),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

try:
    with open(os.path.join(os.path.dirname(__file__), 'local_urls.py')) as f:
        exec(f.read(), globals())
except IOError:
    pass

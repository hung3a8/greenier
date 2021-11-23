"""apicta URL Configuration

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
from product.views import TitledView, home, register, user
from product.urls import profile
from product.views.profile import ProfileDetailView, ProfileUpdateView

register_patterns = [
    url(r'^login/$', user.CustomLoginView.as_view(), name='auth_login'),
    url(r'^logout/$', user.UserLogoutView.as_view(), name='auth_logout'),
    url(r'^register/$', register.RegistrationView.as_view(), name='registration_register'),
    url(r'^register/complete$',
        TitledView.as_view(title="Registration completed", template_name='registration/registration_complete.html'),
        name='registration_complete'),
    url(r'^register/closed/$',
        TitledView.as_view(title="Registraion closed", template_name='registration/registration_closed.html'),
        name='registration_closed'),
    url(r'^activate/complete/$',
        TitledView.as_view(title="Activation completed", template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$', register.ActivationView.as_view(), name='registration_activate'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^martor/', include('martor.urls')),
    path('accounts/', include(register_patterns)),
    url(r'^$', home.HomePageView.as_view(), name='home'),
    path('user/', include([
        path('<str:username>/', include([
            path('', ProfileDetailView.as_view(), name='profile-detail'),
            path('update/', ProfileUpdateView.as_view(), name='profile-update'),
        ])),
    ])),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

try:
    with open(os.path.join(os.path.dirname(__file__), 'local_urls.py')) as f:
        exec(f.read(), globals())
except IOError:
    pass

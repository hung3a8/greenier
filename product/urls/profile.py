"""
Product URL configurations
"""

from django.conf.urls import include
from django.urls import path
from product.views.profile import ProfileDetailView, ProfileUpdateView
from product.views.product import ProductListView, ProductCreateView, ProductUpdateView

app_name = "profile"
urlpatterns = [
    path('user/', include([
        path('<str:username>/', include([
            path('', ProfileDetailView.as_view(), name='profile-detail'),
            path('update/', ProfileUpdateView.as_view(), name='profile-update'),
            path('product/', include([
                path('', ProductListView.as_view(), name='product-list'),
                path('create/', ProductCreateView.as_view(), name='product-create'),
                path('<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
                # path('<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete')
            ])),
        ])),
    ])),
]

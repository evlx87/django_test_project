from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, ContactsView, ProductView, ProductCreateView, ProductDetailView, ProductDeleteView, \
    ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product', ProductView.as_view(), name="product-detail"),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product-view'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product-delete'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
]

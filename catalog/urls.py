from django.urls import path

from catalog.views import IndexView, ContactsView, ProductView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product', ProductView.as_view(), name="product-detail"),
]

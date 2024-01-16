from django.urls import path

from catalog.views import IndexView, ContactsView, ProductView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product', ProductView.as_view(), name="product-detail"),
]

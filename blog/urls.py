from django.urls import path

from blog.views import BlogList, BlogCreate, BlogDetail, BlogUpdate, BlogDelete
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogList.as_view(), name='blog'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetail.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDelete.as_view(), name='delete'),
]

from django.shortcuts import render
from catalog.models import Product


def index(request):
    context = {
        'page_title': 'Главная',
        'objects_list': Product.objects.all()
    }
    return render(request, 'index.html', context)


def contacts(request):
    context = {
        'page_title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'contacts.html', context)


def product(request):
    context = {
        'page_title': 'Товары',
        'objects_list': Product.objects.all()
    }
    return render(request, 'product.html', context)

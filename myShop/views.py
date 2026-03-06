from django.shortcuts import render
from myShop.models import Category, Product


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def category_products_view(request, id):
    products = Product.objects.filter(category_id=id)
    return render(request, 'category_products.html', {'products': products})
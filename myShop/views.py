from django.views import generic
from myShop.models import Category, Product


class CategoryListView(generic.ListView):
    template_name = 'categories.html'
    model = Category
    context_object_name = 'categories'


class ProductListView(generic.ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'


class CategoryProductsView(generic.ListView):
    template_name = 'category_products.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('id')
        return self.model.objects.filter(category_id=category_id)
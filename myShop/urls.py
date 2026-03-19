from django.urls import path
from myShop.views import CategoryListView, ProductListView, CategoryProductsView


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/', ProductListView.as_view(), name='products'),
    path('categories/<int:id>/', CategoryProductsView.as_view(), name='category_products'),
]
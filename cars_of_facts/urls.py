from django.urls import path
from cars_of_facts.views import bmw, audi, mercedes, cars_list_view, cars_detail_view

urlpatterns = [
    path('bmw/', bmw),
    path('audi/', audi),
    path('mercedes/', mercedes),
    path('cars/', cars_list_view),
    path('cars/<int:id>/', cars_detail_view),
]
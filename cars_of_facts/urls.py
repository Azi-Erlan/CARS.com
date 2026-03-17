from django.urls import path
from cars_of_facts.views import bmw, audi, mercedes, cars_list_view, cars_detail_view, search_car_view

app_name = 'cars'

urlpatterns = [
    path('', cars_list_view, name='cars'),  # только здесь name
    path('cars/<int:id>/', cars_detail_view),
    path('search/', search_car_view),
    
    path('bmw/', bmw),
    path('audi/', audi),
    path('mercedes/', mercedes),
]
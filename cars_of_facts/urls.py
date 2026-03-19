from django.urls import path
from cars_of_facts.views import CarListView, CarDetailView, SearchCarView, BmwView, AudiView, MercedesView


app_name = 'cars'

urlpatterns = [
    path('', CarListView.as_view(), name='cars'),
    path('cars/<int:id>/', CarDetailView.as_view(), name='car_detail'),
    path('search/', SearchCarView.as_view(), name='search'),

    path('bmw/', BmwView.as_view()),
    path('audi/', AudiView.as_view()),
    path('mercedes/', MercedesView.as_view()),
]
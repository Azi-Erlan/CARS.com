from django.urls import path
from cars_of_facts.views import bmw, audi, mercedes

urlpatterns = [
    path('bmw/', bmw),
    path('audi/', audi),
    path('mercedes/', mercedes),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view),
    path('login/', views.auth_login_view),
        path('congratulation/', views.cong_view),
]
from django.urls import path
from drivers.views import DriverCreateView, DriverListView, DriverUpdateView, DriverDeleteView


urlpatterns = [
    path('create_driver/', DriverCreateView.as_view(), name='create_driver'),
    path('drivers_list/', DriverListView.as_view(), name='drivers_list'),
    path('update_driver/<int:id>/', DriverUpdateView.as_view(), name='update_driver'),
    path('delete_driver/<int:id>/', DriverDeleteView.as_view(), name='delete_driver'),
]
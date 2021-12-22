from django.urls import path
from .views import reservations_list, update_reservation

urlpatterns = [
    path('reservations/', reservations_list, name='reservations_list'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reserve')
]
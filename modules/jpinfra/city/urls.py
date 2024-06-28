from django.urls import path
from .views import CityListCreateView

urlpatterns = [
    path('cities/', CityListCreateView.as_view(), name='cities-list-create'),
    path('cities/<int:pk>/', CityListCreateView.as_view(), name='cities-detail'),
]
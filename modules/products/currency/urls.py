from django.urls import path
from .views import CurrencyListCreateView

urlpatterns = [
    path('currency/', CurrencyListCreateView.as_view(), name='currency-list-create'),
    path('currency/<int:pk>/', CurrencyListCreateView.as_view(), name='currency-detail'),
]

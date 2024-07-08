from django.urls import path
from .views import PaymentModeListCreateView

urlpatterns = [
    path('payment_mode/', PaymentModeListCreateView.as_view(), name='payment_mode-list-create'),
    path('payment_mode/<int:pk>/', PaymentModeListCreateView.as_view(), name='payment_mode-detail'),
]

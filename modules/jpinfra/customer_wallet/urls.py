from django.urls import path
from .views import CustomerWalletListCreateView

urlpatterns = [
    path('customer_wallets/', CustomerWalletListCreateView.as_view(), name='customer_wallet-list-create'),
    path('customer_wallets/<int:pk>/', CustomerWalletListCreateView.as_view(), name='customer_wallet-detail'),
]

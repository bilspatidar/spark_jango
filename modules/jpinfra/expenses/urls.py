from django.urls import path
from .views import ExpenseListCreateView

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expenses-list-create'),
    path('expenses/<int:pk>/', ExpenseListCreateView.as_view(), name='expenses-detail'),
]

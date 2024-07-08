from django.urls import path
from .views import ExpenseCategoryListCreateView

urlpatterns = [
    path('expense_categories/', ExpenseCategoryListCreateView.as_view(), name='expense_categories-list-create'),
    path('expense_categories/<int:pk>/', ExpenseCategoryListCreateView.as_view(), name='expense_categories-detail'),
]

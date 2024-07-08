from django.urls import path
from .views import EmployeeListCreateView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employees-list-create'),
    path('employees/<int:pk>/', EmployeeListCreateView.as_view(), name='employees-detail'),
]

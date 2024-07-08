from django.urls import path
from .views import MachineListCreateView

urlpatterns = [
    path('machines/', MachineListCreateView.as_view(), name='machines-list-create'),
    path('machines/<int:pk>/', MachineListCreateView.as_view(), name='machines-detail'),
]

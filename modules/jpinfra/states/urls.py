from django.urls import path
from .views import StateListCreateView

urlpatterns = [
    path('states/', StateListCreateView.as_view(), name='states-list-create'),
    path('states/<int:pk>/', StateListCreateView.as_view(), name='states-detail'),
]

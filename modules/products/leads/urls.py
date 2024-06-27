from django.urls import path
from .views import LeadListCreateView

urlpatterns = [
    path('leads/', LeadListCreateView.as_view(), name='leads-list-create'),
    path('leads/<int:pk>/', LeadListCreateView.as_view(), name='leads-detail'),
]

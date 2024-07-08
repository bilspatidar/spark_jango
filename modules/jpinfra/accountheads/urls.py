from django.urls import path
from .views import AccountHeadListCreateView

urlpatterns = [
    path('accountheads/', AccountHeadListCreateView.as_view(), name='accounthead-list-create'),
    path('accountheads/<int:pk>/', AccountHeadListCreateView.as_view(), name='accounthead-detail'),
]

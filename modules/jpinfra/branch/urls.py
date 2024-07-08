from django.urls import path
from .views import BranchListCreateView

urlpatterns = [
    path('branch/', BranchListCreateView.as_view(), name='branch-list-create'),
    path('branch/<int:pk>/', BranchListCreateView.as_view(), name='branch-detail'),
]

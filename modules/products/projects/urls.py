from django.urls import path
from .views import ProjectListCreateView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='projects-list-create'),
    path('projects/<int:pk>/', ProjectListCreateView.as_view(), name='projects-detail'),
]

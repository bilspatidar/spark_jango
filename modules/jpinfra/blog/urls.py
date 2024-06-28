from django.urls import path
from .views import BlogListCreateView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blogs-list-create'),
    path('blogs/<int:pk>/', BlogListCreateView.as_view(), name='blogs-detail'),
]

from django.urls import path
from .views import CategoryListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryListCreateView.as_view(), name='category-detail'),
]

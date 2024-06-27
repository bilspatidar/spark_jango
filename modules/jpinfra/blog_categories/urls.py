from django.urls import path
from .views import BlogCategoryListCreateView

urlpatterns = [
    path('blog_categories/', BlogCategoryListCreateView.as_view(), name='blog-category-list-create'),
    path('blog_categories/<int:pk>/', BlogCategoryListCreateView.as_view(), name='blog-category-detail'),
]

from django.urls import path
from .views import SubCategoryCustomView

urlpatterns = [
    path('subcategories/', SubCategoryCustomView.as_view(), name='subcategory-create'),
    path('subcategories/<int:pk>/', SubCategoryCustomView.as_view(), name='subcategory-detail'),
]

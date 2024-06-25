from django.urls import path
from .views import DocumentTypeCustomView

urlpatterns = [
    path('document_type/', DocumentTypeCustomView.as_view(), name='document_type-create'),
    path('document_type/<int:pk>/', DocumentTypeCustomView.as_view(), name='document_type-detail'),
]

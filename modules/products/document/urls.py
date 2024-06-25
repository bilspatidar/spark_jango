from django.urls import path
from .views import DocumentCustomView

urlpatterns = [
    path('document/', DocumentCustomView.as_view(), name='document-create'),
    path('document/<int:pk>/', DocumentCustomView.as_view(), name='document-detail'),
]
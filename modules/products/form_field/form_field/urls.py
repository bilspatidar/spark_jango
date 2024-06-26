from django.urls import path
from .views import FormFieldListCreateView

urlpatterns = [
    path('form_fields/', FormFieldListCreateView.as_view(), name='form-field-list-create'),
    path('form_fields/<int:pk>/', FormFieldListCreateView.as_view(), name='form-field-detail'),
]
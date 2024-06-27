from django.urls import path
from .views import ServiceCustomView

urlpatterns = [
    path('service/', ServiceCustomView.as_view(), name='service-create'),
    path('service/<int:pk>/', ServiceCustomView.as_view(), name='service-detail'),
]

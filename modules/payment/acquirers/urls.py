from django.urls import path
from .views import AcquirerListCreateView

urlpatterns = [
    path('acquirers/', AcquirerListCreateView.as_view(), name='acquirers-list-create'),
    path('acquirers/<int:pk>/', AcquirerListCreateView.as_view(), name='acquirers-detail'),
]

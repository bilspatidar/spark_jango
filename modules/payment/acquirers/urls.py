from django.urls import path
from .views import AcquirerListCreateView

urlpatterns = [
    path('acquirers/', AcquirerListCreateView.as_view(), name='acquirer-list-create'),
    path('acquirers/<int:pk>/', AcquirerListCreateView.as_view(), name='acquirer-detail'),
]

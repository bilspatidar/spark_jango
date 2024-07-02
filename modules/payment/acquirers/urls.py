from django.urls import path
from .views import AcquirerListCreateView

urlpatterns = [
<<<<<<< HEAD
    path('acquirers/', AcquirerListCreateView.as_view(), name='acquirers-list-create'),
    path('acquirers/<int:pk>/', AcquirerListCreateView.as_view(), name='acquirers-detail'),
=======
    path('acquirers/', AcquirerListCreateView.as_view(), name='acquirer-list-create'),
    path('acquirers/<int:pk>/', AcquirerListCreateView.as_view(), name='acquirer-detail'),
>>>>>>> 657db95 (Payment Complete)
]

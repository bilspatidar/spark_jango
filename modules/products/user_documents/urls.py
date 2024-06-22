from django.urls import path
from .views import UserDocumentCustomView

urlpatterns = [
    path('userdocuments/', UserDocumentCustomView.as_view(), name='userdocument-create'),
    path('userdocuments/<int:pk>/', UserDocumentCustomView.as_view(), name='userdocument-detail'),
]
 
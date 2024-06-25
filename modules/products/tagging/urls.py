from django.urls import path
from .views import TaggingCustomViewList

urlpatterns = [
    path('tagging/', TaggingCustomViewList.as_view(), name='tagging-create'),
    path('tagging/<int:pk>/', TaggingCustomViewList.as_view(), name='tagging-detail'),
]

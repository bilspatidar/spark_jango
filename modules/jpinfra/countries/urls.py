from django.urls import path
from .views import CountryListCreateView

urlpatterns = [
    path('countries/', CountryListCreateView.as_view(), name='countries-list-create'),
    path('countries/<int:pk>/', CountryListCreateView.as_view(), name='countries-detail'),
]

from django.urls import path
from .views import FaqListCreateView

urlpatterns = [
    path('faqs/', FaqListCreateView.as_view(), name='faq-list-create'),
    path('faqs/<int:pk>/', FaqListCreateView.as_view(), name='faq-detail'),
]

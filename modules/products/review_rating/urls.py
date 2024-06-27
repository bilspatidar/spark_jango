from django.urls import path
from .views import ReviewRatingListCreateView

urlpatterns = [
    path('review_rating/', ReviewRatingListCreateView.as_view(), name='review-rating-list-create'),
    path('review_rating/<int:pk>/', ReviewRatingListCreateView.as_view(), name='review-rating-detail'),
]

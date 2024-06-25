from rest_framework import serializers
from .models import ReviewRating
from django.contrib.auth.models import User
from utils.common_helpers import format_datetime 
from utils.base64_helpers import Base64ImageField

class ReviewRatingSerializer(serializers.ModelSerializer):
    
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = ReviewRating
        fields = ['id', 'service_id', 'image', 'rating', 'review', 'date', 'date_created', 'date_updated', 'user_created', 'user_updated']
        extra_kwargs = {
            'image': {'required': False}
        }  

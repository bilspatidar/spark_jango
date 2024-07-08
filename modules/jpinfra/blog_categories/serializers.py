from rest_framework import serializers
from .models import BlogCategory
from django.contrib.auth.models import User
from utils.base64_helpers import Base64ImageField
from utils.common_helpers import format_datetime 

class BlogCategorySerializer(serializers.ModelSerializer):
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'image', 'status', 'date_created', 'date_updated', 'user_created', 'user_updated']
        extra_kwargs = {
            'image': {'required': False},
            'status': {'required': False},
            
        }
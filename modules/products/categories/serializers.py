from rest_framework import serializers
from .models import Category
from django.contrib.auth.models import User
# from .common_helper import  format_datetime
from utils.common_helpers import format_datetime 
from utils.base64_helpers import Base64ImageField

class CategorySerializer(serializers.ModelSerializer):
    
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'status', 'image', 'slug', 'date_created', 'date_updated', 'user_created', 'user_updated']
        extra_kwargs = {
            'image': {'required': False},
            'status': {'required': False}
        }  

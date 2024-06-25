from rest_framework import serializers
from .models import Service
from modules.products.categories.serializers import CategorySerializer
from modules.products.categories.models import Category
from modules.products.subcategories.models import SubCategory
from modules.products.subcategories.serializers import SubCategorySerializer
from django.contrib.auth.models import User
from utils.common_helpers import format_datetime
from utils.base64_helpers import Base64ImageField

class ServiceSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_details = CategorySerializer(source='category', read_only=True)
    subcategory = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())
    subcategory_details = SubCategorySerializer(source='subcategory', read_only=True)
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    images = Base64ImageField(required=False)
    icon = Base64ImageField(required=False)

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'slug', 'icon', 'category', 'category_details', 
            'subcategory', 'subcategory_details', 'images', 'date_created', 
            'date_updated', 'user_created', 'user_updated'
        ]
        extra_kwargs = {
            'images': {'required': False},
            'icon': {'required': False},
            'status': {'required': False},
            'category': {'required': False},
            'subcategory': {'required': False}
        }


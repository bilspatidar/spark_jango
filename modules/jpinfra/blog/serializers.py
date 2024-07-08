from rest_framework import serializers
from .models import Blog
from modules.jpinfra.blog_categories.serializers import BlogCategorySerializer
from modules.jpinfra.blog_categories.models import BlogCategory
from django.contrib.auth.models import User
from utils.base64_helpers import Base64ImageField

class BlogSerializer(serializers.ModelSerializer):
    blog_category = serializers.PrimaryKeyRelatedField(queryset=BlogCategory.objects.all())
    blog_category_details = BlogCategorySerializer(source='blog_category', read_only=True)
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'blog_category', 'blog_category_details', 'status', 'image', 'description', 'date_created', 'date_updated', 'user_created', 'user_updated']  
        extra_kwargs = {
            'image': {'required': False},
            'status': {'required': False}
        }

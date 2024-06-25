# modules/products/document/serializers.py

from rest_framework import serializers
from .models import Document
from django.contrib.auth.models import User
from utils.base64_helpers import Base64ImageField

class DocumentSerializer(serializers.ModelSerializer):
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    sample = Base64ImageField(required=False)

    class Meta:
        model = Document
        fields = ['id', 'name', 'side', 'sample', 'status', 'date_created', 'date_updated', 'user_created', 'user_updated']
        extra_kwargs = {
            'status': {'required': False}
        }



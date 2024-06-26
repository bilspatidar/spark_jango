from rest_framework import serializers
from .models import DocumentType
from django.contrib.auth.models import User
from utils.common_helpers import format_datetime

class DocumentTypeSerializer(serializers.ModelSerializer):
    
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)

    class Meta:
        model = DocumentType
        fields = ['id', 'name', 'status', 'date_created', 'date_updated', 'user_created', 'user_updated']
        extra_kwargs = {
            'status': {'required': False}
        }  

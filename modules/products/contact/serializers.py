from rest_framework import serializers
from .models import Contact
from django.contrib.auth.models import User
from utils.common_helpers import format_datetime
from utils.base64_helpers import Base64ImageField

class ContactSerializer(serializers.ModelSerializer):
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'address', 'message', 'status', 'date_created', 'date_updated', 'user_created', 'user_updated']
        extra_kwargs = {
            'status': {'required': False}
        }

from rest_framework import serializers
from .models import Machine
from django.contrib.auth.models import User
from utils.base64_helpers import Base64ImageField

class MachineSerializer(serializers.ModelSerializer):
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = Machine
        fields = [
            'id', 'name', 'image', 'code', 'description', 'status',
            'date_created', 'date_updated', 'user_created', 'user_updated'
        ]
        extra_kwargs = {
            'status': {'required': False},
            'description': {'required': False},
            'image': {'required': False}
        }

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Tagging
from user.serializers import UserSerializer
from utils.base64_helpers import Base64ImageField

# Get the CustomUser model
User = get_user_model()

class TaggingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    verified_details = UserSerializer(source='user', read_only=True)
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = Tagging
        fields = [
            'id', 'booking_id', 'user', 'verified_details', 'status', 'image', 'next_date', 'followup_date', 'date_created', 'date_updated', 'user_created', 'user_updated'
        ]
        extra_kwargs = {
            'status': {'required': False},
            'followup_date': {'required': False},
            'next_date': {'required': False}
        }

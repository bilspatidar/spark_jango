from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserDocument
from user.serializers import UserSerializer
from utils.base64_helpers import Base64ImageField

# Get the CustomUser model
User = get_user_model()

class UserDocumentSerializer(serializers.ModelSerializer):
    verified_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    verified_details = UserSerializer(source='verified_by', read_only=True)
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    front_image = Base64ImageField(required=False)
    back_image = Base64ImageField(required=False)

    class Meta:
        model = UserDocument
        fields = [
            'id', 'document_id', 'verified_by', 'verified_details', 'status', 
            'front_image', 'back_image', 'is_verified', 'verified_date', 
            'date_created', 'date_updated', 'user_created', 'user_updated'
        ]
        extra_kwargs = {
            'front_image': {'required': False},
            'back_image': {'required': False},
            'status': {'required': False},
            'verified_by': {'required': False},
            'is_verified': {'required': False},
            'verified_date': {'required': False}
        }

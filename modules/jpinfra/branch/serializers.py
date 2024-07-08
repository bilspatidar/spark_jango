from rest_framework import serializers
from .models import Branch
from django.contrib.auth.models import User
from utils.common_helpers import format_datetime 
from utils.base64_helpers import Base64ImageField

class BranchSerializer(serializers.ModelSerializer):
    
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    branch_image = Base64ImageField(required=False)

    class Meta:
        model = Branch
        fields = [
            'id', 'name', 'branch_phone', 'side_code', 'branch_email', 'branch_address',
            'branch_location', 'city', 'lang', 'latt', 'country_id', 'state_id', 'city_id',
            'area_name', 'branch_image', 'status', 'date_created', 'date_updated', 'user_created', 'user_updated'
        ]
        extra_kwargs = {
            'branch_image': {'required': False},
            'status': {'required': False}
        }  
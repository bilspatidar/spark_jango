from rest_framework import serializers
from .models import FormField
from django.contrib.auth.models import User
from utils.common_helpers import format_datetime 

class FormFieldSerializer(serializers.ModelSerializer):
    
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)

    class Meta:
        model = FormField
        fields = ['id', 'lable', 'type', 'type_id', 'field_type', 'field_value', 'default_value', 'is_required', 'date_created', 'date_updated', 'user_created', 'user_updated']
        extra_kwargs = {
            'field_value': {'required': False},
            'default_value': {'required': False}
        }  

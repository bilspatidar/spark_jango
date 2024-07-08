from rest_framework import serializers
from .models import PaymentMode
from django.contrib.auth.models import User

class PaymentModeSerializer(serializers.ModelSerializer):
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)

    class Meta:
        model = PaymentMode
        fields = [
            'id', 'name', 'description', 'status',
            'date_created', 'date_updated', 'user_created', 'user_updated'
        ]
        extra_kwargs = {
            'status': {'required': False},
            'description': {'required': False}
        }

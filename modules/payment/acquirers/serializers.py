from rest_framework import serializers
from .models import Acquirer
from django.contrib.auth.models import User

class AcquirerSerializer(serializers.ModelSerializer):
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)

    class Meta:
        model = Acquirer
<<<<<<< HEAD
        fields = [
            'id', 'encription_key', 'name', 'country', 'currency', 'prod_url',
            'prod_key', 'prod_secret', 'sandbox_url', 'sandbox_key',
            'sandbox_secret', 'status', 'min_value', 'max_value', 'daily_value',
            'cards', 'date_created', 'date_updated', 'user_created', 'user_updated'
        ]
=======
        fields = ['id', 'encription_key', 'name', 'country', 'currency', 'prod_url', 'prod_key', 'prod_secret', 'sandbox_url', 'sandbox_key', 'sandbox_secret', 'status', 'min_value', 'max_value', 'daily_value', 'cards', 'date_created', 'date_updated', 'user_created', 'user_updated']
>>>>>>> 657db95 (Payment Complete)
        extra_kwargs = {
            'status': {'required': False}
        }

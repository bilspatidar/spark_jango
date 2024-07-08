from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)

    class Meta:
        model = Lead
        fields = ['id', 'fullname', 'email', 'phone', 'address', 'pincode', 'state', 'city', 'landmark', 'service_id', 'service_form_id', 'status', 'description', 'date_created', 'date_updated', 'user_created', 'user_updated']
        extra_kwargs = {
            'status': {'required': False}
        }

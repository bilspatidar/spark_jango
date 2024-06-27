from rest_framework import serializers
from .models import Project
from user.models import CustomUser 

class ProjectSerializer(serializers.ModelSerializer):
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    customer = serializers.CharField(source='customer.username', read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='customer')

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'charge_type', 'total_budget', 'currency', 'total_hours', 'hourly_rate', 'status', 'customer', 'customer_id', 'date_created', 'date_updated', 'user_created', 'user_updated']
        extra_kwargs = {
            'status': {'required': False}
        }

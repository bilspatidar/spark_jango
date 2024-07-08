from rest_framework import serializers
from .models import Expense
from django.contrib.auth.models import User
from utils.base64_helpers import Base64ImageField

class ExpenseSerializer(serializers.ModelSerializer):
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = Expense
        fields = [
            'id', 'title', 'expense_category', 'amount', 'payment_mode',
            'admin_remarks', 'remarks', 'status', 'parts_name', 'machine', 'employee',
            'salary_month', 'image', 'date_created', 'date_updated', 'user_created', 'user_updated'
        ]
        extra_kwargs = {
            'status': {'required': False},
            'admin_remarks': {'required': False},
            'remarks': {'required': False},
            'image': {'required': False}
        }

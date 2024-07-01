from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile  

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'first_name', 'last_name', 'email', 'mobile', 'alt_mobile', 'password',
            'user_type', 'father_name', 'mother_name', 'dob', 'doj',
            'country_id', 'state_id', 'city_id', 'street_address', 'street_address2',
            'profile_pic', 'address_proof', 'id_proof', 'businessSignature', 'status'
        ]
        extra_kwargs = {
            'password': {'write_only': True}, 
            'status': {'required': False} 
        }
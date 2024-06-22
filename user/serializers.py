from rest_framework import serializers
from rest_framework.response import Response
from utils.base64_helpers import Base64ImageField
from utils.common_helpers import validate_phone_number, format_datetime, validate_password
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=False)
    profile_image = Base64ImageField(required=False)
    phone = serializers.CharField(validators=[validate_phone_number], required=True)
    user_type = serializers.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    date_created = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()

    def get_date_created(self, obj):
        return format_datetime(obj.date_created)

    def get_date_updated(self, obj):
        return format_datetime(obj.date_updated)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        
        errors = {}
        
        if password and not validate_password(password):
            errors['password'] = ["Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, one digit, and one special character."]
        
        if password != confirm_password:
            errors['confirm_password'] = ["Passwords do not match"]

        email = attrs.get('email')
        if email and CustomUser.objects.filter(email=email).exists():
            errors['email'] = ["Custom user with this email already exists."]
        
        phone = attrs.get('phone')
        if phone and len(phone) != 10:
            errors['phone'] = ["Phone number must be exactly 10 digits long"]

        if errors:
            raise serializers.ValidationError(errors)
        
        return attrs

    class Meta:
        model = CustomUser
        fields = [
            'id', 'first_name', 'full_name', 'last_name', 'email', 'phone', 
            'user_type', 'status', 'profile_image', 'password', 'confirm_password', 
            'date_created', 'date_updated','is_active'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
            'profile_image': {'required': False}
        }

    def create(self, validated_data):
        profile_image = validated_data.pop('profile_image', None)
        confirm_password = validated_data.pop('confirm_password', None)
        user = CustomUser.objects.create_user(**validated_data)
        if profile_image:
            user.profile_image = profile_image
            user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("New password and confirm password do not match")
        return data

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value

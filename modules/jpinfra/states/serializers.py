from rest_framework import serializers
from .models import State
from modules.jpinfra.countries.serializers import CountrySerializer
from modules.jpinfra.countries.models import Country
from django.contrib.auth.models import User

class StateSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    country_details = CountrySerializer(source='country', read_only=True)
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)

    class Meta:
        model = State
        fields = [
            'id', 'name','country_details', 'country', 'status', 'date_created', 'date_updated', 'user_created', 'user_updated'
        ]
        extra_kwargs = {
            'status': {'required': False}
        }  
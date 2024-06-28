from rest_framework import serializers
from .models import City
from modules.jpinfra.states.serializers import StateSerializer
from modules.jpinfra.states.models import State
from django.contrib.auth.models import User

class CitySerializer(serializers.ModelSerializer):
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())
    states_details = StateSerializer(source='state', read_only=True)
    user_created = serializers.CharField(source='user_created.first_name', read_only=True)
    user_updated = serializers.CharField(source='user_updated.first_name', read_only=True)

    class Meta:
        model = City 
        fields = [
            'id', 'name','states_details', 'state', 'status', 'date_created', 'date_updated', 'user_created', 'user_updated'
        ]
        extra_kwargs = {
            'status': {'required': False}
        }  
from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from utils.common_helpers import validate_name
from rest_framework import serializers
from modules.jpinfra.states.models import State

class City(BaseModel):
    name = models.CharField(max_length=100, unique=True, validators=[validate_name])
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
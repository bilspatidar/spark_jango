from django.db import models
from django.conf import settings
from myproject.models import BaseModel

class FormField(BaseModel):
    lable = models.CharField(max_length=255, unique=False)
    type = models.CharField(max_length=255, unique=False)
    type_id = models.IntegerField(unique=False)
    field_type = models.CharField(max_length=255, unique=False)
    default_value = models.CharField(max_length=255, unique=False)
    field_value = models.TextField(blank=True, null=True) 
    default_value = models.CharField(max_length=255, blank=True, null=True)

    is_required = models.BooleanField(default=True)

    def __str__(self):
        return self.service_id

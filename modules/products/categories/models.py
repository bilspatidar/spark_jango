from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from utils.common_helpers import validate_name
from rest_framework import serializers


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True, validators=[validate_name])
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category_images/')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
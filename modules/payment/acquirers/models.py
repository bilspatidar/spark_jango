from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from utils.common_helpers import validate_name

class Acquirer(BaseModel):
    name = models.CharField(max_length=100, unique=True, validators=[validate_name])
    encription_key = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100, unique=False)
    currency = models.CharField(max_length=100, unique=False)
    prod_url = models.CharField(max_length=100, unique=False)
    prod_key = models.CharField(max_length=100, unique=False)
    prod_secret = models.CharField(max_length=100, unique=False)
    sandbox_url = models.CharField(max_length=100, unique=False)
    sandbox_key = models.CharField(max_length=100, unique=False)
    sandbox_secret = models.CharField(max_length=100, unique=False)
    min_value = models.CharField(max_length=100, unique=False)
    max_value = models.CharField(max_length=100, unique=False)
    daily_value = models.CharField(max_length=100, unique=False)
    cards = models.CharField(max_length=100, unique=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

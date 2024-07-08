from django.db import models
from django.conf import settings
from myproject.models import BaseModel

class Acquirer(BaseModel):
    encription_key = models.CharField(max_length=255)
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=10)
    prod_url = models.URLField()
    prod_key = models.CharField(max_length=255)
    prod_secret = models.CharField(max_length=255)
    sandbox_url = models.URLField()
    sandbox_key = models.CharField(max_length=255)
    sandbox_secret = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    min_value = models.DecimalField(max_digits=10, decimal_places=2)
    max_value = models.DecimalField(max_digits=10, decimal_places=2)
    daily_value = models.DecimalField(max_digits=10, decimal_places=2)
    cards = models.CharField(max_length=255)

    def __str__(self):
        return self.name

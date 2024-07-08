from django.db import models
from django.conf import settings
from myproject.models import BaseModel

class PaymentMode(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

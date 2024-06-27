from django.db import models
from django.conf import settings
from myproject.models import BaseModel


class Document(BaseModel):
    name = models.CharField(max_length=255)
    side = models.CharField(max_length=255)
    sample = models.ImageField(upload_to='samples/', null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
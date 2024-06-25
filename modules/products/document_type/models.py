from django.db import models
from django.conf import settings
from myproject.models import BaseModel


class DocumentType(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
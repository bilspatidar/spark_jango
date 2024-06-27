from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from utils.common_helpers import validate_name

class Contact(BaseModel):
    name = models.CharField(max_length=100, validators=[validate_name])
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    message = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

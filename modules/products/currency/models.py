from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from utils.common_helpers import validate_name

class Currency(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
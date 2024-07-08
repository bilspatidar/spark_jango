from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from utils.common_helpers import validate_name

class CustomerWallet(BaseModel):
    title = models.CharField(max_length=100, unique=True, validators=[validate_name])
    amount = models.FloatField()
    description = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

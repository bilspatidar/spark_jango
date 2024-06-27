from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from utils.common_helpers import validate_name

class AccountHead(BaseModel):
    name = models.CharField(max_length=100, unique=True, validators=[validate_name])
    date = models.DateField()
    type = models.CharField(max_length=50)
    accountNo = models.CharField(max_length=50, unique=False)
    openingBalance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

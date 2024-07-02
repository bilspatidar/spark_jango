from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from modules.jpinfra.countries.models import Country

class State(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
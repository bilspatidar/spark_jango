from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from user.models import CustomUser
from utils.common_helpers import validate_name

class Project(BaseModel):
    name = models.CharField(max_length=100, unique=False, validators=[validate_name])
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    charge_type = models.CharField(max_length=10, choices=[('fixed', 'Fixed'), ('hourly', 'Hourly')])
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    total_hours = models.DecimalField(max_digits=5, decimal_places=2)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, default='Pending')
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name

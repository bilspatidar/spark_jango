from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from utils.common_helpers import validate_name

class Lead(BaseModel):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    landmark = models.CharField(max_length=255)
    service_id = models.CharField(max_length=100)
    service_form_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='Pending')
    description = models.TextField()

    def __str__(self):
        return self.fullname

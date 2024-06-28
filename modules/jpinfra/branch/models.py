from django.db import models
from django.conf import settings
from myproject.models import BaseModel

class Branch(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    branch_phone = models.CharField(max_length=15)
    side_code = models.CharField(max_length=10)
    branch_email = models.EmailField(max_length=100)
    branch_address = models.TextField()
    branch_location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)
    latt = models.CharField(max_length=100)
    country_id = models.IntegerField()
    state_id = models.IntegerField()
    city_id = models.IntegerField()
    area_name = models.CharField(max_length=100)
    branch_image = models.ImageField(upload_to='uploads/branch_images/')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
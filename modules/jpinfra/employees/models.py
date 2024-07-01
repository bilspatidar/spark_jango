from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from utils.common_helpers import validate_name

class Employee(BaseModel):
    first_name = models.CharField(max_length=100, validators=[validate_name])
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    alt_mobile = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=100) 
    user_type = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    dob = models.DateField()
    doj = models.DateField()
    country_id = models.IntegerField()
    state_id = models.IntegerField()
    city_id = models.IntegerField()
    street_address = models.TextField()
    street_address2 = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='uploads/profile_pics/')
    address_proof = models.FileField(upload_to='uploads/address_proofs/')
    id_proof = models.FileField(upload_to='uploads/id_proofs/')
    businessSignature = models.ImageField(upload_to='uploads/business_signatures/')
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

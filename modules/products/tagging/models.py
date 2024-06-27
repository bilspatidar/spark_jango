from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from django.contrib.auth.models import User

class Tagging(BaseModel):
    # name = models.CharField(max_length=100, unique=True)
    booking_id = models.IntegerField(unique=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tagging')
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads/tagging/')
    followup_date = models.DateField()
    next_date = models.DateField()

    def __str__(self):
        return self.name
from django.db import models
from django.conf import settings
from myproject.models import BaseModel

class Faq(BaseModel):
    question = models.CharField(max_length=255, unique=True)
    answer = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

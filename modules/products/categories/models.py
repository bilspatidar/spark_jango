from django.db import models
from django.conf import settings
from myproject.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category_images/')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
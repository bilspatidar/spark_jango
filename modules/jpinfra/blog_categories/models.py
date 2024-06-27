from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from utils.common_helpers import validate_name

class BlogCategory(BaseModel):
    name = models.CharField(max_length=100, unique=True, validators=[validate_name])
    image = models.ImageField(upload_to='uploads/blog_category_images/')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

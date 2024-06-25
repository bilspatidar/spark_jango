from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from modules.products.categories.models import Category
from modules.products.subcategories.models import SubCategory

class Service(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='service')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='service')
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads/service_images/')
    icon = models.ImageField(upload_to='uploads/service_icon/')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
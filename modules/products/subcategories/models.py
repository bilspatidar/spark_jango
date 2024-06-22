from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from modules.products.categories.models import Category

class SubCategory(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads/sub_category_images/')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
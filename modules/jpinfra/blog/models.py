from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from modules.jpinfra.blog_categories.models import BlogCategory

class Blog(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog')
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads/blog_images/')
    description = models.TextField()

    def __str__(self):
        return self.title
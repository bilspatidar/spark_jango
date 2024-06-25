from django.db import models
from django.conf import settings
from myproject.models import BaseModel

class ReviewRating(BaseModel):
    review = models.CharField(max_length=100, unique=False)
    service_id = models.IntegerField(unique=True)
    rating = models.IntegerField(unique=True)
    date =  models.DateField(unique=False)
    image = models.ImageField(upload_to='review_rating_images/')

    def __str__(self):
        return self.service_id
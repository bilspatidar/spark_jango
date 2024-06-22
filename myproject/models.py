from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.request import Request

User = get_user_model()

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    user_updated = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')

    class Meta:
        abstract = True

@receiver(pre_save)
def update_user_fields(sender, instance, *args, **kwargs):
    # Check if the model is a subclass of BaseModel
    if issubclass(sender, BaseModel):
        # Get the current user from the request
        request = kwargs.get('request')
        if request and isinstance(request, Request):
            user = request.user
            # Set user_created and user_updated if they are not set
            if not instance.user_created:
                instance.user_created = user
            instance.user_updated = user
from django.db import models
from django.conf import settings
from myproject.models import BaseModel
from django.contrib.auth.models import User

class UserDocument(BaseModel):
    document_id = models.IntegerField(unique=True)
    # verified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_documents')
    verified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_documents')

    status = models.BooleanField(default=True)
    is_verified = models.IntegerField(default=False)
    front_image = models.ImageField(upload_to='uploads/user_documents_images/')
    back_image = models.ImageField(upload_to='uploads/user_documents_images/')
    verified_date = models.DateField()


    def __str__(self):
        return f"Document ID: {self.document_id}, Verified by: {self.verified_by.first_name}"

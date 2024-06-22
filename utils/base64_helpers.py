# serializers.py

import base64
from django.core.files.base import ContentFile
from django.utils.text import slugify
from rest_framework import serializers

class Base64ImageField(serializers.ImageField):
   

    def to_internal_value(self, data):
       
        if isinstance(data, str) and data.startswith('data:image'):
            # Extract base64 data from the string
            format, imgstr = data.split(';base64,')
            # Determine the file format
            ext = format.split('/')[-1]
            # Generate a unique filename
            filename = f'{slugify(format[:20])}.{ext}'
            # Create a ContentFile object with the decoded base64 data
            decoded_img = ContentFile(base64.b64decode(imgstr), name=filename)
            return decoded_img
        return super().to_internal_value(data)

# Other serializers can be defined here

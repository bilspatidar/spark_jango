from rest_framework import serializers
from django.core.validators import RegexValidator
from django.utils import timezone
import re
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils.crypto import get_random_string

def validate_phone_number(value):
    phone_validator = RegexValidator(
        regex=r'^\d{10}$',  # Ensure exactly 10 digits
        message='Phone number must be exactly 10 digits long',
        code='invalid_phone_number'
    )
    phone_validator(value)


def format_datetime(dt):
     dt = timezone.localtime(dt, timezone=timezone.get_current_timezone())
     return dt.strftime("%d/%b/%Y %H:%M:%S")

def validate_password(password):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    pattern = re.compile(regex)
    if not pattern.match(password):
        return False
    return True


def send_custom_email(subject, html_content, recipient_list):
    email_from = settings.EMAIL_HOST_USER
    text_content = 'This is an important message.'
    
    msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    
    msg.send()

def generate_token():
    return get_random_string(length=6)

def token_expire_time():
    return timezone.now() + timezone.timedelta(minutes=10)
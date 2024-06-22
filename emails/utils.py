from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_subcategory_creation_email(subcategory):
    subject = 'New SubCategory Created'
    html_content = render_to_string('subcategories/subcategories_email.html', {'subcategory_name': subcategory.name})
    recipient_list = ['nirbhaydhangar@gmail.com']  # Replace with actual recipient list
    send_custom_email(subject, html_content, recipient_list)

def send_custom_email(subject, html_content, recipient_list):
    email_from = settings.EMAIL_HOST_USER
    text_content = 'This is an important message.'
    
    msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    
    msg.send()
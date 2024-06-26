# Generated by Django 5.0.4 on 2024-06-25 09:50

import utils.common_helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[utils.common_helpers.validate_name]),
        ),
    ]

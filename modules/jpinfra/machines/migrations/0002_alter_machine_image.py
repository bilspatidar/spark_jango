# Generated by Django 5.0.4 on 2024-07-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='image',
            field=models.ImageField(upload_to='uploads/machine_files/'),
        ),
    ]

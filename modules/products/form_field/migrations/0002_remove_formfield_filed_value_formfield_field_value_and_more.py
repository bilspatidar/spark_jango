# Generated by Django 5.0.4 on 2024-06-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_field', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='filed_value',
        ),
        migrations.AddField(
            model_name='formfield',
            name='field_value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='default_value',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

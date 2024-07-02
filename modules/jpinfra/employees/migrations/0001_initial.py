# Generated by Django 5.0.4 on 2024-07-02 06:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=15)),
                ('alt_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('doj', models.DateField()),
                ('country_id', models.IntegerField()),
                ('state_id', models.IntegerField()),
                ('city_id', models.IntegerField()),
                ('street_address', models.TextField()),
                ('street_address2', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(upload_to='uploads/profile_pics/')),
                ('address_proof', models.FileField(upload_to='uploads/address_proofs/')),
                ('id_proof', models.FileField(upload_to='uploads/id_proofs/')),
                ('businessSignature', models.ImageField(upload_to='uploads/business_signatures/')),
                ('status', models.BooleanField(default=True)),
                ('user_created', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
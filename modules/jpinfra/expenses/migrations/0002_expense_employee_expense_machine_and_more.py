# Generated by Django 5.0.4 on 2024-07-08 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('expenses', '0001_initial'),
        ('machines', '0001_initial'),
        ('payment_mode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='employees.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='machine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='machines.machine'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='payment_mode',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='payment_mode.paymentmode'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.2.3 on 2025-06-22 09:08

import organizer.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_alter_organizer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True, validators=[organizer.validators.PhoneNumberValidator()]),
        ),
    ]

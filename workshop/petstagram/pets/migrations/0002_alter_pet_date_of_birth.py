# Generated by Django 5.0.4 on 2025-06-10 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

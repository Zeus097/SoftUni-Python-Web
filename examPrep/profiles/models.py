from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.validators import AlphaNumericUnderscoreValidator


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericUnderscoreValidator()
        ]
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators=[
            MinValueValidator(0),
        ],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username

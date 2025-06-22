from django.core.validators import MinLengthValidator
from django.db import models
from organizer.validators import CompanyNameValidator, SecretKeyValidator, PhoneNumberValidator


class Organizer(models.Model):
    company_name = models.CharField(
        max_length=110,
        validators=[
            MinLengthValidator(2),
            CompanyNameValidator()
        ],
        help_text="*Allowed names contain letters, digits, spaces, and hyphens."
    )

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            PhoneNumberValidator()
        ],
        error_messages={
            'unique': "That phone number is already in use!"
        },
    )

    secret_key = models.CharField(
        max_length=4,
        unique=True,
        validators=[
            SecretKeyValidator()
        ],
        help_text="*Pick a combination of 4 unique digits."
    )

    website = models.URLField(
        blank=True,
        null=True,
    )

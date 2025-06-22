import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CompanyNameValidator:
    def __init__(self, message: str = None) -> None:
        self.message = message

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, value: str):
        self.__message = value or "The company name is invalid!"

    def __call__(self, value) -> None:
        for char in value.strip():
            if not (char.isalnum() or char in [' ', '-']):
                raise ValidationError(self.message)


@deconstructible
class SecretKeyValidator:
    def __init__(self, message: str = None) -> None:
        self.message = message

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, value: str):
        self.__message = value or "Your secret key must have 4 unique digits!"

    def __call__(self, value) -> None:
        if not (value.isdigit() and len(value) == 4 and len(set(value)) == 4):
            raise ValidationError(self.message)


@deconstructible
class PhoneNumberValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, value: str):
        self.__message = value or "Enter a valid phone number (digits only)..."

    def __call__(self, value):
        if not re.fullmatch(r'\d+', value):
            raise ValidationError(self.message)

from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible



@deconstructible
class NotValidDepartmentValidator:
    def __init__(self, fake_department: Optional[list]= None, message: str = None):
        self.fake_department = fake_department
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or "Not a valid Department"

    def __call__(self, value):
        for department in value.split():
            if department.lower() in self.fake_department:
                raise ValidationError(self.message)









@deconstructible
class BadWordValidator:
    def __init__(self, bad_words: Optional[list] = None, message: Optional[str] = None):
        self.bad_words = bad_words
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or "The text contains bad words"

    def __call__(self, value: str):
        for bad_word in value.split():
            if bad_word.lower() in self.bad_words:
                raise ValidationError(self.message)


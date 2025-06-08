from django.db import models

from posts.choices import LanguageChoices
from posts.validators import BadWordValidator


class Department(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name











class Post(models.Model):
    title = models.CharField(
        max_length=100,
    )

    content = models.TextField(
        validators=[
            BadWordValidator(
                bad_words=[
                    "bad_word1",
                    "bad_word2",
                ]
            )
        ]
    )

    author = models.CharField(
        max_length=50,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    language = models.CharField(
        max_length=20,
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER,
    )

    image = models.ImageField(
        upload_to='',
        blank=True,
        null=True,
    )


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=50,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

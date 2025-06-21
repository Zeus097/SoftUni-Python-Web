from django.core.validators import MinValueValidator
from django.db import models
from albums.choices import GenreChoices

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        unique=True,
    )
    artist_name = models.CharField(
        max_length=30,
    )
    genre = models.CharField(
        max_length=30,
        choices=GenreChoices.choices
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField()
    price = models.FloatField(
        validators=[MinValueValidator(0)]
    )
    owner = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        related_name='albums'
    )

    def __str__(self):
        return self.album_name

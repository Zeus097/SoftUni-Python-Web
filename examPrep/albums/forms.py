from django import forms

from albums.models import Album
from albums.mixins import ReadOnlyMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist_name': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(attrs={'placeholder': 'description'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'image_url'}),
            'price': forms.TextInput(attrs={'placeholder': 'price'}),
        }


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(ReadOnlyMixin, AlbumBaseForm):
    pass

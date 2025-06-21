from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from albums.models import Album
from common.utils import get_profile
from albums.forms import AlbumCreateForm


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    success_url = reverse_lazy('home')
    template_name = 'album-add.html'

    def form_valid(self, form):
        #  Преди да се запази задаваме собственика
        form.instance.owner = get_profile()
        return super().form_valid(form)


class DetailsAlbum():
    pass


class EditAlbum():
    pass


class DeleteAlbum():
    pass

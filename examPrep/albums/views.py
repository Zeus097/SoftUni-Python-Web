from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from albums.models import Album
from common.utils import get_profile
from albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    success_url = reverse_lazy('home')
    template_name = 'album-add.html'

    def form_valid(self, form):
        #  Преди да се запази задаваме собственика
        form.instance.owner = get_profile()
        return super().form_valid(form)


class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'album-details.html'
    pk_url_kwarg = 'id'


class AlbumEditView(UpdateView):
    model = Album
    template_name = 'album-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    form_class = AlbumEditForm


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'album-delete.html'
    form_class = AlbumDeleteForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


    # Задава се формата да се попълни с данните,
    # понеже не идва формата в DeleteView
    def get_initial(self):
        return self.object.__dict__

    # Проверяваме за невалидна, понеже то се опитва да я създаде а такава има
    # а unique constraint не позволява повторно.
    def form_invalid(self, form):
        return self.form_valid(form)

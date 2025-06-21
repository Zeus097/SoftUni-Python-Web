from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from common.utils import get_profile
from albums.models import Album
from profiles.forms import ProfileCreateForm


class HomePage(ListView, FormView):
    model = Album  # Пише Албума защото ще рендерираме през него
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        if not get_profile():
            return ['home-no-profile.html']
        return ['home-with-profile.html']

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super().form_valid(form)


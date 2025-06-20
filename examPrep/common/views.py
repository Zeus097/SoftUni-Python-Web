from django.shortcuts import render
from django.views.generic import ListView, FormView
from common.utils import get_profile
from albums.models import Album
from profiles.forms import ProfileCreateForm


class HomePage(ListView, FormView):
    model = Album
    form_class = ProfileCreateForm

    def get_template_names(self):
        if not get_profile():
            return ['home-no-profile.html']
        return ['home-with-profile.html']

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super().form_valid(form)

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from common.utils import get_organizer
from event.models import Event
from organizer.forms import OrganizerCreateForm


class HomePage(ListView, FormView):
    model = Event
    form_class = OrganizerCreateForm
    success_url = reverse_lazy('home-page')

    def get_template_names(self):
        if not get_organizer():
            return ['index.html']
        return ['base.html']

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super().form_valid(form)

from typing import Optional

from django.db.models import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from common.utils import get_organizer
from organizer.models import Organizer
from organizer.forms import OrganizerCreateForm, OrganizerEditForm
from django.utils import timezone
from event.models import Event


class OrganizerCreateView(CreateView):
    model = Organizer
    form_class = OrganizerCreateForm
    success_url = reverse_lazy('events-details')
    template_name = 'create-organizer.html'

    def form_valid(self, form):
        #  Преди да се запази задаваме собственика
        form.instance.owner = get_organizer()
        return super().form_valid(form)


class OrganizerDetailView(DetailView):
    model = Organizer
    template_name = 'details-organizer.html'

    def get_object(self, queryset=None):
        return get_organizer()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organizer = context['organizer']

        # Get upcoming events ordered by start_time
        context['upcoming_events'] = Event.objects.filter(
            organizer=organizer,
            start_time__gt=timezone.now()
        ).order_by('start_time')

        return context


class OrganizerEditView(UpdateView):
    model = Organizer
    template_name = 'edit-organizer.html'
    form_class = OrganizerEditForm
    success_url = reverse_lazy('details-organizer')

    def get_object(self, queryset=None):
        return get_organizer()


class OrganizerDeleteView(DeleteView):
    model = Organizer
    template_name = 'delete-organizer.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset: Optional[QuerySet] = None) -> QuerySet:
        return get_organizer()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organizer = context['organizer']

        upcoming_events_qs = Event.objects.filter(
            organizer=organizer,
            start_time__gt=timezone.now()
        ).order_by('start_time')

        context['upcoming_events'] = upcoming_events_qs
        context['has_upcoming_events'] = upcoming_events_qs.exists()

        return context

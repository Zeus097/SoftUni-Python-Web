from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, DetailView, UpdateView, DeleteView

from common.utils import get_organizer
from event.forms import EventCreateForm, EventEditForm, EventDeleteForm
from event.models import Event


class EventDetailsView(ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.all().order_by('-start_time')


class EventCreateView(CreateView):
    model = Event
    form_class = EventCreateForm
    success_url = reverse_lazy('events-details')
    template_name = 'create-event.html'

    def form_valid(self, form):
        form.instance.organizer = get_organizer()
        return super().form_valid(form)


class CurrentEventDetailsView(DetailView):
    model = Event
    template_name = 'details-event.html'
    pk_url_kwarg = 'id'


class EventEditView(UpdateView):
    model = Event
    template_name = 'edit-event.html'
    form_class = EventEditForm
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        form.instance.organizer = get_organizer()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('current-event-details', kwargs={'id': self.object.pk})


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'delete-event.html'
    form_class = EventDeleteForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home-page')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

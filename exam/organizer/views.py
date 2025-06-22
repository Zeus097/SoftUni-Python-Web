from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.utils import get_organizer
from organizer.models import Organizer
from organizer.forms import OrganizerCreateForm


class OrganizerCreateView(CreateView):
    model = Organizer
    form_class = OrganizerCreateForm
    success_url = reverse_lazy('events-details')
    template_name = 'create-organizer.html'

    def form_valid(self, form):
        #  Преди да се запази задаваме собственика
        form.instance.owner = get_organizer()
        return super().form_valid(form)

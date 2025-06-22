from django import forms
from django.utils.timezone import now

from event.models import Event


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer']
        widgets = {
            'slogan': forms.TextInput(attrs={'placeholder': 'Provide an appealing text...'}),
            'start_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local',},
                format='%Y-%m-%dT%H:%M'
            ),
            'key_features': forms.Textarea(attrs={'placeholder': 'Provide important event details...'}),
            'banner_url': forms.TextInput(attrs={'placeholder': 'An optional banner image URL...'}),
        }
        labels = {
            'start_time': 'Event Date/Time:',
        }


class EventCreateForm(EventBaseForm):
    pass


class EventEditForm(EventBaseForm):
    pass


class EventDeleteForm(EventBaseForm):
    pass

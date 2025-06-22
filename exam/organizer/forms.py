from django import forms
from organizer.models import Organizer


class OrganizerBaseForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = "__all__"
        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Enter a company name...',
                'type': 'text',
            }),

            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter a valid phone number (digits only)...',
                'type': 'text',
            }),

            'secret_key': forms.TextInput(attrs={
                'placeholder': 'Enter a secret key like <1234>...',
                'type': 'password',
            }),
        }


class OrganizerCreateForm(OrganizerBaseForm):
    pass


class OrganizerEditForm(OrganizerBaseForm):
    pass


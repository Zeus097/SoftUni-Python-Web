from django.utils.timezone import now

from crispy_forms.helper import FormHelper
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.forms import modelformset_factory, formset_factory

from posts.mixins import ReadOnlyFieldsMixin, DisabledFieldsMixin, InputDateDisabledMixin
from posts.models import Post, Department, Comment


class BaseDepartmentForm(InputDateDisabledMixin, forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'type': 'text'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

        error_messages = {
            'description': {
                'min_length': "Too short for a description...",
            }
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')

        if date > now().date():
            raise ValidationError("Date cannot be in the future")

        return date

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name.lower() in description.lower():
            raise ValidationError('Description must not contain Department name')

        return cleaned_data


class CreateDepartmentForm(BaseDepartmentForm):
    pass


class EditDepartmentForm(CreateDepartmentForm):
    pass


class DeleteDepartmentForm(DisabledFieldsMixin, BaseDepartmentForm):
    pass


class SearchDepartmentForm(forms.Form):
    query = forms.CharField(
        max_length=30,
        label='Department: ',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search by name...'}
        ),
        validators=[
            MinLengthValidator(
                5, message="That's too short for a valid Department.."
            )
        ],
    )








class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'language': forms.RadioSelect(
                attrs={'class': 'radio-select'},
            )
        }
        error_messages = {
            'author': {
                'max_length': "Hey thats a lot",
            }
        }

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if not author.isalpha():
            raise ValidationError('Author name should contain only letters')

        return author

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title.lower() in content.lower():
            raise ValidationError("The post title shouldn't be included in the content!")

        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)

        post.author = post.author.capitalize()

        if commit:
            post.save()

        # send_notifications()...

        return post


class PostCreateForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(ReadOnlyFieldsMixin, PostBaseForm):
    pass


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search for posts...'},
        )
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        labels = {
            'content': '',
        }

        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add a comment...',
                }
            )
        }


CommentFormSet = formset_factory(CommentForm, extra=1)

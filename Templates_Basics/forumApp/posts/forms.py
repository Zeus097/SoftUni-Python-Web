from django import forms
from posts.models import Post


class DepartmentSearchForm(forms.Form):

    department_id = forms.IntegerField(
        required=False,
        widget=forms.NumberInput
    )

    department_name = forms.CharField(
        required=True,
        max_length=50,
    )

    is_available = forms.BooleanField(
        label='Available to apply',
        required=False,
        widget=forms.CheckboxInput,
    )

    date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={'type': 'date'}
        ),
    )


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'language': forms.RadioSelect(
                attrs={'class': 'radio-select'}
            )
        }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search for posts...'},
        )
    )

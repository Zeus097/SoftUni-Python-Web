from django import forms
from posts.models import Post, Department


class BaseDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'type': 'text'}),
        }


class CreateDepartmentForm(BaseDepartmentForm):
    pass


class EditDepartmentForm(CreateDepartmentForm):
    pass


class DeleteDepartmentForm(BaseDepartmentForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchDepartmentForm(forms.Form):
    query = forms.CharField(
        max_length=30,
        label='Department: ',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search by name...'}
        )
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

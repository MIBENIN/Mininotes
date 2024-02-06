from django import forms
from .models import Note
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'tags', 'content']

    def clean_tags(self):
        tags = self.cleaned_data['tags']
        if not tags:
            raise forms.ValidationError("This field is required.")
        return tags


class EditProfileForm(UserChangeForm):
    password = None

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control'

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if any(char.isdigit() for char in first_name):
            raise forms.ValidationError(
                "First name must only contain letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if any(char.isdigit() for char in last_name):
            raise forms.ValidationError("Last name must only contain letters.")
        return last_name

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

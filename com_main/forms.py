from django import forms
from django.contrib.auth.models import User

from .models import Group


class UserForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget=forms.PasswordInput())


class FindGroupform(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name_of_group']
        labels = {'name_of_group': 'Group name: '}

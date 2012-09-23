from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import Textarea


class RegistrationForm(UserCreationForm):
    info = forms.CharField(widget=Textarea)

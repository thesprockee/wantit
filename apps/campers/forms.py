from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import Textarea
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password

from apps.campers.models import AccountRequest


class RegistrationForm(UserCreationForm):
    info = forms.CharField(label="Info",
            widget=Textarea(attrs={'class': 'span5', 'rows': 3}),
            required=True,
            help_text="How do you know Want It!?")
    email = forms.EmailField()


class RegistrationView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        password = make_password(form.cleaned_data['password1'])
        request = AccountRequest(username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=password, info=form.cleaned_data['info'])
        request.save()
        return HttpResponseRedirect(self.success_url)

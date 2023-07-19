from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy("accounts:login") # on success sign up reverse to login
    template_name = 'accounts/signup.html'

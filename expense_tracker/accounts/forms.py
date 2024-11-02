# accounts/forms.py
from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
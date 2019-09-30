from django import forms
from .models import *

class LoginForm (forms.Form):
    username = forms.EmailField(help_text="Email address")
    password = forms.CharField(widget=forms.PasswordInput)
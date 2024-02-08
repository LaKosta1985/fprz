from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User
class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    class Meta():
        model=User

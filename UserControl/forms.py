from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
class RegisterForm(UserCreationForm):
    name= forms.CharField(max_length=100, required=False)
    contact= forms.CharField(max_length=20, required=False)
    class Meta:
        model=User
        fields= ['name','contact','username', 'password1', 'password2']
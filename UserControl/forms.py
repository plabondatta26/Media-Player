from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CreateProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username', 'password1', 'password2']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = CreateProfile
        fields = ['name', 'contact', 'address','birthday']
        labels = {
            "name": "Name",
            "contact": "Contact",
            "birthday": "Birthday",
            "address": "Address",
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name cannot exceed 100 characters'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact cannot exceed 100 characters (example: 01*********)'}),
            'address': forms.TextInput(attrs={'class': 'form-control',  'placeholder':'Address cannot exceed 200 characters'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'yy/mm/dd'}),

        }


class UpdateProfilePic(forms.ModelForm):
    class Meta:
        model = CreateProfile
        fields = ['image', ]
        labels = {
            "image": "Picture",
        }
        widgets ={
            'image': forms.FileInput(attrs={'class':'form-group', 'accept': 'image/*'})
        }










"""
class Captcha(forms.Form):
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.85,

            }
        )
    )
    """
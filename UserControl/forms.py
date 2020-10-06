from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CreateProfile
#from captcha.fields import ReCaptchaField,ReCaptchaV3
#from captcha.widgets import ReCaptchaV2Checkbox

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username', 'password1', 'password2']


class Update_Profile(forms.ModelForm):
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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'yy/mm/dd'}),

        }

class Update_Profile_Pic(forms.ModelForm):
    class Meta:
        model = CreateProfile
        fields = ['image', ]










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
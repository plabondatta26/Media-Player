from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField,ReCaptchaV3
from captcha.widgets import ReCaptchaV2Checkbox

class RegisterForm(UserCreationForm):
    name= forms.CharField(max_length=100, required=True)
    contact= forms.CharField(max_length=20, required=True)
    class Meta:
        model=User
        fields= ['name','contact','username', 'password1', 'password2']








class Captcha(forms.Form):
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.85,

            }
        )
    )
from .models import Video
from django import forms
class video_upload(forms.ModelForm):
    class Meta:
        model= Video
        fields = ['title','file']
from .models import Video, Comment_Model
from django import forms
class video_upload(forms.ModelForm):
    class Meta:
        model= Video
        fields = ['title','file', 'make_privet']
class commentForm(forms.ModelForm):
    class Meta:
        model = Comment_Model
        fields = ['comment']
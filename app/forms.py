from .models import Video, Comment_Model, ReplyModel
from django import forms


class video_upload(forms.ModelForm):
    class Meta:
        model= Video
        fields = ['title','file', 'make_privet', ]


class commentForm(forms.ModelForm):
    class Meta:
        model = Comment_Model
        fields = ['comment', ]


class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = ReplyModel
        fields = ['reply', ]

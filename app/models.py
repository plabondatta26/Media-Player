from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    title= models.CharField(max_length=50)
    file = models.FileField(upload_to='videos/', null=True, verbose_name="")
    make_privet= models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,blank=False ,on_delete=models.CASCADE )
    def __str__(self):
        return self.title

class Comment_Model(models.Model):
    comment= models.TextField(max_length=1000, blank=False, null=False, unique=False)
    comment_video= models.ForeignKey(Video, blank=False, on_delete=models.CASCADE, related_name='comments')
    comment_user= models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_aproved = models.BooleanField(default=True)
    def __str__(self):
        return self.comment


class ReplyModel(models.Model):
    comment_video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=False, null=False)
    comment = models.ForeignKey(Comment_Model, on_delete=models.CASCADE, blank=False, null=False)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    reply = models.TextField()
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply



""""
------------------------------------ Next Update--------------------------------




class Like(models.Model):
    like = models.IntegerField()
    video= models.ForeignKey(Video, blank=False, on_delete=models.CASCADE)

class DiLike(models.Model):
    dislike = models.IntegerField()
    video= models.ForeignKey(Video, blank=False, on_delete=models.CASCADE)

class LikedComment(models.Model):
    like = models.IntegerField()
    video= models.ForeignKey(Video, blank=False, on_delete=models.CASCADE)

class DiLikeComment(models.Model):
    dislike = models.IntegerField()
    video= models.ForeignKey(Video, blank=False, on_delete=models.CASCADE)
    """
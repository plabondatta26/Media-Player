from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/', null=True, verbose_name="")
    make_privet = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def NoOfRating(self):
        ratings = Rating.objects.filter(video=self)
        return len(ratings)
    def avgRatings(self):
        sum = 0
        ratings = Rating.objects.filter(video=self)
        for rating in ratings:
            sum += rating
        if len(ratings) > 0:
            avg_rating = sum / len(ratings)
            return avg_rating
        else:
            return 0


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=False, null=False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.pk)

    class Meta:
        unique_together = (('user', 'video'),)
        index_together = (('user', 'video'),)


class Comment_Model(models.Model):
    comment = models.TextField(max_length=1000, blank=False, null=False, unique=False)
    comment_video = models.ForeignKey(Video, blank=False, on_delete=models.CASCADE, related_name='comments')
    comment_user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_aproved = models.BooleanField(default=True)
    def __str__(self):
        return self.comment


class ReplyModel(models.Model):
    comment = models.ForeignKey(Comment_Model, on_delete=models.CASCADE, blank=False, null=False)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    reply = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply



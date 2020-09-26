from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    title= models.CharField(max_length=50)
    file = models.FileField(upload_to='videos/', null=True, verbose_name="")
    make_privet= models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,blank=False ,on_delete=models.CASCADE )
    def __str__(self):
        return self.title
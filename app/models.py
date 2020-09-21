from django.db import models

# Create your models here.
class Video(models.Model):
    title= models.CharField(max_length=50)
    file = models.FileField(upload_to='videos/', null=True, verbose_name="")
    def __str__(self):
        return self.title
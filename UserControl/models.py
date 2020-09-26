from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CreateProfile(models.Model):
    image = models.ImageField(verbose_name=None, name=None, width_field=None, height_field=None)
    pass

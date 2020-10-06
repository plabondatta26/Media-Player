from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CreateProfile(models.Model):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=100, unique=False, blank=True)
    contact = models.CharField(max_length=11, blank=True, unique=False)
    address = models.CharField(max_length=200, blank=True, unique=False)
    birthday= models.DateField(auto_now=False, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


    #need to use django signals for emplement this.
    def __str__(self):
        return str(self.pk)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        CreateProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
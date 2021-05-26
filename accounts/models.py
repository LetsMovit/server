from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    first_name = None
    last_name = None

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile' ,default='profile/defaultIMG.gif')

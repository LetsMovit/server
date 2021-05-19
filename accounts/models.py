from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class User(AbstractUser):
    first_name = None
    last_name = None

class Profile(models.Model):
    pass
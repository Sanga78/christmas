from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    # Add your additional fields if needed
    objects = CustomUserManager()

    def __str__(self):
        return self.username

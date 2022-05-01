from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name="Email Address", unique=True)
    age = models.IntegerField(verbose_name="Age", null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    objects = CustomUserManager()

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    password = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True, default="")
    is_critic = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["email", "first_name", "last_name", "birthdate"]

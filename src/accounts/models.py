from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    website_url = models.URLField()
    bio = models.TextField(blank=True)


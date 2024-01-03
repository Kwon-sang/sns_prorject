from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(blank=True, upload_to='accounts/profile/%Y/%m/%d')

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_in_store'
            ),
        )

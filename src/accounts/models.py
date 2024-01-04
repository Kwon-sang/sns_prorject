from collections import defaultdict

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

    def get_tags_all(self):
        tags_counter = defaultdict(int)
        for post in list(self.post_set.all()):
            tags = post.tags.all()
            for tag in tags:
                tags_counter[tag] += 1
        return tags_counter.items()


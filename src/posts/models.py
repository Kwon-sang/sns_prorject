from django.db import models
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager


def user_image_upload_path(instance, filename):
    return f'posts/{instance.author.id}/%Y/%m/%d/{filename}'


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampMixin, models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_image_upload_path)
    caption = models.TextField(max_length=500)
    location = models.CharField(max_length=100, blank=True)

    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('posts: post_detail', args=[self.id])

from collections import Counter

from django.db import models
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager


def photo_upload_path(instance, filename):
    return f'posts/{instance.author.id}/{filename}'


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampMixin, models.Model):
    class Meta:
        ordering = ['-created_at']

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=photo_upload_path)
    caption = models.TextField(max_length=500)
    location = models.CharField(max_length=100, blank=True)

    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('posts: post_detail', args=[self.id])

    def is_author(self, request):
        return request.user.id is self.author.id

    @classmethod
    def get_all_tag_counts_by_author(cls, author) -> dict:
        tags = []
        post_qs = Post.objects.select_related('author').filter(author=author).prefetch_related('tags')
        for post in post_qs:
            tags += [tag.name for tag in post.tags.all()]
        tag_counter = Counter(tags)
        return dict(tag_counter)


class Comment(TimeStampMixin, models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    body = models.TextField(max_length=500)

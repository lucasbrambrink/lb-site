from __future__ import unicode_literals

from django.db import models
from common.models import PublishedManager


class BlogPost(models.Model):
    masthead_image = models.ImageField()
    title = models.CharField(max_length=1000)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    template_path = models.CharField(max_length=255, default='', blank=True)

    published = PublishedManager()
    objects = models.Manager()


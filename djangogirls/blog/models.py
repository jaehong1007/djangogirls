from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    # settings.AUTH_USER_MODEL > auth.user
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_Date = models.DateTimeField(blank=True, null=True)

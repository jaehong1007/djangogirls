from django.utils import timezone

from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    # settings.AUTH_USER_MODEL > auth.user
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

        """
        게시글을 발행상태로 만듬
            자신의 published_date를 timezone.now()로 할당
            이후 self.save()를 호출
        :return: 
        """

    def hide(self):
        self.published_date = None
        self.save()
        """
        게시글을 미발행상태로 만듬
            자신의 published_date를 None으로 할당
            이후 self.save()를 호출
        :return:
        """
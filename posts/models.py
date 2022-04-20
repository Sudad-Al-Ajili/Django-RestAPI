from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    title: str = models.CharField(max_length=100)
    url: str = models.URLField()
    poster: int = models.ForeignKey(User, on_delete=models.CASCADE)
    created: datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


class Vote(models.Model):
    voter: int = models.ForeignKey(User, on_delete=models.CASCADE)
    post: int = models.ForeignKey(Post, on_delete=models.CASCADE)

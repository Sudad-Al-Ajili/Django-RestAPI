from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    created: datetime = models.DateTimeField(auto_now_add=True)
    poster: int = models.ForeignKey(User, on_delete=models.CASCADE)
    title: str = models.CharField(max_length=100)
    url: str = models.URLField()

    class Meta:
        ordering = ['-created']


class Vote(models.Model):
    post: int = models.ForeignKey(Post, on_delete=models.CASCADE)
    voter: int = models.ForeignKey(User, on_delete=models.CASCADE)

import datetime

from django.conf import settings
from django.db import models

from users.models import User



class Ad(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['created_at']


class Comment(models.Model):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

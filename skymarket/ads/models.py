import datetime

from django.conf import settings
from django.db import models

from skymarket.users.models import User


class Ad(models.Model):
    image = models.ImageField(upload_to="image/", null=True)
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['created_at']


class Comment(models.Model):
    ad_pk = models.ForeignKey(Ad, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

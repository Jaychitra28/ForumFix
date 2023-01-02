from django.contrib.auth.models import User
from django.db import models

from .category import Category


class Topic(models.Model):
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=3000)
    category = models.ForeignKey(
        Category, related_name="topics", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

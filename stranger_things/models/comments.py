from django.contrib.auth.models import User
from django.db import models

from .topics import Topic


class Comment(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    created_by = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE
    )
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

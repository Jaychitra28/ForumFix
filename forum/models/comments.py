from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel

from .topics import Topic


class Comment(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name="comments", on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User, null=True, related_name="+", on_delete=models.CASCADE
    )

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

from .category import Category


class Topic(TimeStampedModel):
    title = models.CharField(max_length=400)
    description = models.TextField(max_length=400)
    category = models.ForeignKey(
        Category, related_name="topic", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topic")

    def get_absolute_url(self):
        return reverse(
            "topic_detail",
            args=[
                self.pk,
            ],
        )

from django.contrib.auth.models import User
from django.db import models

from .category import Category

# from django.urls import reverse


class Thread(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(max_length=400)
    category = models.ForeignKey(
        Category, related_name="thread", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="thread"
    )

    # def get_absolute_url(self):
    #     return reverse(
    #         "topic_detail",
    #         args=[
    #             self.pk,
    #         ],
    #     )


# choices = Category.objects.all().values_list('title','title')

# choices_list =[]

# for item in choices:
#     choices_list.append(item)

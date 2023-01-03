from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from forum.models.topic import Topic


class TopicListView(LoginRequiredMixin, ListView):
    model = Topic
    template_name = "topic/topic_list.html"

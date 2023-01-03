from django.views.generic import DetailView

from ..models.topic import Topic


class TopicDetailView(DetailView):
    model = Topic
    template_name = "topic/topic_detail.html"
    # context_object_name = "topic"


# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.list import ListView

# from forum.models.topic import Topic


# class TopicListView(LoginRequiredMixin, ListView):
#     model = Topic
#     template_name = "topic/topic_list.html"

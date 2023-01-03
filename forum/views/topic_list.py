from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from topics.models.topics import Topic


class QuestionListView(LoginRequiredMixin, ListView):
    model = Topic
    template_name = "question/question_list.html"

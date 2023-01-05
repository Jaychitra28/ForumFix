from django.views.generic import DetailView

from ..models.thread import Thread


class ThreadDetailView(DetailView):
    model = Thread
    template_name = "thread/thread_detail.html"

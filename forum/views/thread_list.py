from django.shortcuts import render

from forum.models.thread import Category, Thread


def list(request, id):
    category = Category.objects.get(id=id)
    threads = Thread.objects.filter(category=category)
    context = {"category": category, "threads": threads}
    return render(request, "thread/thread_list.html", context)

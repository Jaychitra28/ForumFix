from django.views.generic import ListView

from ..models.category import Category


class CategoryListView(ListView):
    queryset = Category.objects.all()
    context_object_name = "categories"
    template_name = "thread/category.html"

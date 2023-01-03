"""forumfix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from forum.views import dashboard, topic_detail, topic_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("account/", include("django.contrib.auth.urls")),
    path("forum/", dashboard.dashboard, name="dashboard"),
    path("list/", topic_list.TopicListView.as_view(), name="topic_list"),
    # path("detail/", topic_detil.TopicDetailView.as_view(), name="topic_detil"),
    # path("detail", topic_detil.TopicDetailView.as_view(), name="topic_detail"),
    path(
        "<pk>/",
        topic_detail.TopicDetailView.as_view(),
        name="topic_detail",
    ),
]

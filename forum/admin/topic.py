from django.contrib import admin

from forum.models.topic import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created")
    list_filter = (
        "created_by",
        "created",
    )
    search_fields = ("title", "description")
    raw_id_fields = ("created_by",)
    date_hierarchy = "created"
    ordering = ("created", "created_by")

from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "status",
        "priority",
        "due_date",
    )

    ordering = ("-id",)

    list_filter = (
        "created_at",
        "due_date",
        "status",
        "priority",
        "category",
    )

    search_fields = (
        "id",
        "title",
        "category",
    )

    list_per_page = 10

    list_max_show_all = 100

    # list_editable = (
    #     "category",
    #     "status",
    #     "priority",
    #     "due_date",
    # )

    list_display_links = (
        "id",
        "title",
    )

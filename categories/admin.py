from django.contrib import admin
from tasks.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "color",
        "user",
    )

    ordering = ("-id",)

    list_filter = (
        "name",
        "color",
    )

    search_fields = (
        "name",
        "color",
    )

    list_per_page = 10

    list_max_show_all = 100

    # list_editable = (
    #     "name",
    #     "color",
    # )

    list_display_links = ("id",)

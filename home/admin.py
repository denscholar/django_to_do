from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "task",
        "is_completed",
        "created_at",
        "updated_at",
    )

    list_display_links = ("task",)


admin.site.register(Todo, TodoAdmin)

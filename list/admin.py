from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_title", "status", "conclusion_date", "created_date")
    list_filter = ("status",)
    search_fields = ("task_title", "created_date")

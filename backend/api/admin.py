"""This is a docstring."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """This is a docstring."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)

"""This is a docstring."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """This is a docstring."""

    class Meta:
        """This is a docstring."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')

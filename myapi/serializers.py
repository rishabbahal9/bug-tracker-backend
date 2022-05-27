from rest_framework import serializers
from .models import Task, TaskStatus, Project


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'priority', 'status', 'project', 'assignee', 'created', 'updated')
class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ('id', 'label', 'value', 'project')
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'owner', 'created', 'updated')

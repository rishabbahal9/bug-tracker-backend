from django import views
from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, TaskStatus, Project
from .serializers import TaskSerializer, TaskStatusSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# def add_task(self):
#     return f""


class TaskView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskStatusView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer

class ProjectView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

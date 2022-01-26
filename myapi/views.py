from django import views
from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
# def add_task(self):
#     return f""


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

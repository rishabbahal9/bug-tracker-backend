from django import views
from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# def add_task(self):
#     return f""


class TaskView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

from django.contrib import admin
from .models import Task, Project, TaskStatus

# Register your models here.
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(TaskStatus)

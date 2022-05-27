from django.urls import path, include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('tasks', views.TaskView)
router.register('tasks-status', views.TaskStatusView)
router.register('projects', views.ProjectView)
urlpatterns = [
    path('', include(router.urls ))
]
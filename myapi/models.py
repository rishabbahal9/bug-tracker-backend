from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class BaseModel(models.Model):
    """
    Base model with timestamps
    """

    created = models.DateTimeField(
        "Created on",
        auto_now_add=True,
        editable=False,
        help_text="This field is autopopulated by the platform and represents the"
        " creation timestamp of the object",
    )
    updated = models.DateTimeField(
        "Updated on",
        auto_now=True,
        editable=False,
        help_text="This field is autopopulated by the platform and represents the"
        " object's last update's timestamp",
    )

    class Meta:
        abstract = True  # add this to base models so it doesn't get migrated


class Project(BaseModel):
    """Project model"""
    title = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey(
       "users.User", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class TaskStatus(models.Model):
    """Task's status model"""
    label = models.CharField(max_length=30, unique=True)
    value = models.CharField(max_length=30)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Task's status"
        verbose_name_plural = "Task's statuses"


class Task(BaseModel):
    """Tasks model"""
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    priority = models.IntegerField(
        default=3, validators=[MinValueValidator(1), MaxValueValidator(3)])

    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.ForeignKey(
        "users.User", on_delete=models.PROTECT)

    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone
from .helpers.model_helper import ModelHelper


# Create your models here.

class DatetimeModel(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)


class ResearchPapers(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    date = models.ForeignKey(DatetimeModel, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to=ModelHelper.user_directory_path, blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectField(models.Model):
    title = models.CharField(max_length=100)
    is_popular = models.BooleanField(default=False)


class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ProjectField, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.ForeignKey(DatetimeModel, on_delete=models.CASCADE, null=True)
    thumbnail = models.FileField(upload_to=ModelHelper.user_directory_path, null=True, blank=True)

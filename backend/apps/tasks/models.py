# Import Django settings to access AUTH_USER_MODEL configuration
from django.conf import settings
# Import Django's models module to create database models
from django.db import models
# Import User model from users app (not actually used since we use settings.AUTH_USER_MODEL)
from apps.users.models import User
# Create your models here.

# Get the user model from settings (best practice for referencing custom user model)
User = settings.AUTH_USER_MODEL
# Define Task model to store user tasks in the database
class Task(models.Model):
    # Foreign key linking task to a user, deletes task if user is deleted (CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Title of the task, maximum 255 characters
    title = models.CharField(max_length=255)
    # Detailed description of the task, can be empty (blank=True)
    description = models.TextField(blank=True)
    # Priority level as integer (default is 1, higher number = higher priority)
    priority = models.IntegerField(default=1)
    # Status of task with predefined choices: Pending, Done, or Discontinued
    status = models.CharField(max_length=20, choices=[('Pending','Pending'),('Done','Done'),('Discontinued','Discontinued')])
    # Timestamp when task was created, automatically set on creation
    created_at = models.DateTimeField(auto_now_add=True)
    # Optional due date for the task, can be null or blank
    due_date = models.DateTimeField(null=True, blank=True)
    # Boolean flag indicating if task is completed (default: False)
    completed = models.BooleanField(default=False)
# Import Django's models module to create database models
from django.db import models
# Import User model from users app to create foreign key relationship
from apps.users.models import User

# Define WorkSession model to track user work/focus sessions
class WorkSession(models.Model):
    # Foreign key linking session to a user, deletes session if user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Foreign key to Task using string reference, sets to null if task is deleted
    task = models.ForeignKey('tasks.Task', on_delete=models.SET_NULL, null=True, blank=True)
    # DateTime when the work session started
    start_time = models.DateTimeField()
    # DateTime when the work session ended
    end_time = models.DateTimeField()
    # Optional integer score representing focus quality (can be null or blank)
    focus_score = models.IntegerField(null=True, blank=True)

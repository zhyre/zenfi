# apps/feedback/models.py - Model definition for user feedback
# Import Django's models module to create database models
from django.db import models
# Import Django settings to access AUTH_USER_MODEL configuration
from django.conf import settings

# Get the user model from settings (best practice for referencing custom user model)
User = settings.AUTH_USER_MODEL

# Define Feedback model to store user mood and stress feedback
class Feedback(models.Model):
    # Foreign key linking feedback to a user, deletes feedback if user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Integer field for mood rating on 1-10 scale (default: 1)
    mood = models.IntegerField(default=1)  # 1–10
    # Integer field for stress level rating on 1-10 scale (default: 1)
    stress_level = models.IntegerField(default=1)  # 1–10
    # Text field for additional notes, can be empty (blank=True)
    notes = models.TextField(blank=True)
    # Timestamp when feedback was created, automatically set on creation
    created_at = models.DateTimeField(auto_now_add=True)

# Empty line for readability
# Import viewsets for creating API views and permissions for access control
from rest_framework import viewsets, permissions
# Import Task model from current app's models
from .models import Task
# Import TaskSerializer to convert Task objects to/from JSON
from .serializers import TaskSerializer

# Define ViewSet for task operations (list, create, retrieve, update, delete)
class TaskViewSet(viewsets.ModelViewSet):
    # Specify which serializer to use for data conversion
    serializer_class = TaskSerializer
    # Require authentication - only logged-in users can access tasks
    permission_classes = [permissions.IsAuthenticated]

    # Override get_queryset to return only tasks belonging to the current user
    def get_queryset(self):
        # Filter tasks to show only those owned by the authenticated user
        return Task.objects.filter(user=self.request.user)

    # Override perform_create to automatically set the user when creating a task
    def perform_create(self, serializer):
        # Save the task with the current user as the owner
        serializer.save(user=self.request.user)

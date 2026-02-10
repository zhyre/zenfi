# Import viewsets for creating API views and permissions for access control
from rest_framework import viewsets, permissions
# Import WorkSession model from current app's models
from .models import WorkSession
# Import WorkSessionSerializer to convert WorkSession objects to/from JSON
from .serializers import WorkSessionSerializer

# Define ViewSet for work session operations (list, create, retrieve, update, delete)
class WorkSessionViewSet(viewsets.ModelViewSet):
    # Specify which serializer to use for data conversion
    serializer_class = WorkSessionSerializer
    # Require authentication - only logged-in users can access work sessions
    permission_classes = [permissions.IsAuthenticated]

    # Override get_queryset to return only sessions belonging to the current user
    def get_queryset(self):
        # Filter work sessions to show only those owned by the authenticated user
        return WorkSession.objects.filter(user=self.request.user)

    # Override perform_create to automatically set the user when creating a session
    def perform_create(self, serializer):
        # Save the work session with the current user as the owner
        serializer.save(user=self.request.user)

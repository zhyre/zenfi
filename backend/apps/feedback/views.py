# Import viewsets for creating API views and permissions for access control
from rest_framework import viewsets, permissions
# Import Feedback model from current app's models
from .models import Feedback
# Import FeedbackSerializer to convert Feedback objects to/from JSON
from .serializers import FeedbackSerializer

# Define ViewSet for feedback operations (list, create, retrieve, update, delete)
class FeedbackViewSet(viewsets.ModelViewSet):
    # Specify which serializer to use for data conversion
    serializer_class = FeedbackSerializer
    # Authentication temporarily disabled for testing (commented out)
    #permission_classes = [permissions.IsAuthenticated]
    # Empty list means no authentication required (for testing only)
    permission_classes = []

    # Override get_queryset to return only feedback belonging to the current user
    def get_queryset(self):
        # Filter feedback to show only those owned by the authenticated user
        return Feedback.objects.filter(user=self.request.user)

    # Override perform_create to automatically set the user when creating feedback
    def perform_create(self, serializer):
        # Save the feedback with the current user as the owner
        serializer.save(user=self.request.user)

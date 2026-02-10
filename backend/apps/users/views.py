# Import Django's render function for rendering templates (not used here)
from django.shortcuts import render
# Import Django REST Framework's viewsets for creating API views and permissions for access control
from rest_framework import viewsets, permissions
# Import the User model from current app's models
from .models import User
# Import the UserSerializer to convert User objects to/from JSON
from .serializers import UserSerializer
# Create your views here.

# Define a ViewSet for user profile operations (CRUD operations via REST API)
class UserProfileViewSet(viewsets.ModelViewSet):
    # Specify which serializer to use for converting data
    serializer_class = UserSerializer
    # Authentication temporarily disabled for testing (commented out: permissions.IsAuthenticated)
    #permission_classes = [permissions.IsAuthenticated]
    # Empty list means no authentication required (for testing only)
    permission_classes = []
    # Base queryset to retrieve all User objects from database
    queryset = User.objects.all()
    # Override get_object to return the specific user object for this request
    def get_object(self):
    # For testing without auth, return first user
        # Check if the request has an authenticated user
        if self.request.user.is_authenticated:
            # If authenticated, return the authenticated user object
            return self.request.user
        # If not authenticated (testing mode), return the first user in database
        return User.objects.first()
    # Original implementation (commented out): just return authenticated user
    #def get_object(self):
    #    return self.request.user   

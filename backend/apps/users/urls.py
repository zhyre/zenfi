# apps/users/urls.py - URL routing configuration for users app
# Import Django's path function to define URL patterns
from django.urls import path
# Import UserProfileViewSet from views to handle user profile requests
from .views import UserProfileViewSet

# List of URL patterns for the users app
urlpatterns = [
    # Define route 'me/' that maps to UserProfileViewSet with specific actions
    path('me/', UserProfileViewSet.as_view({
        'get': 'retrieve',  # HTTP GET request maps to 'retrieve' action (get user profile)
        'put': 'update',  # HTTP PUT request maps to 'update' action (full update)
        'patch': 'partial_update'  # HTTP PATCH request maps to 'partial_update' (partial update)
    })),  # Closing parenthesis for path function
]  # Closing bracket for urlpatterns list

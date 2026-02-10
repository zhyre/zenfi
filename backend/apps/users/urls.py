# apps/users/urls.py - URL routing configuration for users app
# Import Django's path function to define URL patterns
from django.urls import path
# Import UserProfileViewSet from views to handle user profile requests
from .views import UserLoginView, UserProfileViewSet, UserRegistrationViewSet

# List of URL patterns for the users app
urlpatterns = [
    # Define route 'me/' that maps to UserProfileViewSet with specific actions
    path('me/', UserProfileViewSet.as_view({
        'get': 'retrieve',  # HTTP GET request maps to 'retrieve' action (get user profile)
        'put': 'update',  # HTTP PUT request maps to 'update' action (full update)
        'patch': 'partial_update'  # HTTP PATCH request maps to 'partial_update' (partial update)
    })),  # Closing parenthesis for path function

    path('register/', UserRegistrationViewSet.as_view({
        'post': 'create'  # HTTP POST request maps to 'create' action (register new user)
    })),  # Closing parenthesis for path function

    path('login/', UserLoginView.as_view()), # Closing parenthesis for path function
]  # Closing bracket for urlpatterns list

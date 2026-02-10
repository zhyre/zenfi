# Empty line for readability
# Import the User model from current app to serialize
from .models import User
# Import Django REST Framework's serializers module for creating serializers
from rest_framework import serializers

# Define serializer for User model to convert between JSON and Python objects
class UserSerializer(serializers.ModelSerializer):
    # Meta class contains serializer configuration
    class Meta:
        # Specify which model this serializer is for
        model = User
        # List of fields to include in the serialized output (JSON)
        fields = [
                    'id',  # User's unique ID
                    'username',  # User's username for login
                    'email',  # User's email address
                    'age',  # User's age (optional)
                    'gender',  # User's gender (optional)
                    'energy_level'  # User's self-reported energy level (1-10)
                  ]
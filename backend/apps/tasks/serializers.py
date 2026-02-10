# Import Django REST Framework's serializers module
from rest_framework import serializers
# Import Task model to serialize
from .models import Task

# Define serializer for Task model to convert between JSON and Python objects
class TaskSerializer(serializers.ModelSerializer):
    # Meta class contains serializer configuration
    class Meta:
        # Specify which model this serializer is for
        model = Task
        # Include all fields from the Task model in serialization
        fields = '__all__'
        # User field is read-only (set automatically, not via API)
        read_only_fields = ['user']

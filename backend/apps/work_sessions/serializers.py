# Import Django REST Framework's serializers module
from rest_framework import serializers
# Import WorkSession model to serialize
from .models import WorkSession

# Define serializer for WorkSession model to convert between JSON and Python objects
class WorkSessionSerializer(serializers.ModelSerializer):
    # Meta class contains serializer configuration
    class Meta:
        # Specify which model this serializer is for
        model = WorkSession
        # Include all fields from the WorkSession model in serialization
        fields = '__all__'
        # User field is read-only (set automatically, not via API)
        read_only_fields = ['user']

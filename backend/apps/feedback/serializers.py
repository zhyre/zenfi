# Import Django REST Framework's serializers module
from rest_framework import serializers
# Import Feedback model to serialize
from .models import Feedback

# Define serializer for Feedback model to convert between JSON and Python objects
class FeedbackSerializer(serializers.ModelSerializer):
    # Meta class contains serializer configuration
    class Meta:
        # Specify which model this serializer is for
        model = Feedback
        # Include all fields from the Feedback model in serialization
        fields = '__all__'
        # User field is read-only (set automatically, not via API)
        read_only_fields = ['user']

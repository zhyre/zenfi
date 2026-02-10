# Empty line for readability
# Import the User model from current app to serialize
from webbrowser import get
from .models import User
# Import Django REST Framework's serializers module for creating serializers
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

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

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'age',
            'gender',
            'energy_level'
        ]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            age=validated_data.get('age'),
            gender=validated_data.get('gender'),
            energy_level=validated_data.get('energy_level', 10)
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid username or password.")

        refresh = RefreshToken.for_user(user)

        return {
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'gender', 'energy_level']   

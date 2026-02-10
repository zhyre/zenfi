# Import Django's render function for rendering templates (not used here)
from django.shortcuts import render
# Import Django REST Framework's viewsets for creating API views and permissions for access control
from rest_framework import viewsets, permissions
# Import the User model from current app's models
from .models import User
# Import the UserSerializer to convert User objects to/from JSON
from .serializers import LoginSerializer, RegistrationSerializer, UserSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Define a ViewSet for user profile operations (CRUD operations via REST API)
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = []
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user   

class UserRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
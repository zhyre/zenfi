# Import Django's models module to create database models
from django.db import models
# Import AbstractUser to extend Django's built-in User model with custom fields
from django.contrib.auth.models import AbstractUser
# Import validators to restrict integer field values to a specific range
from django.core.validators import MinValueValidator, MaxValueValidator

# Define custom User model that extends Django's AbstractUser
class User(AbstractUser):
    # Email field that must be unique across all users in the database
    email = models.EmailField(unique=True)
    # Integer field for user's age, can be null or blank (optional)
    age = models.IntegerField(null=True, blank=True)
    
    # Define choices for gender field as a list of tuples (value, display_name)
    GENDER_CHOICES = [
        ('Male', 'male'),  # First option: Male
        ('Female', 'female'),  # Second option: Female
        ('Other', 'other'),  # Third option: Other
    ]
    # CharField for gender with predefined choices, max 10 characters, optional
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    
    # Integer field for energy level (1-10 scale), defaults to 10, validated to stay within 1-10 range
    energy_level = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])

    # Specify that 'username' is the field used for authentication (login)
    USERNAME_FIELD = 'username'

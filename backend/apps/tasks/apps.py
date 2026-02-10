# Import Django's AppConfig class to configure this app
from django.apps import AppConfig

# Empty line for readability
# Configuration class for the tasks app
class TasksConfig(AppConfig):
    # Specify the full Python path to this app (required for Django to find it)
    name = "apps.tasks"

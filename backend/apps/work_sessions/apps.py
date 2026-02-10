# Import Django's AppConfig class to configure this app
from django.apps import AppConfig

# Empty line for readability
# Configuration class for the work_sessions app
class WorkSessionsConfig(AppConfig):
    # Specify the full Python path to this app (required for Django to find it)
    name = "apps.work_sessions"

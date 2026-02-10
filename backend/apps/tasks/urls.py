# Import DefaultRouter from DRF to automatically generate URL patterns for viewsets
from rest_framework.routers import DefaultRouter
# Import TaskViewSet to handle task-related API requests
from .views import TaskViewSet

# Create a router instance to automatically generate URL patterns
router = DefaultRouter()
# Register TaskViewSet with empty prefix ('') and basename 'task' for URL naming
router.register('', TaskViewSet, basename='task')

# Assign the automatically generated URL patterns from router to urlpatterns
urlpatterns = router.urls

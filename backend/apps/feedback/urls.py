# apps/feedback/urls.py - URL routing configuration for feedback app
# Import DefaultRouter from DRF to automatically generate URL patterns for viewsets
from rest_framework.routers import DefaultRouter
# Import FeedbackViewSet to handle feedback API requests
from .views import FeedbackViewSet

# Create a router instance to automatically generate URL patterns
router = DefaultRouter()
# Register FeedbackViewSet with empty prefix ('') and basename 'feedback'
router.register('', FeedbackViewSet, basename='feedback')

# Assign the automatically generated URL patterns from router to urlpatterns
urlpatterns = router.urls

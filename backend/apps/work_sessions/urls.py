# Import DefaultRouter from DRF to automatically generate URL patterns for viewsets
from rest_framework.routers import DefaultRouter
# Import WorkSessionViewSet to handle work session API requests
from .views import WorkSessionViewSet

# Create a router instance to automatically generate URL patterns
router = DefaultRouter()
# Register WorkSessionViewSet with empty prefix ('') and basename 'worksession'
router.register('', WorkSessionViewSet, basename='worksession')

# Assign the automatically generated URL patterns from router to urlpatterns
urlpatterns = router.urls

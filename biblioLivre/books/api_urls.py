from rest_framework.routers import DefaultRouter
from .api_views import AvisViewSet

router = DefaultRouter()


router.register("avis", AvisViewSet)

urlpatterns = router.urls
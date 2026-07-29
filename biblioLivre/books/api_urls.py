from rest_framework.routers import DefaultRouter
from .app_views import LivreViewSet

router = DefaultRouter()
router.register('livres', LivreViewSet)

urlpatterns = router.urls
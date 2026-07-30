from rest_framework.routers import DefaultRouter
from .api_views import AvisViewSet, LivreViewSet

router = DefaultRouter()
router.register("avis", AvisViewSet)
router.register('livres', LivreViewSet)

urlpatterns = router.urls
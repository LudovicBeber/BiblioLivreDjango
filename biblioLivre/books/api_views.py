from rest_framework import viewsets, status
from .models import Livre, Avis
from .serializers import LivreSerializer, AvisSerializer
from .permissions import IsAuthenticatedOrOwnerOrAdmin

class AvisViewSet(viewsets.ModelViewSet):
    queryset = Avis.objects.all()
    serializer_class = AvisSerializer
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
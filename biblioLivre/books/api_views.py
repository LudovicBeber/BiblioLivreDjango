from rest_framework import viewsets, status
from .models import Livre, Avis
from .serializers import LivreSerializer, AvisSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsAuthenticatedOrOwnerOrAdmin, IsAuthenticated

class AvisViewSet(viewsets.ModelViewSet):
    queryset = Avis.objects.all()
    serializer_class = AvisSerializer
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        avis = self.get_object()
        user = request.user
        if user in avis.like.all():
            avis.like.remove(user)
            avis.save()
            return Response({'status': 'like retiré', 'likes': avis.like.count()}, status=status.HTTP_200_OK)
        else:
            avis.like.add(user)
        avis.save()
        return Response({'status': 'like ajouté', 'likes': avis.like.count()}, status=status.HTTP_200_OK)

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

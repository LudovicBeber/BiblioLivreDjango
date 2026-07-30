from rest_framework import viewsets, status
from .models import Livre, Avis
from .serializers import LivreSerializer, AvisSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class AvisViewSet(viewsets.ModelViewSet):
    queryset = Avis.objects.all()
    serializer_class = AvisSerializer

    @action(detail=True, methods=['post'])
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

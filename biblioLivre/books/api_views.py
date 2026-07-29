from rest_framework import viewsets, status
from .models import Livre, Avis

class AvisViewSet(viewsets.ModelViewSet):
    queryset = Avis.objects.all()


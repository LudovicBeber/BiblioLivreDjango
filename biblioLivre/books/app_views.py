from rest_framework import viewsets
from .models import Livre
from .serializers import LivreSerializer


class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer


    
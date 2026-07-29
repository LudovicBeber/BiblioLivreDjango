from rest_framework import viewsets
from .models import Livre


class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()


    
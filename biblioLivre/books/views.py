from .models import Livre, Avis
from django.shortcuts import render


def Acceuil(request):
    livres = Livre.objects.all()
    avis = Avis.objects.all()
    return render(request, 'books/acceuil.html', {'livres': livres, 'avis': avis})

from .models import Livre
from django.shortcuts import render



def Acceuil(request):
    livres = Livre.objects.all()
    return render(request, 'books/acceuil.html', {'livres': livres})
# Create your views here.

from django.shortcuts import render
from .models import Livre

def Acceuil(request):
    livres = Livre.objects.all()
    return render(request, 'books/acceuil.html', {'livres': livres})
# Create your views here.

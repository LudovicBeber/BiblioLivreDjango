from .models import Livre
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

@api_view(['GET'])
def livre_list_api(request):
    livres = Livre.objects.all()
    return Response(livres.values())

def Acceuil(request):
    livres = Livre.objects.all()
    return render(request, 'books/acceuil.html', {'livres': livres})
# Create your views here.

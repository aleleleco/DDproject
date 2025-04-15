from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'ddproject/home.html')

def pagina_pergaminho_view(request):
    return render(request, 'ddproject/pagina_pergaminho.html')
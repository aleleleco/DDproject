from django.shortcuts import render
from .utils import gera_submenu

# Create your views here.
from django.shortcuts import render

def home(request):

    

    context = {'submenu': gera_submenu('home')}

    return render(request, 'ddproject/home.html', context)

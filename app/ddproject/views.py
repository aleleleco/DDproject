from django.shortcuts import render, redirect
from .utils import gera_submenu

from django.contrib import messages

# Create your views here.
from django.shortcuts import render

def home(request):

    
   

    return render(request, 'ddproject/home.html')


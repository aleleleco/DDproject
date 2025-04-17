from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):

    if request.method == 'POST':
        user = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username = user, password = senha)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login realizado com sucesso.')
            return redirect('home')
        else:
            messages.error(request, 'Não foi possivel logar, verifique usuário e senha corretos')


    return render(request, 'ddproject/login.html')


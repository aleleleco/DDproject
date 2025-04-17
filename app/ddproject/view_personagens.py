from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PersonagemForm
from .models import Personagens
from .utils import gera_submenu,obter_detalhes_usuario

@login_required
def lista_personagens(request):
    personagens = Personagens.objects.filter(jogador=request.user)

    context = {'submenu': gera_submenu('personagens'),
               'personagens': personagens,
               'title':'Lista Personagens',
               'usuario': obter_detalhes_usuario(request.user)
               }

    return render(request, 'ddproject/lista_personagens.html', context)

@login_required
def cadastrar_personagem(request):
    if request.method == 'POST':
        form = PersonagemForm(request.POST)
        if form.is_valid():
            personagem = form.save(commit=False)
            personagem.jogador = request.user
            personagem.save()
            form.save_m2m()  # Salva os relacionamentos ManyToMany (idiomas)
            return redirect('lista_personagens')  # Redirecione para a página de listagem
    else:
        form = PersonagemForm()
        context = {'form': form,
                   'submenu': gera_submenu('personagens'),
                   'title':'Cadastro Personagens',
                    'usuario': obter_detalhes_usuario(request.user)
                   }

    return render(request, 'ddproject/cadastrar_personagem.html', context)
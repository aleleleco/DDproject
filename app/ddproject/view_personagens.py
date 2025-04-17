from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .forms import PersonagemForm
from .models import Personagens, Classe, Raca, Idioma
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
    classes = Classe.objects.all()
    racas = Raca.objects.all()
    idiomas = Idioma.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        classe_id = request.POST.get('classe')
        raca_id = request.POST.get('raca')
        nivel = request.POST.get('nivel')
        forca = request.POST.get('forca')
        destreza = request.POST.get('destreza')
        inteligencia = request.POST.get('inteligencia')
        sabedoria = request.POST.get('sabedoria')
        carisma = request.POST.get('carisma')
        pontos_vida_maxima = request.POST.get('pontos_vida_maxima')
        pontos_vida_atual = request.POST.get('pontos_vida_atual')
        idioma_ids = request.POST.getlist('idiomas')
        historia = request.POST.get('historia')

        erros = {}
        if not nome:
            erros['nome'] = 'O nome é obrigatório.'
        if not nivel or not nivel.isdigit() or int(nivel) < 1:
            erros['nivel'] = 'O nível deve ser um número maior que 0.'
        if not forca or not forca.isdigit():
            erros['forca'] = 'A força deve ser um número.'
        if not destreza or not destreza.isdigit():
            erros['destreza'] = 'A destreza deve ser um número.'
        if not inteligencia or not inteligencia.isdigit():
            erros['inteligencia'] = 'A inteligência deve ser um número.'
        if not sabedoria or not sabedoria.isdigit():
            erros['sabedoria'] = 'A sabedoria deve ser um número.'
        if not carisma or not carisma.isdigit():
            erros['carisma'] = 'O carisma deve ser um número.'
        if not pontos_vida_maxima or not pontos_vida_maxima.isdigit():
            erros['pontos_vida_maxima'] = 'Os pontos de vida máxima devem ser um número.'
        if not pontos_vida_atual or not pontos_vida_atual.isdigit():
            erros['pontos_vida_atual'] = 'Os pontos de vida atuais devem ser um número.'
        if not historia:
            erros['historia'] = 'A história é obrigatória.'

        if erros:
            messages.error(request, f'Erro ao cadastrar personagem. Verifique os campos obrigatórios e tente novamente. {erros}')    
            return render(request, 'ddproject/cadastrar_personagem.html')
        else:
            try:
                personagem = Personagens(
                    nome=nome,
                    classe_id=classe_id,
                    raca_id=raca_id,
                    nivel=nivel,
                    forca=forca,
                    destreza=destreza,
                    inteligencia=inteligencia,
                    sabedoria=sabedoria,
                    carisma=carisma,
                    pontos_vida_maxima=pontos_vida_maxima,
                    pontos_vida_atual=pontos_vida_atual,
                    jogador=request.user,
                    historia=historia,
                    data_criacao=timezone.now()

                )
                personagem.save()
    else:
        context = {
            'submenu': gera_submenu('personagens'),
            'title': 'Cadastrar Personagem',
            'classes': classes,
            'racas': racas,
            'idiomas': idiomas,
            'usuario': obter_detalhes_usuario(request.user)
        }
            
    return render(request, 'ddproject/cadastrar_personagem.html', context)
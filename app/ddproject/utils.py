from .models import Submenu
from django.contrib.auth.models import User
from django.utils import timezone


def gera_submenu(pagina):
    
    submenus = Submenu.objects.filter(pagina=pagina)
    submenu = {}
    for menu in submenus:
        print(menu.nome)
        print(menu.link)
        submenu[menu.nome] = menu.link

    return submenu



def obter_detalhes_usuario(user):
    """
    Recebe um objeto User do Django e retorna uma lista com nome completo,
    nome de usuário, email e tempo logado (se aplicável).

    Args:
        user: Um objeto User do Django.

    Returns:
        Uma lista contendo:
        - Nome completo (str)
        - Nome de usuário (str)
        - Email (str)
        - Tempo logado (timedelta ou None se não estiver logado ou a informação não estiver disponível)
    """
    nome_completo = f"{user.first_name} {user.last_name}".strip()
    nome_usuario = user.username
    email_usuario = user.email

    tempo_logado = None
    if user.is_authenticated:
        # Para rastrear o tempo logado, você precisaria armazenar o momento do login
        # em algum lugar (por exemplo, na sessão do usuário ou em um campo customizado
        # no modelo User ou em um modelo relacionado).

        # Exemplo hipotético (requer implementação adicional no login):
        ultimo_login_str = user.last_login
        if ultimo_login_str:
            agora = timezone.now()
            tempo_logado = agora - ultimo_login_str

    
    return {'nome_completo':nome_completo, 'nome_usuario':nome_usuario,'email_usuario':email_usuario,'tempo_logado':tempo_logado }
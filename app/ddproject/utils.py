from .models import Submenu

def gera_submenu(pagina):
    
    submenus = Submenu.objects.filter(pagina=pagina)
    submenu = {}
    for menu in submenus:
        print(menu.nome)
        print(menu.link)
        submenu[menu.nome] = menu.link

    return submenu
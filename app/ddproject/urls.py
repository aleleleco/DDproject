# app/ddproject/urls.py
from django.urls import path
from . import views, views_login, view_personagens

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views_login.login, name='login'),
    path('lista_personagens/', view_personagens.lista_personagens, name='lista_personagens'),
    path('cadastrar_personagem/', view_personagens.cadastrar_personagem, name='cadastrar_personagem')

]

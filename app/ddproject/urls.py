# app/ddproject/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pergaminho/', views.pagina_pergaminho_view, name='pagina_pergaminho'),

]

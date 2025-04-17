from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Submenu(models.Model):
    nome = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    pagina = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Classe(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Raca(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nome

class Idioma(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nome

class Personagens(models.Model):
    jogador = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, null=False, blank=False)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True, blank=True)
    raca = models.ForeignKey(Raca, on_delete=models.SET_NULL, null=True, blank=True)
    nivel = models.IntegerField(default=1, null=False, blank=False)
    forca = models.IntegerField(null=False, blank=False)
    destreza = models.IntegerField(null=False, blank=False)
    inteligencia = models.IntegerField(null=False, blank=False)
    sabedoria = models.IntegerField(null=False, blank=False)
    carisma = models.IntegerField(null=False, blank=False)
    pontos_vida_maxima = models.IntegerField(null=False, blank=False)
    pontos_vida_atual = models.IntegerField(null=False, blank=False)
    idiomas = models.ManyToManyField(Idioma, blank=True)
    historia = models.TextField(max_length=500, null=False, blank=False)  # Use TextField para textos maiores
    data_criacao = models.DateField(default=timezone.now)
    ultima_atualizacao = models.DateTimeField(auto_now=True)



    




from django.db import models
from jogos.models import Jogos
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)

    '''remover email e usuario'''
    email = models.CharField(max_length=100, blank=False, null=False, unique=True)
    usuario = models.CharField(max_length=50, blank=False, null=False, unique=True)
    discord = models.CharField(max_length=100, default='Não possui')
    disponivel_para_torneio = models.BooleanField(default=False)
    foto_de_perfil =  models.ImageField(blank=True, null=True)
    id_auth_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_usuario', default=1)

    def __str__(self):
        return self.nome




class UsuarioJoga(models.Model):
    jogador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogos, on_delete=models.CASCADE)
    link_perfil_jogador = models.CharField(max_length=150, blank=True)
    
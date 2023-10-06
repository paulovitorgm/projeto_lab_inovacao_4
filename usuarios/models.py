from django.db import models
from jogos.models import Jogos, Plataforma
from django.contrib.auth.models import User


class Usuario(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    discord = models.CharField(max_length=100, default='Não possui')
    disponivel_para_torneio = models.BooleanField(null=True,blank=True,default=False)
    foto_de_perfil = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.id_usuario.first_name


class NickUsuario(models.Model):
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False, related_name="nicknames")
    nick = models.CharField(unique=True, max_length=100, blank=True)
    regiao_server = models.CharField(max_length=75,blank=True)

    def __str__(self):
        return self.nick


class UsuarioJoga(models.Model):
    nick_jogador = models.ForeignKey(NickUsuario, on_delete=models.CASCADE, related_name="nickname" )
    jogo = models.ForeignKey(Jogos, on_delete=models.CASCADE, related_name="jogo")
    link_perfil_jogador = models.CharField(max_length=150, blank=True)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, related_name="plataforma_usada")


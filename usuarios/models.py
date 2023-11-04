from django.db import models
from jogos.models import Jogos, Plataforma
from django.contrib.auth.models import User


class Usuario(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    discord = models.CharField(max_length=100, default='Não possui')
    disponivel_para_torneio = models.CharField(max_length=1, blank=False, null=False)
    foto_de_perfil = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.id_usuario.first_name


class NickUsuario(models.Model):
    nick = models.CharField(unique=True, max_length=100, blank=True)
    regiao_server = models.CharField(max_length=75, blank=True)
    link_perfil_jogador = models.CharField(max_length=150, blank=True, unique=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False, related_name="nicknames")
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, related_name="plataforma_usada")
    jogo = models.ForeignKey(Jogos, on_delete=models.CASCADE, related_name="jogo")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nick', 'regiao_server', 'jogo'], name='combinacao_unique')
        ]

    def __str__(self):
        return self.nick

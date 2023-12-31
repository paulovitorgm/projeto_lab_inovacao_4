from django.db import models


class Plataforma(models.Model):
    plataforma = models.CharField(blank=False, null=False)

    def __str__(self):
        return self.plataforma


class Jogos(models.Model):
    nome = models.CharField(max_length=75, blank=False, null=False, unique=True)
    empresa_desenvolvedora = models.CharField(max_length=50, blank=False, null=False)
    ano_lancamento = models.IntegerField(blank=False, null=False)
    imagem = models.ImageField(blank=True, null=True)
    plataforma = models.ForeignKey(Plataforma,  on_delete=models.CASCADE, related_name="jogo_plataforma")

    def __str__(self):
        return self.nome

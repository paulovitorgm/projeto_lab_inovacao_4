from django.db import models


class Jogos(models.Model):
    nome = models.CharField(max_length=75, blank=False, null=False, unique=True)
    empresa_desenvolvedora = models.CharField(max_length=50, blank=False, null=False)
    ano_lancamento = models.IntegerField(blank=False, null=False)
    imagem = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Plataforma(models.Model):
    plataforma = models.CharField(blank=False, null=False)
    jogo = models.ForeignKey(Jogos, null=False, blank=False, on_delete=models.CASCADE, related_name="jogo_plataforma")

    def __str__(self):
        return self.plataforma

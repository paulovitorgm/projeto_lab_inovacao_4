from django.db import models


class Jogos(models.Model):
    nome = models.CharField(max_length=75, blank=False, null=False, unique=True)
    plataforma = models.CharField(max_length=75, blank=False, null=False)
    empresa_desenvolvedora = models.CharField(max_length=50, blank=False, null=False)
    ano_lancamento = models.IntegerField(blank=False, null=False)
    imagem = models.ImageField(blank=True, null=True)
    


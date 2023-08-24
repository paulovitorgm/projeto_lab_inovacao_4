from django.urls import path
from jogos.views import cadastrar_jogo


urlpatterns = [
    path('',view=cadastrar_jogo, name='cadastrar_jogo')

]
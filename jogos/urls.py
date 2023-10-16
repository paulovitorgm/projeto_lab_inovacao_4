from django.urls import path
from jogos.views import cadastrar_jogo
from usuarios.views import cadastrar_nick

urlpatterns = [
    path('cadastrar_jogo', view=cadastrar_jogo, name='cadastrar_jogo'),
    path('cadastrar_nick', view=cadastrar_nick, name='cadastrar_nick')

]
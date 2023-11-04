from django.urls import path
from jogos.views import cadastrar_jogo, editar_jogo, deletar_jogo

urlpatterns = [
    path('cadastrar_jogo/', view=cadastrar_jogo, name='cadastrar_jogo'),
    path('editar_jogo/<int:pk>/', view=editar_jogo, name='editar_jogo'),
    path('deletar_jogo/<int:pk>/', view=deletar_jogo, name='deletar_jogo'),


]

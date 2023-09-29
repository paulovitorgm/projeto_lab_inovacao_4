from django.urls import path
from usuarios.views import cadastrar_usuario, editar_usuario, alterar_senha,  deleta_usuario


urlpatterns = [
    # path('login/', view=fazer_login, name='fazer_login'),
    # path('logout/', view=fazer_logout, name='fazer_logout'),

    path('cadastro/', view=cadastrar_usuario, name='cadastrar_usuario'),
    path('editar/<int:pk>/', view=editar_usuario, name='editar_usuario'),
    path('altera_senha/<str:username>/', view=alterar_senha, name='altera_senha'),
    path('delete/<int:pk>/', view=deleta_usuario, name='deletar_usuario')

]
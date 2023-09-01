from django.urls import path
from usuarios.views import cadastrar_usuario, editar_usuario, alterar_senha #, fazer_login, fazer_logout


urlpatterns = [
    # path('login/', view=fazer_login, name='fazer_login'),
    # path('logout/', view=fazer_logout, name='fazer_logout'),

    path('cadastro/', view=cadastrar_usuario, name='cadastrar_usuario'),
    path('editar/<int:usuario_id>/', view=editar_usuario, name='editar_usuario'),
    path('altera_senha/<str:username>/', view=alterar_senha, name='altera_senha'),

]
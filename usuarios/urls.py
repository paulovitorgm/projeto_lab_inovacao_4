from django.urls import path
from usuarios.views import fazer_login, fazer_logout, cadastrar_usuario


urlpatterns = [
    path('login/', view=fazer_login, name='fazer_login'),
    path('logout/', view=fazer_logout, name='fazer_logout'),

    path('cadastro/', view=cadastrar_usuario, name='cadastrar_usuario')
]
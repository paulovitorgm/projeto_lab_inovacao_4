
from django.contrib import admin
from django.urls import path
from jogos.views import *
from usuarios.views import usuario_form
from jogos.views import jogos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('usuario/', usuario_form),
    path('jogos/', jogos),

]

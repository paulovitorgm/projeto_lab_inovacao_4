from django.contrib import admin
from django.urls import path, include

 
from usuarios.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('usuario/', include('usuarios.urls')),
    path('jogos/', include('jogos.urls')),
    path("accounts/", include("django.contrib.auth.urls"))
]

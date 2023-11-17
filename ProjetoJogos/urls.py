from django.contrib import admin
from django.urls import path, include

from usuarios.views import index
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('usuario/', include('usuarios.urls')),
    path('jogos/', include('jogos.urls')),
    path("accounts/", include("django.contrib.auth.urls"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from usuarios.models import Usuario, NickUsuario, UsuarioJoga


class UsuarioAdmin(admin.ModelAdmin):
    exclude = ['']
    list_display = ['id_usuario', 'discord']
    list_display_links = ['id_usuario', 'discord']
    list_per_page = 15
    

class NickUsuarioAdmin(admin.ModelAdmin):
    exclude = ['']
    list_per_page = 15


class UsuarioJogaAdmin(admin.ModelAdmin):
    exclude = ['']
    list_per_page = 15


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(NickUsuario, NickUsuarioAdmin)
admin.site.register(UsuarioJoga, UsuarioJogaAdmin)

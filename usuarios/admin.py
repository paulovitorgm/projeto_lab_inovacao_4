from django.contrib import admin
from usuarios.models import Usuario, NickUsuario


class UsuarioAdmin(admin.ModelAdmin):
    exclude = ['']
    list_display = ['id_usuario', 'discord']
    list_display_links = ['id_usuario', 'discord']
    list_per_page = 15


class NickUsuarioAdmin(admin.ModelAdmin):

    list_display = ['nick', 'usuario_id_id', 'jogo_id', 'link_perfil_jogador']
    list_display_links = ['nick', 'usuario_id_id', 'jogo_id', 'link_perfil_jogador']
    list_per_page = 15


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(NickUsuario, NickUsuarioAdmin)

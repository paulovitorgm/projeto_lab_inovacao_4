from django.contrib import admin
from usuarios.models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    exclude = ['']
    # list_display_links = ['nome', 'usuario', 'discord']
    list_per_page = 15
    


admin.site.register(Usuario, UsuarioAdmin)
